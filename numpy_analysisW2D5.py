import numpy as np
import time

# 1D Array
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(arr1)

# 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:")
print(arr2)

# 3D Array
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("\n3D Array:")
print(arr3)

# Vectorized Operations
print("\nAddition:")
print(arr1 + 10)

print("\nMultiplication:")
print(arr1 * 2)

# Boolean Masking
print("\nValues greater than 25:")
print(arr1[arr1 > 25])

# Fancy Indexing
print("\nFancy Indexing:")
print(arr1[[0, 2, 4]])

# Statistics
print("\nMean:", np.mean(arr1))
print("Standard Deviation:", np.std(arr1))
print("90th Percentile:", np.percentile(arr1, 90))
print("Correlation:")
print(np.corrcoef(arr1, arr1 * 2))

# Performance Comparison
python_list = list(range(1000000))

start = time.time()
python_result = [x * 2 for x in python_list]
python_time = time.time() - start

numpy_array = np.arange(1000000)

start = time.time()
numpy_result = numpy_array * 2
numpy_time = time.time() - start

print("\nPython Loop Time:", python_time)
print("NumPy Time:", numpy_time)