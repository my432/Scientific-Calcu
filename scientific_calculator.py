import streamlit as st
import math

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    return math.log(x, base)

def exp(x):
    return math.exp(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    return math.factorial(x)

# Streamlit App
st.title("Scientific Calculator")

# Select operation
operation = st.selectbox("Select Operation", 
                         ["Addition", "Subtraction", "Multiplication", "Division", "Power", "Square Root",
                          "Logarithm", "Exponential", "Sine", "Cosine", "Tangent", "Factorial"])

# Input fields based on selected operation
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    x = st.number_input("Enter first number", format="%.6f")
    y = st.number_input("Enter second number", format="%.6f")
    
elif operation in ["Square Root", "Logarithm", "Exponential", "Sine", "Cosine", "Tangent", "Factorial"]:
    x = st.number_input("Enter number", format="%.6f")

    # Additional input for logarithm base
    if operation == "Logarithm":
        base = st.number_input("Enter base (default is 10)", format="%.6f", value=10.0)

# Perform calculation and display result
if st.button("Calculate"):
    if operation == "Addition":
        result = add(x, y)
    elif operation == "Subtraction":
        result = subtract(x, y)
    elif operation == "Multiplication":
        result = multiply(x, y)
    elif operation == "Division":
        result = divide(x, y)
    elif operation == "Power":
        result = power(x, y)
    elif operation == "Square Root":
        result = square_root(x)
    elif operation == "Logarithm":
        result = logarithm(x, base)
    elif operation == "Exponential":
        result = exp(x)
    elif operation == "Sine":
        result = sine(x)
    elif operation == "Cosine":
        result = cosine(x)
    elif operation == "Tangent":
        result = tangent(x)
    elif operation == "Factorial":
        try:
            result = factorial(int(x))
        except ValueError:
            result = "Factorial is only defined for non-negative integers."

    # Display the result
    st.write(f"Result: {result}")
