# WardOps tanıtım sitesi

Tek sayfalık, İngilizce, açık temalı tanıtım sitesi ve hukuki sayfalar. Düz HTML üretilir; arama
motorları ve yapay zekâ tarayıcıları içeriği JavaScript çalıştırmadan okur.

## Klasörler

| Konum | İçerik |
|---|---|
| `site.json` | Alan adı, iletişim e-postası, form adresi, özel alan adı |
| `src/index.html` | Ana sayfa (tek H1, yapılandırılmış veri, SSS) |
| `src/legal/*.md` | Hukuki metinlerin İngilizce taslakları (Türkçe asılları `backend/legal/`) |
| `src/legal.html`, `src/404.html` | Hukuki sayfa ve 404 şablonları |
| `src/robots.txt`, `src/llms.txt` | Tarayıcı izinleri ve yapay zekâ özeti |
| `src/assets/` | Stil, betik, ikonlar, paylaşım görseli; Inter yazı tipi dosyaları (OFL) depoda tutulmaz, derlemede indirilir |
| `src/assets/brands/` | Gmail ve Outlook logoları (Wikimedia Commons; telifsiz ama tescilli marka, değiştirilmeden kullanılır) |
| `tools/make_images.py` | İkon ve paylaşım görselini yeniden üretir (yalnızca macOS) |
| `build.py` | `src/` → `dist/` derlemesi, sitemap ve SEO denetimi |

## Derleme ve önizleme

```bash
cd website && python3 build.py
cd website/dist && python3 -m http.server 8020
```

`build.py` her sayfada şunları denetler; biri bozulursa hata koduyla çıkar (GitHub Actions da durur):
tek `<h1>`, başlık ≤ 65 karakter, açıklama ≤ 160 karakter, doğru canonical, `lang="en"`,
indekslenecek sayfada `noindex` olmaması, geçerli JSON-LD, görsellerde alt metni.

Yayından önce `python3 build.py --strict` yer tutucu alan adı veya e-posta kaldıysa hata verir.

## Yayın (GitHub Pages)

1. Bu klasörü ayrı bir GitHub deposu olarak gönder (depo kökü `website/` olmalı).
2. Depo ayarlarında **Settings → Pages → Source: GitHub Actions** seç.
3. `site.json` içinde `url` alanını gerçek adresle değiştir:
   - özel alan adıyla: `"url": "https://alanadi.com/"` ve `"custom_domain": "alanadi.com"`
   - alan adı yokken: `"url": "https://KULLANICI.github.io/DEPO/"`
4. `main` dalına gönderince site derlenip yayımlanır.

**Önemli:** Arama motorları `robots.txt` ve `llms.txt` dosyalarını yalnızca alan adının kökünde
okur. `KULLANICI.github.io/DEPO/` biçimindeki adreste bu dosyalar kökte olmadığı için
dikkate alınmaz. SEO için özel alan adı (veya `KULLANICI.github.io` adlı depo) gerekir.

GitHub Pages koşulları, sitenin kendisinin ticari bir SaaS olarak çalışmasına izin vermez;
tanıtım sayfası bu kapsamda değildir. Uygulamanın kendisi başka bir sunucuda çalışacaktır.

## Form

`form_endpoint` boşsa "Request early access" düğmesi kullanıcının e-posta programını doldurulmuş
bir iletiyle açar (`contact_email` adresine). Bir form hizmeti (ör. Formspree) kullanılacaksa
adresi `form_endpoint` alanına yaz; form JSON olarak oraya gönderilir. Gizlilik politikasının
9.1 maddesindeki köşeli parantez de buna göre güncellenmeli.

## İçerik kuralları

- Sitede ürünün yapmadığı bir şey vaat edilmez (bkz. `context/konumlandirma.md`).
- Rakip adı verilmez; karşılaştırma "klasik kurulum" üzerinden yapılır.
- Gmail/Outlook logoları yalnızca "ile çalışır" anlamında kullanılır; renkleri veya biçimleri değiştirilmez,
  Google ya da Microsoft ile ortaklık ima edilmez (alt bilgide marka notu var).
- Mor tonları kullanılmaz; yazı tipi Apple cihazlarda sistem yazı tipi (SF Pro), diğerlerinde Inter.
