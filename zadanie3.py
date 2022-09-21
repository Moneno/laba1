while (True):
    i = int(input('Введите число:\n'))
    fibonachi = False
    if (i == 1):
        fibonachi = True
    elif (i == 0):
        fibonachi = True
    f1 = f2 = 1
    k = i
    while k > 0:
        f1, f2 = f2, f1+f2
        k -= 1
        if (f2 == i):
            fibonachi = True
    print('Фибоначчи: ' + str(fibonachi))
