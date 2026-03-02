while True:
    a = float(input("Enter your number 'A' (1-100): "))

    if 1 <= a <= 100:
        b = float(input("Enter your number 'B' (1-100): "))

        if 1 <= b <= 100:
            break
               
        else:            
            print("Out of range exception, choose a number from 1 to 100.") 
    else:
        print("Out of range exception, choose a number from 1 to 100.")
    
if a == b:
    x = 3425
elif a > b:
    x = b * a + 1
else: 
    x = (2 * a - 5) / b

print(f"Your function is equal to: {x}")