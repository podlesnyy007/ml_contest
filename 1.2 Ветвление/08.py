k=int(input())
if (1<k<5) or ((k%10==2) and  (k%100!=12)) or ((k%10==3) and  (k%100!=13))\
        or ((k%10==4) and  (k%100!=14)):
    print("Мне", k, "года")
elif (k%10==1) and (k%100!=11):
    print("Мне", k, "год")
else:
    print("Мне", k, "лет")
