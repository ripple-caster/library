# main.py

from mathlib import add, subtract, power, factorial, is_even

a = 5
b = 3

result_add = add(a, b)
result_subtract = subtract(a, b)
result_power = power(a, b)
result_factorial = factorial(a)
is_a_even = is_even(a)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Power: {result_power}")
print(f"Factorial: {result_factorial}")
print(f"Is 'a' even? {is_a_even}")
