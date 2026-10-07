# ==========================================
# LAB WORK #4.1 - ALL SOLUTIONS IN ONE CODE
# ==========================================


# Q.1 - First Name and Last Name
print("--- Q.1 ---")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Hello, {last_name}, {first_name}!")

print()


# Q.2 - Using f-string
print("--- Q.2 ---")

item = "apple"
price = 5.50

print(f"The price of {item} is {price} dollars.")

print()


# Q.3 - Reverse String and Palindrome
print("--- Q.3 ---")

text = input("Enter a string: ")

reversed_text = text[::-1]

print("Reversed string:", reversed_text)

if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

print()


# Q.4 - Uppercase, Lowercase and Title Case
print("--- Q.4 ---")

text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())

print()


# Q.5 - Count total number of names using len()
print("--- Q.5 ---")

names = ["Bhavya", "Rahul", "Riya", "Amit", "Neha"]

print("Names:", names)
print("Total number of names:", len(names))


print()
print("==========================================")
print("       LAB WORK #4.1 COMPLETED")
print("==========================================")