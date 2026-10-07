# ==========================================
# LAB WORK #3.4 - ALL SOLUTIONS IN ONE CODE
# ==========================================


# Q.1
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

print("Q.1")

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print()


# Q.2
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

print("Q.2")

for i in range(5, 0, -1):
    for j in range(i, 6):
        print(j, end=" ")
    print()

print()


# Q.3
# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

print("Q.3")

for i in range(5, 0, -1):
    for j in range(6 - i):
        print(i, end=" ")
    print()

print()


# Q.4
# 1 0 1 0 1
# 0 1 0 1
# 1 0 1
# 0 1
# 1

print("Q.4")

for i in range(5, 0, -1):
    for j in range(i):
        print(j % 2, end=" ")
    print()

print()


# Q.5
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

print("Q.5")

for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print(j, end=" ")
    print()

print()


# Q.6
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

print("Q.6")

for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print(j, end=" ")
    print()


print("------------------------------------------")
print("       LAB WORK #3.4 COMPLETED")
print("------------------------------------------")