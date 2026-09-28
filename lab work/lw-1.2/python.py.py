# ==========================================
# LAB WORK #1.2 - ALL SOLUTIONS IN ONE CODE
# ==========================================

print("------------------------------------------")
print("          STARTING LAB WORK #1.2          ")
print("------------------------------------------\n")


# --- Q.1: Demo of sep and end in print() ---
print("--- Q.1: Demonstrating sep and end in print() ---")
print("Python", "Programming", "Language", sep=" - ")
print("Hello", end=" ")
print("World!", end="\n\n")


# --- Q.2: User Details & Formatted Message ---
print("--- Q.2: Interactive User Details ---")
name = input("Enter your name: ")
age = input("Enter your age: ")
hobby = input("Enter your favourite hobby: ")
print(f"Hello, {name}! At {age}, enjoying {hobby} sounds fun!\n")


# --- Q.3: Arithmetic Operations ---
print("--- Q.3: Arithmetic Operations on Two Numbers ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition ({num1} + {num2}) = {num1 + num2}")
print(f"Subtraction ({num1} - {num2}) = {num1 - num2}")
print(f"Multiplication ({num1} * {num2}) = {num1 * num2}")

if num2 != 0:
    print(f"Division ({num1} / {num2}) = {num1 / num2}")
    print(f"Floor Division ({num1} // {num2}) = {num1 // num2}")
    print(f"Modulus ({num1} % {num2}) = {num1 % num2}")
else:
    print("Division, Floor Division, and Modulus are not possible with zero.")

print(f"Exponentiation ({num1} ** {num2}) = {num1 ** num2}\n")


# --- Q.4: Different Datatypes and type() ---
print("--- Q.4: Variables of Different Datatypes ---")
var_int = 25
var_float = 99.50
var_str = "Python Lab"
var_bool = True

print(f"Value: {var_int}, Type: {type(var_int)}")
print(f"Value: {var_float}, Type: {type(var_float)}")
print(f"Value: {var_str}, Type: {type(var_str)}")
print(f"Value: {var_bool}, Type: {type(var_bool)}\n")


# --- Q.5: Height and Weight Collector ---
print("--- Q.5: Height and Weight Input ---")
height = input("Enter your height (e.g., 5.8 ft / 175 cm): ")
weight = input("Enter your weight (e.g., 65 kg): ")

print(f"Your recorded height is {height} and your weight is {weight}.\n")

print("------------------------------------------")
print("      LAB WORK #1.2 COMPLETED SUCCESSFULLY!     ")
print("------------------------------------------")