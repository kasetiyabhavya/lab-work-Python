# ==========================================
# LAB WORK #3.1 - ALL SOLUTIONS IN ONE CODE
# ==========================================

print("------------------------------------------")
print("          STARTING LAB WORK #3.1          ")
print("------------------------------------------\n")

# --- Q.1: Minimum number from three numbers using nested statement ---
print("--- Q.1: Minimum of Three Numbers ---")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

if n1 <= n2:
    if n1 <= n3:
        print(f"Minimum number is: {n1}\n")
    else:
        print(f"Minimum number is: {n3}\n")
else:
    if n2 <= n3:
        print(f"Minimum number is: {n2}\n")
    else:
        print(f"Minimum number is: {n3}\n")


# --- Q.2: Maximum number from four numbers using nested statement ---
print("--- Q.2: Maximum of Four Numbers ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))

if a >= b:
    if a >= c:
        if a >= d:
            print(f"Maximum number is: {a}\n")
        else:
            print(f"Maximum number is: {d}\n")
    else:
        if c >= d:
            print(f"Maximum number is: {c}\n")
        else:
            print(f"Maximum number is: {d}\n")
else:
    if b >= c:
        if b >= d:
            print(f"Maximum number is: {b}\n")
        else:
            print(f"Maximum number is: {d}\n")
    else:
        if c >= d:
            print(f"Maximum number is: {c}\n")
        else:
            print(f"Maximum number is: {d}\n")


# --- Q.3: Positive or Non-Positive in a single line (Shorthand if-else) ---
print("--- Q.3: Positive / Non-Positive (Single Line) ---")
num_q3 = float(input("Enter a number: "))
print("Positive" if num_q3 > 0 else "Non-Positive")
print()


# --- Q.4: Pass or Fail using shorthand if-else (marks >= 40) ---
print("--- Q.4: Pass or Fail (Shorthand If-Else) ---")
marks = float(input("Enter student marks: "))
print("Pass" if marks >= 40 else "Fail")
print()


# --- Q.5: Even or Odd using shorthand if-else ---
print("--- Q.5: Even or Odd (Shorthand If-Else) ---")
num_q5 = int(input("Enter an integer: "))
print("Even" if num_q5 % 2 == 0 else "Odd")
print()

print("------------------------------------------")
print("      LAB WORK #3.1 COMPLETED SUCCESSFULLY!     ")
print("------------------------------------------")