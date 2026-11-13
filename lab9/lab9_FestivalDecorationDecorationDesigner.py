# 1. Take input from the user
n = int(input("Enter the number of rows: "))

# Pattern 1: Star Triangle (Right-Angled)
print("Pattern 1: Star Triangle")
print("----------------------------------------")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("* ", end="")
    print()

print()

# Pattern 2: Number Triangle
print("Pattern 2: Number Triangle")
print("----------------------------------------")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(f"{j} ", end="")
    print()

print()

# Pattern 3: Inverted Star Triangle
print("Pattern 3: Inverted Star Triangle")
print("----------------------------------------")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("* ", end="")
    print()

print()

# Pattern 4: Pyramid (Centered Triangle)
print("Pattern 4: Pyramid")
print("----------------------------------------")
for i in range(1, n + 1):
    # Print spaces for centering
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(i):
        print("* ", end="")
    print()