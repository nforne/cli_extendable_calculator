from operators import *
from art import logo
from replit import clear


def calculator():
    print(logo)
    memory = []
    num1 = float(input('What is the first number? '))

    while True:
        # for symbol in operations:
        #     print(f"{symbol}")
        # print('operators:  "+" , "-" , "*" or "/"')
        print(f'operators: {[str(i) for i in operations]}')
        operation_symbol = input("Pick an operator from the line above: ")
        num2 = float(input('What is the second number? '))
        result = operations[operation_symbol](num1, num2)
        memory.append(result)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        print('=>/ ~~ ------------------------------------------------------------------- ~~ /')
        if input(f'Would you like to continue calculating with {result}? Y/N ').upper() == 'Y':
            num1 = result
        else:
            break
    print('=>/ ~~ ------------------------------------------------------------------- ~~ /')
    clear()
    calculator()


calculator()
