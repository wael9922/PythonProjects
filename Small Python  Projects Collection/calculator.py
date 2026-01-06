def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    first_number = float(input("What is the first number: "))

    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)

        operation = input("Pick an operation: ")
        next_number = float(input("What is the next number: "))

        calculation_function = operations[operation]
        answer = calculation_function(first_number, next_number)

        print(f"{first_number} {operation} {next_number} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, "
            f"or type 'n' to start a new calculation: "
        )

        if choice == 'y':
            first_number = answer
        else:
            should_continue = False
            calculator()   # restart


calculator()
