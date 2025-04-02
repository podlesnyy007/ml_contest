x=input() #символ
s=input()
res=''
for symbol in s:
    if symbol==x:
        res+=2*symbol
    else:
        res += symbol
print(res)
