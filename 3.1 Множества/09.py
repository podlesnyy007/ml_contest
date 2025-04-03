n = int(input())
str1 = input().split() #строка с числами
l = []
for i in range(n):
    if len(str1[i]) != len(set(str1[i])): #различны
        l.append(str1[i])
print(' '.join(str(i) for i in l))
