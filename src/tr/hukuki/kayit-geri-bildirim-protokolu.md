# Ek-3: İşlem Kayıtları, Kullanım Verileri ve Geri Bildirim Protokolü

Sürüm: 1.2-TASLAK · Tarih: 30 Eylül 2026

Bu Protokol, WardOps Hizmet Sözleşmesinin ayrılmaz ekidir. Platformun hangi kayıtları tuttuğunu,
kullanıcı deneyimi ve geri bildirimlerin nasıl toplandığını, bu kayıtların hangi amaçla
kullanıldığını, kimlerin erişebildiğini ve ne kadar saklandığını düzenler.

## 1. Amaç

1.1. Kayıtlar; (a) hangi işlemin kim tarafından ve ne zaman yapıldığının ispatı, (b) güvenlik
olaylarının tespiti ve incelenmesi, (c) olası uyuşmazlıklarda tarafların sorumluluğunun
belirlenmesi, (d) Hizmetin hatalarının giderilmesi ve geliştirilmesi amacıyla tutulur.

1.2. Kayıtlar, Müşteriyi ve Hizmet Sağlayıcıyı birlikte korur: bir e-postanın otomatik mi yoksa
hangi kullanıcı tarafından gönderildiği, bir belgenin kim tarafından üretildiği veya bir ayarın kim tarafından değiştirildiği bu
kayıtlarla gösterilir.

## 2. Tutulan Kayıtlar

### 2.1. İşlem kaydı

Aşağıdaki işlemler; işlemi yapan kullanıcı, tarih ve saat, ilgili kayıt (dosya, kullanıcı, taslak
vb.) ve özet bilgiyle kaydedilir:

- giriş, Google/Apple ile giriş ve başarısız giriş denemeleri;
- parola değişikliği ve parola sıfırlama;
- firma kaydı, kullanıcı ekleme, rol değişikliği, pasifleştirme;
- yanıt ve bildirimlerin gönderilmesi, elle gönderildi olarak işaretlenmesi, kapatılması ve gönderim
  hataları (alıcılar dahil);
- mail hesabı bağlama ve bağlantı kesme;
- uyarı eşikleri, tarifeler, firma bilgileri, logo ve belge şablonu değişiklikleri;
- belge üretimi ve belge alanlarının elle düzeltilmesi;
- belgenin yapay zekâ ile yeniden okutulması;
- müşteri kartı ve fiyat bilgisi değişiklikleri;
- ortak ana veride (liman) yapılan birleştirmeler;
- sözleşme ve politika kabulleri.

İşlem kaydına **parola, erişim jetonu, anahtar veya benzeri gizli değerler yazılmaz**.

### 2.2. Kabul kaydı

Sözleşme ve politika kabullerinde; kabul eden kullanıcı, firma, belge adı, sürümü, metnin özet değeri,
tarih ve saat, IP adresi ve tarayıcı bilgisi saklanır.

### 2.3. Operasyon geçmişi

Dosyaların kendi geçmişi (ETA değişiklikleri ve kaynakları, olaylar, görevlerin açılıp kapanması,
belgelerin okunması ve doğrulama sonuçları, gönderilen yanıtların içeriği) Müşteri Verisinin parçası
olarak tutulur.

### 2.4. Yapay zekâ kullanım kaydı

Her yapay zekâ çağrısı için tarih, kullanılan model, gönderim biçimi (metin veya görüntü), girdi ve
çıktı jeton (token) sayısı, başarı durumu ve ilgili belge kaydedilir. Bu kayıt belge içeriğini
içermez; maliyet ve kullanım sınırlarının izlenmesi için tutulur.

### 2.5. Teknik kayıtlar

Sunucu ve uygulama hata kayıtları, performans ölçümleri ve güvenlik kayıtları; hataların giderilmesi
ve saldırıların tespiti için tutulur. Bu kayıtlara Müşteri Verisinin içeriği mümkün olduğunca
yazılmaz.

## 3. Kullanıcı Deneyimi ve Geri Bildirimlerin Toplanması

3.1. Hizmet Sağlayıcı, Hizmeti geliştirmek için aşağıdaki yollarla geri bildirim toplayabilir:

