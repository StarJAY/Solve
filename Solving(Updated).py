# coding: utf-8
from math import sqrt
#导入数学模块
def solve():
    #申明函数名称
    print '='*10,'Solve','='*10
    print 'ax^2+bx+c=0'
    print '-'*10,'Enter a,b,c','-'*10
    a=float(raw_input('a='))
    b=float(raw_input('b='))
    c=float(raw_input('c='))
    #获取a,b,c的值
    print '-'*10,'Solution','-'*10
    if (a==0) and (b==0):
        print '0=',c
        print 'Erro'
    if (a==0) and (b!=0) and (c!=0):
        print '(',b,')+(',c,')x=0'
        print 'X=',-c/b
    if (a==0) and (b!=0) and (c==0):
        print '(',b,')x=0'
        print 'X=0'
    #求解非二次方程
    if (a!=0):
        #求解二次方程
        print '(',a,')x^2+(',b,')x+(',c,')=0'
        delta=(b*b)-4*a*c
        if delta<0:
            print 'No answer💢'
        if delta==0:
            print 'X=',(-b)/(2*a)
        if delta>0:
            print 'X1=',(-b+sqrt(delta))/(2*a)
            print 'X2=',(-b-sqrt(delta))/(2*a)
    print '-'*10,'Over','-'*10
    print ' '
    print ' '
    return 
    #求根函数

solve()
#调用求根函数
def reset():
    string=raw_input('Press reset to reset:')
    if string=='reset' or string=='Reset':
        print ''
        print ''
        print ''
        print ''
        print ''
        solve()
        #判断
    else:
        print 'Erro'
        reset()
    #重启函数

while (True):
    #无穷无尽的循环
    reset()
    #调用重启函数
        

    
        
    
        
    

        
    
    