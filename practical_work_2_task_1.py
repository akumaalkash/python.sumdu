import math

def calculate_z(x):
    return (math.sqrt(2) / 2) * math.sin(1 / x) + 1

def check_deficient(n):
    total = 0 

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total < n

x = float(input('Enter your number: '))

print(calculate_z(x))

n = int(input('Enter your integer: '))

if check_deficient(n):
    print("Число є недостатнім.")
else:
    print("Число НЕ є недостатнім.") 