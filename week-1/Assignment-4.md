# Assignment 4: Virtual Environment Setup

## Concept of a Virtual Environment

A virtual environment in Python is an isolated environment that allows you to manage dependencies and packages for a project separately from the system-wide Python installation. This is crucial in data science projects to ensure that different projects with varying dependencies do not conflict with each other.

## Importance in Data Science Projects

- **Isolation:** Prevents package version conflicts between projects.
- **Dependency Management:** Ensures that the correct versions of libraries are used.
- **Reproducibility:** Facilitates consistent environments for different users or systems.

## Steps to Create and Use a Virtual Environment

1. **Create a Virtual Environment:**
   ```bash
   python -m venv ml_env
# 2 Activate the Virtual Environment:

On Windows:
```bash
ml_env\Scripts\activate
```
On macOS/Linux:
```bash
source ml_env/bin/activate
```
Install a Python Library (e.g., NumPy):

```bash
pip install numpy
```
Write a Python Script:

Create a script named example.py with the following content:

```python
import numpy as np

# Create a 2x2 matrix
matrix = np.array([[1, 2], [3, 4]])

print("Matrix:")
print(matrix)
```
Run the Script:

```bash 
python example.py
```
Output:
```lua
Matrix:
[[1 2]
 [3 4]]
```
### This script imports NumPy, creates a 2x2 matrix, and prints it, demonstrating a basic operation within the virtual environment.
