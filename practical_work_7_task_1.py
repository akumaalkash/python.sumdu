def create_first_file(filename):
    """Етап а): Створення файлу TF23_1 із рядків різної довжини"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Line 1: 101011\n")
            f.write("Second line: 000111\n")
            f.write("Short: 1\n")
            f.write("A bit longer line with numbers 1100\n")
        print(f"File {filename} created successfully.")
    except IOError as e:
        print(f"Error creating file: {e}")

def process_and_save(input_file, output_file):
    """Етап б): Читання, заміна символів та запис у TF23_2 по 15 символів"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Заміна "1" на "0" та навпаки за допомогою тимчасового символу
        processed_content = content.replace('1', 'temp').replace('0', '1').replace('temp', '0')
        
        # Видаляємо символи переносів рядків для коректного форматування по 15 символів
        raw_data = processed_content.replace('\n', '')
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for i in range(0, len(raw_data), 15):
                f.write(raw_data[i:i+15] + '\n')
        print(f"Data processed and saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except IOError as e:
        print(f"Error processing data: {e}")

def print_second_file(filename):
    """Етап в): Читання вмісту TF23_2 та друк по рядках"""
    print(f"\nContent of {filename}:")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except IOError as e:
        print(f"Error reading file: {e}")

# --- Виконання програми ---
file1 = "TF23_1.txt"
file2 = "TF23_2.txt"

create_first_file(file1)
process_and_save(file1, file2)
print_second_file(file2)