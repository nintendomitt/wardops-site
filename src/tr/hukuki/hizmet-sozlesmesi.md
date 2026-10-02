# WardOps Hizmet Sözleşmesi ve Kullanım Koşulları

Sürüm: 1.7-TASLAK · Tarih: 3 Ekim 2026

Bu Sözleşme, WardOps platformunu kullanan işletme ile platformu işleten şirket arasındaki
hak ve yükümlülükleri düzenler. Sözleşmenin ekleri (Ek-1 Otomasyon ve Sorumluluk
Paylaşımı Protokolü; Ek-2 Veri İşleme Sözleşmesi; Ek-3 İşlem Kayıtları, Kullanım Verileri ve
Geri Bildirim Protokolü) Sözleşmenin ayrılmaz parçasıdır. Ekler ile bu metin arasında çelişki
olursa, konusuna özgü olduğu ölçüde ekteki hüküm uygulanır.

## 1. Taraflar

1.1. **Hizmet Sağlayıcı:** [ŞİRKET UNVANI], [ADRES], MERSİS No: [MERSİS NO], Vergi Dairesi ve
No: [VERGİ DAİRESİ / NO], e-posta: [E-POSTA], KEP: [KEP ADRESİ] ("Hizmet Sağlayıcı").

1.2. **Müşteri:** Platforma kayıt olurken veya sipariş formunda bilgileri verilen ve bu
Sözleşmeyi elektronik ortamda kabul eden tüzel kişi ya da tacir ("Müşteri").

1.3. Hizmet yalnızca ticari amaçla faaliyet gösteren işletmelere sunulur. Müşteri, tüketici
sıfatıyla hareket etmediğini, Hizmeti ticari veya mesleki faaliyeti kapsamında kullandığını
kabul eder.

## 2. Tanımlar

Bu Sözleşmede büyük harfle başlayan terimler aşağıdaki anlamları taşır:

- **Platform / Hizmet:** WardOps adıyla sunulan; sevkiyat dosyası, konteyner, rota, olay, belge,
  e-posta ve görev kayıtlarını yöneten, uyarı üreten, taslak hazırlayan ve belge üreten
  bulut tabanlı yazılım hizmeti, buna bağlı uygulama programlama arayüzleri (API), yönetim
  komutları ve belgeler.
- **Yetkili Kullanıcı:** Müşterinin Platforma eriştirdiği, Müşteri adına işlem yapan gerçek
  kişiler (çalışanlar, danışmanlar ve Müşterinin yetkilendirdiği diğer kişiler).
- **Yönetici Kullanıcı:** Müşteri hesabında kullanıcı ekleme, rol değiştirme, entegrasyon
  bağlama, firma bilgilerini ve şablonları değiştirme yetkisine sahip Yetkili Kullanıcı.
- **Müşteri Verisi:** Müşteri veya Yetkili Kullanıcılar tarafından Platforma yüklenen,
  girilen, Entegrasyonlar aracılığıyla Platforma aktarılan ya da Müşteri adına Platformda
  üretilen her türlü veri; sevkiyat, konteyner, taraf, belge, e-posta, görev ve kayıt verileri
  dahil.
- **Operasyon Verisi:** Müşteri Verisinin, Müşterinin taşıma ve lojistik faaliyetlerine ilişkin
  kısmı (dosya, konşimento, konteyner, varış bildirimi, serbest bırakma, gümrük ve ISF bilgileri
  vb.).
- **Kişisel Veri:** 6698 sayılı Kişisel Verilerin Korunması Kanunu ("KVKK") ve uygulanabildiği
  ölçüde diğer veri koruma mevzuatı anlamında kimliği belirli veya belirlenebilir gerçek kişiye
  ilişkin her türlü bilgi.
- **Çıktı:** Platformun Müşteri Verisini işleyerek ürettiği her türlü sonuç: ayrıştırılmış
  alanlar, eşleştirmeler, sınıflandırmalar, tahmini tarihler, aşama bilgisi, uyarılar,
  görevler, istatistikler, yanıt ve bildirimler, belgeler (arrival notice, delivery order, cargo
  release, proof of delivery vb.), muhasebe belgeleri (invoice, debit note, credit note, ekstre)
  ve raporlar.
- **Taslak:** Platformun hazırladığı ve henüz gönderilmemiş metin veya belge; otomatik
  gönderilemeyen veya otomatik gönderimi kapalı firmada Yetkili Kullanıcının göndermesini bekler.
- **Kullanıcı İşlemi:** Bir Yetkili Kullanıcının Platformda açık bir eylemle (ör. "Gönder",
  "İndir", "Kaydet", "Kes") başlattığı ve dış dünyada etki doğurabilecek işlem.
- **Otomatik İşlem:** Platformun kullanıcı eylemi olmadan yaptığı işlem (ör. e-postanın dosyaya
  bağlanması, uyarı üretilmesi, yanıt hazırlanması).
- **Otomatik Gönderim:** Ek-1'de kapsamı ve frenleri tanımlanan, Platformun Müşteri adına ve
  Müşterinin bağlı e-posta hesabından kullanıcı onayı beklemeden gönderdiği ileti (durum sorusuna
  yanıt ile ETA değişikliği, gemi varışı ve çekilebilirlik bildirimleri). Müşteri Otomatik
  Gönderimi kapatabilir.
- **Entegrasyon:** Müşterinin yetkilendirmesiyle Platforma bağlanan dış hizmetler (ör. Microsoft
  365/Outlook, Gmail, takip veri sağlayıcıları, ISF sağlayıcıları, Paraşüt gibi muhasebe programları,
  Google veya Apple ile giriş).
- **Üçüncü Taraf Hizmeti:** Hizmet Sağlayıcının kontrolünde olmayan, Entegrasyonlar veya alt
  işleyenler aracılığıyla kullanılan hizmetler (taşıyıcı ve terminal sistemleri, e-posta
  sağlayıcıları, yapay zekâ sağlayıcıları, barındırma sağlayıcıları vb.).
