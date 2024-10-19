# Print numbers from 1 to 100 using a for Loop
for i in range(1, 101):
    print(i)

# Take two inputs from the user and return addition, subtraction, and multiplication
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print(f"The addition of {num1} and {num2} is: {addition}")
print(f"The subtraction of {num1} amd {num2} is: {subtraction}")
print(f"The multiplication of {num1} and {num2} is: {multiplication}")