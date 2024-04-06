def rectangles_relation(rect1, rect2):
    x1_1, y1_1, x1_2, y1_2 = rect1
    x2_1, y2_1, x2_2, y2_2 = rect2

    if x1_2 < x2_1 or x2_2 < x1_1 or y1_2 < y2_1 or y2_2 < y1_1:
        return "Прямоугольники лежат вне друг друга, не касаясь"
    elif x1_2 == x2_1 or x2_2 == x1_1 or y1_2 == y2_1 or y2_2 == y1_1:
        return "Прямоугольники имеют касание"
    else:
        return "Прямоугольники имеют пересечение"

rect1 = tuple(map(float, input("Введите координаты верхней левой и правой нижней вершин первого прямоугольника через пробел: ").split()))
rect2 = tuple(map(float, input("Введите координаты верхней левой и правой нижней вершин второго прямоугольника через пробел: ").split()))

relation = rectangles_relation(rect1, rect2)
print(relation)