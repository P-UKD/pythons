def count_password_combinations(m):
    if m <= 0:
        return 0
    combinations = 1
    for i in range(25, 25 - m, -1):
        combinations *= i
    return combinations


m = int(input())
combinations = count_password_combinations(m)
print("Кількість можливих комбінацій:", combinations)
