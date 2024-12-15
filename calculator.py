# 1. Create a Python program that asks the user to enter two numbers.
# 2. Prompt the user to choose an operation: addition, subtraction, multiplication, or division.
# 3. Perform the chosen operation on the two numbers.
# 4. Display the result of the calculation.
# 5. Include basic error handling:
# - Print an error message if the user enters an invalid operation.
# - Prevent division by zero.
import os
import time


def quitCheck(x):
    if x.lower() == 'q':
        quit()

active = True

while active:
    result = 0
    os.system('cls')
    print('Welcome to Calculator!')
    print('Type Q at any point to quit.\n')

    # User number input
    n1 = input('Enter the first number: ')
    quitCheck(n1)
    try:
        n1 = float(n1)
    except ValueError:
        print('ERROR: Input requires exclusively a number.')
        time.sleep(3)
        continue
    n2 = input('Enter the second number: ')
    quitCheck(n2)
    try:
        n2 = float(n2)
    except ValueError:
        print('ERROR: Input requires exclusively a number.')
        time.sleep(3)
        continue

    # User operation input
    print('\nPlease choose the operation you would like to perform on the numbers:'
          '\n1. Addition'
          '\n2. Subtraction'
          '\n3. Multiplication'
          '\n4. Division')
    c = input('\nYour choice: ')
    quitCheck(c)
    try:
        c = int(c)
    except ValueError:
        print('ERROR: Selection does not exist.')
        time.sleep(3)
        continue

    # Begin match
    match c:

        # Addition
        case 1:
            try:
                result = n1 + n2
            except ValueError:
                print('ERROR: Unexpected ValueError.')
                time.sleep(3)
                continue
            print(f'\nResult: {result}')
            input('Press any key to continue or "Q" to exit.')
            continue

        # Subtraction
        case 2:
            try:
                result = n1 - n2
            except ValueError:
                print('ERROR: Unexpected ValueError.')
                time.sleep(3)
                continue
            print(f'\nResult: {result}')
            input('Press any key to continue or "Q" to exit.')
            continue

        # Multiplication
        case 3:
            try:
                result = n1 * n2
            except ValueError:
                print('ERROR: Unexpected ValueError.')
                time.sleep(3)
                continue
            print(f'\nResult: {result}')
            input('Press any key to continue or "Q" to exit.')
            continue

        # Division
        case 4:
            try:
                result = n1 / n2
            except ValueError:
                print('ERROR: Unexpected ValueError.')
                time.sleep(3)
                continue
            except ZeroDivisionError:
                print('ERROR: Cannot divide by zero.')
                time.sleep(3)
                continue
            print(f'\nResult: {result}')
            input('Press any key to continue or "Q" to exit.')
            continue

        # Wildcard
        case _:
            print('ERROR: Selection does not exist.')
            time.sleep(3)
            continue