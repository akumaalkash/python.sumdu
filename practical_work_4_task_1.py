n = int(input("Enter the number of elements (N): "))
array = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

reversed_array = array[::-1]
print("Array in reverse order:", reversed_array)