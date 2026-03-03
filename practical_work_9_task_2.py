import json
import os

DATA_FILE = 'trains_data.json'
SEARCH_RESULT_FILE = 'found_trains.json'

def load_from_file():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return [] 

def save_to_file(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    trains = load_from_file()
    
    if not trains:
        trains = [
            {"number": "101", "route": "Kyiv - Lviv", "arr": [10, 0], "dep": [10, 30]},
            {"number": "722", "route": "Kharkiv - Kyiv", "arr": [14, 15], "dep": [14, 45]}
        ]
        save_to_file(trains)

    while True:
        print("\n1 - View all trains\n2 - Add train\n3 - Search trains at station (Task 19)\n4 - Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print("\nCurrent Schedule (from JSON):")
            for t in trains:
                print(f"Train #{t['number']}: {t['route']} (Arr: {t['arr'][0]:02}:{t['arr'][1]:02}, Dep: {t['dep'][0]:02}:{t['dep'][1]:02})")

        elif choice == '2':
            num = input("Number: ")
            route = input("Route: ")
            ah, am = int(input("Arrival hour: ")), int(input("Arrival min: "))
            dh, dm = int(input("Departure hour: ")), int(input("Departure min: "))
            
            trains.append({"number": num, "route": route, "arr": [ah, am], "dep": [dh, dm]})
            save_to_file(trains)
            print("Saved to JSON file.")

        elif choice == '3':
            h = int(input("Enter current hour: "))
            m = int(input("Enter current minute: "))
            now = h * 60 + m
            
            results = []
            for t in trains:
                arr = t['arr'][0] * 60 + t['arr'][1]
                dep = t['dep'][0] * 60 + t['dep'][1]
                if arr <= now <= dep:
                    results.append(t)
            
            if results:
                print("Found trains. Saving to result file...")
                with open(SEARCH_RESULT_FILE, 'w', encoding='utf-8') as rf:
                    json.dump(results, rf, indent=4, ensure_ascii=False)
                for r in results:
                    print(f"Train {r['number']} is at the station.")
            else:
                print("No trains found.")

        elif choice == '4':
            break

if __name__ == "__main__":
    main()