import math
from my_module import check_deficient  

def calculate_z(x):
    return (math.sqrt(2) / 2) * math.sin(1 / x) + 1


try:
    x_val = float(input("Введіть число x для обчислення z: "))
    if x_val == 0:
        print("Помилка: x не може бути нулем (ділення на нуль).")
    else:
        result_z = calculate_z(x_val)
        print(f"Результат виразу z = {result_z}")
except ValueError:
    print("Будь ласка, введіть числове значення.")

print("-" * 30)

try:
    n_val = int(input("Введіть ціле число n для перевірки на 'недостатність': "))
    if check_deficient(n_val):
        print(f"Число {n_val} є недостатнім.")
    else:
        print(f"Число {n_val} НЕ є недостатнім.")
except ValueError:
    print("Помилка: потрібно ввести ціле число.")