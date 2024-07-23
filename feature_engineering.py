import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data from csv file
df = pd.read_csv('data.csv')

# Delete columns with min_bank
df = df.drop(['min_bank'], axis=1)

# Delete columns with national_inv
df = df.drop(['national_inv'], axis=1)

# Fill NaN values with appropriate method
df = df.fillna(method='ffill')

# Initialize label encoder
le = LabelEncoder()

# Encode categorical variables
categorical_vars = ['potential_issue', 'oe_constraint', 'stop_auto_buy', 'deck_risk', 'ppap_risk', 'rev_stop', 'went_on_backorder']
for var in categorical_vars:
    df[var] = le.fit_transform(df[var])

# Print the result
print(df)

# Save the transformed data frame as cleaned_data.csv
df.to_csv('cleaned_data.csv', index=False)

# Print the top 5 rows of cleaned dataframe
print(df.head(5))