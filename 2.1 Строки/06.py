s=input()
summa=0
for symbol in s:
    if symbol.isdigit(): # состоит ли строка только из цифр
        summa+=int(symbol)
print(summa)
