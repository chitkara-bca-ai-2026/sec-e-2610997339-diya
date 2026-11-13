import sys

# Header
print("========================================")
print("     CALENDAR VERIFICATION SYSTEM")
print("========================================")

# 1. Take input
year = int(input("Enter year: "))

# 2. Validate input
if year <= 0:
    print("Error: Year must be a positive integer greater than 0.")
    sys.exit()

# 3. Check leap year rules using if-else and determine exact reason
if year % 100 == 0:
    if year % 400 == 0:
        is_leap = True
        reason = "Century year divisible by 400"
    else:
        is_leap = False
        reason = "Century year not divisible by 400"
else:
    if year % 4 == 0:
        is_leap = True
        reason = "Divisible by 4 and not a century year"
    else:
        is_leap = False
        reason = "Not divisible by 4"

# 4. Determine calendar details based on leap year status
if is_leap:
    status = "LEAP YEAR"
    days_in_year = 366
    feb_days = 29
else:
    status = "COMMON YEAR"
    days_in_year = 365
    feb_days = 28

# 5. Display the results
print("----------------------------------------")
print(f"Year: {year}")
print(f"Status: {status}")
print(f"Days in Year: {days_in_year} days")
print(f"Days in February: {feb_days} days")
print(f"Reason: {reason}")