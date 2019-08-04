# -*- coding: utf-8 -*-
def error(a):
    if not isinstance(a,(str,int)):
        raise TypeError('bad operand type')
    if a >= 0:
        return a
    else:
        return (-a)
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def quadratic(a, b, c):
    #a*x^2+b*x+c=0
    if b^2-4*a*c > 0:
        x1 = (-b+math.sqrt(b^2-4*a*c))/2*a
        x2 = (-b - math.sqrt(b ^ 2 - 4 * a * c)) / 2 * a
        return x1,x2
    if b^2-4*a*c == 0:
        x = (-b+math.sqrt(b^2-4*a*c))/2*a
        return x
    if b^2-4*a*c < 0:
        print("no solution")

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def f2(a,b,c=0,*args,**kw):#传入参数
    print(a,b,c,args,kw)

def fact1(n):#阶乘fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
    if n == 1:
        return 1
    return n*fact1(n-1)#递归函数
# def fact1(n):
#     if n == 1:
#         s = 1
#     if n > 1:
#         s= n*fact1(n-1)
#     return s
def fact2(n):#尾递归优化
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    return  fact_iter(num-1,num*product)
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)



if __name__=='__main__':
    hanoi(3, 'A', 'B', 'C')
    # print(quadratic(1,2,1))

    # x,y = move(10,10,1,math.pi/2)
    # r= move(10, 10, 1, math.pi / 2)
    # print(x,y,r)

    # try:
    #     a = input('message:')
    #     error(a)
    # except TypeError:
    #     print(str(a))


