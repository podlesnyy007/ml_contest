s=input()
d = {'0': 0, '100': 0, '101': 0, '11': 0}
temp=''
maxc='0'
for c in s:
    temp+=c
    if (d.get (temp)!=None): 
        d[temp]+=1 
        if (d[temp]>d[maxc]):
            maxc=temp
        temp=''
d3 = {'0': 2, '100': 3, '101': 4, '11': 5}
print(d3[maxc])
