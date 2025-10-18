import pandas as pd

df = pd.read_csv('used_cars_data.csv')

print("--- INITIAL DATA HEAD ---")
print(df.head())

print("\n--- DATASET DIAGNOSTICS (INFO) ---")
print(df.info())

print("\n--- MISSING DATA COUNT ---")
print(df.isnull().sum())


print("\n--- DUPLICATE DATA HUNT ---")

duplicate_count = df.duplicated().sum()
print(f"Found {duplicate_count} duplicate rows.")

if duplicate_count > 0:
    print("\n--- THE CLONES ARE LISTED BELOW ---")
    print(df[df.duplicated()])


df.drop_duplicates(inplace=True)
print(f"\nTermination complete. {duplicate_count} duplicate rows have been destroyed.")

print("\n--- Running verification scan... ---")
remaining_duplicates = df.duplicated().sum()
print(f"Remaining duplicate rows: {remaining_duplicates}")

print("\n--- CATEGORICAL DATA INTERROGATION ---")
print("Exposing unique values to find hidden inconsistencies...")

print("\nUnique Seller Types Found:")
print(df['seller_type'].unique())

print("\nUnique Transmission Types Found:")
print(df['transmission'].unique())

print("\nUnique Owner Types Found:")
print(df['owner'].unique())


print("\n--- Final Interrogation: Fuel Types ---")
print(df['fuel'].unique())

print("\n--- FEATURE ENGINEERING: Calculating Car Age ---")
current_year = 2025

df['car_age'] = current_year - df['year']


df.drop('year', axis=1, inplace=True)

print("Feature 'car_age' created successfully.")
print("Original 'year' column has been terminated.")

print("\n--- FINAL DATAFRAME HEAD ---")
print(df.head())



print("\n--- SECURING FINAL ASSET ---")

df.to_csv('cleaned_cars_data.csv', index=False)

print("Phase 1 Complete. Clean data has been secured in 'cleaned_cars_data.csv'.")
print("Your asset is ready for analysis.")