number = abs(int(input("Enter the size of the pattern: ")))
while number >= 1:
    for i in range(0, number):
        print("*" * number)
    break
