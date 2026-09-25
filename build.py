"""WardOps tanıtım sitesini üretir: src/ → dist/.

Yalnızca Python standart kütüphanesi kullanılır (GitHub Actions'ta ek kurulum
gerekmez). Alan adı, iletişim adresi ve form adresi `site.json` içindedir;
bunlar değişince yalnızca yeniden derlemek yeterlidir.

Kullanım:
    python3 build.py            # dist/ klasörünü üretir ve SEO denetimini çalıştırır
    python3 build.py --strict   # yer tutucu alan adı/e-posta varsa hata verir (yayın öncesi)
"""
from __future__ import annotations

import datetime as dt
import html
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
DIST = ROOT / "dist"

#: Hukuki sayfalar: (adres, markdown dosyası, sekme başlığındaki kısa ad, arama sonucundaki açıklama)
LEGAL = [
    ("terms", "terms.md", "Terms of Service",
     "Terms of Service for WardOps, the operations platform for ocean freight forwarders. Draft under legal review."),
    ("automation-protocol", "automation-protocol.md", "Automation, Approval & Responsibility",
     "How WardOps automates work, what always needs your approval, and how responsibility is shared. Draft."),
    ("data-processing", "data-processing.md", "Data Processing Agreement",
     "WardOps Data Processing Agreement: roles, sub-processors, security measures and deletion. Draft."),
    ("records-and-feedback", "records-and-feedback.md", "Records, Usage Data & Feedback",
     "Which records WardOps keeps, how feedback is collected, who can access it and for how long. Draft."),
    ("privacy", "privacy.md", "Privacy Policy",
     "WardOps Privacy Policy: what personal data we process, why, where it goes and your rights. Draft."),
]

TITLE_MAX, DESCRIPTION_MAX = 65, 160


def load_config() -> dict:
    config = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
    if not config["url"].endswith("/"):
        config["url"] += "/"
    return config


def fill(text: str, values: dict) -> str:
    def replace(match: re.Match) -> str:
        key = match.group(1)
        if key not in values:
            raise KeyError(f"Tanımsız yer tutucu: {{{{{key}}}}}")
        return str(values[key])
    return re.sub(r"\{\{([A-Z_]+)\}\}", replace, text)


# --- markdown (hukuki metinler) ------------------------------------------------
# backend/app/services/legal.py içindeki alt kümenin aynısı: başlık, paragraf,
# madde listesi, tablo, **kalın**, `kod`.

def render_markdown(text: str) -> str:
    lines = text.splitlines()
    output, paragraph = [], []
    index = 0

    def flush() -> None:
        if paragraph:
            output.append(f"<p>{_inline(' '.join(paragraph))}</p>")
            paragraph.clear()

    while index < len(lines):
        line = lines[index].rstrip()
        stripped = line.strip()
        heading = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if not stripped:
            flush()
        elif heading:
            flush()
            level = len(heading.group(1))
            anchor = _slug(heading.group(2)) if level > 1 else ""
            attr = f' id="{anchor}"' if anchor else ""
            output.append(f"<h{level}{attr}>{_inline(heading.group(2))}</h{level}>")
        elif stripped.startswith("|"):
            flush()
            rows = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append(lines[index].strip())
                index += 1
            output.append(_table(rows))
            continue
        elif re.match(r"^[-*]\s+", stripped):
            flush()
            items = []
            while index < len(lines) and (re.match(r"^\s*[-*]\s+", lines[index]) or
                                          (items and lines[index].startswith("  ") and lines[index].strip())):
                current = lines[index]
                if re.match(r"^\s*[-*]\s+", current):
                    items.append(re.sub(r"^\s*[-*]\s+", "", current).strip())
                else:
                    items[-1] += " " + current.strip()
                index += 1
            output.append("<ul>" + "".join(f"<li>{_inline(item)}</li>" for item in items) + "</ul>")
            continue
        else:
            if re.match(r"^\d+(\.\d+)*\.\s", line):
                flush()
            paragraph.append(stripped)
        index += 1
    flush()
    return "\n".join(output)


