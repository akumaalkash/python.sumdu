s = input("Enter a string: ")

if len(s) >= 2:
    result = s[1:-1]
    print("Slicing result:", result)
else:
    print("String is too short")