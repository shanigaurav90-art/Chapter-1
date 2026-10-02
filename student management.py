import json
import os

FILE_NAME = "students.json"

# Load Data 
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save Data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

students = load_data()

# Add Student
def add_student():
    roll = input("Enter Roll No: ")

    for student in students:
        if student["Roll"] == roll:
            print("Student already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    mobile = input("Enter Mobile: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course,
        "Mobile": mobile
    }

    students.append(student)
    save_data(students)
    print("Student Added Successfully!")

# View Students
def view_students():
    if len(students) == 0:
        print("No Student Found!")
        return

    print("\n========== Student List ==========")

    for student in students:
        print("----------------------------")
        print("Roll   :", student["Roll"])
        print("Name   :", student["Name"])
        print("Age    :", student["Age"])
        print("Course :", student["Course"])
        print("Mobile :", student["Mobile"])
# Search Student
def search_student():
    roll = input("Enter Roll No. & Name to Search: ")

    for student in students:
        if student["Roll"] == roll:
            print("\nStudent Found")
            for key, value in student.items():
                print(f"{key}: {value}")
            return

    print("Student Not Found!")
# Search Student by Name
def search_student():
        name = input("Enter Name to Search: ")
        for student in students:
            if student["Name"] == name:
                print("\nStudent Found")
                for key, value in student.items():
                    print(f"{key}: {value}")
                return
    
        print("Student Not Found!")

# Update Student
def update_student():
    roll = input("Enter Roll No to Update: ")

    for student in students:
        if student["Roll"] == roll:
            student["Name"] = input("New Name: ")
            student["Age"] = input("New Age: ")
            student["Course"] = input("New Course: ")
            student["Mobile"] = input("New Mobile: ")

            save_data(students)
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")

# Delete Student
def delete_student():
    roll = input("Enter Roll No to Delete: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            save_data(students)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

# Menu
while True:
    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")