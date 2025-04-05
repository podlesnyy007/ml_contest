s1 = input ()
d1={}
for c in s1:
    d1[c]=d1.get(c,0)+1

s2 = input ()
d2={}
for c in s2:
    d2[c]=d2.get(c,0)+1

f=True
for c in d2: #по ключам второго
    if d2[c]>d1.get(c,0):
            f=False
print(f)
