# Ek-1: Otomasyon ve Sorumluluk Paylaşımı Protokolü

Sürüm: 1.9-TASLAK · Tarih: 3 Ekim 2026

Bu Protokol, WardOps Hizmet Sözleşmesinin ayrılmaz ekidir. Platformun hangi işlemleri kendiliğinden
yaptığını, hangi iletileri otomatik gönderdiğini, hangi işlemlerin bir Yetkili Kullanıcının eylemine bağlı
olduğunu, her işlevde Müşterinin
kontrol yükümlülüğünü ve olası olaylarda sorumluluğun nasıl paylaşıldığını ayrıntılı olarak
düzenler. Bu Protokolde tanımlanmayan terimler Hizmet Sözleşmesindeki anlamı taşır.

## 1. Temel İlkeler

1.1. **Otomatik gönderim tanımlı kapsamla sınırlıdır.** Platform, Müşteri adına yalnızca bu Protokolün
3. maddesinde sayılan iletileri (durum sorusuna yanıt; müşterinin rutin dışı sorusuna yanıt; ETA değişikliği, gemi varışı ve yükün çekilebilir
olması bildirimleri; müşterinin gümrükçüsüne gümrük evrak paketi; peşin çalışan müşteriye ödeme talebi; mailden açılan dosyada eksik bilgi talebi) bir Yetkili Kullanıcının onayını beklemeden, Müşterinin bağlı e-posta hesabından
gönderir. Bu iletiler yalnızca dosyada kayıtlı bilgilerden kural tabanlı olarak oluşturulur; metin
yapay zekâ ile yazılmaz. Bunların dışındaki her e-posta, mesaj veya belge gönderimi bir Yetkili
Kullanıcının eylemiyle yapılır. Müşteri otomatik gönderimi firma ayarlarından kapatabilir; kapalıyken
iletiler bekler ve Yetkili Kullanıcı tarafından gönderilir. Her gönderim; gönderen (Platform veya
kullanıcı), tarih, saat, alıcılar ve içerikle birlikte işlem kaydına yazılır.

1.2. **Platform var olan bilgiyi sessizce değiştirmez.** Belgeden veya e-postadan okunan bir değer,
dosyada daha önce girilmiş bir değerin üzerine yazılmaz; boş alanlar doldurulur, çelişkiler uyarı
ve görev olarak gösterilir. Tahmini varış tarihi (ETA) gibi değişken bilgilerde kaynak önceliği
uygulanır ve her değişiklik geçmişte tutulur.

1.3. **Uyarı, kontrolün yerine geçmez.** Uyarılar ve görevler kayıtlı veriye ve tanımlı kurallara
dayanır. Bir uyarının olmaması risk bulunmadığı anlamına gelmez.

1.4. **Belge ve iletişim Müşterinin beyanıdır.** Platformda üretilen veya Platform üzerinden
gönderilen belge ve iletişimlerin düzenleyeni ve göndericisi Müşteridir.

1.5. **Şeffaflık.** Platform; bir değerin nereden geldiğini (belge, e-posta, hat sistemi, elle giriş),
ne zaman kaydedildiğini ve uygulanıp uygulanmadığını gösterir. Müşteri, kararlarını bu bilgilerle
birlikte değerlendirir.

## 2. İşlev Bazında Otomasyon ve Sorumluluk Tablosu

Aşağıdaki tabloda "Otomatik" sütunu, işlemin kullanıcı eylemi olmadan Platform içinde yapılıp
yapılmadığını; "Dışarıya etki" sütunu, işlemin tek başına üçüncü kişilere ulaşıp ulaşmadığını gösterir.

