# Save your file as: lab06_shop_billing.py

print("========================================")
print("     CLOTHING STORE BILLING SYSTEM      ")
print("========================================")

# 1. Accept inputs from the user
customer_name = input("Enter Customer Name: ")
garment_name = input("Enter Garment Name: ")
price_per_unit = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

# 2. Calculate the total cost
total_amount = price_per_unit * quantity

print("========================================")
print("                  BILL                  ")
print("========================================")

# 3. Display the details in a formatted output
print(f"Customer Name   : {customer_name}")
print(f"Garment Name    : {garment_name}")
print(f"Price per Unit  : Rs. {price_per_unit}")
print(f"Quantity        : {quantity}")
print(f"Total Amount    : Rs. {total_amount}")

print("========================================")