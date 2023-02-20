# addition
def add(n1, n2):
    """Returns Addition"""
    return n1 + n2


# subtration
def sub(n1, n2):
    """Returns Subtraction"""
    return n1 - n2


# multiply
def mult(n1, n2):
    """Return Multiplication"""
    return n1 * n2


# divide

def div(n1, n2):
    """Returns Division"""
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}


def calculator():
    """Returns Calculation"""

    num1 = float(input("Enter your First number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation ")
        num2 = float(input("Enter your next number: "))
        calculation_fuction = operations[operation_symbol]
        answer = calculation_fuction(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with the {answer}, or type 'n' to start new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
