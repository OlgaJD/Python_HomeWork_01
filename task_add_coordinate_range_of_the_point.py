# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def coordinate_range():
    try:
        x = int(input('Введите номер четверти (целое число от 1 до 4): '))
        if x == 1:
            print('Значение точки по коодинате x > 0, значение по коодинате y > 0')
        elif x == 2:
            print('Значение точки по коодинате x < 0, значение по коодинате y > 0')
        elif x == 3:
            print('Значение точки по коодинате x < 0, значение по коодинате y < 0')
        elif x == 4:
            print('Значение точки по коодинате x > 0, значение по коодинате y < 0')
        else:
            print('Вводите только числа от 1 до 4')
    except: print('Вводите только целые числа, не используйте буквы и символы')
    
coordinate_range()