# from art import logo

# def calculate(num1, num2, operator):
#     if operator == "+":
#         result = num1 + num2
    
#     elif operator == "-":
#         result = num1 - num2
    
#     elif operator == "*":
#         result = num1 * num2
      
#     elif operator == "/":
#         result = num1 / num2

#     print(f"{num1} {operator} {num2} = {result}")
#     more_calculations = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation, or 'exit' to quit:  ").lower()
    
#     if more_calculations == "y":
#       continue_calculating = True
#       num1 = result
#       operator = input("Pick an operation:  ")
#       num2 = int(input("What's the next number?:  "))
#       calculate(num1, num2, operator)
#     if more_calculations == "n":
#       continue_calculating = False
#       num1 = int(input("What's the first number?:  "))
#       print("+")
#       print("-")
#       print("*")
#       print("/")
#       operator = input("Pick an operation:  ")
#       num2 = int(input("What's the next number?:  "))
#       calculate(num1, num2, operator)
#     if more_calculations == "exit":
#       print("Thank you for calculating. Goodbye")
      
      

# print(logo)
# num1 = int(input("What's the first number?:  "))
# print("+")
# print("-")
# print("*")
# print("/")
# operator = input("Pick an operation:  ")
# num2 = int(input("What's the next number?:  "))
# result = 0
# continue_calculating = False

# calculate(num1, num2, operator)
# # print(f"{num1} {operator} {num2} = {result}")


#Lesson follow along


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


num1 = int(input("Whats the first number?: "))

for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation from above: ")

num2 = int(input("Whats the second number?: "))

calculation_function = operations[operation_symbol]

answer1 = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer1}")

operation_symbol = input("pick another operation: ")

num3 = int(input("Pick another number: "))

calculation_function = operations[operation_symbol]

answer2 = calculation_function(answer1, num3)

print(f"{answer1} {operation_symbol} {num3} = {answer2}")
