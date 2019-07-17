def func1():
    num = 3
    print(num)

def func2():
    global num
    double_num = num * 2
    num = 6
    print(double_num)



func1()

func2()


##func1() prints out 3, func2() prints out 10, and the value of num in the global scope is 6.