# 6) Toplamda 10 sorunun sorulduğu bir sınavda her doğru cevap için 10 puan alınırken
# her yanlış cevap için -5 puan alınmaktadır. Tüm soruları cevaplayan bir kişinin doğru
# yanlış sayısı klavyeden girildiğinde toplam puanını ekrana yazan programın kodunu
# yazınız.

dogru = input("Doğru Cevap Sayısını Giriniz : ")
yanlis = input("Yanlış Cevap Sayısını Giriniz : ")


dogru_p = int(dogru) * 10
yanlis_p = int(yanlis) * (-5)

toplam = dogru_p + yanlis_p


print("Bu Testte Toplam : " + str(toplam) + " Puan Aldınız.")
