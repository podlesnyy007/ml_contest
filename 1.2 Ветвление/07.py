a=int(input())
b=int(input())
c=int(input())
d=int(input())
# по теореме Пифагора
if (pow((c*c+b*b), 0.5)<=d) or (pow((a*a+b*b), 0.5)<=d) or (pow((a*a+c*c), 0.5)<=d):
    print('Yes')
else:
    print('No')

"""
pow — используется для возведения числа в степень
"""
