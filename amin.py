#
# price = int(input("the order: "))
# if price>=100:
#   print("high price")
#
# else:
#   print("regular price")
# #
# # class Playerchracter:
# #     def __init__(self):
# #         pass
#
# # try:
# #     price = int(input("how old are you: "))
# #     divisor = 10 / 0
# #     print(divisor)
# # except ZeroDivisionError:
#     print("You cannot divide by zero")
try:
    number1 = float(input("Enter number "))
    number2 = float(input("Enter number "))
    result = number1 / number2
    print(f" {result}")
except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

