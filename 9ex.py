import math

def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def circles_relation(x1, y1, r1, x2, y2, r2):
    distance = distance_between_points(x1, y1, x2, y2)

    if distance > r1 + r2:
        return "Окружности лежат одна вне другой, не касаясь"
    elif distance == r1 + r2:
        return "Окружности имеют внешнее касание"
    elif distance < r1 + r2 and distance > abs(r1 - r2):
        return "Окружности пересекаются"
    elif distance == abs(r1 - r2):
        return "Окружности имеют внутреннее касание"
    else:
        return "Одна окружность лежит внутри другой, не касаясь"

x1 = float(input("Введите x-координату центра первой окружности: "))
y1 = float(input("Введите y-координату центра первой окружности: "))
r1 = float(input("Введите радиус первой окружности: "))
x2 = float(input("Введите x-координату центра второй окружности: "))
y2 = float(input("Введите y-координату центра второй окружности: "))
r2 = float(input("Введите радиус второй окружности: "))

relation = circles_relation(x1, y1, r1, x2, y2, r2)
print(relation)