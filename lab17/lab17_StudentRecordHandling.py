students = {
    "101": {"Name": "Aman", "Marks": [85, 90, 80]},
    "102": {"Name": "Rohan", "Marks": [70, 65, 75]},
    "103": {"Name": "Diya", "Marks": [92, 88, 95]},
}

def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, student):
    total, average = calculate_results(student["Marks"])
    print(f"Roll: {roll} | Name: {student['Name']} | Marks: {student['Marks']} | Total: {total} | Average: {average:.2f}")

def add_student(records, roll, name, marks):
    if roll in records:
        print("Error: Roll number already exists.")
    else:
        records[roll] = {"Name": name, "Marks": marks}
        print("Student added successfully.")

while True:
    print("\n1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        for roll, student in students.items():
            display_student(roll, student)

    elif choice == "2":
        roll = input("Enter Roll Number: ").strip()
        name = input("Enter Name: ").strip()
        marks = []
        for i in range(1, 4):
            marks.append(int(input(f"Enter marks for subject {i}: ")))
        add_student(students, roll, name, marks)

    elif choice == "3":
        roll = input("Enter Roll Number to search: ").strip()
        student = students.get(roll)
        if student:
            display_student(roll, student)
        else:
            print("Student not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
