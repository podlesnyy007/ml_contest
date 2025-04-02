i=20
s=1
while i <=20:
    a = float(input())
    if (a>=0):
        s*=a
    else:
        break
print("\n""{:.6f}".format(s))
