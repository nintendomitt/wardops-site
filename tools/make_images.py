"""Favicon, uygulama ikonları ve paylaşım görselini (og-image) üretir.

SVG'ler macOS QuickLook (WebKit) ile PNG'ye çevrilir; bu yüzden betik yalnızca
macOS'ta çalışır. Üretilen dosyalar src/assets altına yazılır ve depoya eklenir;
site derlemesi (build.py) bu betiğe ihtiyaç duymaz.

Paylaşım görselindeki yazılar Inter ile çizilir (SF Pro'nun lisansı görsel
üretimine izin vermez). Renkler marka brifindendir.

Kullanım (proje kökünden, PyMuPDF kurulu Python ile):
    backend/.venv/bin/python website/tools/make_images.py
"""
from __future__ import annotations

import base64
import subprocess
import tempfile
from pathlib import Path

import fitz  # PyMuPDF: yalnızca kırpma ve PNG yazımı için

ASSETS = Path(__file__).resolve().parents[1] / "src" / "assets"
FONT = ASSETS / "fonts" / "inter-latin.woff2"
QL_SCALE = 1.5625   # QuickLook SVG'yi bu oranda büyütür; genişlik buna bölünerek verilir

GRADIENT = ('<linearGradient id="tide" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="#1FB5A5"/><stop offset=".55" stop-color="#2B63D9"/>'
            '<stop offset="1" stop-color="#183C8C"/></linearGradient>')


def mark(x: float, y: float, size: float, stroke: float = 4) -> str:
    scale = size / 48
    return (f'<g transform="translate({x} {y}) scale({scale})"><rect width="48" height="48" rx="12" fill="url(#tide)"/>'
            f'<path d="M11 16l6.5 16 6.5-11 6.5 11L37 16" stroke="#fff" stroke-width="{stroke}" fill="none" '
            f'stroke-linecap="round" stroke-linejoin="round"/></g>')


CANVAS = 1200   # QuickLook ölçeği bu boyutta doğrulandı; küçük boyutlar buradan küçültülür


def draw(svg_body: str) -> fitz.Pixmap:
    """1200×1200 tuvalde SVG'yi çizer (şeffaflık korunur)."""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS / QL_SCALE:.4f}" height="{CANVAS / QL_SCALE:.4f}" '
           f'viewBox="0 0 {CANVAS} {CANVAS}">{svg_body}</svg>')
    with tempfile.TemporaryDirectory() as tmp:
        source = Path(tmp) / "image.svg"
        source.write_text(svg, encoding="utf-8")
        subprocess.run(["qlmanage", "-t", "-s", str(CANVAS), "-o", tmp, str(source)],
                       check=True, capture_output=True)
        return fitz.Pixmap(str(Path(tmp) / "image.svg.png"))


def save(pix: fitz.Pixmap, out: Path) -> None:
    pix.save(str(out))
    print(f"{out.name}: {pix.width}×{pix.height}")


def icon(size: int, out: Path, stroke: float = 4, square: bool = False) -> None:
    """Uygulama ikonu. `square`: köşesiz tam kare (iOS köşeleri kendisi yuvarlar)."""
    if square:
        scale = CANVAS / 48
        body = (f'<defs>{GRADIENT}</defs><g transform="scale({scale})"><rect width="48" height="48" fill="url(#tide)"/>'
                f'<path d="M11 16l6.5 16 6.5-11 6.5 11L37 16" stroke="#fff" stroke-width="{stroke}" fill="none" '
                f'stroke-linecap="round" stroke-linejoin="round"/></g>')
    else:
        body = f"<defs>{GRADIENT}</defs>{mark(0, 0, CANVAS, stroke)}"
    pix = draw(body)
    if square and pix.alpha:
        pix = fitz.Pixmap(pix, 0)
    save(fitz.Pixmap(pix, size, size, None), out)


