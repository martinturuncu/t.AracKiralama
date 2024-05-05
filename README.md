Araç Kiralama Uygulaması
Bu belge, PyQt6 kullanılarak geliştirilmiş basit bir araç kiralama uygulamasının dökümantasyonunu içerir. Bu uygulama, kullanıcıların araçları kiralayabileceği ve kiralık araçların takibini yapabileceği bir platform sağlar.

İçindekiler
Giriş
Kullanıcı Girişi
Araç Kiralama Sistemi
Araç Sınıfı
Ana Program Akışı
Stil ve Tema
Giriş
Bu uygulama, PyQt6 ve Python dilinde geliştirilmiş bir masaüstü uygulamasıdır. Kullanıcıların araçları kiralayabilmesi için bir kullanıcı girişi ekranı ve ardından araçları listeleyen ve kiralama işlemlerini gerçekleştiren bir ana ekran içerir.

Kullanıcı Girişi
Kullanıcı girişi ekranı, kullanıcı adı ve şifre ile giriş yapmayı sağlar. Varsayılan kullanıcı adı "admin" ve şifre "password" olarak ayarlanmıştır. Kullanıcı doğrulaması başarılı olduğunda, ana arayüze geçiş yapılır.

Araç Kiralama Sistemi
Araç kiralama sistemi, kullanıcının bir araç seçmesine, kiralama tarihini ve saati belirlemesine ve ardından kiralama işlemini gerçekleştirmesine izin verir. Kullanıcı, takvimden bir tarih seçer ve saat seçimini tamamlar. Kiralama işlemi başarılı olduğunda, kullanıcı bilgilendirilir ve başka bir kiralama yapmak isteyip istemediği sorulur.

Araç Sınıfı
Araç sınıfı, her aracın benzersiz bir kimliği (ID), modeli ve kiralama durumu bilgilerini depolar. Kiralama durumu, belirli bir tarihte aracın kiralanabilir veya kiralanamaz olduğunu belirtir.

Ana Program Akışı
Program, LoginScreen sınıfından başlar. Kullanıcı girişi başarılı olduğunda, KiralamaSistemiUI sınıfına geçiş yapılır. Bu sınıf, araçların listelendiği ve kiralama işleminin gerçekleştirildiği ana ekranı temsil eder.

Stil ve Tema
Uygulamanın arayüzü, PyQt6'nın widget'larına özel CSS stil dosyaları kullanılarak özelleştirilmiştir. Renkler, fontlar ve widget stilleri özelleştirilerek kullanıcı dostu bir arayüz oluşturulmuştur.
