fibonacсi1 = fibonacсi2 = 1

quantity = int(input("Введите количество чисел в ряду Фибоначчи: "))
print(fibonacсi1, fibonacсi2, end =" ")

for row in range(2, quantity):
    fibonacсi1, fibonacсi2 = fibonacсi2, fibonacсi1 + fibonacсi2
    print(fibonacсi2, end=" ")