def og_image(out: Path) -> None:
    font = base64.b64encode(FONT.read_bytes()).decode()
    style = (f'<style>@font-face{{font-family:"Inter";src:url(data:font/woff2;base64,{font}) format("woff2");'
             f'font-weight:400 700}} text{{font-family:"Inter"}}</style>')
    body = f"""<defs>{GRADIENT}
      <radialGradient id="glow1" cx="0.92" cy="0.1" r="0.55"><stop offset="0" stop-color="#1FB5A5" stop-opacity=".16"/><stop offset="1" stop-color="#1FB5A5" stop-opacity="0"/></radialGradient>
      <radialGradient id="glow2" cx="0.75" cy="0.95" r="0.5"><stop offset="0" stop-color="#2B63D9" stop-opacity=".12"/><stop offset="1" stop-color="#2B63D9" stop-opacity="0"/></radialGradient>
    </defs>{style}
    <rect width="1200" height="1200" fill="#FBFBF9"/>
    <rect width="1200" height="630" fill="url(#glow1)"/><rect width="1200" height="630" fill="url(#glow2)"/>
    {mark(80, 72, 60)}
    <text x="156" y="113" font-size="34" font-weight="700" fill="#0F1C2E" letter-spacing="-0.6">Ward<tspan fill="#0B7A72" font-weight="600">Ops</tspan></text>
    <text x="80" y="236" font-size="60" font-weight="700" fill="#0F1C2E" letter-spacing="-2">Documents, email</text>
    <text x="80" y="308" font-size="60" font-weight="700" fill="#0F1C2E" letter-spacing="-2">and tracking</text>
    <text x="80" y="380" font-size="60" font-weight="700" fill="#0B7A72" letter-spacing="-2">in one place.</text>
    <text x="80" y="452" font-size="27" fill="#56657A">Operations software for ocean</text>
    <text x="80" y="490" font-size="27" fill="#56657A">freight forwarders.</text>
    <text x="80" y="566" font-size="20" font-weight="600" fill="#0B7A72" letter-spacing="1.6">EARLY ACCESS · FCL OCEAN FREIGHT</text>

    <g transform="translate(700 150)">
      <rect x="0" y="0" width="420" height="330" rx="22" fill="#FFFFFF" stroke="#DDE3E1" stroke-width="2"/>
      <text x="32" y="58" font-size="24" font-weight="700" fill="#0F1C2E">OI-26090118</text>
      <rect x="244" y="32" width="146" height="36" rx="18" fill="#FFF3DC"/>
      <circle cx="265" cy="50" r="5" fill="#8F5E00"/>
      <text x="278" y="57" font-size="17" font-weight="600" fill="#8F5E00">Discharged</text>
      <text x="32" y="98" font-size="19" font-weight="600" fill="#0F1C2E">Harbor &amp; Pine Imports</text>
      <text x="32" y="128" font-size="17" fill="#56657A">Istanbul → New York</text>
      <line x1="32" y1="152" x2="388" y2="152" stroke="#E9EDEB" stroke-width="2"/>
      <text x="32" y="184" font-size="14" font-weight="600" fill="#56657A" letter-spacing="1">ETA</text>
      <text x="32" y="212" font-size="21" font-weight="700" fill="#0F1C2E">18 Oct</text>
      <rect x="110" y="192" width="58" height="26" rx="7" fill="#FCE8E8"/>
      <text x="119" y="211" font-size="15" font-weight="700" fill="#B42A33">+17d</text>
      <text x="220" y="184" font-size="14" font-weight="600" fill="#56657A" letter-spacing="1">LAST FREE DAY</text>
      <text x="220" y="212" font-size="21" font-weight="700" fill="#0F1C2E">27 Oct</text>
      <line x1="32" y1="238" x2="388" y2="238" stroke="#E9EDEB" stroke-width="2"/>
      <text x="32" y="268" font-size="14" font-weight="600" fill="#56657A" letter-spacing="1">NEEDS ATTENTION</text>
      <circle cx="39" cy="294" r="6" fill="#B42A33"/>
      <text x="56" y="300" font-size="17" fill="#26364B">Free time ends in 2 days</text>
    </g>"""
    pix = draw(body)
    if pix.alpha:
        pix = fitz.Pixmap(pix, 0)
    cropped = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 1200, 630), False)
    cropped.copy(pix, fitz.IRect(0, 0, 1200, 630))
    cropped.save(str(out), jpg_quality=80)
    print(f"{out.name}: {cropped.width}×{cropped.height}")


def favicon_svg(out: Path) -> None:
    out.write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">'
        f"<defs>{GRADIENT}</defs>{mark(0, 0, 48, 4.6)}</svg>\n", encoding="utf-8")
    print(f"{out.name}: SVG")


if __name__ == "__main__":
    favicon_svg(ASSETS / "favicon.svg")
    icon(48, ASSETS / "favicon-48.png", stroke=5.5)
    icon(180, ASSETS / "apple-touch-icon.png", stroke=4.4, square=True)
    icon(192, ASSETS / "icon-192.png", stroke=4.4)
    og_image(ASSETS / "og-image.jpg")
