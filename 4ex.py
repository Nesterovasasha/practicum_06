column = input("Введите столбец (букву от A до H): ")
row = int(input("Введите строку (число от 1 до 8): "))

if (column.upper() in ['A', 'C', 'E', 'G'] and row % 2 == 0) or (column.upper() in ['B', 'D', 'F', 'H'] and row % 2 != 0):
    print("Клетка", column.upper() + str(row), "– черного цвета.")
else:
    print("Клетка", column.upper() + str(row), "– белого цвета.")