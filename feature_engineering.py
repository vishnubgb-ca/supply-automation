import pandas as pd

# Load data from csv file
df = pd.read_csv('data.csv')

# Check if 'PNEUMONIA' column exists
if 'PNEUMONIA' in df.columns:
    # Delete 'PNEUMONIA' column
    df = df.drop('PNEUMONIA', axis=1)
else:
    print("'PNEUMONIA' column not found in the dataframe.")

# Handle NaN values
df = df.dropna()

# Save the cleaned dataframe to a new csv file
df.to_csv('cleaned_data.csv', index=False)

# Print the top 5 rows of the cleaned dataframe
print(df.head(5))