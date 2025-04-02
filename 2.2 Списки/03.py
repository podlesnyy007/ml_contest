n, m, k=map(int, input().split())
a=list(map(int, input().split()))
summa = sum(x for x in a if abs(x) % 10 == k and abs(x) % m != 0)
print(summa)
