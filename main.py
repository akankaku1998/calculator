from replit import clear
def add(n1, n2):
  return n1+n2

def substract(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2

operation = {
  '+' : add,
  '-' : substract,
  '*' : multiply,
  '/' : divide
}
def calculator():
  from art import logo
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operation:
    print(symbol)
  choice = True

  while choice:
    operator = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    result = operation[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {result}")
    
    should_continue = input(f"Type 'y' to continue calculating with 14.0, or type 'n' to start a new calculation: ")
    if should_continue == "n":
      choice = False
      clear()
      calculator()
    else:
      num1 = result

calculator()