- **Yapay Zekâ Özelliği:** Belgelerden veri okunması gibi, Müşterinin tercihine veya hesap
  ayarlarına bağlı olarak üçüncü taraf yapay zekâ modelleri kullanılarak gerçekleştirilen
  işlemler.
- **Şablon:** Belge üretiminde kullanılan, Platformun hazır şablonları veya Müşterinin
  yüklediği kendi şablonları.
- **Gizli Bilgi:** Bir Tarafın diğerine açıkladığı, gizli olduğu belirtilen veya niteliği
  gereği gizli sayılması gereken her türlü bilgi; Müşteri Verisi, fiyat bilgisi, ticari
  sırlar, güvenlik bilgileri dahil.
- **Güvenlik Olayı:** Müşteri Verisinin yetkisiz erişime, açıklanmaya, değiştirilmeye,
  kaybolmaya veya yok edilmeye maruz kaldığı olay.

## 3. Sözleşmenin Kurulması ve Elektronik Kabul

3.1. Sözleşme, Müşteri adına hareket eden kişinin kayıt ekranında Sözleşmeyi ve eklerini
okuduğunu ve kabul ettiğini belirten kutucuğu işaretleyerek kaydı tamamlamasıyla veya
Hizmet Sağlayıcı ile yazılı ya da elektronik bir sipariş formu imzalanmasıyla kurulur.

3.2. Kabulü gerçekleştiren kişi, Müşteriyi bu Sözleşmeyle bağlamaya yetkili olduğunu beyan ve
taahhüt eder. Yetkisiz kabulden doğan her türlü sonuç, kabulü yapan kişi ve Müşteri
bakımından müteselsilen geçerlidir.

3.3. Kabul anında Platform; kabul eden kullanıcıyı, firmayı, kabul edilen belgelerin adını ve
sürümünü, belge metninin özet değerini (hash), tarih ve saati, IP adresini ve tarayıcı
bilgisini kaydeder. Taraflar bu kayıtların kabulün delili olduğunu kabul eder.

3.4. Sözleşmenin ve eklerinin güncel sürümleri Platform içinde ve https://wardops.co üzerinden her
zaman erişilebilir durumdadır. Müşteri, Sözleşmeyi kaydetme ve yazdırma imkânına sahiptir.

## 4. Hizmetin Tanımı ve Niteliği

4.1. Platform, deniz yolu taşımacılığında faaliyet gösteren freight forwarder ve benzeri
işletmelerin **operasyon süreçlerini destekleyen** bir yazılım hizmetidir. Başlıca işlevleri:
sevkiyat dosyası ve konteyner kayıtlarının tutulması; takip verisinin toplanması ve yükün
aşamasının hesaplanması; tahmini varış tarihi (ETA) geçmişinin tutulması; e-postaların
dosyalarla eşleştirilmesi ve sınıflandırılması; belgelerden alan okunması; belge zorunlulukları
ve süreler için uyarı ve görev üretilmesi; serbest bırakma ve ücretsiz süre takibi; yanıt ve
bildirim Taslaklarının hazırlanması; Şablonlar ile belge üretimi; kullanıcı ve yetki yönetimi;
işlem kayıtları ve raporlar.

4.2. **Platform bir karar destek aracıdır.** Müşterinin operasyonel, ticari, hukuki ve mesleki
kararlarını Müşteri adına vermez. Platformun ürettiği Çıktılar, Müşterinin kendi kontrolü ve
değerlendirmesi için hazırlanır.

4.3. Hizmet Sağlayıcı; taşıyıcı, NVOCC, freight forwarder, gümrük müşaviri, gümrük komisyoncusu
(customs broker), antrepo işletmecisi, sigortacı, hukuk veya vergi danışmanı **değildir** ve bu
sıfatlarla hareket etmez. Platform; gümrük beyanı, ISF, AMS veya benzeri resmî beyanları
Müşterinin yerine yapmaz, bu beyanların doğruluğunu veya zamanında yapılmasını garanti etmez.
Resmî beyanlar Müşterinin veya Müşterinin yetkilendirdiği üçüncü kişilerin sorumluluğundadır.

4.4. Platform fiyat hesaplamaz, teklif hazırlamaz ve satış işlemi yapmaz. Müşterinin Platforma
kaydettiği fiyat bilgileri (ör. satış biriminin paylaştığı ücretler) yalnızca Müşterinin başvuru
kaydıdır; bu bilgilerin doğruluğu ve kullanımı Müşterinin sorumluluğundadır.

4.5. Hizmetin kapsamı, özellikleri ve arayüzü zaman içinde geliştirilebilir, değiştirilebilir
veya kaldırılabilir. Esaslı bir işlevin kaldırılması halinde Hizmet Sağlayıcı makul süre önce
bildirimde bulunur.

## 5. Hesap, Yetkili Kullanıcılar ve Erişim Güvenliği

5.1. Müşteri hesabı ilk kaydı yapan kişi tarafından açılır; bu kişi hesabın ilk Yönetici
Kullanıcısı olur. Yönetici Kullanıcılar diğer Yetkili Kullanıcıları ekler, rollerini belirler,
erişimlerini kaldırır ve hesap ayarlarını yönetir.

5.2. Müşteri; Yetkili Kullanıcıların kimliğini doğrulamak, yalnızca işi gereği erişmesi gereken
kişilere erişim vermek, görev değişikliği veya iş ilişkisinin sona ermesi halinde erişimi
**gecikmeksizin** kaldırmakla yükümlüdür. Yetkili Kullanıcıların Platformdaki tüm işlemleri
Müşterinin işlemi sayılır.

5.3. Giriş; e-posta ve parola ile veya Google ya da Apple gibi kimlik sağlayıcılar aracılığıyla
yapılabilir. Kimlik sağlayıcı hesaplarının güvenliği, Yetkili Kullanıcının ve Müşterinin
sorumluluğundadır. Müşteri, hesabına bağlı kimlik sağlayıcı hesaplarının ele geçirilmesinden
doğan zararlardan Hizmet Sağlayıcıyı sorumlu tutamaz; ancak bu tür bir durumu fark ettiğinde
derhal Hizmet Sağlayıcıya bildirir.

