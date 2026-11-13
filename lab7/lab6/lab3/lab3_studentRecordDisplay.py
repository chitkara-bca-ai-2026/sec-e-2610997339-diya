# Print header banner
print("========================================")
print("        STUDENT RECORD DISPLAY")
print("========================================")

# Take inputs from user
name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))

# Print formatted student details using f-strings
print("----------------------------------------")
print("Student Details:")
print(f"  Name  : {name}")
print(f"  Age   : {age}")
print(f"  Marks : {marks}")
print("----------------------------------------")