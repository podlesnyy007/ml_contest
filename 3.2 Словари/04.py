s=''
d=dict()
while s.find('.')==-1:
    s = input ().lower()
    for i in s:
        if i.isalpha(): #является ли он буквой
            d[i]=d.get(i,0)+1 # d.get(i, 0) возвращает значение для ключа i в словаре, если оно существует, иначе возвращает 0 и увеличиваем счетчик.
mc=0 #maxcount
ml='' #maxletter
for key in sorted(d.keys()):
    if d[key]>mc:
        mc=d[key]
        ml=key
print(ml, mc)
