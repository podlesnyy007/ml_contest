n=int(input())
d = {}
for i in range(n):
    s=input().split(',')
    if (d.get (s[0]) != None):
        d[s[0]]+=int(s[1])
    else:
        d[s[0]]=int(s[1])
a=sorted(d.items(), key=lambda x: (-x[1], x[0]))
#-x[1]: значение берётся с минусом, чтобы сортировка происходила по убыванию.
#x[0]: ключ используется для дополнительной сортировки по алфавиту (по возрастанию).
for i in range(len(a)):
    print(a[i][0], f"{a[i][1]*0.95:.2f}", f"{a[i][1]*0.05:.2f}")
