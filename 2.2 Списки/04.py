s=input()
s1=''.join(i.upper() for i in s if i.isalpha()) # if i.isalpha(): проверяет, является ли символ буквой
                                                # ''.join(...): объединяет все полученные символы в одну строку.
if s1==s1[::-1]:
    print('Yes')
else:
    print('No')
