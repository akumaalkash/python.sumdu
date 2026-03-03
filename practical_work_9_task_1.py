import csv

def process_exports_data():
    input_file = 'world_bank_data.csv'
    output_file = 'filtered_exports.csv'
    
    try:
        min_val = float(input("Enter minimum % of GDP: "))
        max_val = float(input("Enter maximum % of GDP: "))
        
        with open(input_file, mode='r', encoding='utf-8') as file:
            # Світовий банк іноді додає порожні рядки на початку, DictReader допоможе знайти заголовки
            reader = csv.DictReader(file)
            filtered_results = []

            print(f"\n{'Country':<40} | {'2015':<10} | {'2019':<10}")
            print("-" * 65)

            for row in reader:
                try:
                    # Отримуємо значення, пропускаючи символи '..' (немає даних)
                    name = row['Country Name']
                    val_2015 = row['2015 [YR2015]']
                    val_2019 = row['2019 [YR2019]']
                    
                    v15 = float(val_2015) if val_2015 != '..' else None
                    v19 = float(val_2019) if val_2019 != '..' else None

                    # Перевіряємо, чи потрапляє хоча б один рік у вказаний діапазон
                    if (v15 and min_val <= v15 <= max_val) or (v19 and min_val <= v19 <= max_val):
                        print(f"{name:<40} | {val_2015:<10} | {val_2019:<10}")
                        filtered_results.append({
                            'Country Name': name,
                            '2015 [YR2015]': val_2015,
                            '2019 [YR2019]': val_2019
                        })
                except KeyError:
                    continue # Пропускаємо технічні рядки в кінці файлу

            # Запис у новий файл
            with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=['Country Name', '2015 [YR2015]', '2019 [YR2019]'])
                writer.writeheader()
                writer.writerows(filtered_results)
            
            print(f"\nSuccess! Results saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: '{input_file}' not found in the directory.")
    except ValueError:
        print("Error: Please enter valid numbers for the range.")

if __name__ == "__main__":
    process_exports_data()