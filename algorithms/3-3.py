# 栈帧调用demo

def func1(param1):
    func2(param1)
    func3(param1)

def func2(param2):
    print param2

def func3(param3):
    print param3


func1(647)


# 阶乘算法

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print factorial(3)