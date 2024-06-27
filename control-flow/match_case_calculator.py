# Prompt user for input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
  case '+':
    add = num1 + num2
    print(f"The result is {add}.")
  case '-':
    sub = num1 - num2
    print(f"The result is {sub}.")
  case '*':
    mult = num1 * num2
    print(f"The result is {mult}.")
  case '/':
    if num2 == 0:
      print("Please input a number greater than 0 for the second number.")
    else:
      div = num1 / num2
      print(f"The result is {int(div)}.")
  case _:
      print("Invalid operation. Please choose one of the following: +, -, *, /.")