5.4. Parolalar ve erişim bilgileri kişiye özeldir; paylaşılamaz. Hizmet Sağlayıcı parolaları
geri döndürülemez biçimde (özet değer olarak) saklar ve hiçbir zaman parola sormaz.

5.5. Yetkisiz erişim şüphesi halinde Müşteri; ilgili kullanıcıyı pasifleştirmek, parolaları
değiştirmek, Entegrasyon bağlantılarını kesmek ve Hizmet Sağlayıcıya [GÜVENLİK E-POSTASI]
adresinden bildirimde bulunmakla yükümlüdür.

## 6. Müşterinin Yükümlülükleri

Müşteri aşağıdakileri kabul, beyan ve taahhüt eder:

6.1. **Verinin doğruluğu:** Platforma girdiği veya aktardığı verilerin doğru, güncel ve eksiksiz
olmasından; müşteri, taraf, adres, e-posta ve iletişim bilgilerinin doğruluğundan sorumludur.
Platformun ürettiği Çıktıların kalitesi, girilen verinin kalitesine bağlıdır.

6.2. **Çıktıların kontrolü:** Çıktıları, özellikle üçüncü kişilere gönderilecek veya
operasyonel karara esas alınacak olanları (alıcı adresleri, konteyner ve konşimento numaraları,
tarihler, serbest bırakma durumu, teslim adresi, ücretsiz süre), kullanmadan önce kendi
kaynaklarıyla karşılaştırarak kontrol eder.

6.3. **Gönderim sorumluluğu:** Otomatik Gönderimle veya bir Yetkili Kullanıcının işlemiyle
gönderilen, indirilen, kaydedilen ya da üçüncü kişilere iletilen her ileti ve belge, Müşterinin
kendi beyanı ve işlemidir. Müşteri, Otomatik Gönderimin dayandığı kayıtların doğruluğunu ve
özelliği açık tutma kararını üstlenir (ayrıntılar Ek-1'dedir).

6.4. **Hukuka uygunluk:** Hizmeti; gümrük, dış ticaret, ihracat kontrolü, yaptırımlar, veri
koruma, elektronik ticaret, rekabet ve diğer uygulanabilir mevzuata uygun şekilde kullanır.
ABD Gümrük ve Sınır Koruma (CBP), Federal Denizcilik Komisyonu (FMC) ve benzeri kurumların
kuralları kapsamındaki yükümlülükler Müşteriye aittir.

6.5. **Kişisel veriler:** Platforma aktardığı Kişisel Veriler bakımından veri sorumlusu olduğunu;
bu verilerin işlenmesi ve Hizmet Sağlayıcıya aktarılması için gerekli hukuki sebeplere,
aydınlatma yükümlülüğünün yerine getirilmesine ve gerektiğinde açık rızaya sahip olduğunu kabul
eder (Ek-2).

6.6. **Entegrasyon yetkisi:** Bağladığı e-posta hesapları ve diğer Entegrasyonlar üzerinde
yetkili olduğunu; bu hesaplardaki verilerin Platform tarafından işlenmesine ilişkin gerekli
iç izinleri ve bilgilendirmeleri yaptığını kabul eder.

6.7. **Bağımsız kayıt:** Resmî yükümlülükleri ve kritik süreleri (ör. ISF süresi, son ücretsiz
gün, boş konteyner iade süresi) yalnızca Platform uyarılarına dayanarak takip etmez; kendi iç
kontrollerini sürdürür.

6.8. **Yasaklı kullanım:** Platformu; zararlı yazılım yaymak, güvenliği aşmaya çalışmak, tersine
mühendislik yapmak (emredici hukukun izin verdiği haller hariç), aşırı yük oluşturmak, başka
müşterilerin verilerine erişmeye çalışmak, yanıltıcı veya hukuka aykırı içerik göndermek, spam
veya izinsiz ticari ileti göndermek amacıyla kullanamaz.

6.9. **Hata bildirimi:** Çıktılarda fark ettiği hataları, özellikle sistematik görünenleri,
makul süre içinde Hizmet Sağlayıcıya bildirir.

## 7. Otomasyon ve Otomatik Gönderim

7.1. Platform, Müşteri adına yalnızca Ek-1'de sayılan iletileri (durum sorusuna yanıt; ETA
değişikliği, gemi varışı ve yükün çekilebilir olması bildirimleri) Otomatik Gönderimle, Müşterinin
bağlı e-posta hesabından gönderir. Bu iletiler yalnızca dosyada kayıtlı bilgilerden kural tabanlı
olarak oluşturulur; metin yapay zekâ ile yazılmaz. **Bunların dışındaki hiçbir e-posta, mesaj veya
belge, bir Yetkili Kullanıcının işlemi olmadan üçüncü kişilere gönderilmez.** Her gönderim; gönderen
(Platform veya kullanıcı), tarih, saat ve alıcılarla kayıt altına alınır.

7.2. Otomatik Gönderim, Ek-1'deki frenlere tabidir: ekip içi alıcılara, otomatik yanıtlayıcılara ve
aynı alıcıya kısa süre içinde tekrar gönderim yapılmaz; bağlı hesap yoksa veya Müşteri özelliği
kapatmışsa ileti gönderilmez ve Yetkili Kullanıcının göndermesini bekler. Müşteri Otomatik Gönderimi
firma ayarlarından her zaman kapatabilir.

