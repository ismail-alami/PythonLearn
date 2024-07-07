def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:

                print("Division by 0 is not possible.")
                
            elif num2 !=0:
                return num1 / num2
            else:
                print("phew")
        case _:
            print("Please choose 1 of the 4 operations.")

