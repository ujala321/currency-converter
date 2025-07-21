import pandas as pd
import numpy as np

data = {
    'RegNo': [101, 102, 103, 104, 105, 106, 107, 108],
    'Name': ['Aman', 'Bina', 'Chetan', 'Divya', 'Esha', 'Farhan', 'Gauri', 'Hari'],
    'Sem1': [80, 75, 60, 85, np.nan, 90, 70, 65],
    'Sem2': [70, 55, 65, np.nan, 60, 85, 50, 45]
}

df = pd.DataFrame(data)

df = pd.DataFrame(data)

print("Complete Student DataFrame:\n", df)

print("\nFirst 7 rows:\n", df.head(7))

custom_indexes = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
df.index = custom_indexes
print("\nDataFrame with custom indexes:\n", df)

df_no_null = df.dropna()
print("\nDataFrame after dropping rows with NULL values:\n", df_no_null)

df_replaced = df.fillna(150)
print("\nDataFrame after replacing NULL values with 150:\n", df_replaced)

students_sem2_above_50 = df[df['Sem2'] > 50]
print("\nStudents with Semester 2 marks greater than 50:\n", students_sem2_above_50)
