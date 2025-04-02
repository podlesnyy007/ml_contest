n, m = map(int, input().split())
# первый
l = [tuple(map(int, input().split())) for i in range(m)]
# оставшиеся
sets = list(set(tuple(map(int, input().split()))
                for k in range(m)) for j in range(n - 1))
ml = [0] * m

for i in range(n - 1): #цикл проходит по всем остальным наборам (кроме первого)
    for j in set(l) & sets[i]: #для каждого набора вычисляется пересечение между множеством точек первого набора
        ml[l.index(j)] += 1 #сколько

if max(ml)==0:
    print(-1)
else:
    print(' '.join(str(i) for i in l[ml.index(max(ml))])) #координата
