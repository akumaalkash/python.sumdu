import pandas as pd

# 1. Словник з Практичної №5 (Варіант 19)
trains_dict = {
    "101": {"route": "Kyiv - Lviv", "arr_h": 10, "arr_m": 0, "dep_h": 10, "dep_m": 30, "price": 450, "sold": 120},
    "722": {"route": "Kharkiv - Kyiv", "arr_h": 14, "arr_m": 15, "dep_h": 14, "dep_m": 45, "price": 600, "sold": 85},
    "045": {"route": "Uzhhorod - Lysychansk", "arr_h": 8, "arr_m": 20, "dep_h": 9, "dep_m": 0, "price": 380, "sold": 210},
    "142": {"route": "Odesa - Chernivtsi", "arr_h": 18, "arr_m": 10, "dep_h": 18, "dep_m": 25, "price": 520, "sold": 145},
    "012": {"route": "Kyiv - Odesa", "arr_h": 22, "arr_m": 0, "dep_h": 22, "dep_m": 40, "price": 750, "sold": 98},
    "091": {"route": "Lviv - Kyiv", "arr_h": 6, "arr_m": 30, "dep_h": 7, "dep_m": 10, "price": 450, "sold": 160},
    "738": {"route": "Zaporizhzhia - Kyiv", "arr_h": 11, "arr_m": 50, "dep_h": 12, "dep_m": 10, "price": 580, "sold": 74},
    "007": {"route": "Kyiv - Frankivsk", "arr_h": 20, "arr_m": 15, "dep_h": 21, "dep_m": 0, "price": 820, "sold": 112},
    "081": {"route": "Kyiv - Uzhorod", "arr_h": 19, "arr_m": 40, "dep_h": 20, "dep_m": 20, "price": 410, "sold": 190},
    "705": {"route": "Kyiv - Przemysl", "arr_h": 5, "arr_m": 45, "dep_h": 6, "min": 15, "price": 1200, "sold": 55}
}

# 2. Перетворення словника у DataFrame
# Перетворюємо так, щоб номер поїзда став окремою колонкою
df = pd.DataFrame.from_dict(trains_dict, orient='index').reset_index()
df.rename(columns={'index': 'Train Number'}, inplace=True)

# 3. Базовий аналіз даних
print("First 3 rows (df.head(3)):")
print(df.head(3), "\n")

print("Data types (df.dtypes):")
print(df.dtypes, "\n")

print(f"Shape of DataFrame (rows, cols): {df.shape}\n")

print("Descriptive statistics (df.describe()):")
print(df.describe(), "\n")

# 4. Додавання нового стовпця (Загальний дохід від продажу квитків)
df['Total Revenue'] = df['price'] * df['sold']

# 5. Фільтрація та сортування
# Поїзди з ціною понад 500 грн, відсортовані за спаданням доходу
expensive_trains = df[df['price'] > 500].sort_values(by='Total Revenue', ascending=False)
print("Filtered trains (Price > 500) sorted by Revenue:")
print(expensive_trains[['Train Number', 'route', 'price', 'Total Revenue']], "\n")

# 6. Групування та агрегація
# Середня ціна та загальний дохід за маршрутами (для прикладу групуємо за ціною)
grouped = df.groupby('price')['Total Revenue'].mean()
print("Average Revenue grouped by Price:")
print(grouped, "\n")

# 7. Додаткові операції
max_revenue = df['Total Revenue'].max()
unique_routes = df['route'].nunique()

print(f"Maximum sale amount in one category: {max_revenue}")
print(f"Number of unique routes: {unique_routes}")