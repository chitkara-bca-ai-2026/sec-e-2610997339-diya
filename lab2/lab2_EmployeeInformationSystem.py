# Lab 02 - Employee Information System

# 1. Take input and check data type for Employee Name
name = input("Enter Employee Name: ")
print("  Data type:", type(name))

# 2. Take input, convert to integer, and check data type for Employee ID
emp_id = int(input("Enter Employee ID: "))
print("  Data type:", type(emp_id))

# 3. Take input, convert to float, and check data type for Salary
salary = float(input("Enter Salary: "))
print("  Data type:", type(salary))

# 4. Take input and check data type for Department
department = input("Enter Department: ")
print("  Data type:", type(department))

# 5. Take input, convert 'yes'/'no' to boolean, and check data type for Active status
active_input = input("Is the employee active? (yes/no): ")
is_active = active_input.strip().lower() == "yes"
print("  Data type:", type(is_active))

# Display formatted details
print("\n--- Employee Details ---")
print(f"Name       : {name}")
print(f"ID         : {emp_id}")
print(f"Salary     : {salary}")
print(f"Department : {department}")
print(f"Active     : {is_active}")