def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"Result is : {float(result)}")
    except ZeroDivisionError:
        print("You can't divide by 0!")

    try:
        print(float(numerator))
        print(float(denominator))

    except ValueError:
        print("It's a non numeric value")

