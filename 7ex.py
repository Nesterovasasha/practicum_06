def can_order_sushi(K):
    if K < 5:
        return False
    if K % 5 == 0 or K % 7 == 0:
        return True

    for i in range(K // 5 + 1):
        for j in range(K // 7 + 1):
            if (i * 5 + j * 7) == K:
                return True

    return False

K = int(input("Введите количество штук суши: "))

if can_order_sushi(K):
    print(f"Можно заказать {K} штук суши!")
else:
    print(f"Нельзя заказать {K} штук суши.")