a = input()
a=a.upper()
V="AEIOU"
C="BCDFGHJKLMNPQRSTVWXZ"
s=''
for i in range(len(a)):
    if (a[i]=='Y' and i==0) or (a[i]=='Y' and s[i-1] == 'C') or a[i] in V:
        s+='V'
    else:
        s+='C'
print(s)
