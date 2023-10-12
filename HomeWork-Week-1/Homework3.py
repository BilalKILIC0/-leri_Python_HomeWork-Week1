# 3) 1’den 10’a kadar olan tek ve çift sayıların ayrı ayrı toplamı

sum_S = 0
sum_D = 0
counter = 1

while counter <=10:
    if counter % 2 == 0:
        sum_D = sum_D + counter
    else:
        sum_S = sum_S + counter
    counter += 1

print("Tek Sayilarin Toplami :" + str(sum_S))
print("Cift Sayilarin Toplami :" + str(sum_D))
