from datetime import date
from utils import add, subtract

print("Name: Tasin Hossain Orko")
print(f"Today's date: {date.today()}")

# Testing our branch features
print(f"Addition (5 + 3): {add(5, 3)}")
print(f"Subtraction (10 - 4): {subtract(10, 4)}")

from utils import add, subtract, multiply
print(f"Multiplication (4 * 3): {multiply(4, 3)}")

from utils import add, subtract, multiply, divide
try:
    print(f"Division (12 / 4): {divide(12, 4)}")
    print(f"Division (12 / 0): {divide(12, 0)}")
except ZeroDivisionError as e:
    print(f"Error caught gracefully: {e}")