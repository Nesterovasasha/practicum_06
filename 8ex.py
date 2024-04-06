def guess_number(n):
    if n == 1:
        return "О"
    else:
        return str(n - 1)

n = int(input("Введите порядковый номер: "))

result = guess_number(n)
print(f"Цифра под порядковым номером {n}: {result}")