- Platform içi geri bildirim formları ve memnuniyet soruları;
- destek talepleri ve e-posta yazışmaları;
- Müşterinin katılmayı kabul ettiği görüşmeler, kullanılabilirlik testleri ve anketler;
- Platformun hangi özelliklerinin ne sıklıkla kullanıldığına ilişkin toplulaştırılmış istatistikler
  (ör. günlük işlenen e-posta sayısı, üretilen belge sayısı, uyarı türlerinin dağılımı).

3.2. Görüşmeler ve kullanılabilirlik testleri **yalnızca katılımcının önceden bilgilendirilmesi ve
onayıyla** kayda alınır (ses, görüntü veya ekran kaydı). Katılımcı kaydın durdurulmasını her zaman
isteyebilir.

3.3. Geri bildirimlerde yer alan kişisel veriler, geri bildirimin değerlendirilmesi tamamlandıktan
sonra anonimleştirilir veya bölüm 5'teki sürelerde silinir.

3.4. Müşterinin adı, logosu veya geri bildirimi; referans, vaka çalışması veya pazarlama amacıyla
**yalnızca Müşterinin yazılı izniyle** kullanılır.

3.5. Hizmet Sağlayıcı, ürün kullanımını ölçmek için üçüncü taraf reklam veya izleme araçları
kullanmaz. Kullanım istatistikleri kişileri tanımlamayacak biçimde toplulaştırılarak kullanılır.

3.6. Geri bildirimler, kullanım istatistikleri ve Müşteri Verisi yapay zekâ modellerinin eğitiminde
kullanılmaz ve üçüncü taraf veya herkese açık yapay zekâ modellerinin eğitimi için hiçbir sağlayıcıyla
paylaşılmaz.

## 4. Erişim

| Kayıt | Müşteri erişimi | Hizmet Sağlayıcı erişimi |
|---|---|---|
| İşlem kaydı | Firma yöneticileri Platformda görür | Yalnızca destek, güvenlik incelemesi veya hukuki gereklilik halinde; erişim kayda alınır |
| Kabul kaydı | Firma yöneticileri talep ettiğinde | Kabulün ispatı ve uyuşmazlık halinde |
| Operasyon geçmişi | Yetkisi olan tüm kullanıcılar | Yalnızca Müşterinin talebiyle destek amacıyla |
| Yapay zekâ kullanım kaydı | Firma yöneticileri (özet) | Maliyet ve kapasite yönetimi |
| Teknik kayıtlar | — (talep halinde olayla ilgili özet) | Operasyon ve güvenlik ekibi |

Kayıtlar kullanıcılar tarafından değiştirilemez veya silinemez. Hizmet Sağlayıcı kayıtların
bütünlüğünü korumak için gerekli teknik tedbirleri alır.

## 5. Saklama Süreleri

| Kayıt | Süre |
|---|---|
| İşlem kaydı | Sözleşme süresince ve sona ermesinden itibaren [2] yıl |
| Kabul kaydı | Sözleşmenin sona ermesinden itibaren [10] yıl |
| Güvenlik ve giriş kayıtları | [2] yıl |
| Yapay zekâ kullanım kaydı | [2] yıl |
| Teknik kayıtlar | [90] gün |
| Görüşme ve test kayıtları | Değerlendirme tamamlanana kadar, en fazla [1] yıl |
| Destek yazışmaları | [3] yıl |

Süresi dolan kayıtlar silinir veya anonim hale getirilir. Hukuki uyuşmazlık veya resmî inceleme
halinde ilgili kayıtlar uyuşmazlık sonuçlanana kadar saklanabilir.

## 6. Kayıtların Delil Değeri

Taraflar, bu Protokol kapsamındaki kayıtların Hizmet Sözleşmesinin 25. maddesi çerçevesinde delil
olarak kullanılabileceğini kabul eder. Müşteri, kayıtların doğruluğuna itiraz etme ve karşı delil
sunma hakkına sahiptir.

## 7. Müşterinin Talepleri

Müşteri; kendi firmasına ait işlem ve kabul kayıtlarının bir kopyasını, olayla ilgili teknik kayıt
özetlerini ve yapay zekâ kullanım dökümünü [DESTEK E-POSTASI] üzerinden talep edebilir. Talepler
makul sürede ve makine tarafından okunabilir biçimde karşılanır.
