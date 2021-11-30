print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

def calculate():

    operation = int(input("Select an operation:"))
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = 0
    if operation == 1:
        result = round(float(num1), 2) + round(float(num2), 2)
        print("Your answer is " + str(result))

    elif operation == 2:
        result = round(float(num1), 2) - round(float(num2), 2)
        print("Your answer is " + str(result))

    elif operation == 3:
        result = round(float(num1), 2) * round(float(num2), 2)
        print("Your answer is " + str(result))

    elif operation == 4:
        result = round(float(num1), 2) / round(float(num2), 2)
        print("Your answer is " + str(result))

    else:
        print("You have selected an invalid operation!")

calculate()

again = input("Do you want to do another operation? (Y/N): ").upper()

while again == 'Y':
    if again == 'Y':
        calculate()
        again = input("Do you want to do another operation? (Y/N): ").upper()

    else:
        pass

print("Have a good day!")