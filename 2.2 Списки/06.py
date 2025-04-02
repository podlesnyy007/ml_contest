n, m=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=a+b
c.sort()
# используется оператор распаковки (*) для вывода элементов массива c через пробел
print(*c)
