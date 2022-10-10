# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

def calculate ():
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    operation = str(input('Введите операцию: '))

    if operation == '+':
        print(num1+num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '/':
        if num2 == 0:
            print('Делить на "0" нельзя')
        else:
            print(num1 / num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == 'mod':
        print(num1 % num2)
    elif operation == 'pow':
        print(num1 ** num2)
    elif operation == 'div':
        print(num1 // num2)
    else:
        print('Вводите верно')
calculate()