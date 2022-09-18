while (True):
    i = int(input())
    prostoe = False
    fibonachi = False
    if (i == 1):
        prostoe = True
        fibonachi = True
    elif (i == 0):
        fibonachi = True
    k = 0
    for l in range(2, i//2+1):
        if (prostoe == True):
            break
        if (i % l == 0):
            k += 1
    if (k <= 0 and i != 0):
        prostoe = True
    else:
        prostoe = False
    f1 = f2 = 1
    k = i
    while k > 0:
        f1, f2 = f2, f1+f2
        k -= 1
        if (f2 == i):
            fibonachi = True
    print('Фибоначчи: ' + str(fibonachi) + ' Простое: ' + str(prostoe))
