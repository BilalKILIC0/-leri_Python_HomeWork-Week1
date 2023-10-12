# 2) 1’den 10’a kadar olan tek sayıların toplamı

sum = 0
counter =1

while counter <=10:

    if counter % 2 == 1:
        sum = sum+counter
    counter +=1

print("Tek Sayilarin Toplami :" + str(sum))
