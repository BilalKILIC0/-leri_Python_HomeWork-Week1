# 5) Girilen sayının faktöriyelini hesaplama


carpim = 1
sayac = 1
sayi = input("Lütfen Faktöriyel Hesaplanacak Sayıyı Giriniz : ")

while sayac <= int(sayi):
    carpim *= sayac
    sayac +=1

print(str(carpim) + "!")