7.3. Otomatik İşlemler ve Otomatik Gönderim hatalı olabilir. Müşteri; Otomatik Gönderimin dayandığı
kayıtları (ETA, serbest bırakma durumu, taraflar ve e-posta adresleri) doğru ve güncel tutmakla,
e-posta eşleşmelerini ve gönderilen iletileri düzenli olarak gözden geçirmekle ve özelliğin uygun
olmadığı durumlarda Otomatik Gönderimi kapatmakla yükümlüdür. **Otomatik Gönderimin içeriğinden,
dayandığı kayıtların doğruluğundan ve Kullanıcı İşlemiyle yapılan gönderimlerin içerik, alıcı ve
sonuçlarından Müşteri sorumludur.** Yanlış alıcıya veya yanlış içerikle gönderilen bir e-postanın
doğurabileceği ticari kayıplar (yükün yanlış tarafa teslimi, gizli bilginin açıklanması, ücret kaybı,
itibar kaybı vb.) bu kapsamdadır.

7.4. Platformun bir yazılım hatası nedeniyle Ek-1'de tanımlanan kapsam veya frenler dışında üçüncü
kişilere iletişim kurulması halinde, Hizmet Sağlayıcı durumu öğrendiğinde derhal Müşteriyi
bilgilendirir, hatayı gidermek için makul çabayı gösterir ve sorumluluğu Madde 18'de belirtilen
çerçevede değerlendirilir.

7.5. Platformda üretilen muhasebe belgeleri (invoice, debit note, credit note, ekstre), Müşterinin
girdiği masraf kalemlerinden oluşturulan ticari belgelerdir. Platform tutar önermez ve hesaplamayı
girilen miktar ve birim fiyat üzerinden yapar. Bu belgeler, vergi mevzuatının öngördüğü resmî fatura
veya belge (ör. e-Fatura, e-Arşiv Fatura) yerine geçmez; resmî belge düzenleme, vergi ve muhasebe
kayıt yükümlülükleri Müşteriye aittir.

7.6. Otomasyon ve sorumluluk paylaşımının işlev bazında ayrıntıları Ek-1'de yer alır.

## 8. Yapay Zekâ Özellikleri ve Otomatik Veri Okuma

8.1. Platform, belgelerden alan okumak için önce belgenin kendi metnini ve yerel optik karakter
tanıma (OCR) yöntemlerini kullanır. Bu yöntemler yetersiz kaldığında ve Yapay Zekâ Özelliği
hesap için etkinse, belgenin gerekli kısmı (metni veya küçültülmüş sayfa görüntüsü) üçüncü
taraf bir yapay zekâ sağlayıcısına gönderilebilir.

8.2. Yapay zekâ ile veya kurallarla okunan değerler **hatalı, eksik veya yanıltıcı olabilir.**
Platform bu değerleri bazı kurallarla (ör. konteyner numarası kontrol basamağı, tarih biçimi)
denetler; ancak bu denetimler doğruluğu garanti etmez. Okunan değerler, var olan kayıtların
üzerine yazılmaz; yalnızca boş alanları doldurur ve çelişkiler uyarı olarak gösterilir.

8.3. Müşteri Verisi, üçüncü taraf veya herkese açık yapay zekâ modellerinin eğitilmesi ya da
geliştirilmesi için hiçbir sağlayıcıyla paylaşılmaz; Hizmet Sağlayıcı da Müşteri Verisini yapay zekâ
modeli eğitmek için kullanmaz. Yapay Zekâ Özelliğinde yalnızca, Müşteri Verisini model eğitiminde
kullanmayacağını sözleşme koşullarında taahhüt eden sağlayıcılar kullanılır; Hizmet Sağlayıcı bu
sağlayıcılara eğitim amaçlı kullanım izni vermez ve geri bildirim göndermez. Kullanılan sağlayıcılar
Ek-2'deki alt işleyen listesinde belirtilir.

8.3a. Hizmet Sağlayıcı, Müşteri Verisini yalnızca kendi altyapısında, Hizmetin okuma kurallarını,
eşleştirme ve uyarı mantığını düzeltmek ve geliştirmek için kullanabilir (ör. yanlış okunan bir belge
düzeninin kuralını düzeltmek). Bu kullanımda Müşteri Verisi başka müşterilere gösterilmez, üçüncü
kişilerle paylaşılmaz ve geliştirme çalışmalarında dış yapay zekâ araçlarına verilmez.

8.4. Müşteri, Yapay Zekâ Özelliğini Yönetim ekranından kapatabilir. Bu durumda belgeler yalnızca metin
ve OCR ile okunur. E-postalar her durumda kurallarla sınıflandırılır.

## 9. Üçüncü Taraf Verileri ve Hizmetleri

9.1. Konteyner hareketleri, gemi seferleri, tahmini varış tarihleri, terminal ve serbest bırakma
durumları gibi bilgiler taşıyıcılardan, terminallerden, veri sağlayıcılarından veya e-postalardan
gelir. Hizmet Sağlayıcı bu bilgilerin **doğruluğunu, eksiksizliğini, güncelliğini veya
kesintisiz erişilebilirliğini garanti etmez.** Tahmini tarihler niteliği gereği değişebilir.

9.2. Entegrasyonlar, ilgili üçüncü tarafın hizmet koşullarına tabidir. Üçüncü tarafın hizmetinde
kesinti, değişiklik, erişim kısıtlaması veya yetki iptali olması Hizmet Sağlayıcının kusuru
sayılmaz.

9.3. Müşteri, bağladığı e-posta hesabı üzerinden Platformun yalnızca operasyonla ilgili görünen
e-postaları işlediğini; filtrelerin kusursuz olmadığını, bazı ilgili e-postaların
işlenmeyebileceğini veya ilgisiz bazı e-postaların işlenebileceğini kabul eder.

9.4. **Muhasebe aktarımı:** Müşteri bir muhasebe programını (ör. Paraşüt) bağladığında, aktarmayı seçtiği
belgeler ve ilgili cari bilgileri (unvan, vergi numarası, e-posta, adres) Müşterinin talimatıyla bu
programa iletilir; muhasebe aktarım dosyası Müşteri tarafından indirilir ve kendi programına aktarılır.
Aktarılan belge programda satış faturası olarak oluşur; e-Fatura veya e-Arşiv gibi resmî belgenin
düzenlenmesi ile KDV oranı, istisna ve diğer vergi uygulamalarının doğruluğu Müşterinin
sorumluluğundadır. Belgelerde kullanılan TCMB döviz kuru bilgi amaçlıdır.

