# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.


def calculate (number1, number2, operation):
    match operation:
        case '+':
            return number1+number2
        case '-':
            return number1-number2
        case '/': 
            if number2 == 0:
                return "Can't be divided by 0"
            else:
                return (number1 / number2)
        case 'div':
            if number2 == 0:
                return "Can't be divided by 0"
            else:
                return number1 // number2
        case '*':
                return number1 * number2
        case 'mod':
            return number1 % number2
        case  'pow':
            return number1 ** number2
                
try:
    number1 = float(input('Enter first number: '))
    number2 = float(input('Enter second number: '))
    operation = str(input('Enter operation: '))
    print(calculate (number1, number2, operation))

except:
    print('Enter condition correctly')



## Version 2: if/elif/ele 

# def calculate ():
#     num1 = float(input('Введите первое число: '))
#     num2 = float(input('Введите второе число: '))
#     operation = str(input('Введите операцию: '))

#     if operation == '+':
#         print(num1+num2)
#     elif operation == '-':
#         print(num1 - num2)
#     elif operation == '/':
#         if num2 == 0:
#             print('Делить на "0" нельзя')
#         else:
#             print(num1 / num2)
#     elif operation == '*':
#         print(num1 * num2)
#     elif operation == 'mod':
#         print(num1 % num2)
#     elif operation == 'pow':
#         print(num1 ** num2)
#     elif operation == 'div':
#         print(num1 // num2)
#     else:
#         print('Вводите верно')
# calculate()