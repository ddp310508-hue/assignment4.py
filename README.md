# Lab Assignment 4: Matrix Addition using Lists and NumPy

**Course:** School of Computer Engineering and Technology  
**Assignment No:** 4  

## Problem Statement
Write a Python program to create an array and perform addition of two matrices. (Using list and NumPy array.)

## Aim
Write a Python program to create an array and perform addition of two matrices.

## Objectives
* To learn the basics of array and it's operation.
* To learn the mathematical operations using arrays and the concept of structured data storage in python programming.

## Theory

### 1. Arrays with Example
An array is a collection of elements stored at contiguous memory locations, where each item can be accessed using an index. In standard Python, arrays are typically represented using **Lists** (or nested lists for 2D structures).
* **Example of a 2D Array (Matrix):** `matrix = [[1, 2], [3, 4]]` where `matrix[0]` gets the first row `[1, 2]`.

### 2. Use of NumPy
**NumPy (Numerical Python)** is an open-source library used for high-performance scientific computing and data analysis. It introduces the `ndarray` object, a multidimensional array wrapper that enables fast math operations on grids of data without manually writing loops.

### 3. Advantages of NumPy over Python Lists
* **Speed:** NumPy operations are written in C, making them significantly faster than standard Python loops.
* **Memory Efficiency:** NumPy arrays store elements close together in memory and use fixed types, consuming less space than Python lists.
* **Convenience:** Allows element-wise arithmetic operations directly (e.g., `A + B`) instead of writing nested loops.

## Platform
Windows/Ubuntu - Python Editor (Jupyter Notebook, IDLE, or any IDE).

## Algorithm/Pseudo code
1. Start the program.
2. **Matrix Addition using Lists:**
   * Initialize two nested lists of equal dimensions.
   * Create an empty or zero-filled result matrix of the same size.
   * Loop through each row index `i` and column index `j`.
   * Add elements: `result[i][j] = matrix1[i][j] + matrix2[i][j]`.
1. **Matrix Addition using NumPy:**
   * Import the `numpy` library.
   * Convert the lists into NumPy arrays using `np.array()`.
   * Add the arrays directly using the `+` operator.
1. Print the final outputs for both approaches.
2. End the program.
###Input
```text
Matrix 1:
[[1, 2]]

Matrix 2:
[[5, 6]]
```
### Output
```text
--- Method 1: Using Python Lists ---
Result of List Addition:
[6, 8]
[10, 12]

--- Method 2: Using NumPy Arrays ---
Result of NumPy Addition:
[[ 6  8]
 [10 12]]
```
## Conclusion
Studied matrix and NumPy library in Python.

## FAQs

### 1. What is a matrix? How can it be represented in Python using arrays or lists?
A matrix is a two-dimensional rectangular grid of numbers structured in rows and columns. In standard Python, it is represented using a nested list (a list containing other lists), where each sub-list is a row. In optimized programming, it is represented as a 2D `numpy.array`.

### 2. What is the condition for two matrices to be added?
Two matrices can only be added together if they share the exact same dimensions. This means both matrices must have the same number of rows and the same number of columns.

### 3. How do you access individual elements of a 2D array (matrix) in Python?
* **In Python Lists:** You use double square brackets representing the row index and column index: `matrix[row][column]`.
* **In NumPy Arrays:** You can use a comma-separated format within a single set of brackets: `matrix[row, column]`.

### 4. Write the general logic or steps to add two matrices element-wise in Python.
1. Ensure both matrices have identical dimensions.
2. Initialize a blank target matrix to store the results.
3. Traverse through each row position using an outer loop.
4. Traverse through each column position using an inner loop.
5. Add the values at the matching row/column indices from both matrices and save them to the target matrix.
