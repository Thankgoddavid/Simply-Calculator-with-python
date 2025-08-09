#calculator application
first_number = int(input('Enter First number: '))
second_number = int(input('Enter Second Number: '))
operation = input('Enter an operation e.g +,-,*,/: ')
#functions
if operation == '+':
    answer = first_number + second_number
    print(answer)
elif operation == '-':
    answer = first_number - second_number
    print(answer)
elif operation == '*':
    answer = first_number * second_number
    print(answer)
elif operation == '/':
    if second_number ==0:
        print('ERROR: Division by Zero not allowed')
    else:
        answer = first_number / second_number
        print(answer)
else:
    print('Invalid operation')