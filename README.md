
Selenium ve time modülleri içe aktarılır.
Chrome tarayıcısı için ayarlar yapılır. Bu ayarlar, tarayıcının gizli modda (--incognito) ve arka planda (--headless) çalışmasını sağlar.
WebDriver başlatılır, Chrome tarayıcısı bu ayarlarla başlatılır.
Tarayıcı penceresi tam ekran yapılır ve tarayıcının çerezleri silinir.
Tarayıcı, belirtilen URL'ye gitmesi için yönlendirilir.
Tarayıcıda belirli bir bekleme süresi tanımlanır (implicitly_wait), bu durum sayfanın yüklenmesini bekler.
Sonsuz bir döngü (while True) başlatılır.
Döngünün içinde, belirtilen XPath kullanılarak bir elementin fiyat bilgisi bulunur (fiyat_bilgisi).
Bu fiyat bilgisi ekrana yazdırılır (print(fiyat_bilgisi)).
Program 5 saniye bekler (sleep(5)) ve ardından döngüyü tekrarlar.
