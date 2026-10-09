
# ==========================================
# LAB WORK #5.3 - ALL SOLUTIONS IN ONE CODE
# ==========================================

# Initial list of students
students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78}
]


# Q.1 - Display all students' names and marks
print("\n--- Q.1: STUDENT DETAILS ---")

for student in students:
    print("Name:", student["name"], "| Marks:", student["marks"])


# Q.2 - Add a new student
print("\n--- Q.2: ADD NEW STUDENT ---")

student_id = int(input("Enter student ID: "))
name = input("Enter student name: ")
marks = float(input("Enter student marks: "))

new_student = {
    "id": student_id,
    "name": name,
    "marks": marks
}

students.append(new_student)

print("Student added successfully!")


# Q.3 - Search student by ID
print("\n--- Q.3: SEARCH STUDENT ---")

search_id = int(input("Enter student ID to search: "))

found = False

for student in students:
    if student["id"] == search_id:
        print("Student details:", student)
        found = True
        break

if not found:
    print("Student not found.")


# Q.4 - Update student marks
print("\n--- Q.4: UPDATE MARKS ---")

update_id = int(input("Enter student ID to update marks: "))

found = False

for student in students:
    if student["id"] == update_id:
        new_marks = float(input("Enter new marks: "))
        student["marks"] = new_marks
        print("Marks updated successfully!")
        found = True
        break

if not found:
    print("Student not found.")

print("Updated students list:", students)


# Q.5 - Remove a student by ID
print("\n--- Q.5: REMOVE STUDENT ---")

remove_id = int(input("Enter student ID to remove: "))

found = False

for student in students:
    if student["id"] == remove_id:
        students.remove(student)
        print("Student removed successfully!")
        found = True
        break

if not found:
    print("Student not found.")

print("Updated students list:", students)


# Q.6 - Sort students by marks in descending order
print("\n--- Q.6: SORT BY MARKS ---")

students.sort(key=lambda student: student["marks"], reverse=True)

for student in students:
    print(student)


# Q.7 - Display students scoring more than 80
print("\n--- Q.7: STUDENTS ABOVE 80 MARKS ---")

found = False

for student in students:
    if student["marks"] > 80:
        print(
            "ID:", student["id"],
            "| Name:", student["name"],
            "| Marks:", student["marks"]
        )
        found = True

if not found:
    print("No students scored more than 80 marks.")


# Final output
print("\n==========================================")
print("      LAB WORK #5.3 COMPLETED")
print("==========================================")