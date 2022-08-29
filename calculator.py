def welcome():
    print("Welcome To Calculator")

def calculate():
    operation = input("""
    Please type in math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    """)

    number_1 = int(input('Please enter the first number:'))
    number_2 = int(input('Please enter the second number:'))

    if operation == '+':
        print('{} + {} ='.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{}-{}='.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{}*{}='.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{}/{}='.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You Have Not Typed A Valid Operator, Please Run The Program Again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input("""
Do You Want To Calculate Again?
PLease Type Y for YES or N for NO.
""")

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print("See You Later.")
    else:
        again()

welcome()
calculate()
