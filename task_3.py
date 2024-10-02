year = int(input("Введите любой год: "))
if year%4 == 0 and year%100 or year%400 ==0:
    print("високосный")
else:
    print("не високосный")