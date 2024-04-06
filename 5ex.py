def is_valid_knight_move(start, end):
    delta_x = abs(ord(start[0]) - ord(end[0]))
    delta_y = abs(int(start[1]) - int(end[1]))

    return (delta_x == 1 and delta_y == 2) or (delta_x == 2 and delta_y == 1)

start_position = input("Введите координаты (столбец и строку) стартовой позиции хода: ")
end_position = input("Введите координаты (столбец и строку) конечной позиции хода: ")

if is_valid_knight_move(start_position, end_position):
    print("Ход конем верный.")
else:
    print("Ход конем неверный.")