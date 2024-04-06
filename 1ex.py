import math

radius = 6.5
length = float(input("Введите длину покрытия в метрах: "))
width = float(input("Введите ширину покрытия в метрах: "))

diagonal = math.sqrt(length**2 + width**2)

if diagonal <= 2 * radius:
    print("Покрытие можно разместить без обрезки или подгибов.")
else:
    print("Покрытие слишком большое для данной арены.")