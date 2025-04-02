x1, x2, x3 = map(int, input().split())
if abs(x2-x1)<abs(x3-x1) :
    print(abs(x2-x1)+abs(x3-x2))
else:
    print(abs(x3-x1)+abs(x3-x2))
