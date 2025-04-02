mstr = input()
mset=set(mstr)
ml=list(i for i in mset if mstr.count(i)==1)
print(''.join(str(i) for i in sorted(ml)))
#Функция sorted() сортирует список ml в алфавитном порядке по возрастанию
#Метод ''.join(...) объединяет отсортированные символы в одну строку.
