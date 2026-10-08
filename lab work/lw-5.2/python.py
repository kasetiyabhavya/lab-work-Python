# ==========================================
# LAB WORK #5.2 - ALL SOLUTIONS IN ONE CODE
# ==========================================


# Q.1 - Set operations
print("--- Q.1: SET ---")

numbers = {10, 20, 30, 40}

print("Original set:", numbers)

# Add new element
numbers.add(50)
print("After adding 50:", numbers)

# Remove existing element
numbers.remove(20)
print("After removing 20:", numbers)

# Demonstrate that sets do not allow duplicates
numbers.add(30)
print("After adding duplicate 30:", numbers)
print("Duplicate elements are not stored in a set.")

print()


# Q.2 - Dictionary operations
print("--- Q.2: DICTIONARY ---")

student = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print("Original dictionary:", student)

# Add new key-value pair
student["course"] = "Python"
print("After adding course:", student)

# Update existing key
student["age"] = 26
print("After updating age:", student)

# Remove key-value pair
del student["city"]
print("After removing city:", student)

print()


# Q.3 - List to set to remove duplicates
print("--- Q.3: REMOVE DUPLICATES ---")

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original list:", numbers)

unique_numbers = set(numbers)

print("Unique numbers:", unique_numbers)

print()


# Q.4 - Product dictionary and highest price
print("--- Q.4: HIGHEST PRICE ---")

products = {
    "Laptop": 50000,
    "Mobile": 25000,
    "Tablet": 30000,
    "Headphones": 5000
}

print("Products:", products)

highest_product = max(products, key=products.get)

print("Product with highest price:", highest_product)
print("Highest price:", products[highest_product])

print()


# Q.5 - Type casting
print("--- Q.5: TYPE CASTING ---")

my_list = [10, 20, 30, 20, 40]

# List to set
my_set = set(my_list)

# List to tuple
my_tuple = tuple(my_list)

# Tuple to list
tuple_list = list(my_tuple)

# Set to list
set_list = list(my_set)

# Set to tuple
set_tuple = tuple(my_set)

print("Original list:", my_list)
print("List to Set:", my_set)
print("List to Tuple:", my_tuple)
print("Tuple to List:", tuple_list)
print("Set to List:", set_list)
print("Set to Tuple:", set_tuple)

print("\nExplanation:")
print("List: Ordered and allows duplicate values.")
print("Set: Unordered and removes duplicate values.")
print("Tuple: Ordered and cannot be changed.")

print()


# Q.6 - String to list, set and tuple
print("--- Q.6: STRING CONVERSION ---")

data = input("Enter comma-separated numbers: ")

# Convert string into list
my_list = data.split(",")

# Convert list into set
my_set = set(my_list)

# Convert list into tuple
my_tuple = tuple(my_list)

print("List:", my_list)
print("Set:", my_set)
print("Tuple:", my_tuple)
print()


# Q.7 - Set to dictionary with square values
print("--- Q.7: INTEGER SQUARE DICTIONARY ---")

numbers = {1, 2, 3, 4, 5}

square_dict = {}

for number in numbers:
    square_dict[number] = number ** 2

print("Set:", numbers)
print("Dictionary:", square_dict)


print()
print("==========================================")
print("       LAB WORK #5.2 COMPLETED")
print("==========================================")