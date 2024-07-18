def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"The result of the division is {float(result)}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    try:
        print(float(numerator))
        print(float(denominator))

    except ValueError:
        print("Error: Please enter numeric values only.")

