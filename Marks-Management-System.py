students = {}

def add_student(name, marks):
    students[name] = marks
    print(f"{name} added successfully")

def view_students():
    if not students:
        print("No records found")
    else:
        print("\nStudents Record: ")
        for name, marks in students.items():
            print(f"{name}: {marks}")

def  update_marks(name, new_marks):
    if name in students:
        students[marks] = new_marks
        print(f"{name}'s marks have been updated!")
    else:
        print("Student not found!")

def delete_students(name):
    if name in students:
        del students[name]
        print(f"{name} deleted successfully!")
    else:
        print("Student not found!")

#                              Main Menu
while True:
    print("\n---Students Marks Management System---")
    print("\n1. Add Student")
    print("\n2. View Students")
    print("\n3. Update Marks")
    print("\n4. Delete Student")
    print("\n5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter the student's name")
        marks = int(input("Enter Marks: "))
        add_student(name, marks)
    
    elif choice == "2":
        view_students()

    elif choice == "3":
        name = input("Enter the student's name")
        new_marks = int(input("Enter Marks: "))
        update_marks(name, new_marks)
    
    elif choice == "4":
        name = input("Enter the student's name")
        delete_students()
    
    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice. Tryu Again!")