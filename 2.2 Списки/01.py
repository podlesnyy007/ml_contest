n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
k=int(input())
for i in range(len(a)):
    a[i]*=k
print(*a)
