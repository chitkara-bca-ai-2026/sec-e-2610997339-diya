# Header
print("========================================")
print("        DATA CONVERSION UTILITY")
print("========================================")

# 1. Take inputs
product_name = input("Enter Product Name : ")
price = float(input("Enter Price        : "))
quantity = int(input("Enter Quantity     : "))

# 4. Calculate total price
total_price = price * quantity

# 5. Convert total amount to string
amount_str = str(total_price)

# 6. Display Type Casting Summary
print("\n----------------------------------------")
print("          TYPE CASTING SUMMARY")
print("----------------------------------------")
print(f"{'Variable':<15}{'Value':<12}{'Python Type'}")
print("----------------------------------------")
print(f"{'product_name':<15}{product_name:<12}{type(product_name)}")
print(f"{'price':<15}{price:<12}{type(price)}")
print(f"{'quantity':<15}{quantity:<12}{type(quantity)}")
print(f"{'total_price':<15}{total_price:<12}{type(total_price)}")
print(f"{'amount_str':<15}{amount_str:<12}{type(amount_str)}")
print("----------------------------------------")

# 7. Display Tax Invoice
print("\n----------------------------------------")
print("               TAX INVOICE")
print("----------------------------------------")
print(f"  Product Name : {product_name}")
print(f"  Price per Unit : Rs. {price:.2f}")
print(f"  Quantity     : {quantity}")
print("----------------------------------------")
print(f"  Invoice Total : Rs. {total_price}")
print("========================================")