| İşlev | Platform ne yapar | Otomatik | Dışarıya etki | Kullanıcı eylemi | Müşterinin kontrol yükümlülüğü |
|---|---|---|---|---|---|
| E-posta okuma ve eşleştirme | Bağlı hesaptaki operasyonla ilgili e-postaları okur, içindeki numaralardan dosyayı bulur, sınıflandırır | Evet | Hayır | Gerekmez | Yanlış dosyaya bağlanan veya bağlanamayan e-postaları düzeltmek |
| Cevapsız e-posta takibi | Cevap bekleyen e-posta süre eşiğini aşınca görev açar | Evet | Hayır | Gerekmez | Eşik süresini ayarlamak, görevleri takip etmek |
| Mailden dosya açma | Eşleşmeyen maildeki B/L, arrival notice veya booking teyidinden (ya da pre-alert metninden) yeni dosya açar; numaralardan biri mevcut bir dosyadaysa açmaz | Evet (firma kapatabilir) | Hayır | Gerekmez | Açılan dosyayı, müşteriyi ve tarafları kontrol etmek |
| Gecikme e-postasından ETA okuma | Yeni ETA'yı okur; kaynağı "e-posta" olarak geçmişe yazar, daha güvenilir kaynak varsa uygulamaz | Evet | Hayır | Gerekmez | Önemli ETA değişikliklerini hat/terminal kaynağından teyit etmek |
| Belgeden alan okuma (metin, OCR) | Konşimento, varış bildirimi gibi belgelerden numara, gemi, liman, tarih okur | Evet | Hayır | Gerekmez | İncelemeye düşen belgeleri ve çelişki uyarılarını kontrol etmek |
| Belgeden alan okuma (yapay zekâ) | Metin/OCR yetmezse, etkinse belgenin gerekli kısmını yapay zekâ sağlayıcısına gönderir | Evet (ayara bağlı) | Veri alt işleyene gider | Hesap ayarı | Okunan değerleri doğrulamak; istenirse özelliği kapattırmak |
| Takip verisi | Taşıyıcı/terminal/veri sağlayıcıdan gelen olayları kaydeder, yükün aşamasını hesaplar | Evet | Hayır | Gerekmez | Kritik olaylarda kaynak sistemi kontrol etmek |
| Evrak teslim talebi (Full Automation) | İthalatta konşimento aslıyla çalışılıyorsa, gümrük müşaviri ve alıcı belliyse ve varışa 3 gün veya daha az kaldıysa evrak teslim talebini açar; talep anlaşmalı kuryeye iletilir | Evet (pakete bağlı) | Evet: kurye evrakı belirtilen kişiden alır ve alıcıya teslim eder | Gerekmez | Alınacak ve teslim edilecek yeri, kişiyi ve evrak listesini kontrol etmek; gerekirse talebi iptal etmek |
| Uyarı ve görev üretimi | Gecikme, ETA kayması, ücretsiz süre, belge süresi, serbest bırakma, ISF/AMS eşleşmesi gibi durumlar için görev açar | Evet | Hayır | Gerekmez | Görevleri değerlendirmek, eşikleri operasyona uygun ayarlamak |
| Demuraj/detention tahmini | Tanımlı tarifeye göre tahmini tutar hesaplar | Evet | Hayır | Gerekmez | Tarifeyi doğru tanımlamak; nihai tutar için taşıyıcı faturasını esas almak |
| Durum sorusuna yanıt | Dosyaya bağlanan durum sorusuna kayıtlı bilgilerden yanıt hazırlar; 3. maddedeki frenlerden geçerse bağlı hesaptan gönderir | Evet | **Evet** | Gerekmez (firma kapatabilir) | Dosya kayıtlarını (ETA, serbest bırakma, taraflar) doğru ve güncel tutmak; gönderilen yanıtları izlemek |
| Müşterinin rutin dışı sorusuna yanıt | Dosyanın müşterisinden gelen maildeki ödeyip son ücretsiz günden önce çekme, terminal masrafı, masraf ve belge talebi sorularına dosyadaki kayıtlardan yanıt yazar (fatura durumu, son ücretsiz gün, serbest bırakma durumu); kesilmiş faturaları ve istenen belgeyi (yalnızca house B/L ve Platformun ürettiği belgeler; master B/L ve hattın arrival notice'i eklenmez) ekler; kesin tutarı bilinmeyen masrafı tahmin etmez. Şikâyet, HS kodu farkı ve rutin dışı talimatta yalnızca alındı bilgisi gönderir. Her durumda ekibe görev açar; aynı frenlerle gönderir | Evet | **Evet** | Gerekmez (firma kapatabilir) | Müşteri kaydındaki e-posta adreslerini, faturaları ve dosyadaki belgelerin türünü doğru tutmak; açılan görevleri ve karar gerektiren konuları (şikâyet, HS farkı, talimat) takip etmek |
| Eksik bilgi talebi | Mailden açılan dosyada boş kalan bilgileri (Shipper, Consignee, Notify, gemi/sefer, tarihler, konteyner ve yük bilgisi, konşimento türü, ticari fatura ve çeki listesi) belgeyi gönderen tarafa (iletilmiş mailde ilk göndericiye) tek e-postayla, dosya başına bir kez ve aynı frenlerle sorar | Evet | **Evet** | Gerekmez (firma kapatabilir) | Belgeden okunan ve konumdan çıkarılan tarafları kontrol etmek; soru giden adresin doğru taraf olduğunu izlemek |
| Proaktif bildirim | ETA değişikliği, gemi varışı ve çekilebilirlik anlarında müşteriye bildirim hazırlar ve aynı frenlerle gönderir | Evet | **Evet** | Gerekmez (firma kapatabilir) | Müşteri kayıtlarındaki e-posta adreslerini güncel tutmak |
| Gümrükçüye evrak paketi | Gümrüklemeyi müşterinin gümrükçüsü yapıyorsa, Platformun ürettiği arrival notice, ticari fatura ve çeki listesi dosyada hazır olduğunda bunları gümrükçüye tek e-postayla ve aynı frenlerle gönderir (dosya başına bir kez) | Evet | **Evet** | Gerekmez (firma kapatabilir) | Gümrükçü kaydındaki e-posta adresini, dosyadaki gümrükleme tercihini ve eklenen belgelerin doğruluğunu kontrol etmek |
| Ödeme talebi | Müşteri kaydında peşin (vadesiz) olarak işaretlenen müşteriye, varışa 7 gün kala veya gemi vardığında, dosyada kesilmiş ve ödenmemiş fatura/debit note'ları ekli ödeme talebini aynı frenlerle gönderir | Evet | **Evet** | Gerekmez (firma kapatabilir) | Müşterinin ödeme koşulunu ve kesilen faturaları doğru tutmak; ödeme gelince faturayı "ödendi" işaretlemek |
| Draft karşılaştırma | House B/L ve Master B/L draft'larını karşılaştırır; fark varsa origin acenteye düzeltme e-postası hazırlar, göndermez | Evet | Hayır | Yetkili Kullanıcı gönderir | Farkların gerçek olduğunu kontrol etmek, gerekirse metni düzeltmek |
| Elle e-posta gönderimi | Otomatik gönderilemeyen veya otomatik gönderimi kapalı firmada bekleyen iletiyi bağlı hesaptan gönderir | **Hayır** | Evet | Yetkili Kullanıcı | Göndermeden önce alıcıyı ve içeriği kontrol etmek |
| Belge üretimi (AN, DO, release, POD) | Firma bilgisi ve dosya kayıtlarıyla PDF/Word üretir; eksik alan ve uyarıları gösterir | **Hayır** | Hayır (indirilen belgeyi Müşteri iletir) | Yetkili Kullanıcı | İçeriği, özellikle teslim tarafını ve serbest bırakma durumunu doğrulamak |
| Masraf kalemleri ve muhasebe belgeleri | Girilen kalemlerden invoice, debit note, credit note keser, numaralar ve PDF üretir; ekstre çıkarır; tutar önermez | **Hayır** | Hayır (belgeyi Müşteri iletir) | Yetkili Kullanıcı | Kalemleri, tutarları, borçluyu ve vergi yükümlülüklerini doğrulamak; kesilen belge değişmez, düzeltme credit note ile yapılır |
| Belge kaydı | Üretilen belgeyi istenirse dosyanın belgelerine ekler | Hayır | Hayır | Yetkili Kullanıcı | — |
| ISF kaydı | ISF beyan bilgisini ve durumunu kaydeder; AMS eşleşmesi yoksa uyarır | Kısmen | Sağlayıcıya bağlıysa evet | Yetkili Kullanıcı | Beyanı zamanında yapmak, eşleşmeyi takip etmek |
| Kullanıcı yönetimi | Kullanıcı ekler, rol verir, pasifleştirir; yetki değişince oturumları kapatır | Hayır | Hayır | Yönetici | Erişimleri güncel tutmak |
| Entegrasyon bağlama | Müşterinin yetkisiyle e-posta hesabı vb. bağlar; erişim bilgisini şifreli saklar | Hayır | Hayır | Yönetici/Yetkili | Bağlanan hesap üzerinde yetkili olmak |

## 3. Otomatik Gönderimin İşleyişi ve Frenler

3.1. **Kapsam:** Platform yalnızca (a) bir dosyaya tek anlamlı olarak bağlanan ve durum soran
e-postalara yanıtı, (b) ETA'nın müşteriye son bildirilen değerden firma eşiği kadar sapması, gemi
varışı (ithalat) ve yükün çekilebilir olması anlarında bildirimi, (c) gümrüklemeyi müşterinin
gümrükçüsünün yaptığı ithalat dosyalarında, Platformun ürettiği arrival notice ile ticari fatura ve çeki
listesi dosyada bulunduğunda bu belgeleri gümrükçüye tek bir e-postayla, (d) müşteri kaydında peşin (vadesiz)
çalıştığı belirtilen müşteriye, varışa 7 gün kala veya gemi vardığında, dosyada kesilmiş ve ödenmemiş
faturaları ekli ödeme talebini, (e) dosyanın müşterisinden (gönderen müşteri kaydıyla veya müşterinin
kurumsal alan adıyla eşleşmeli) gelen maildeki rutin dışı soruya (ödeyip son ücretsiz günden önce çekme,
terminal masrafı, masraf ve belge talebi; şikâyet, HS kodu farkı ve talimatta alındı bilgisi) yanıtı
otomatik gönderir; (f) mailden açılan dosyada eksik kalan bilgileri belgeyi gönderen tarafa soran e-postayı
(iletilmiş mailde ilk göndericiye, dosya başına bir kez) otomatik gönderir; bu e-postaya ek konmaz. Müşteri
dışındaki göndericiye tutar, fatura veya belge gönderilmez. Freight release'i Platform kendiliğinden vermez. Origin
acenteye gönderilen draft düzeltme e-postası otomatik gönderilmez; Yetkili Kullanıcının eylemiyle
gönderilir. Diğer e-postalar yanıtlanmaz; cevap bekleyenler süre eşiğini aşınca görev olarak ekibe döner.

3.2. **İçerik:** İleti yalnızca dosyada kayıtlı bilgilerden oluşur; kayıtta olmayan bilgi metne
girmez. Zayıf kaynaktan gelen ETA "tahmini" olarak yazılır. İç referans numaraları müşteriye giden
metne eklenmez. İmza ve firma kimliği Müşterinin kaydından gelir.

3.3. **Frenler:** Aşağıdaki durumlarda ileti gönderilmez, "Yanıtlar" ekranında bekler ve Yetkili
Kullanıcı tarafından gönderilebilir: otomatik gönderim firma ayarında kapalıysa; bağlı e-posta hesabı
yoksa; alıcı Müşterinin kendi alan adındaysa (ekip içi yazışma); yanıtlanacak e-posta başka yoldan
cevaplanmışsa; aynı alıcıya aynı dosya için son 12 saat içinde durum yanıtı gönderilmişse; ileti 2
günden daha önce hazırlanmışsa. Otomatik yanıtlayıcı, ofis dışı ve iletilemedi bildirimleri cevap
beklemez sayılır ve bunlara yanıt hazırlanmaz.

3.4. **Elle gönderim:** Bekleyen iletileri Yetkili Kullanıcı inceleyebilir, düzenleyebilir, gönderebilir
veya kendi e-posta programından gönderip "elle gönderildi" olarak işaretleyebilir. İzleyici rolündeki
kullanıcılar gönderim yapamaz.

3.5. **Başka yoldan yanıt:** Aynı yazışmaya bağlı hesap üzerinden başka bir yanıt gönderildiği tespit
edilirse bekleyen ileti kendiliğinden kapatılır; bu durum bir gönderim sayılmaz.

3.6. **Gönderim hatası:** E-posta sağlayıcısı gönderimi reddederse ileti "gönderilemedi" durumuna geçer
ve hata metni gösterilir. Platform otomatik olarak yeniden denemez; yeniden deneme Yetkili Kullanıcının
kararıdır.

3.7. **Kayıt:** Otomatik ve elle yapılan her gönderim, kapatma ve işaretleme; gönderen (Platform veya
kullanıcı), zaman, alıcılar ve içerikle işlem kaydına yazılır. Bu kayıtlar Müşterinin yöneticileri
tarafından görülebilir ve değiştirilemez.

3.8. **Kapatma:** Müşteri otomatik gönderimi firma ayarlarından her zaman kapatabilir. Kapatma, bir
sonraki gönderim döngüsünden itibaren uygulanır; o ana kadar gönderilmiş iletileri etkilemez.

## 4. Olay Senaryoları ve Sorumluluk Paylaşımı

Bu bölüm, operasyonda yaşanabilecek başlıca olaylarda Platformun önleyici tedbirlerini, Müşterinin
tedbirlerini ve sorumluluğun kimde olduğunu gösterir. Sorumluluğun kapsamı ve üst sınırı Hizmet
Sözleşmesinin 18. maddesine tabidir.

### 4.1. Yanlış alıcıya veya yanlış içerikle e-posta gönderilmesi

- **Platformun tedbirleri:** Otomatik iletiler yalnızca kayıtlı bilgiden kurulur; alıcı, gelen e-postanın
  göndericisi veya müşteri kaydındaki adrestir, tahmin edilmez; ekip içi alıcılara ve otomatik
  yanıtlayıcılara gönderilmez; aynı alıcıya kısa sürede tekrar yazılmaz; iç referanslar müşteriye
  giden metne eklenmez; her gönderim kayda geçer; Müşteri otomatik gönderimi kapatabilir.
- **Müşterinin tedbirleri:** Dosya kayıtlarını (ETA, serbest bırakma, taraflar) ve müşteri e-posta
  adreslerini doğru ve güncel tutmak; e-posta eşleşmelerini ve gönderilen iletileri düzenli gözden
  geçirmek; otomatik gönderimin uygun olmadığı müşteri veya dönemlerde özelliği kapatmak; elle
  gönderimlerde alıcıyı ve içeriği kontrol etmek.
- **Sorumluluk:** Otomatik iletinin içeriği, Müşterinin Platforma girdiği veya Platformun Müşteri
  adına kaydettiği bilgiden oluşur; bu bilginin doğruluğundan ve otomatik gönderimi açık tutma
  kararından Müşteri sorumludur. Elle gönderilen iletilerin içeriğinden ve alıcısından Müşteri
  sorumludur. Platformun bu Protokolde tanımlanan kapsam veya frenler dışında gönderim yapmasına yol
  açan bir yazılım hatası halinde Hizmet Sağlayıcının sorumluluğu Hizmet Sözleşmesi 18. maddeye göre
  değerlendirilir.

### 4.2. E-postanın yanlış dosyaya bağlanması

- **Platformun tedbirleri:** Birden fazla dosyayla eşleşen bir numara eşleştirmede kullanılmaz;
  tek bir dosyayı gösteren numara bulunamazsa e-posta hiçbir dosyaya bağlanmaz ve görev açılır;
  iç referans numaraları eşleştirmede kullanılmaz; eşleşmenin hangi numarayla yapıldığı kaydedilir.
- **Müşterinin tedbirleri:** Yanlış eşleşmeleri düzeltmek; yanlış dosyaya bağlanan bir e-postaya
  otomatik yanıt gittiyse ilgili müşteriye düzeltme iletmek.
- **Sorumluluk:** Yanlış eşleşme, eşleşen dosyanın bilgisiyle otomatik yanıt gönderilmesine yol
  açabilir. Eşleşme bu maddedeki kurallara uygun yapılmışsa sonuçlarından Müşteri; kurallara aykırı
  bir yazılım hatasından kaynaklanıyorsa Hizmet Sağlayıcı Hizmet Sözleşmesi 18. madde çerçevesinde
  sorumludur.

### 4.3. Yanlış veya güncel olmayan ETA

- **Platformun tedbirleri:** ETA kaynak önceliği (hat/terminal sistemi > elle giriş > e-posta >
  rezervasyon > belge) uygulanır; zayıf kaynaktan gelen değer kaydedilir ama uygulanmaz; eski
  bilgi yeninin üzerine yazılmaz; zayıf kaynaktan gelen ETA müşteriye giden metinde "tahmini" diye
  yazılır; gemi vardıktan sonra eski ETA müşteriye yazılmaz.
- **Müşterinin tedbirleri:** Kritik kararlarda (nakliye randevusu, müşteri taahhüdü) ETA'yı kaynak
  sistemden teyit etmek.
- **Sorumluluk:** ETA niteliği gereği tahminidir. Üçüncü taraf verisinin hatalı veya geç olmasından
  doğan zararlardan Hizmet Sağlayıcı sorumlu değildir.

### 4.4. Hatalı serbest bırakma (release) veya teslim talimatı

- **Platformun tedbirleri:** Sistemde navlun/belge veya gümrük serbest bırakması kayıtlı değilse
  belge üretim ekranı uyarır; release belgesi bu durumda "orijinal konşimento teslim edildi" gibi
  bir gerekçe yazmaz; serbest bırakılmış ama teslim talimatı verilmemiş yükler için görev açılır.
- **Müşterinin tedbirleri:** Release ve delivery order düzenlemeden önce ödeme, orijinal konşimento
  veya telex release, gümrük serbest bırakması ve teslim alacak tarafın yetkisini kendi kaynaklarından
  doğrulamak.
- **Sorumluluk:** Release ve delivery order Müşterinin belgesidir; yükün yanlış tarafa teslim
  edilmesinden doğan zararlar Hizmet Sağlayıcının sorumluluğunda değildir.

### 4.5. Ücretsiz sürenin (son ücretsiz gün) kaçırılması

- **Platformun tedbirleri:** Son ücretsiz gün yaklaşırken ve geçtiğinde görev açılır; serbest bırakma
  eksikse kritik uyarı verilir; tanımlı tarifeye göre tahmini maliyet gösterilir.
- **Müşterinin tedbirleri:** Son ücretsiz günü ve boş iade tarihini doğru kaydetmek; uyarı eşiklerini
  operasyonuna uygun ayarlamak; görevleri takip etmek.
- **Sorumluluk:** Demuraj, detention ve ardiye ücretleri Hizmet Sağlayıcının sorumluluğunda değildir.

### 4.6. ISF'in geç verilmesi veya AMS ile eşleşmemesi

- **Platformun tedbirleri:** ISF belge zorunluluğu ve son tarih takibi; ISF verilmiş ancak AMS ile
  eşleşmemişse, gemi kalktıktan sonra uyarı ve varışa yaklaştıkça kritik görev.
- **Müşterinin tedbirleri:** ISF'i süresinde vermek veya verdirmek; eşleşme durumunu filer/müşavir ile
  teyit etmek ve Platforma işlemek.
- **Sorumluluk:** ISF ve AMS beyanları ile bunlara bağlı cezalar Müşterinin ve beyanı yapan tarafın
  sorumluluğundadır.

### 4.7. Belgeden hatalı veri okunması

- **Platformun tedbirleri:** Konteyner numarası kontrol basamağı ve tarih biçimi denetimi; güveni düşük
  veya dosyayla çelişen belgenin incelemeye düşürülmesi ve görev açılması; okunan değerin var olan
  değerin üzerine yazılmaması.
- **Müşterinin tedbirleri:** İncelemeye düşen belgeleri ve çelişki uyarılarını kontrol etmek; kritik
  alanları belgenin aslından doğrulamak.
- **Sorumluluk:** Hatalı okunup Müşterinin incelemesinden geçmeden dosyada kalan veriye dayanan
  işlemlerin (otomatik iletiler dahil) sonuçlarından Müşteri sorumludur.

### 4.8. Entegrasyon veya Hizmet kesintisi

- **Platformun tedbirleri:** Entegrasyon hatalarının hesap ekranında ve görevlerde gösterilmesi;
  takip verisi uzun süre gelmezse uyarı; bir hesabın hatasının diğer hesapları durdurmaması.
- **Müşterinin tedbirleri:** Kesinti süresince kritik işlemleri kaynak sistemlerden takip etmek.
- **Sorumluluk:** Üçüncü taraf kesintileri Hizmet Sağlayıcının kusuru sayılmaz; Hizmetin kendi
  kesintileri Hizmet Sözleşmesi 11. madde kapsamındadır.

### 4.9. Yetkisiz erişim

- **Platformun tedbirleri:** Firma bazında veri ayrımı; rol bazlı yetki; parola kuralı; başarısız giriş
  kaydı; yetki veya parola değişince oturumların sonlandırılması; işlem kaydı.
- **Müşterinin tedbirleri:** Ayrılan çalışanların erişimini derhal kaldırmak; parolaları ve kimlik
  sağlayıcı hesaplarını korumak; şüpheli durumu bildirmek.
- **Sorumluluk:** Müşterinin kullanıcı hesaplarının ele geçirilmesinden doğan zararlar, Platform
  kaynaklı bir güvenlik açığından kaynaklanmadıkça Müşterinin sorumluluğundadır.

### 4.10. Veri kaybı

- **Platformun tedbirleri:** Üretim ortamında düzenli yedekleme; işlem kaydı.
- **Müşterinin tedbirleri:** Yasal saklama yükümlülüğü olan belgeleri kendi sistemlerinde de saklamak.
- **Sorumluluk:** Hizmet Sözleşmesi 11.3 ve 18. maddeye tabidir.

## 5. Olay Bildirimi ve İşbirliği

5.1. Müşteri, Platformdan kaynaklandığını düşündüğü bir hata veya olayı fark ettiğinde; olayın
tarihini, ilgili dosya numarasını, varsa ekran görüntüsünü ve etkisini [DESTEK E-POSTASI] adresine
bildirir. Güvenlik olayları [GÜVENLİK E-POSTASI] adresine derhal bildirilir.

5.2. Hizmet Sağlayıcı, bildirimi aldığında olayı kayda alır, önem derecesini belirler ve Müşteriyi
inceleme sonucundan bilgilendirir. Kritik olaylarda (tanımlı kapsam veya frenler dışında dış iletişim, veri ayrımının ihlali,
güvenlik olayı) ilk geri dönüş [4] iş saati içinde yapılır.

5.3. Taraflar, zararın azaltılması için makul işbirliğini yapar. Hizmet Sağlayıcı, talep halinde
olayla ilgili işlem kayıtlarını Müşteriye sunar.

## 6. Müşterinin Operasyonel Kontrol Listesi (Öneri)

Aşağıdaki kontroller, Platformun kullanımında önerilen asgari uygulamalardır:

- Her gün açık görevleri ve kritik uyarıları gözden geçirmek.
- Otomatik gönderilen iletileri ve "Yanıtlar" ekranında bekleyenleri düzenli gözden geçirmek; müşteri
  e-posta adreslerini güncel tutmak.
- Muhasebe belgelerini kesmeden önce kalemleri ve borçluyu kontrol etmek; resmi fatura ve vergi
  yükümlülüklerini kendi muhasebe düzeninde yerine getirmek.
- Release ve delivery order öncesi ödeme, konşimento ve gümrük durumunu kaynaktan teyit etmek.
- Son ücretsiz gün ve boş iade tarihlerini dosyaya girmek.
- İncelemeye düşen belgeleri aynı gün kontrol etmek.
- Kullanıcı listesini ayda bir gözden geçirmek; ayrılanların erişimini kaldırmak.
- Müşteri kartlarındaki e-posta ve iletişim bilgilerini güncel tutmak.
- Uyarı eşiklerini (ücretsiz süre uyarısı, cevapsız e-posta süresi, aşama süreleri) operasyonun
  gerçek sürelerine göre ayarlamak.
