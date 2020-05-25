def func1 (a,b):
    return a*b

def func2 ():
    print ("Введите число 1:")
    a = int(input())
    print ("Введите число 2:")
    b = int(input())
    print ("Результат: " +str(func1(a,b)))

func2()