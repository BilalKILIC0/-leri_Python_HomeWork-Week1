# 7) Yukarıda verilen toplam sembolüne göre klavyeden girilen n sayısı için işlemin
# sonucunu hesaplayıp ekrana yazan programın kodunu yazınız. ( 5i + 6 Toplam n)

sayi = input("Lütfen Formül için N Değerini Giriniz : ")

toplam = 0
sayac = 0

while sayac <= int(sayi):
    toplam += (5*sayac)+6
    sayac +=1

print("Formül Toplami : " + str(toplam))
