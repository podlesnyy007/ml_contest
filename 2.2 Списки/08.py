n = int (input ())
a = list (map (int, input ().split ()))

min = min (a)
l_index = a.index (min) #находит индекс самого левого минимума в массиве

max = max (a)
r_index = len (a) - 1 - a[::-1].index (max) #находит индекс самого правого максимума в массиве

if l_index < r_index:
    a[l_index:r_index + 1] = a[l_index:r_index + 1][::-1]
else:
    a[r_index:l_index + 1] = a[r_index:l_index + 1][::-1]

print (*a)
