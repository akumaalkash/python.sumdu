import random

def set_operations():
    set_a = {random.randint(1, 20) for _ in range(10)}
    set_b = {random.randint(1, 20) for _ in range(10)}
    
    intersection = set_a.intersection(set_b)
    
    print("Set A:", set_a)
    print("Set B:", set_b)
    print("Common elements:", intersection)

set_operations()