9.5. **İşe alım:** Müşteri, iş ilanları ve aday başvuruları için Platformu kullandığında adayların kişisel
verileri bakımından veri sorumlusudur. Başvuru sayfasındaki aydınlatma metni örnek niteliğindedir;
Müşteri kendi aydınlatma yükümlülüğünü yerine getirmekten, verileri amaca uygun süre saklamaktan ve
adayın talebi halinde silmekten sorumludur. Hizmet Sağlayıcı aday verilerini yalnızca Müşteri adına
işler ve ilan platformlarına (ör. LinkedIn, Kariyer.net) aday verisi göndermez.

9.6. **Evrak teslim hizmeti:** Müşteri, Platform üzerinden orijinal evrakın (ör. konşimento aslı, ticari fatura,
menşe belgesi) teslimi için talep açabilir; Full Automation paketinde koşullar sağlandığında talep Platform
tarafından açılır. Talep, Hizmet Sağlayıcının anlaşmalı kurye veya taşıma firmaları aracılığıyla yerine getirilir:
evrak, Müşterinin belirttiği yerden ve yetkili kişiden teslim alınır ve belirtilen alıcıya (ör. gümrük müşaviri,
liman, acente) teslim edilir. Evrak Hizmet Sağlayıcının ofisine gelmez ve Hizmet Sağlayıcı tarafından saklanmaz.
Teslim alan ve teslim eden kişiler ile zamanlar kayda alınır ve teslim tutanağı düzenlenir. Teslim süreleri kurye
firmasının hizmet koşullarına tabidir; evrakın kaybı, hasarı veya gecikmesinde Hizmet Sağlayıcının sorumluluğu
Madde 18'deki sınırlarla sınırlıdır ve Hizmet Sağlayıcı, kurye firmasına karşı haklarını Müşteri lehine kullanır.
Evrak teslim ücreti ve kapsamı sipariş formunda veya fiyat sayfasında belirtilir.

## 10. Üretilen Belgeler ve Şablonlar

10.1. Platform; arrival notice, delivery order, cargo release ve benzeri belgeleri Müşterinin
firma bilgileri ve dosya kayıtları kullanılarak üretir. **Bu belgelerin düzenleyeni ve
sorumlusu Müşteridir.** Hizmet Sağlayıcı belgelerin taraflarından biri değildir.

10.2. Belge üretimi sırasında Platform eksik alanları ve dikkat edilmesi gereken durumları (ör.
serbest bırakmanın sistemde kayıtlı olmaması) gösterir. Bu uyarıların gösterilmemesi, belgenin
doğru veya kullanıma hazır olduğu anlamına gelmez.

10.3. Özellikle serbest bırakma (release) ve teslim talimatı (delivery order) içeren belgeler,
yükün teslim edileceği tarafı belirler. Müşteri, bu belgeleri düzenlemeden ve göndermeden önce
navlun ve belge serbest bırakması, gümrük serbest bırakması, ödeme durumu ve yetkili teslim alan
taraf bilgilerini kendi kaynaklarından **ayrıca doğrulamakla** yükümlüdür.

10.4. Müşterinin yüklediği Şablonların içeriği, hukuki niteliği ve üçüncü kişi haklarına
uygunluğu Müşterinin sorumluluğundadır. Hazır şablonlarda fiyat ve masraf kalemi bulunmaz.

## 11. Hizmet Seviyesi, Bakım ve Yedekleme

11.1. Hizmet Sağlayıcı, Platformu yılın her ayında en az %[99,5] erişilebilirlik hedefiyle
işletmek için makul ticari çabayı gösterir. Planlı bakım, mücbir sebep, Müşterinin veya üçüncü
tarafların kaynaklı kesintiler bu hesaba dahil değildir. [Erişilebilirlik taahhüdü ve hizmet
kredisi ayrı bir Hizmet Seviyesi Eki ile düzenlenecektir.]

11.2. Planlı bakımlar mümkün olduğunca iş saatleri dışında yapılır ve makul süre önce duyurulur.

11.3. Müşteri Verisi düzenli olarak yedeklenir. Yedekler felaket kurtarma amaçlıdır; Müşterinin
kendi hatasıyla sildiği verinin geri getirilmesi taahhüt edilmez, ancak mümkünse ücreti karşılığında
yardımcı olunur.

11.4. Destek talepleri [DESTEK E-POSTASI] üzerinden, iş günlerinde [09:00–18:00 (TSİ)] arasında
yanıtlanır. Kritik güvenlik olayları için ayrıca [GÜVENLİK E-POSTASI] adresi kullanılır.

## 12. Ücretler ve Ödeme

12.1. Hizmet bedelleri, abonelik planı ve ödeme koşulları sipariş formunda veya Platformdaki
fiyat sayfasında belirtilir. [Ücretlendirme modeli belirlenecektir.]

12.2. Bedeller, aksi belirtilmedikçe KDV hariçtir ve peşin ödenir. Geciken ödemelerde Hizmet
Sağlayıcı, yazılı bildirimden [15] gün sonra Hizmeti askıya alabilir.

12.3. Deneme veya ücretsiz dönemlerde Hizmet "olduğu gibi" sunulur; bu dönemlerde Madde 11'deki
hedefler uygulanmaz.

12.4. **Yıllık ödeme:** Müşteri yıllık ödemeyi seçerse paket bedeli bir yıllık peşin faturalanır ve fiyat sayfasında
belirtilen indirim (%20) uygulanır. Ek kullanıcı ücretleri indirimden yararlanmaz ve aylık fiyat üzerinden hesaplanır.
Yıllık dönem içinde paket yükseltilirse fark kalan süre için orantılı olarak faturalanır. Yıllık dönem dolmadan
Müşteri tarafından yapılan fesihte ödenmiş bedelin iadesi [belirlenecektir].

