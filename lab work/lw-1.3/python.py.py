# ==========================================
# LAB WORK #1.3 - ALL SOLUTIONS IN ONE CODE
# ==========================================

print("------------------------------------------")
print("          STARTING LAB WORK #1.3          ")
print("------------------------------------------\n")

# --- Q.1: Type Casting Constructors (int, float, str, bool) ---
print("--- Q.1: Type Casting Constructors ---")
user_input = input("Enter a value as string (e.g., 10): ")

val_int = int(user_input)
val_float = float(user_input)
val_str = str(user_input)
val_bool = bool(user_input)

print(f"Integer Value: {val_int}, Type: {type(val_int)}")
print(f"Float Value: {val_float}, Type: {type(val_float)}")
print(f"String Value: {val_str}, Type: {type(val_str)}")
print(f"Boolean Value: {val_bool}, Type: {type(val_bool)}\n")


# --- Q.2: Floating-point to Integer Conversion ---
print("--- Q.2: Float to Integer Difference ---")
float_num = float(input("Enter a floating-point number (e.g., 15.75): "))
int_num = int(float_num)

print(f"Original Float Value: {float_num} (Type: {type(float_num)})")
print(f"Converted Integer Value: {int_num} (Type: {type(int_num)})")
print("Difference: Converting float to int removes the decimal part (truncates it).\n")


# --- Q.3: Boolean Conversion to Integer and String ---
print("--- Q.3: Boolean Conversion ---")
bool_input = input("Enter boolean value (True/False): ")

if bool_input.lower() == 'true':
    b_val = True
else:
    b_val = False

b_int = int(b_val)
b_str = str(b_val)

print(f"Boolean Value: {b_val}, Type: {type(b_val)}")
print(f"Converted to Integer: {b_int}, Type: {type(b_int)}")
print(f"Converted to String: {b_str}, Type: {type(b_str)}\n")


# --- Q.4: Variables of Each Datatype and type() ---
print("--- Q.4: Variables of Different Datatypes ---")
my_int = 50
my_float = 23.45
my_str = "Python"
my_bool = True

print(f"Value: {my_int}, Type: {type(my_int)}")
print(f"Value: {my_float}, Type: {type(my_float)}")
print(f"Value: {my_str}, Type: {type(my_str)}")
print(f"Value: {my_bool}, Type: {type(my_bool)}\n")


# --- Q.5: Area Calculations (Circle, Rectangle, Square) ---
print("--- Q.5: Area of Circle, Rectangle, and Square ---")

# 1. Area of Circle calculation
print(">> Circle Area Calculation:")
radius = float(input("Enter radius of the circle: "))
area_circle = 3.14159 * (radius ** 2)
print(f"Area of Circle = {area_circle}\n")

# 2. Area of Rectangle calculation
print(">> Rectangle Area Calculation:")
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area_rectangle = length * width
print(f"Area of Rectangle = {area_rectangle}\n")

# 3. Area of Square calculation
print(">> Square Area Calculation:")
side = float(input("Enter side length of the square: "))
area_square = side ** 2
print(f"Area of Square = {area_square}\n")

print("------------------------------------------")
print("      LAB WORK #1.3 COMPLETED SUCCESSFULLY!     ")
print("------------------------------------------")