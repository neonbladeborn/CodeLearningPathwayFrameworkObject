text = input("What is the first number?")
num1 = int(text)

operation = input("What operation? '*' '/' '+' '-'")

text = input("What is the second number?")
num2 = int(text)

if operation == "*":
    result = num1 * num2

if operation == "/":
    result = num1 / num2

if operation == "+":
    result = num1 + num2

if operation == "-":
    result = num1 - num2

print(result)
