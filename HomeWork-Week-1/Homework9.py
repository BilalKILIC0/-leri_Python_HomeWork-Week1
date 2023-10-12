# 9) Toplamda 3 cevap hakkı verilen bir sayı tahmin oyununda;
# ● Yarışmacı sayıyı doğru tahmin ettiğinde kaçıncı hakkında doğru tahmin ettiği ile
# birlikte ekrana yazan ve programı sonlandıran, (Örnek Çıktı: 2. Tahminde bildiniz)
# ● 3 hakkında da doğru tahmin edemeyen yarışmacıya “Doğru tahmin yapamadınız” mesajı
# veren programın kodunu yazınız.

import random

rnd=random.randint(0,10)

# İstenirse Kapatılabilir
print("Bulmanız Gereken Sayı : " + str(rnd))

tahmin = int(input("Lütfen Tahmin Ettiğiniz Sayıyı Giriniz : "))

sayac = 0

while sayac < 3:
    if rnd == tahmin:
        print(str(sayac+1) + ".Tahminde Bildiniz.")
        break
    else:
        tahmin = int(input("Lütfen "+str(sayac+2) + ".Tahmin Ettiğiniz Sayıyı Giriniz :"))
    sayac += 1
    if sayac == 2 and rnd != tahmin:
        print("Doğru Tahmin Yapamadınız.")
        break
