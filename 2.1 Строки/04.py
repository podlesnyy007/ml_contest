s=input()
if len(s)%2==0 and s[:len(s)//2]==s[len(s)//2::-1]: # равна ли первая половина строки второй половине строки
# срез строки от начала до середины строки = срез строки от середины до начала строки, но в обратном порядке
        print(1)
elif s==s[::-1]: #палиндром
        print(1)
else:
    print(0)
