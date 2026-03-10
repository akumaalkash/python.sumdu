import pandas as pd
import matplotlib.pyplot as plt

filename = 'comptagevelo2009.csv'

try:
    df = pd.read_csv(filename, parse_dates=['Date'], dayfirst=True)
    
    df = df.dropna(axis=1, how='all')

    print("--- First 5 rows ---")
    print(df.head())
    
    print("\n--- DataFrame Info ---")
    print(df.info())

    numeric_df = df.select_dtypes(include=['number'])
    total_bikers = numeric_df.sum().sum()
    print(f"\nTotal cyclists in 2009: {total_bikers:.0f}")

    path_totals = numeric_df.sum()
    print("\nTotals per bike path:")
    print(path_totals)

    df['Month'] = df['Date'].dt.month
    selected_paths = numeric_df.columns[:3] 
    
    print("\nMost popular month per path:")
    for path in selected_paths:
        popular_month = df.groupby('Month')[path].sum().idxmax()
        print(f"- {path}: Month #{popular_month}")

    plot_path = selected_paths[0]
    monthly_data = df.groupby('Month')[plot_path].sum()

    plt.figure(figsize=(10, 5))
    monthly_data.plot(kind='bar', color='green', alpha=0.7)
    plt.title(f'Usage of {plot_path} (2009)')
    plt.xlabel('Month')
    plt.ylabel('Cyclists Count')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--')
    plt.show()

except FileNotFoundError:
    print(f"Error: File '{filename}' not found. Check the filename in your folder!")
except Exception as e:
    print(f"An error occurred: {e}")