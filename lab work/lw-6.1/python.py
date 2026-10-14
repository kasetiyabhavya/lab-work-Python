# ==========================================    
# LAB WORK #6.1 - ALL SOLUTIONS IN ONE CODE
# ==========================================

import random

# Q.1: Built-in Functions
print("Q.1: Built-in Functions")

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sorted:", sorted(numbers))
print("Sum:", sum(numbers))
print("Type:", type(numbers))


# Q.2: Float Number Operations
print("\nQ.2: Float Number Operations")

num = float(input("Enter a negative float number: "))

print("Absolute Value:", abs(num))
print("Power of 3:", pow(num, 3))
print("Rounded Value:", round(num, 2))


# Q.3: Random Integers
print("\nQ.3: Random Integers")

random_numbers = [random.randint(1, 100) for i in range(5)]

print("Random Numbers:", random_numbers)
print("Minimum:", min(random_numbers))
print("Maximum:", max(random_numbers))
print("Sum:", sum(random_numbers))


# Q.4: Sorting and Reversing
print("\nQ.4: Sorting and Reversing")

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Ascending Order:", sorted(nums))
print("Descending Order:", sorted(nums, reverse=True))
print("Reversed Order:", nums[::-1])

# Final output

print("\n==========================================")
print("      LAB WORK #6.1 COMPLETED")
print("==========================================")