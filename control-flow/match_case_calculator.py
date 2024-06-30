num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
result = None
error_message = None
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            error_message = "Error: Division by zero is not allowed."
        else:
            result = num1 / num2
    case _:
        error_message = "Invalid operation. Please select +, -, * or /."
if error_message:
    print(error_message)
else:
    print(f"The result is {result}")
