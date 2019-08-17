
# 变量作用域测试
# 如果函数内部未定义变量，python直接寻找局部变量，否则使用局部变量

def f1(a):
    print(a)
    print(b)

def f2(a):
    print(a)
    print(b)
    b=6

f2(3)