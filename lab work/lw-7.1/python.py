# ==========================================    
# LAB WORK #7.1- ALL SOLUTIONS IN ONE CODE
# ==========================================.

# 1D Array (List) Operations

# Q.1 Display array using loop
print("Q.1: Display Array")
arr = [10, 20, 30, 40, 50]

for i in arr:
    print(i)


# Q.2 Calculate sum of all elements
print("\nQ.2: Sum of Array")
arr = [10, 20, 30, 40, 50]
total = 0

for i in arr:
    total += i

print("Sum =", total)


# Q.3 Find maximum and minimum
print("\nQ.3: Maximum and Minimum")
arr = [25, 10, 45, 5, 30]

print("Maximum =", max(arr))
print("Minimum =", min(arr))


# Q.4 Insert element at a specific position
print("\nQ.4: Insert Element")
arr = [10, 20, 30, 40, 50]

position = int(input("Enter position (0-5): "))
value = int(input("Enter new element: "))

if 0 <= position <= len(arr):
    arr.insert(position, value)
    print("Updated Array:", arr)
else:
    print("Invalid position")


# Q.5 Delete element by value
print("\nQ.5: Delete Element")
arr = [10, 20, 30, 40, 50]

value = int(input("Enter value to delete: "))

if value in arr:
    arr.remove(value)
    print("Updated Array:", arr)
else:
    print("Element not found")


# Q.6 Update element using index
print("\nQ.6: Update Element")
arr = [10, 20, 30, 40, 50]

index = int(input("Enter index (0-4): "))
value = int(input("Enter new value: "))

if 0 <= index < len(arr):
    arr[index] = value
    print("Updated Array:", arr)
else:
    print("Invalid index")


# Q.7 Search element and return index
print("\nQ.7: Search Element")
arr = [10, 20, 30, 40, 50]

value = int(input("Enter element to search: "))

if value in arr:
    print("Index =", arr.index(value))
else:
    print("Element not found")


# Q.8 Concatenate two arrays
print("\nQ.8: Concatenate Arrays")
arr1 = [10, 20, 30]
arr2 = [40, 50, 60]

arr3 = arr1 + arr2

print("Combined Array:", arr3)


# Q.9 Sort array in ascending order
print("\nQ.9: Sort Array")
arr = [50, 20, 40, 10, 30]

arr.sort()

print("Sorted Array:", arr)

print("\n==========================================")
print("      LAB WORK #7.1 COMPLETED")
print("==========================================")