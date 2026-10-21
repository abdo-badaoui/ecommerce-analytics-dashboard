import pandas as pd
import numpy as np
import os

def run_pipeline():
    print("Extracting: Generating raw transactional data...")
    np.random.seed(42)
    dates = pd.date_range(start='2025-01-01', end='2026-10-21', freq='h') # 'h' instead of 'H'
    data = {
        'OrderID': range(1000, 1000 + len(dates)),
        'Date': dates,
        'Category': np.random.choice(['Electronics', 'Apparel', 'Home & Garden', 'Sports'], len(dates)),
        'Price': np.random.uniform(10, 500, len(dates)),
        'Quantity': np.random.randint(1, 6, len(dates)),
        'CustomerID': np.random.randint(100, 500, len(dates)),
        'Status': np.random.choice(['Completed', 'Completed', 'Completed', 'Refunded'], len(dates))
    }
    df = pd.DataFrame(data)
    
    # Inject deliberate missing values to simulate real-world messy data
    df.loc[10:50, 'Price'] = np.nan
    
    print("Transforming: Cleaning data and engineering features...")
    # 1. Handle Nulls (Median Imputation)
    df['Price'] = df['Price'].fillna(df['Price'].median())
    
    # 2. Feature Engineering
    df['Total_Sales'] = df['Price'] * df['Quantity']
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    
    # 3. Filter valid transactions
    df_clean = df[df['Status'] == 'Completed'].copy()
    
    print("Loading: Saving production dataset...")
    os.makedirs('data', exist_ok=True)
    df_clean.to_csv('data/processed_sales.csv', index=False)
    print("Pipeline Complete! Data saved to data/processed_sales.csv")

if __name__ == '__main__':
    run_pipeline()
