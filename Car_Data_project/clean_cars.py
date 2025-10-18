import pandas as pd

df = pd.read_csv('used_cars_data.csv')

print("--- INITIAL DATA HEAD ---")
print(df.head())

print("\n--- DATASET DIAGNOSTICS (INFO) ---")
print(df.info())

print("\n--- MISSING DATA COUNT ---")
print(df.isnull().sum())

# (Keep all the previous code above this line)

print("\n--- DUPLICATE DATA HUNT ---")

# First, count how many clones exist
duplicate_count = df.duplicated().sum()
print(f"Found {duplicate_count} duplicate rows.")

# Now, expose the clones. Show me the actual duplicate rows.
if duplicate_count > 0:
    print("\n--- THE CLONES ARE LISTED BELOW ---")
    print(df[df.duplicated()])

# (Keep the code that finds and prints the duplicate count)

# --- TERMINATE THE CLONES ---
df.drop_duplicates(inplace=True)
print(f"\nTermination complete. {duplicate_count} duplicate rows have been destroyed.")

# --- VERIFY THE KILL ---
print("\n--- Running verification scan... ---")
remaining_duplicates = df.duplicated().sum()
print(f"Remaining duplicate rows: {remaining_duplicates}")

# --- CATEGORICAL DATA INTERROGATION ---
print("\n--- CATEGORICAL DATA INTERROGATION ---")
print("Exposing unique values to find hidden inconsistencies...")

print("\nUnique Seller Types Found:")
print(df['seller_type'].unique())

print("\nUnique Transmission Types Found:")
print(df['transmission'].unique())

print("\nUnique Owner Types Found:")
print(df['owner'].unique())

# (Keep all the previous code above this line)

print("\n--- Final Interrogation: Fuel Types ---")
print(df['fuel'].unique())

print("\n--- FEATURE ENGINEERING: Calculating Car Age ---")
# Get the current year
current_year = 2025

# Create the new 'car_age' column
df['car_age'] = current_year - df['year']

# Now, we don't need the original 'year' column anymore. Terminate it.
df.drop('year', axis=1, inplace=True)

print("Feature 'car_age' created successfully.")
print("Original 'year' column has been terminated.")

print("\n--- FINAL DATAFRAME HEAD ---")
print(df.head())

# (Keep all the previous code above this line)

print("\n--- SECURING FINAL ASSET ---")
# Save the cleaned and engineered DataFrame to a new file.
df.to_csv('cleaned_cars_data.csv', index=False)

print("Phase 1 Complete. Clean data has been secured in 'cleaned_cars_data.csv'.")
print("Your asset is ready for analysis.")