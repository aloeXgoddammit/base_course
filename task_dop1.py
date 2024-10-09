print("ax^2 + bx + c = 0")
coef_a=int(input("Введите коэффицент a: "))
coef_b=int(input("Введите коэффицент b: "))
coef_c=int(input("Введите коэффицент c: "))

print(f"Квадратное уравнение: {coef_a} * x**2 + {coef_b} * x + {coef_c}")

D = coef_b ** 2 - 4 * coef_a * coef_c

x1 = (-coef_b - D ** 0.5) / (2 * coef_a)
x2 = (-coef_b + D ** 0.5) / (2 * coef_a)
if D > 0:
    print(f"Уравнение имеет два корня: {x1} и {x2}")
elif D == 0:
    print(f"Уравнение имеет один корень: {x1}")
elif D < 0:
    print("Уравнение не имеет корней")