storona1 = int(input("Введите длину первой стороны: "))
storona2 = int(input("Введите длину второй стороны: "))
storona3 = int(input("Введите длину третьей стороны: "))

if storona1 + storona2 > storona3 and storona1 + storona3 > storona2 and storona3 + storona2 > storona1:
    print("Треугольник существует")

    if storona1 == storona2 == storona3:
        print("Треугольник равносторонний")
    elif storona1 == storona2 or storona1 == storona3 or storona2 == storona3:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник не существует")