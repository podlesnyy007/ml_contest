n=int(input())
while n>9:
    summa=sum(int(number) for number in str(n))
    n=summa
print(n)
