def calculate_ride_time(N, K, M):
    total_sessions = 2 * N
    full_sessions = total_sessions // K
    remaining_children = total_sessions % K
    if remaining_children > 0:
        full_sessions += 1
    total_time = full_sessions * M
    return total_time

N = input("Введите количество детей: ")
K = input("Введите количество детей, которых вмещает карусель: ")
M = input("Введите длительность сеанса в минутах: ")

total_time = calculate_ride_time(N, K, M)
print(f"Наименьшее время для завершения мероприятия: {total_time} минут")