import sys

def display_all(trains):
    """Виведення всіх записів словника."""
    if not trains:
        print("\nSchedule is empty.")
        return
    print(f"\n{'Number':<8} | {'Route':<25} | {'Arrival':<8} | {'Departure':<8}")
    print("-" * 55)
    for num, info in trains.items():
        print(f"{num:<8} | {info['route']:<25} | {info['arr'][0]:02}:{info['arr'][1]:02} | {info['dep'][0]:02}:{info['dep'][1]:02}")

def add_train(trains):
    """Додавання нового поїзда з обробкою помилок введення."""
    try:
        num = input("Enter train number: ")
        route = input("Enter route (e.g., Kyiv - Lviv): ")
        ah = int(input("Arrival hour (0-23): "))
        am = int(input("Arrival minute (0-59): "))
        dh = int(input("Departure hour (0-23): "))
        dm = int(input("Departure minute (0-59): "))
        
        if not (0 <= ah <= 23 and 0 <= am <= 59 and 0 <= dh <= 23 and 0 <= dm <= 59):
            raise ValueError("Time values out of range.")
            
        trains[num] = {"route": route, "arr": (ah, am), "dep": (dh, dm)}
        print(f"Train {num} added.")
    except ValueError as e:
        print(f"Error: {e}. Please enter integers for time.")

def delete_train(trains):
    """Видалення поїзда з обробкою виняткової ситуації (неіснуючий ключ)."""
    num = input("Enter train number to delete: ")
    try:
        del trains[num]
        print(f"Train {num} deleted.")
    except KeyError:
        print(f"Error: Train #{num} not found.")

def display_sorted(trains):
    """Перегляд словника за відсортованими ключами."""
    if not trains:
        print("\nNothing to sort.")
        return
    print("\nSorted Schedule:")
    for num in sorted(trains.keys()):
        print(f"Train #{num}: {trains[num]['route']}")

def find_at_station(trains):
    """Розв'язання завдання варіанту 19: пошук поїздів на станції."""
    try:
        h = int(input("Current hour: "))
        m = int(input("Current minute: "))
        now = h * 60 + m
        
        print(f"\nTrains at the station at {h:02}:{m:02}:")
        found = False
        for num, info in trains.items():
            arr_time = info['arr'][0] * 60 + info['arr'][1]
            dep_time = info['dep'][0] * 60 + info['dep'][1]
            
            if arr_time <= now <= dep_time:
                print(f"- #{num}: {info['route']}")
                found = True
        if not found:
            print("No trains at the station.")
    except ValueError:
        print("Invalid time input.")

# Початкові дані (10 поїздів за умовою)
train_schedule = {
    "101": {"route": "Kyiv - Lviv", "arr": (10, 0), "dep": (10, 30)},
    "722": {"route": "Kharkiv - Kyiv", "arr": (14, 15), "dep": (14, 45)},
    "045": {"route": "Uzhhorod - Lysychansk", "arr": (8, 20), "dep": (9, 0)},
    "142": {"route": "Odesa - Chernivtsi", "arr": (18, 10), "dep": (18, 25)},
    "012": {"route": "Kyiv - Odesa", "arr": (22, 0), "dep": (22, 40)},
    "091": {"route": "Lviv - Kyiv", "arr": (6, 30), "dep": (7, 10)},
    "738": {"route": "Zaporizhzhia - Kyiv", "arr": (11, 50), "dep": (12, 10)},
    "007": {"route": "Kyiv - Frankivsk", "arr": (20, 15), "dep": (21, 0)},
    "081": {"route": "Kyiv - Uzhorod", "arr": (19, 40), "dep": (20, 20)},
    "705": {"route": "Kyiv - Przemysl", "arr": (5, 45), "dep": (6, 15)}
}

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Display all")
        print("2. Add train")
        print("3. Delete train")
        print("4. Show sorted by number")
        print("5. Find trains at station (Task 19)")
        print("0. Exit")
        
        choice = input("Select: ")
        if choice == "1": display_all(train_schedule)
        elif choice == "2": add_train(train_schedule)
        elif choice == "3": delete_train(train_schedule)
        elif choice == "4": display_sorted(train_schedule)
        elif choice == "5": find_at_station(train_schedule)
        elif choice == "0": break
        else: print("Invalid option.")

if __name__ == "__main__":
    main()