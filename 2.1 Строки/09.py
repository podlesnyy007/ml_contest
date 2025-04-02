n = int (input ())
count=0
for i in range(n):
  s = input ()
  if s[0] != '@' and s[-1] != '@' and s.count ('@') == 1 and s.find ("..") == -1:
    count+=1
print (count)
