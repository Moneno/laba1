# функция логарифма
from math import log
# точное представление дробных чисел и их округление
from decimal import Decimal, ROUND_DOWN, ROUND_UP

# Проверка являются ли символы в строке числами


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

# Проверка является ли число дробным или целым


def toNumber(str):
    if ('.' in str):
        return float(str)
    else:
        return int(str)


operations = ['Сложение', 'Вычитание', 'Умножение', 'Деление', 'Возведение в степень', 'Логарифм',
              'Округление в большую сторону до N знака после запятой', 'Округление в меньшую сторону до N знака после запятой']

oper = input(f'Введите необходимую функцию ({", ".join(operations)}):\n')

while (not (oper in operations)):
    print('Введите доступную функцию из списка:')
    oper = input('')

a = input('Введите первый элемент:\n')
while (is_number(a) == False):
    a = input('Введенный элемент не является числом, введите первый элемент:\n')

b = input('Введите второй элемент:\n')
while (is_number(b) == False):
    b = input('Введенный элемент не является числом, введите второй элемент:\n')

a, b = toNumber(a), toNumber(b)


result = 'Результат программы: '

if (oper == operations[0]):
    result += str(a+b)
elif (oper == operations[1]):
    result += str(a-b)
elif (oper == operations[2]):
    result += str(a*b)
elif (oper == operations[3]):
    result += str(a/b)
elif (oper == operations[4]):
    result += str(a**b)
elif (oper == operations[5]):
    result += str(log(a, b))
elif (oper == operations[6]):
    # округление в большую сторону с большей точностью
    result += str(Decimal(a).quantize(Decimal(f'1.{"0"*b}'), ROUND_UP))
else:
    # округление в меньшую сторону с большей точностью
    result += str(Decimal(a).quantize(Decimal(f'1.{"0"*b}'), ROUND_DOWN))

print(result)
