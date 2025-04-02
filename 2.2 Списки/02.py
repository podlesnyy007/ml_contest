n=int(input())
a=list(map(int, input().split())) # list - список, map(int...) - преобразует каждую строку в целое число 
# перебирает все пары (индекс, значение) и выбирает только те индексы i, для которых значение x равно максимальному
# enumerate(a) создаёт пары (индекс, значение)
index=next(i for i, x in enumerate(a) if x == max(a)) #  next возвращает первый элемент
a=[-x if i == index else x for i, x in enumerate(a)]
print(*a)
