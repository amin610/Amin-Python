num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

while True:
    op = input("Choose (+, -, *, /): ")
    if num1 < 5:
        print("exit")
        break
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        try:
            result = num1 / num2
            print(result)
        except ZeroDivisionError:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")
        if num1 < 5:
            print("Thank you")
            break