
# Assignment 1: NumPy and Pandas

## NumPy

### Summary of NumPy Official Documentation

**NumPy** (Numerical Python) is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

### Essential Concepts and Features

1. **Introduction to NumPy**:
   - **Array Object**: The primary object in NumPy is the `ndarray`, a powerful N-dimensional array object. Arrays are homogeneous, meaning all elements must be of the same type.
   - **Installation**: NumPy can be installed using `pip`:

     ```bash
     pip install numpy
     ```

2. **Array Creation**:
   - **From Lists/Tuples**: Arrays can be created from Python lists or tuples using `np.array()`.

     ```python
     import numpy as np
     arr = np.array([1, 2, 3, 4])
     ```

   - **Built-in Functions**: Functions such as `np.zeros()`, `np.ones()`, and `np.arange()` generate arrays with specific values or ranges.

     ```python
     zeros_array = np.zeros((2, 3))
     ones_array = np.ones((2, 2))
     range_array = np.arange(10)
     ```

3. **Array Attributes**:
   - **Shape and Size**: Attributes such as `.shape`, `.size`, and `.dtype` provide information about the dimensions, total number of elements, and data type of the array.

     ```python
     shape = arr.shape
     size = arr.size
     dtype = arr.dtype
     ```

4. **Array Operations**:
   - **Mathematical Operations**: NumPy supports element-wise arithmetic operations, linear algebra operations, and statistical functions.

     ```python
     arr1 = np.array([1, 2, 3])
     arr2 = np.array([4, 5, 6])
     sum_arr = arr1 + arr2  # Output: array([5, 7, 9])
     ```

   - **Indexing and Slicing**: Arrays can be indexed and sliced to access specific elements or sub-arrays.

     ```python
     sub_array = arr[1:3]
     ```

5. **Broadcasting**:
   - **Broadcasting**: This feature allows NumPy to perform arithmetic operations on arrays of different shapes in a manner that is consistent with their dimensions.

     ```python
     arr = np.array([1, 2, 3])
     result = arr + 5  # Output: array([6, 7, 8])
     ```

6. **Useful Functions**:
   - **Mathematical Functions**: Functions like `np.mean()`, `np.std()`, and `np.sum()` provide statistics and aggregations.

     ```python
     mean_val = np.mean(arr)
     ```

7. **Random Module**:
   - **Generating Random Data**: The `numpy.random` module allows generation of random numbers, arrays, and distributions.

     ```python
     random_array = np.random.rand(3, 2)
     ```

## Pandas

### Summary of Pandas Official Documentation

**Pandas** is a powerful data manipulation and analysis library for Python. It provides data structures and functions needed to work on structured data seamlessly.

### Key Aspects for Beginners

1. **Introduction to Pandas**:
   - **Data Structures**: Pandas introduces two main data structures: `Series` and `DataFrame`. `Series` is a one-dimensional array-like object, while `DataFrame` is a two-dimensional table of data.

     ```python
     import pandas as pd
     series = pd.Series([1, 2, 3, 4])
     dataframe = pd.DataFrame({
         'A': [1, 2, 3],
         'B': [4, 5, 6]
     })
     ```

2. **Creating DataFrames**:
   - **From Various Sources**: DataFrames can be created from dictionaries, lists, or reading data from files (CSV, Excel).

     ```python
     df_from_dict = pd.DataFrame({
         'Name': ['Alice', 'Bob'],
         'Age': [25, 30]
     })
     ```

3. **Data Manipulation**:
   - **Selecting Data**: Access rows, columns, and specific data using methods like `.loc[]`, `.iloc[]`, and `.at[]`.

     ```python
     selected_data = dataframe.loc[0]  # Access first row
     ```

   - **Filtering Data**: Filter data based on conditions.

     ```python
     filtered_df = dataframe[dataframe['A'] > 1]
     ```

4. **Handling Missing Data**:
   - **Missing Values**: Methods such as `.isna()`, `.dropna()`, and `.fillna()` help in identifying and handling missing data.

     ```python
     cleaned_df = dataframe.dropna()
     ```

5. **Data Aggregation**:
   - **GroupBy Operations**: Group data by specific columns and perform aggregation functions.

     ```python
     grouped_df = dataframe.groupby('A').sum()
     ```

6. **Data Visualization**:
   - **Plotting**: Pandas integrates with libraries like Matplotlib for data visualization.

     ```python
     dataframe.plot(kind='bar')
     ```

7. **Data Input/Output**:
   - **Reading/Writing Data**: Read from and write to various file formats such as CSV, Excel, and JSON.

     ```python
     dataframe.to_csv('data.csv')
     ```

### Summary

- **NumPy** focuses on numerical operations with multi-dimensional arrays, offering efficient mathematical computations and array manipulations.
- **Pandas** is designed for data analysis and manipulation, providing powerful data structures (`Series` and `DataFrame`) and functions for handling structured data.

These resources are crucial for data analysis and scientific computing, offering essential tools for handling and analyzing data efficiently in Python.
```
