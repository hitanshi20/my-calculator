# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:   # To avoid division by zero error
        return "Error! Division by zero is not allowed."
    return a / b

# Display calculator menu
print("===== Simple Calculator =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user choice
choice = int(input("Enter choice (1/2/3/4): "))

# Take numbers as input
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

# Perform operation based on user choice
if choice == 1:
    print("Result:", add(x, y))
elif choice == 2:
    print("Result:", subtract(x, y))
elif choice == 3:
    print("Result:", multiply(x, y))
elif choice == 4:
    print("Result:", divide(x, y))
else:
    print("Invalid choice! Please enter 1, 2, 3, or 4.")