def _table(rows):
    cells = [[cell.strip() for cell in row.strip("|").split("|")] for row in rows]
    cells = [row for row in cells if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in row)]
    if not cells:
        return ""
    head = "".join(f"<th>{_inline(cell)}</th>" for cell in cells[0])
    body = "".join("<tr>" + "".join(f"<td>{_inline(cell)}</td>" for cell in row) + "</tr>" for row in cells[1:])
    return f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def _inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`(.+?)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+|/[^)\s]*)\)", r'<a href="\2">\1</a>', escaped)
    return escaped


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", text).lower()).strip("-")[:60]


# --- sayfalar -----------------------------------------------------------------

def build(strict: bool = False) -> int:
    config = load_config()
    site_url = config["url"]
    host = urlparse(site_url).hostname or ""
    placeholders = []
    if host.endswith(".example") or host in {"example.com", "localhost"}:
        placeholders.append(f"site.json 'url' hâlâ yer tutucu: {site_url}")
    if config["contact_email"].endswith(("@example.com", ".example")):
        placeholders.append(f"site.json 'contact_email' hâlâ yer tutucu: {config['contact_email']}")
    if strict and placeholders:
        print("\n".join("HATA: " + p for p in placeholders))
        return 1

    today = dt.date.today()
    endpoint = config.get("form_endpoint", "").strip()
    base = {
        "SITE_URL": site_url,
        "SITE_NAME": config["name"],
        "CONTACT_EMAIL": config["contact_email"],
        "FORM_ACTION": endpoint or f"mailto:{config['contact_email']}",
        "FORM_ENDPOINT": endpoint,
        "YEAR": today.year,
        "BUILD_DATE": today.isoformat(),
    }

    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(SRC / "assets", DIST / "assets")

    pages = []   # (adres, dosya yolu, indekslenir mi)

    index_html = fill((SRC / "index.html").read_text(encoding="utf-8"), {**base, "ROOT": ""})
    (DIST / "index.html").write_text(index_html, encoding="utf-8")
    pages.append(("", DIST / "index.html", True))

    template = (SRC / "legal.html").read_text(encoding="utf-8")
    legal_links = []
    for slug, source, short_title, description in LEGAL:
        markdown = (SRC / "legal" / source).read_text(encoding="utf-8")
        title = re.match(r"#\s+(.+)", markdown).group(1).strip()
        body = render_markdown(markdown)
        page = fill(template, {**base, "ROOT": "../../", "DOC_TITLE": html.escape(short_title),
                               "DOC_DESCRIPTION": html.escape(description), "DOC_PATH": f"legal/{slug}/",
                               "DOC_BODY": body})
        target = DIST / "legal" / slug / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page, encoding="utf-8")
        pages.append((f"legal/{slug}/", target, True))
        legal_links.append((title, f"{site_url}legal/{slug}/", description))

    not_found = fill((SRC / "404.html").read_text(encoding="utf-8"), {**base, "ROOT": "/"})
    (DIST / "404.html").write_text(not_found, encoding="utf-8")
    pages.append(("404.html", DIST / "404.html", False))

    (DIST / "robots.txt").write_text(fill((SRC / "robots.txt").read_text(encoding="utf-8"), base), encoding="utf-8")
    legal_list = "\n".join(f"- [{title}]({url}): {description}" for title, url, description in legal_links)
    (DIST / "llms.txt").write_text(fill((SRC / "llms.txt").read_text(encoding="utf-8"),
                                        {**base, "LEGAL_LINKS": legal_list}), encoding="utf-8")
    (DIST / "site.webmanifest").write_text(fill((SRC / "site.webmanifest").read_text(encoding="utf-8"), base),
                                           encoding="utf-8")
    urls = "".join(
        f"  <url><loc>{site_url}{path}</loc><lastmod>{today.isoformat()}</lastmod></url>\n"
        for path, _, indexable in pages if indexable
    )
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n",
        encoding="utf-8")
    (DIST / ".nojekyll").write_text("", encoding="utf-8")
    if config.get("custom_domain"):
        (DIST / "CNAME").write_text(config["custom_domain"].strip() + "\n", encoding="utf-8")

    problems = audit(pages, site_url)
    for warning in placeholders:
        print("UYARI:", warning)
    for problem in problems:
        print("SEO HATASI:", problem)
    print(f"{len(pages)} sayfa üretildi → {DIST}")
    return 1 if problems else 0


def audit(pages, site_url: str):
    """Her sayfada tek H1, başlık/açıklama uzunluğu, canonical ve dil etiketini denetler."""
    problems = []
    for path, file, indexable in pages:
        text = file.read_text(encoding="utf-8")
        name = path or "index.html"
        h1 = len(re.findall(r"<h1[\s>]", text))
        if h1 != 1:
            problems.append(f"{name}: {h1} adet <h1> var (1 olmalı)")
        title = re.search(r"<title>(.*?)</title>", text, re.S)
        if not title or not title.group(1).strip():
            problems.append(f"{name}: <title> yok")
        elif len(html.unescape(title.group(1).strip())) > TITLE_MAX:
            problems.append(f"{name}: başlık {len(html.unescape(title.group(1)))} karakter (en fazla {TITLE_MAX})")
        description = re.search(r'<meta name="description" content="([^"]*)"', text)
        if not description:
            problems.append(f"{name}: meta description yok")
        elif len(html.unescape(description.group(1))) > DESCRIPTION_MAX:
            problems.append(f"{name}: açıklama {len(html.unescape(description.group(1)))} karakter (en fazla {DESCRIPTION_MAX})")
        if '<html lang="en"' not in text:
            problems.append(f"{name}: <html lang=\"en\"> yok")
        robots = re.search(r'<meta name="robots" content="([^"]*)"', text)
        if indexable:
            canonical = re.search(r'<link rel="canonical" href="([^"]*)"', text)
            if not canonical or canonical.group(1) != site_url + path:
                problems.append(f"{name}: canonical eksik veya yanlış")
            if robots and "noindex" in robots.group(1):
                problems.append(f"{name}: indekslenmesi gereken sayfa noindex")
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
            try:
                json.loads(block)
            except json.JSONDecodeError as err:
                problems.append(f"{name}: JSON-LD bozuk ({err})")
        for image in re.findall(r"<img\b[^>]*>", text):
            if "alt=" not in image:
                problems.append(f"{name}: alt metni olmayan görsel")
    return problems


if __name__ == "__main__":
    sys.exit(build(strict="--strict" in sys.argv))
