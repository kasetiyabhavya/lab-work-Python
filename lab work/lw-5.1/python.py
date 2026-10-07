# ==========================================
# LAB WORK #5.1 - ALL SOLUTIONS IN ONE CODE
# ==========================================


# Q.1 - Create a list from 1 to 10 and append a new number
print("--- Q.1 ---")

numbers = list(range(1, 11))

print("Original list:", numbers)

numbers.append(11)

print("Updated list:", numbers)

print()


# Q.2 - Find largest and smallest number
print("--- Q.2 ---")

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("List:", numbers)
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))

print()


# Q.3 - Print unique values from a tuple
print("--- Q.3 ---")

my_tuple = (1, 2, 2, 3, 4, 4, 5)

unique_values = tuple(set(my_tuple))

print("Original tuple:", my_tuple)
print("Unique values:", unique_values)

print()


# Q.4 - Modify the third element of a list
print("--- Q.4 ---")

my_list = [10, 20, 30, 40, 50]

print("Original list:", my_list)

my_list[2] = 100

print("Updated list:", my_list)

print()


# Q.5 - Create a list with nested elements and modify inner list
print("--- Q.5 ---")

my_list = [1, [2, 3], 4]

print("Original list:", my_list)

my_list[1][0] = 100

print("Updated list:", my_list)

print()


# Q.6 - Adding, removing and replacing elements in a list
print("--- Q.6 ---")

my_list = [10, 20, 30, 40]

print("Original list:", my_list)

# Adding
my_list.append(50)
print("After adding:", my_list)

# Removing
my_list.remove(20)
print("After removing:", my_list)

# Replacing
my_list[1] = 100
print("After replacing:", my_list)

print("Lists are mutable, so their elements can be changed.")

print()


# Q.7 - Tuple containing lists
print("--- Q.7 ---")

my_tuple = ([1, 2], [3, 4], [5, 6])

print("Original tuple:", my_tuple)

my_tuple[0][0] = 100

print("Updated tuple:", my_tuple)

print("The tuple is immutable, but the inner lists are mutable.")

print()


# Q.8 - Swap using a third variable
print("--- Q.8 ---")

a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

print()


# Q.9 - Swap without using a third variable
print("--- Q.9 ---")

a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


print()
print("==========================================")
print("       LAB WORK #5.1 COMPLETED")
print("==========================================")