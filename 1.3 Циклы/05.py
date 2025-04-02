a, b = map(int, input().split())
a1=a
i=1
while (a1<b):
    a1*=3 # сколько листьев распустилось в n-ый день
    i+=1
print(i, end=' ') # /n
a2=a
i=1
while (a2<1000000):
    a2+=a*3**(i) # сколько листьев распустилось суммарно
    i+=1
print(i)
