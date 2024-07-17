
# Assignment 1: Python Learning Resources

## GeeksforGeeks Python Tutorial

### Summary

The GeeksforGeeks Python Tutorial covers a range of topics from basic to advanced Python concepts. Key areas include:

1. **Introduction to Python**: Basic syntax, installation, and environment setup.
2. **Data Types and Variables**: Integers, floats, strings, lists, tuples, and dictionaries.
3. **Control Flow**: `if`, `elif`, `else`, `for` loops, `while` loops, and `break`/`continue` statements.
4. **Functions**: Defining and calling functions, scope of variables, and lambda functions.
5. **File Handling**: Reading from and writing to files, working with different file modes.
6. **Modules and Packages**: Importing modules, creating packages, and using built-in libraries.
7. **Object-Oriented Programming (OOP)**: Classes, objects, inheritance, and polymorphism.
8. **Exception Handling**: Using `try`, `except`, `finally`, and custom exceptions.
9. **Advanced Topics**: Generators, decorators, context managers, and regular expressions.

### Helpful Code Example

Here's a simple code example from the tutorial demonstrating a basic function:

```python
# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calling the function
print(factorial(5))  # Output: 120
```

## Real Python

### Summary

**Real Python** is a comprehensive platform dedicated to Python programming with a focus on practical, hands-on learning. It offers a mix of tutorials, articles, and courses designed to help users master Python through real-world applications.

### Unique Features

- **In-Depth Tutorials**: Detailed explanations and practical examples covering a wide range of topics.
- **Interactive Exercises**: Allows users to practice coding directly in the browser.
- **Community Engagement**: Forums and discussion groups for learners to seek help and share knowledge.

### Informative Tutorial Summary

One notable tutorial is **"Understanding List Comprehensions in Python"**:

- **Overview**: Explains how to create lists in a concise and readable way using list comprehensions.
- **Example**:

  ```python
  # List comprehension to create a list of squares
  squares = [x**2 for x in range(10)]
  print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  ```

## TutorialsPoint Python Tutorial

### Summary

The **TutorialsPoint Python Tutorial** provides a structured introduction to Python programming, focusing on essential concepts and practical applications.

### Key Sections

- **Python Basics**: Introduction to Python, installation, basic syntax, and data types.
- **Control Flow**: Conditional statements and loops.
- **Functions**: Definition, arguments, and return values.
- **Modules and Libraries**: Importing and using modules.

### Unique Insights

- **Interactive Coding**: TutorialsPoint offers interactive Python exercises to practice coding concepts.
- **Step-by-Step Guidance**: Clear, incremental steps make it easy for beginners to follow along.

### Example Exercise

**Exercise**: Write a Python program to check if a number is prime.

```python
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Check if the number is prime
print(is_prime(29))  # Output: True
```

## W3Schools Python Tutorial

### Summary

**W3Schools Python Tutorial** is designed for beginners with a focus on simplicity and ease of learning.

### Key Features

- **Beginner-Friendly**: Provides a gentle introduction to Python with clear examples.
- **Interactive Examples**: In-browser interactive coding examples enhance learning.

### Interactive Example

**Example**: A simple Python program to print "Hello, World!":

```python
# Print statement
print("Hello, World!")
```

Users can run and modify this example directly on the W3Schools website to see changes in real-time.

## Programiz Python Programming

### Summary

**Programiz** offers a beginner-friendly approach to learning Python, emphasizing practical coding skills and hands-on exercises.

### Approach

- **Structured Learning**: The tutorial is organized into well-defined sections covering basic to advanced topics.
- **Practical Coding Exercises**: Provides exercises that reinforce learning through practice.

### Valuable Exercise

**Exercise**: Write a Python program to find the largest of three numbers.

```python
# Function to find the largest of three numbers
def find_largest(a, b, c):
    return max(a, b, c)

# Example usage
print(find_largest(3, 7, 5))  # Output: 7
```

This exercise helps learners understand basic function usage and conditional logic.

```
