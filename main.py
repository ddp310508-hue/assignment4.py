#List and Numpy Operations
import numpy as np

# Define two sample 2x2 matrices using lists
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

print("--- Method 1: Using Python Lists ---")
# Create a 2x2 result matrix filled with zeros
list_result = [[0, 0], [0, 0]]

# Nested loop to add elements element-wise
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        list_result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Result of List Addition:")
for row in list_result:
    print(row)


print("\n--- Method 2: Using NumPy Arrays ---")
# Convert lists into NumPy array objects
array1 = np.array(matrix1)
array2 = np.array(matrix2)

# Direct element-wise addition
numpy_result = array1 + array2

print("Result of NumPy Addition:")
print(numpy_result)

#Output:
#--- Method 1: Matrix Addition Using #Python Lists ---
#Result of List Addition:
#[6, 8]
#[10, 12]

#--- Method 2: Matrix Addition Using #NumPy Arrays ---
#Result of NumPy Addition:
#[[ 6  8]
#[10 12]]
