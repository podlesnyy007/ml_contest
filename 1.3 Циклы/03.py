s=0
b=0
n=int(input())
for i in range(n):
    a=int(input())
    if (abs(a)>=s):
        s=abs(a)
        b=i+1
print(b)