## 13. Fikri Mülkiyet

13.1. Platform, yazılım, arayüz, hazır şablonlar, dokümantasyon, marka ve logolar ile bunların
geliştirmeleri üzerindeki tüm fikri ve sınai haklar Hizmet Sağlayıcıya veya lisans verenlerine
aittir. Müşteriye, Sözleşme süresince ve yalnızca kendi iç iş amaçları için, devredilemez ve
münhasır olmayan bir kullanım hakkı tanınır.

13.2. Müşteri Verisi Müşteriye aittir. Müşteri, Hizmetin sunulması, güvenliğinin sağlanması,
hataların giderilmesi, Madde 8.3a'daki iç geliştirme ve yasal yükümlülüklerin yerine getirilmesi için gerekli olduğu ölçüde
Müşteri Verisinin işlenmesine izin verir.

13.3. Hizmet Sağlayıcı, Müşteriyi veya kişileri tanımlamaya imkân vermeyecek biçimde
anonimleştirilmiş ve toplulaştırılmış kullanım istatistiklerini (ör. işlenen belge sayısı,
uyarı türlerinin sıklığı) Hizmeti geliştirmek için kullanabilir.

13.4. Müşterinin veya Yetkili Kullanıcıların sağladığı öneri ve geri bildirimler, herhangi bir
bedel veya yükümlülük doğmaksızın Hizmetin geliştirilmesinde kullanılabilir. Geri bildirimlerin
kişisel veri içeren kısımları Ek-3'e göre işlenir.

13.5. **Müşterinin iş ilişkilerinin korunması:** Hizmet Sağlayıcı, Müşteri Verisinde yer alan müşteri, alıcı,
gönderici, acente, tedarikçi ve diğer iş ilişkilerini kendi ticari amacı için kullanmaz; bu kişi ve firmalara
Müşteri adına yapılan bildirimler dışında teklif, tanıtım veya başka bir iletişim göndermez ve onlarla Müşteriyi
devre dışı bırakacak şekilde doğrudan iş ilişkisi kurmak için kullanmaz. Müşteri Verisi diğer müşterilerle,
özellikle Müşterinin rakipleriyle paylaşılmaz; bir müşterinin verisi diğer müşterilere gösterilmez.

13.6. **Hizmet Sağlayıcının tanıtım iletileri:** Hizmet Sağlayıcı, Müşteriye ve Yetkili Kullanıcılarına Hizmetle
ilgili bilgilendirme, yeni özellik ve kampanya iletileri gönderebilir. Müşteri ve Yetkili Kullanıcılar bu iletileri
her zaman ücretsiz olarak reddedebilir (abonelikten çıkma); ret, Hizmetin işleyişine ilişkin zorunlu bildirimleri
kapsamaz. Hizmet Sağlayıcı, Müşterinin müşterilerine ve iş ilişkilerine tanıtım iletisi göndermez (13.5).

## 14. Gizlilik

14.1. Taraflar, birbirlerinin Gizli Bilgilerini yalnızca bu Sözleşmenin amacı için kullanır,
kendi gizli bilgilerine gösterdikleri özenden az olmamak üzere korur ve yalnızca bilmesi gereken
çalışanları, alt işleyenleri ve danışmanlarıyla, eşdeğer gizlilik yükümlülüğü altında paylaşır.

14.2. Kanunen yetkili makamların talebi halinde açıklama yapılabilir; bu durumda, hukuken mümkünse,
diğer Taraf önceden bilgilendirilir.

14.3. Gizlilik yükümlülüğü Sözleşmenin sona ermesinden sonra [5] yıl, ticari sırlar ve Kişisel
Veriler bakımından süresiz olarak devam eder.

## 15. Kişisel Verilerin Korunması

15.1. Müşteri Verisinde yer alan Kişisel Veriler bakımından **Müşteri veri sorumlusu, Hizmet
Sağlayıcı veri işleyendir.** Tarafların bu kapsamdaki hak ve yükümlülükleri Ek-2 Veri İşleme
Sözleşmesinde düzenlenmiştir.

15.2. Yetkili Kullanıcıların hesap, giriş ve iletişim bilgileri bakımından Hizmet Sağlayıcı veri
sorumlusudur. Bu verilerin işlenmesine ilişkin bilgilendirme KVKK Aydınlatma Metni ve Gizlilik
Politikasında yer alır.

## 16. Bilgi Güvenliği

16.1. Hizmet Sağlayıcı, Müşteri Verisini korumak için Ek-2'de özetlenen teknik ve idari
tedbirleri uygular; bunlar arasında firma bazında veri ayrımı, rol bazlı yetki, parolaların
özet değer olarak saklanması, entegrasyon erişim bilgilerinin şifreli saklanması, işlem
kayıtları ve oturumların yetki değişikliğinde sonlandırılması bulunur.

16.2. Müşteri; kendi cihazlarının, ağlarının, e-posta ve kimlik sağlayıcı hesaplarının
güvenliğinden ve Yetkili Kullanıcıların güvenli kullanımından sorumludur.

16.3. Hizmet Sağlayıcı, Müşteri Verisini etkileyen bir Güvenlik Olayını öğrendiğinde Müşteriyi
Ek-2'de belirtilen sürede bilgilendirir ve etkileri azaltmak için makul tedbirleri alır.

16.4. **Barındırma:** Müşteri Verisi Türkiye'de bulunan sunucularda barındırılır. Şifreli yedeklerin saklandığı yer
Ek-2'deki alt işleyen listesinde belirtilir.

## 17. Garanti Reddi

17.1. Hizmet, bu Sözleşmede açıkça belirtilenler dışında **"olduğu gibi" ve "mevcut haliyle"**
sunulur. Hizmet Sağlayıcı; Hizmetin kesintisiz veya hatasız olacağını, Çıktıların doğru, eksiksiz
veya güncel olacağını, belirli bir amaca uygun olacağını, tüm hataların giderileceğini veya
Hizmetin Müşterinin tüm operasyonel ihtiyaçlarını karşılayacağını garanti etmez.

