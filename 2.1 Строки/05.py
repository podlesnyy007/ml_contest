s=input()
if len(s)%2==0:
    print(s[:len(s)//2-1] + s[len(s)//2+1:])
else:
    mid=len(s)//2+1
    print(s[:mid-1] + s[mid:])
