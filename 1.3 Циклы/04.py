n=int(input())
count=0
max=0
s=0 #предыдущее число
for i in range(n):
    a=int(input())
    if (a==s):
        count+=1
        if (count>max):
            max=count
    else:
        count=0
    s=a
print(max+1)
