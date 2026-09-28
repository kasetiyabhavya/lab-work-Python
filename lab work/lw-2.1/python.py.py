# ==========================================
# LAB WORK #2.1 - ALL SOLUTIONS IN ONE CODE
# ==========================================

print("------------------------------------------")
print("          STARTING LAB WORK #2.1          ")
print("------------------------------------------\n")

# --- Q.1: Check Even or Odd using if-else ---
print("--- Q.1: Even or Odd Checker ---")
num1 = int(input("Enter a number to check even/odd: "))
if num1 % 2 == 0:
    print(f"The number {num1} is Even.\n")
else:
    print(f"The number {num1} is Odd.\n")


# --- Q.2: Find Minimum Number from Two Numbers ---
print("--- Q.2: Minimum Number Finder ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a < b:
    print(f"Minimum number is: {a}\n")
elif b < a:
    print(f"Minimum number is: {b}\n")
else:
    print("Both numbers are equal.\n")


# --- Q.3: Positive, Negative, or Neutral using Ladder if-elif-else ---
print("--- Q.3: Positive, Negative, or Neutral Checker ---")
num2 = float(input("Enter a number to check its sign: "))

if num2 > 0:
    print("Positive\n")
elif num2 < 0:
    print("Negative\n")
else:
    print("Neutral\n")


# --- Q.4: Find Largest Among Three Integers using if-elif-else ---
print("--- Q.4: Largest Among Three Numbers ---")
x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))
z = int(input("Enter third integer: "))

if x >= y and x >= z:
    print(f"The largest number is: {x}\n")
elif y >= x and y >= z:
    print(f"The largest number is: {y}\n")
else:
    print(f"The largest number is: {z}\n")


# --- Q.5: Calculator using Ladder if-elif-else statement ---
print("--- Q.5: Basic Calculator using Ladder ---")
num_a = float(input("Enter first number: "))
num_b = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    print(f"Result: {num_a} + {num_b} = {num_a + num_b}\n")
elif operator == '-':
    print(f"Result: {num_a} - {num_b} = {num_a - num_b}\n")
elif operator == '*':
    print(f"Result: {num_a} * {num_b} = {num_a * num_b}\n")
elif operator == '/':
    if num_b != 0:
        print(f"Result: {num_a} / {num_b} = {num_a / num_b}\n")
    else:
        print("Error: Division by zero is not allowed.\n")
else:
    print("Invalid operator entered!\n")

print("------------------------------------------")
print("      LAB WORK #2.1 COMPLETED SUCCESSFULLY!     ")
print("------------------------------------------")