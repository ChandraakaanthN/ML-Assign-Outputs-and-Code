import numpy as np
import pandas as pd
# Count the Occurrence of Sequences in Given Array
arr = np.array([2, 8, 9, 4, 2, 8, 2, 8])
output = repr(arr).count("2, 8")
print("Number of Occurrences of sequence:", output)
# Count Individual Occurrences
print("Number of 10's:", np.count_nonzero(arr == 2))
# Find the Most Frequent Value in a NumPy Array
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())
# Combining a One and a Two-Dimensional NumPy Array
print("\nUsing np.nditer:")
num_1d = np.arange(5)
num_2d = np.arange(10).reshape(2, 5)
print(num_2d)
for a, b in np.nditer([num_1d, num_2d]):
    print(f"{a}:{b}", end=", ")
print("\n\nUsing np.column_stack and np.vstack:")
arr1 = np.array([20, 30])
arr2 = np.array([[1, 2], [3, 4]])
res_column = np.column_stack([arr1, arr2])
print("Result using column stack:\n", res_column, "\n")
res_row = np.vstack([arr1, arr2])
print("Result using vstack (row stack):\n", res_row)
# All Possible Combinations of Arrays
array_1 = np.array([1, 2])
array_2 = np.array([4, 6])
comb_array = np.array(np.meshgrid(array_1, array_2)).T.reshape(-1, 2)
print("\nCombination array of all elements of array 1 and 2:")
print(comb_array)
# Border for Array
array = np.ones((3, 3))
print("\n7 on the border and 1 inside the array")
array = np.pad(array, pad_width=1, mode='constant', constant_values=7)
print(array)

# Creating DataFrame from Pandas Series
series1 = pd.Series([10, 20, 30, 40], name="A")
series2 = pd.Series([5, 15, 25, 35], name="B")
df = pd.DataFrame({series1.name: series1, series2.name: series2})
print("\nDataFrame created from Pandas Series:")
print(df)

# Data Cleaning in a String Data DataFrame
names = pd.Series(['Alice', 'Bob'])
cities = pd.Series([' New York ', 'Los Angeles'])
professions = pd.Series(['  Engineer  ', 'Doctor'])
data = {'Name': names, 'City': cities, 'Profession': professions}
res = pd.DataFrame(data)
res["City"] = res["City"].str.strip()
res["Name"] = res["Name"].str.lower()
print("\nCleaned DataFrame:")
print(res)

# Reindexing in Pandas DataFrame
data = {
    "age": [50, 40, 30, 40],
    "qualified": [True, False, False, False]
}
idx = ["chandra", "anishma", "surya", "lokesh"]
df = pd.DataFrame(data, index=idx)

newidx = ["cha", "ani", "suri", "loki"]
newdf = df.reindex(newidx)
print("\nReindexed DataFrame:")
print(newdf)

# Mapping New Data to an Existing DataFrame
initial_data = {
    'First_name': ['Ram', 'Bheem'],
    'Last_name': ['Sri', 'Shri'],
    'Age': [42, 52],
    'City': ['complex1', 'complex2']
}
df = pd.DataFrame(initial_data, columns=['First_name', 'Last_name', 'Age', 'City'])

# Create new column using dictionary
new_data = {
    "Ram": "Shabda Vidya",
    "Bheem": "Bhramastra"
}

# Combine this new data with existing DataFrame
df["skills"] = df["First_name"].map(new_data)
print("\nDataFrame with Mapped Data:")
print(df)
