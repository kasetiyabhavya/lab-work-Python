# ==========================================
# LAB WORK #3.3 - ALL SOLUTIONS IN ONE CODE
# ==========================================

print("------------------------------------------")
print("          STARTING LAB WORK #3.3")
print("------------------------------------------\n")


# Q.1 - Right Half Pyramid (Reverse Numbers)
print("--- Q.1 ---")

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()zy;lguiolguityvgikkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkbuh

print()


# Q.2 - Right Half Pyramid (Increasing Numbers)
print("--- Q.2 ---")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()


# Q.3 - Right Half Pyramid (Repeated 
print("--- Q.3 ---")

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

print()


# Q.4 - Inverted Right Half Pyramid
print("--- Q.4 ---")

for i in range(1, 6):
    for j in range(i, 6):
        print(j, end=" ")
    print()

print()


# Q.5 - Inverted Right Half Pyramid (Repeated Numbers)
print("--- Q.5 ---")

for i in range(1, 6):
    for j in range(i, 6):
        print(i, end=" ")
    print()

print()


# Q.6 - Inverted Right Half Pyramid (1 and 0 Pattern)
print("--- Q.6 ---")

for i in range(5, 0, -1):
    for j in range(i):
        print((j % 2), end=" ")
    print()

print()


# Q.7 - Right Half Pyramid using Alphabets
print("--- Q.7 ---")

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(chr(64 + j), end=" ")
    print()

print()


# Q.8 - Floyd's Triangle
print("--- Q.8 ---")

num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print("------------------------------------------")
print("       LAB WORK #3.3 COMPLETED")
print("------------------------------------------")