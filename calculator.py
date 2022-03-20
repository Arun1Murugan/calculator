def addition(num1, num2):
    #plus
    return num1 + num2
def subtraction(num1, num2):
    #minus
    return num1 - num2
def multiplicatin(num1, num2):
    #multiply
    return num1 * num2
def division(num1, num2):
    #divide
    return num1 / num2
operations = {"+" : addition,
           "-" : subtraction ,
           "*" : multiplicatin,
           "/" : division}

def calculator():
    print("PyCalCulaTor")
    number1 = float(input("What is the first number : "))
    for symbols in operations:
        print(symbols)
    should_continue = True
    while should_continue:
        operation_symbol = input("pick up an operations : ")
        number2 = float(input("what is the next number : "))
        calculation = operations[operation_symbol]
        answer = calculation(number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")
        if input(f"Type 'c' to continue with calculating with last answer({answer}) or type 'n' to start new calculation : ") == "c":
            number1 = answer
        else:
            should_continue = False
            calculator()
calculator()