17.2. Uyarılar ve görevler, kayıtlı veriye ve tanımlı kurallara dayanır. **Bir uyarının
üretilmemesi, ilgili riskin bulunmadığı anlamına gelmez.** Kural eşikleri (ör. ücretsiz süre uyarı
günü, aşama süre limitleri) Müşteri tarafından ayarlanabilir ve Müşterinin sorumluluğundadır.

17.3. Bu madde, emredici hukukun izin verdiği azami ölçüde uygulanır.

## 18. Sorumluluğun Sınırlandırılması

18.1. **Dolaylı zararlar:** Taraflar; kâr kaybı, gelir kaybı, iş kaybı, müşteri kaybı, itibar
kaybı, veri kaybından doğan dolaylı zararlar, üçüncü kişilerin talepleri nedeniyle doğan dolaylı
zararlar ile öngörülemeyen zararlardan, bu zararların olasılığı bildirilmiş olsa dahi, birbirine
karşı sorumlu değildir.

18.2. **Operasyonel zararlar:** Hizmet Sağlayıcı, aşağıdaki zararlardan, bunlar Hizmetin
kullanımıyla bağlantılı olsa dahi, sorumlu değildir:

- demuraj (demurrage), detention, ardiye, depolama, liman ve terminal ücretleri;
- gümrük, ISF, AMS, ihracat beyanı ve diğer resmî beyanlarla ilgili idari para cezaları, tasfiye
  edilmiş zararlar (liquidated damages), gecikme cezaları ve el koyma işlemleri;
