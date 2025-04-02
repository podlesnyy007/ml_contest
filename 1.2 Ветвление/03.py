n=int(input())
if (n%3==0) and (n%10==3):
    print(0)
elif (n%3==0) or (n%10==3):
    print(1)
else:
    print(0)
