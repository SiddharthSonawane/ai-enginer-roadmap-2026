import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Task 1: Print the shape of data
# Task 2: Reshape it into 4 rows and 2 columns, store as data_2d
# Task 3: Print the shape of data_2d to confirm

print(f"Shape of date: {data.shape}")

data_2d = data.reshape(4, 2)
print(f"Shape of data_2d: {data_2d.shape}")