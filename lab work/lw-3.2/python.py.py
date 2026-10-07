# ==========================================
# LAB WORK #3.2 SOLUTIONS
# ==========================================

# --- 5
print("--- Q.1: Input until 0 ---")
num = int(input("Enter a number (enter 0 to stop): "))
while num != 0:
    print(f"You entered: {num}")
    num = int(input("Enter a number (enter 0 to stop): "))
print("Loop stopped because you entered 0.\n")


# --- Q.2: Create a program using a `for` loop to: Iterate over a given range(1 to 10). Print each digit's square, one per line. ---
print("--- Q.2: Square of digits from 1 to 10 ---")
for i in range(1, 11):
    print(f"Square of {i} is {i ** 2}")
print()


# --- Q.3: Write a program to: Use a `while` loop to print all even numbers between 1 and 50. ---
print("--- Q.3: Even numbers between 1 and 50 using while loop ---")
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print("\n\n")


# --- Q.4: Write a program to: Use the `range()` function to generate a sequence of numbers from 1 to 20. Print only the odd numbers using a `for` loop. ---j
print("--- Q.4: Odd numbers from 1 to 20 ---")
for i in range(1, 21):
    if i % 2 != 0:
        print(i, end=" ")
print("\n\n")


# --- Q.5: Implement a program that: Uses the `range()` function with three arguments (start, stop, step) to print multiples of 5 from 5 to 50. ---
print("--- Q.5: Multiples of 5 from 5 to 50 ---")
for i in range(5, 51, 5):
    print(i, end=" ")
print("\n\n")


# --- Q.6: Create a program using a `for` loop and `range()` to: Print a reverse countdown from 10 to 1. ---
print("--- Q.6: Reverse countdown from 10 to 1 ---")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n\n")


# --- Q.7: Create a program that: Iterates over a string (e.g., "PYTHON"). Uses a continue statement to skip vowels and print only consonants. ---
print("--- Q.7: Print consonants from 'PYTHON' ---")
word = "PYTHON"
for char in word:
    if char in "AEIOUaeiou":
        continue
    print(char, end=" ")
print("\n")