#!/usr/bin/env python3
"""
Interactive Python Examples for Certification Prep

This file contains examples that can be run directly or used
for debugging practice in VS Code.
"""


def basic_examples():
    """Basic Python concepts examples."""
    print("=== Basic Python Examples ===")
    
    # Variables and types
    name = "Python Learner"
    age = 25
    is_learning = True
    
    print(f"Hello, {name}!")
    print(f"Age: {age}, Learning: {is_learning}")
    
    # Basic operations
    x, y = 10, 3
    print(f"\nBasic Operations:")
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y:.2f}")
    print(f"{x} // {y} = {x // y}")
    print(f"{x} % {y} = {x % y}")


def data_structures_examples():
    """Data structures examples."""
    print("\n=== Data Structures Examples ===")
    
    # Lists
    fruits = ["apple", "banana", "orange"]
    print(f"Fruits: {fruits}")
    fruits.append("grape")
    print(f"After adding grape: {fruits}")
    
    # Dictionaries
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    print(f"Person: {person}")
    print(f"Name: {person['name']}")
    
    # Tuples
    coordinates = (10, 20)
    print(f"Coordinates: {coordinates}")


def control_flow_examples():
    """Control flow examples."""
    print("\n=== Control Flow Examples ===")
    
    # If statements
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    
    print(f"Score: {score}, Grade: {grade}")
    
    # Loops
    print("\nCounting to 5:")
    for i in range(1, 6):
        print(f"Count: {i}")
    
    # While loop
    print("\nCountdown:")
    countdown = 3
    while countdown > 0:
        print(f"{countdown}...")
        countdown -= 1
    print("Launch!")


def function_examples():
    """Function examples."""
    print("\n=== Function Examples ===")
    
    def greet(name, greeting="Hello"):
        """Simple greeting function."""
        return f"{greeting}, {name}!"
    
    def calculate_area(length, width):
        """Calculate rectangle area."""
        return length * width
    
    # Function calls
    print(greet("Python"))
    print(greet("World", "Hi"))
    
    area = calculate_area(5, 3)
    print(f"Rectangle area (5x3): {area}")


def main():
    """Main function to run all examples."""
    print("🐍 Python Certification Prep - Interactive Examples")
    print("=" * 50)
    
    try:
        basic_examples()
        data_structures_examples()
        control_flow_examples()
        function_examples()
        
        print("\n🎉 All examples completed successfully!")
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")


if __name__ == "__main__":
    main()