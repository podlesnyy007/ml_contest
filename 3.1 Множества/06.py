n, m = map(int, input().split())
#tuple - каждая строка преобразуется в кортеж (x, y)
a= set(tuple(map(int, input().split())) for i in range(n))
b= set(tuple(map(int, input().split())) for j in range(m))
s1= sorted(a & b)
s2 = sorted(a - b)

if len(s1) == 0:
    print("empty")
else:
    print(*s1)

if len(s2) == 0:
    print("empty")
else:
    print(*s2)
