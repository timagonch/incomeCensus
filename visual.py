import pandas as pd
import numpy as np

adult_data = pd.read_csv('adult.data', header=None, names=['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'class'])

# Strip whitespace from the entire DataFrame to handle spaces around "?"
adult_data = adult_data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
# Replace "?" with NaN
adult_data.replace('?', np.nan, inplace=True)

# Set the option to display all columns
#pd.set_option('display.max_columns', None)
#pd.reset_option('display.max_columns')

print(adult_data.head(29))
print(adult_data.isnull().sum())

print(adult_data.shape)


# plot missing values of occupation based on age
import matplotlib.pyplot as plt

# Filter rows where 'occupation' is missing (NaN)
missing_occupation = adult_data[adult_data['occupation'].isnull()]
'''
# Plot missing values of 'occupation' based on 'age'
plt.figure(figsize=(10, 6))
plt.hist(missing_occupation['age'], bins=10, color='blue', edgecolor='black')
plt.title('Distribution of Missing Values in Occupation by Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
'''
# Check unique entries in the 'occupation' column
unique_occupations = adult_data['occupation'].unique().tolist()

# Print the unique values
print(unique_occupations)

# Check how many rows both 'workclass' and 'occupation' are missing
combined_missing = adult_data[(adult_data['workclass'].isnull()) & (adult_data['occupation'].isnull())]
# Print the number of rows where both 'workclass' and 'occupation' are missing
print(combined_missing.shape[0])

#Make pop-up window to display the DataFrame
import tkinter as tk
from tkinter import ttk

def show_dataframe(df):
    # Create a new Tkinter window
    root = tk.Tk()
    root.title("DataFrame Viewer")

    # Create a Treeview widget to display the DataFrame
    tree = ttk.Treeview(root)

    # Define columns
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    # Add column headers
    for col in df.columns:
        tree.heading(col, text=col)

    # Add rows to the treeview
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.pack(expand=True, fill="both")

    # Start the Tkinter event loop
    root.mainloop()

show_dataframe(combined_missing.sort_values(by='age', ascending=True))
