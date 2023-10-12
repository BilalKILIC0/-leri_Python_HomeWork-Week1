# 8) İkinci dereceden bir bilinmeyenli bir denklemin delta değerini hesaplayan ve bu
# değere göre denklemin köklerini ekrana yazan uygulamanın kodunu yazınız.

from math import sqrt

print("*** 2.Dereceden Benklemin Köklerini Bulma ***")
a = input("A Sayısını Giriniz : ")
b = input("B Sayısını Giriniz : ")
c = input("C Sayısını Giriniz : ")


delta = ((int(b)*(int(b))) - (4*int(a)*int(c)))


kok_1 = (-int(b) + sqrt(delta)) / (2*int(a))
kok_2 = (-int(b) - sqrt(delta)) / (2*int(a))

print("Denklemin 1. Kökü : " + str(kok_1))
print("Denklemin 2. Kökü : " + str(kok_2))



