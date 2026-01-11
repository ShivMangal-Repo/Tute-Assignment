# Task 1: Test math_utils

import math_utils
from math_utils import square

print("Add:", math_utils.add(5, 3))           # 8
print("Subtract:", math_utils.subtract(10, 4)) # 6
print("Square:", square(6))                   # 36


# Task 2: Test string_utils

import string_utils

text = "hello world from python"

print("Capitalize:", string_utils.capitalize_words(text))  # "Hello World From Python"
print("Reverse:", string_utils.reverse_string(text))       # "nohtyp morf dlrow olleh"
print("Word Count:", string_utils.word_count(text))        # 5


# Task 4: Test shop_package

import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

# Discount functions
print("Apply Discount:", disc.apply_discount(1000, 10))   # 900
print("Flat Discount:", disc.flat_discount(500))          # 450

# Billing functions
prices = [100, 200, 300]
total = calculate_total(prices)
print("Total:", total)                                     # 600
print("Total with Tax:", apply_tax(total))                # 630.0

# Optional: Using functions directly from package if __init__.py is used
from shop_package import apply_discount, flat_discount, calculate_total, apply_tax
print("Direct import - Apply Discount:", apply_discount(2000, 25))  # 1500
