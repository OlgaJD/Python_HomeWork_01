# задача 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ - отрицание (not)
# ⋁ - дизъюнкция (or)
# ⋀ - конъюнкция (and)
# not (x or y or z) = no(x) and no(y) and no(z)
# функция принимает истинное значение при:
# X	Y Z	Результат
# 0	0 0	1
# 0	0 1	1
# 0	1 0	1
# 0	1 1	1
# 1	0 0	1
# 1	0 1	1
# 1	1 0	1
# 1	1 1	1


def proof_expression():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                first_statement = not (x or y or z)
                second_statement = not (x) and not (y) and not(z)
                print(f'Для предикат, принимающих значения: {x}, {y}, {z}', end = ' - ')
                if first_statement == second_statement:
                    print('утверждение верно')
                else:
                    print('утверждение неверно')

proof_expression()