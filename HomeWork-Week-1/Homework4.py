# 4) Kullanıcının girdiği sayının rakamlarının toplamı

number = input("Lütfen Bir Sayi Giriniz : ")

sum = 0
number1 = 0
number2 = int(number)

while number2 > 0:
    number1 = number2 % 10
    sum = sum + int(number1)
    number2 = number2 / 10

print("Girdiğiniz Sayinin Rakamlari Toplami :" + str(sum))
