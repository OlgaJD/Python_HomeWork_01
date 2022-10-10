# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# -


def day_of_the_week ():
    try:
        day = int(input("Enter number representing the day of the week: "))
        if day == 6 or day ==7:
            print('Yes, it is a holiday')
        elif 0 < day < 6:
         print('No. it is a work day')
        else:
         print('Enter only integers from 1 to 7')
    except:
        print("Don't use letters or symbols")

day_of_the_week ()