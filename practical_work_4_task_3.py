def transform_list():
    raw_input = input("Enter float numbers separated by space: ")
    float_list = [float(x) for x in raw_input.split()]
    
    # Округлення та перетворення в int
    int_list = [int(round(x)) for x in float_list]
    
    print("Original list:", float_list)
    print("Transformed list (rounded):", int_list)

transform_list()