- yükün yanlış tarafa teslimi, geç teslimi, teslim edilememesi, kaybı veya hasarı;
- Otomatik Gönderimle veya Kullanıcı İşlemiyle gönderilen, Müşteri kayıtlarındaki hatalı veya eksik
  bilgiye dayanan ya da yanlış alıcıya gitmiş e-posta, belge veya bildirimlerden doğan zararlar
  (Ek-1'deki kapsam ve frenler dışında gönderime yol açan yazılım hatası hariç);
- üçüncü taraf verilerinin (takip, sefer, terminal, taşıyıcı bilgileri) hatalı, eksik veya geç
  olmasından doğan zararlar;
- Müşterinin girdiği veya aktardığı hatalı verilerden, Müşterinin yüklediği Şablonlardan veya
  Müşterinin kontrol yükümlülüğünü yerine getirmemesinden doğan zararlar.

18.3. **Azami sorumluluk:** Hizmet Sağlayıcının bu Sözleşmeden veya Hizmetten doğan toplam
sorumluluğu, hangi hukuki sebebe dayanırsa dayansın, zarara yol açan olaydan önceki
**[12] ay içinde Müşterinin Hizmet Sağlayıcıya fiilen ödediği Hizmet bedeli** ile sınırlıdır.
[Ücretsiz kullanım döneminde azami sorumluluk [TUTAR] ile sınırlıdır.]

18.4. **İstisnalar:** Bu maddedeki sınırlamalar; kast ve ağır ihmal, kişilerin hayatına ve vücut
bütünlüğüne verilen zararlar, gizlilik yükümlülüğünün kasten ihlali ile emredici hukuk uyarınca
sınırlandırılamayan sorumluluklar bakımından uygulanmaz.

18.5. Müşteri, zararın doğmasında veya artmasında kendi kusurunun bulunduğu ölçüde (ör. kontrol
yükümlülüğünü yerine getirmemesi, uyarıları dikkate almaması, erişimleri zamanında kaldırmaması)
Hizmet Sağlayıcıdan tazminat talep edemez.

18.6. Zararın öğrenilmesinden itibaren [30] gün içinde yazılı olarak bildirilmeyen talepler,
emredici hukukun izin verdiği ölçüde, dinlenmez. [Avukat incelemesine tabidir.]

## 19. Tazminat ve Hizmet Sağlayıcının Korunması

19.1. Müşteri; (a) Müşteri Verisinin hukuka aykırılığı veya üçüncü kişi haklarını ihlal etmesi,
(b) Otomatik Gönderimle veya Kullanıcı İşlemiyle gönderilen iletişim ve belgeler, (c) Hizmetin bu Sözleşmeye
veya mevzuata aykırı kullanımı, (d) Müşterinin veri sorumlusu sıfatıyla yükümlülüklerini yerine
getirmemesi nedeniyle üçüncü kişilerin Hizmet Sağlayıcıya yönelttiği talep, dava ve idari
yaptırımlardan doğan zarar ve makul avukatlık ücretlerini Hizmet Sağlayıcıya öder ve Hizmet
Sağlayıcıyı bu taleplerden ari kılar.

19.2. Hizmet Sağlayıcı; Platformun, üçüncü kişilerin fikri mülkiyet haklarını ihlal ettiği
iddiasıyla Müşteriye yöneltilen taleplerde, Müşterinin talebi derhal bildirmesi ve makul
işbirliği yapması şartıyla, Müşteriyi savunur ve kesinleşmiş zararları karşılar. Bu yükümlülük,
Müşteri Verisi, Müşteri Şablonları veya Platformun değiştirilmiş ya da amacı dışında kullanımı
kaynaklı iddiaları kapsamaz.

## 20. Süre, Askıya Alma ve Fesih

20.1. Sözleşme kabul tarihinde yürürlüğe girer ve abonelik dönemi boyunca yürürlükte kalır.
Taraflardan biri dönem sonundan [30] gün önce bildirimde bulunmadıkça aynı süreyle yenilenir.

20.2. Hizmet Sağlayıcı; güvenlik tehdidi, hukuka aykırı kullanım, ödeme gecikmesi veya diğer
müşterileri etkileyen kötüye kullanım hallerinde Hizmeti tamamen veya kısmen, derhal ve gerekli
olduğu süre boyunca askıya alabilir. Askıya alma, mümkün olan en kısa sürede Müşteriye bildirilir.

20.3. Taraflardan biri, diğer Tarafın esaslı bir yükümlülüğünü ihlal etmesi ve ihlalin yazılı
bildirimden itibaren [30] gün içinde giderilmemesi halinde Sözleşmeyi feshedebilir.

20.4. Müşteri, Sözleşmeyi dönem sonuna kadar olan bedeli ödemek kaydıyla her zaman feshedebilir.
[Kısmi iade koşulları belirlenecektir.]

## 21. Sözleşme Sonunda Verilerin İadesi ve Silinmesi

21.1. Sözleşmenin sona ermesinden itibaren [30] gün boyunca Müşteri, Müşteri Verisini Platformun
dışa aktarma araçlarıyla veya Hizmet Sağlayıcıdan talep ederek makine tarafından okunabilir bir
biçimde alabilir.

21.2. Bu sürenin sonunda Müşteri Verisi, yasal saklama yükümlülükleri saklı kalmak kaydıyla,
canlı sistemlerden silinir; yedeklerden ise olağan yedek döngüsü içinde en geç [90] gün içinde
silinir. İşlem kayıtları Ek-3'teki sürelere tabidir.

21.3. Entegrasyon erişim bilgileri (ör. e-posta hesabı erişim jetonları ve IMAP şifreleri) Sözleşmenin sona ermesi
veya bağlantının kesilmesiyle derhal geçersiz kılınır ve silinir.

## 22. Mücbir Sebep

Tarafların makul kontrolü dışındaki olaylar (doğal afet, salgın, savaş, terör, grev, siber saldırı,
kamu otoritesinin kararları, enerji veya internet altyapısı kesintileri, üçüncü taraf
sağlayıcıların genel çaplı kesintileri) nedeniyle yükümlülüklerin yerine getirilememesi veya
gecikmesi ihlal sayılmaz. Mücbir sebep [60] günü aşarsa taraflardan her biri Sözleşmeyi
feshedebilir.

## 23. Sözleşmenin Değiştirilmesi

23.1. Hizmet Sağlayıcı bu Sözleşmeyi ve eklerini güncelleyebilir. Esaslı değişiklikler yürürlüğe
girmeden en az [30] gün önce Platform içinde ve Yönetici Kullanıcıların e-posta adreslerine
bildirilir.

23.2. Güncellenen metin, Yetkili Kullanıcılar Platforma girdiğinde gösterilir ve kabul edilmeden
Platformun kullanımına devam edilemez. Müşteri değişikliği kabul etmezse, değişiklik yürürlüğe
girmeden önce Sözleşmeyi ek bedel ödemeksizin feshedebilir.

## 24. Bildirimler

Sözleşme kapsamındaki bildirimler; Hizmet Sağlayıcı için Madde 1.1'deki e-posta veya KEP adresine,
Müşteri için kayıtta verilen ve Yönetici Kullanıcılarda tanımlı e-posta adreslerine yapılır.
Platform içi bildirimler de geçerli bildirim sayılır. Adres değişiklikleri bildirilmedikçe eski
adrese yapılan bildirimler geçerlidir.

## 25. Delil Sözleşmesi

Taraflar, Sözleşmeden doğacak uyuşmazlıklarda Hizmet Sağlayıcının ve Müşterinin ticari defter ve
kayıtlarının, Platformun işlem kayıtlarının (kabul kayıtları, gönderim kayıtları, kullanıcı işlem kayıtları),
e-posta yazışmalarının ve elektronik kayıtların 6100 sayılı Hukuk Muhakemeleri Kanunu'nun 193.
maddesi uyarınca delil teşkil edeceğini kabul eder. Bu hüküm, karşı delil sunma hakkını ortadan
kaldırmaz.

## 26. Uygulanacak Hukuk ve Uyuşmazlık Çözümü

26.1. Bu Sözleşme Türkiye Cumhuriyeti hukukuna tabidir. [Yurt dışında yerleşik müşteriler için
ayrı hukuk seçimi ve İngilizce sürüm değerlendirilecektir.]

26.2. Uyuşmazlıklarda [İSTANBUL (ÇAĞLAYAN)] Mahkemeleri ve İcra Daireleri yetkilidir. [Tahkim
seçeneği değerlendirilecektir.]

## 27. Çeşitli Hükümler

27.1. **Bölünebilirlik:** Bir hükmün geçersizliği diğer hükümleri etkilemez; geçersiz hüküm,
amacına en yakın geçerli hükümle değiştirilmiş sayılır.

27.2. **Devir:** Müşteri, Hizmet Sağlayıcının yazılı onayı olmaksızın Sözleşmeyi devredemez. Hizmet
Sağlayıcı, birleşme, devralma veya varlık devri halinde Sözleşmeyi bildirimde bulunarak devredebilir.

27.3. **Feragat:** Bir hakkın kullanılmaması o haktan feragat anlamına gelmez.

27.4. **Bütünlük:** Sözleşme ve ekleri, taraflar arasındaki anlaşmanın tamamıdır; önceki sözlü veya
yazılı anlaşmaların yerine geçer. Müşterinin satın alma siparişi veya genel koşulları, Hizmet
Sağlayıcı yazılı olarak kabul etmedikçe uygulanmaz.

27.5. **Bağımsız taraflar:** Taraflar arasında ortaklık, acentelik, temsil veya iş ilişkisi yoktur.

27.6. **Dil:** Sözleşme Türkçe düzenlenmiştir. Başka dillerdeki çeviriler bilgi amaçlıdır; çelişki
halinde Türkçe metin esas alınır.

27.7. **Sona ermeden sonra devam eden hükümler:** Madde 13, 14, 17, 18, 19, 21, 25, 26 ve niteliği
gereği devam etmesi gereken diğer hükümler Sözleşmenin sona ermesinden sonra da yürürlükte kalır.
