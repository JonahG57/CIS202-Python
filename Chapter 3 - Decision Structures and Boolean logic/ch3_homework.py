num1 = int(input('Number 1: '))
op = input('Operator +, -, *, /: ')
num2 = int(input('Number 2: '))

if op == '+':
    ans = num1 + num2
    print(f'{num1} + {num2} = {ans}')
elif op == '-':
    ans = num1 - num2
    print(f'{num1} - {num2} = {ans}')
elif op == '*':
    ans = num1 * num2
    print(f'{num1} * {num2} = {ans}')
elif op == '/':
    if num1 == 0 or num2 == 0:
        print('You can not divide by 0')
    elif num1 != 0 or num2 != 0:
        ans = num1 / num2
        print(f'{num1} / {num2} = {ans}')
