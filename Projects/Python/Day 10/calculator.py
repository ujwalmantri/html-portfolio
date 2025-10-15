print(r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    while True:
        print("SIMPLE MENU-DRIVEN CALCULATOR")
        print("1. New Calculation")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == "2":
            print("Aya hi kyu bhai??")
            break
        elif choice == "1":
            first_number = float(input("What is the first number? "))

            while True:
                print("Available operations:")
                for symbol in operations:
                    print(*symbol)
                print()

                op_symbol = input("What is the operation? ")
                if op_symbol not in operations:
                    print("Invalid operation. Try again.")
                    continue

                second_number = float(input("What is the second number: "))
                operation_function = operations[op_symbol]
                result = operation_function(first_number, second_number)

                print(f"{first_number} {op_symbol} {second_number} = {result}")

                print("Next Step..")
                print("1. Continue with result")
                print("2. Start new calculation")
                print("3. Exit")
                next_choice = input("Enter your choice: ")

                if next_choice == "1":
                    first_number = result
                elif next_choice == "2":
                    break
                elif next_choice == "3":
                    print("Bye!")
                    return
                else:
                    print("Invalid Input!")
                    break
        else:
            print("Invalid Input!")

calculator()