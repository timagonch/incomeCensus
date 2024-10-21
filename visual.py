import pandas as pd
import numpy as np

adult_data = pd.read_csv('adult.data', header=None, names=['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'class'])

# Strip whitespace from the entire DataFrame to handle spaces around "?"
adult_data = adult_data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
# Replace "?" with NaN
adult_data.replace('?', np.nan, inplace=True)

print(adult_data.head(29))
print(adult_data.isnull().sum())

print(adult_data.shape)

'''
# plot missing values of occupation based on age
import matplotlib.pyplot as plt

# Filter rows where 'occupation' is missing (NaN)
missing_occupation = adult_data[adult_data['occupation'].isnull()]

# Plot missing values of 'occupation' based on 'age'
plt.figure(figsize=(10, 6))
plt.hist(missing_occupation['age'], bins=5, color='blue', edgecolor='black')
plt.title('Distribution of Missing Values in Occupation by Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
'''
# Check unique entries in the 'occupation' column
unique_occupations = adult_data['occupation'].unique().tolist()

# Print the unique values
print(len(unique_occupations))



