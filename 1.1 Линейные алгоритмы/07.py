def max_squares(a, b, k):
    # Количество квадратов, которые помещаются вдоль стороны a и b
    squares_a = a // k
    squares_b = b // k
    # Общее количество квадратов
    return squares_a * squares_b

# Пример использования:
a = int(input())
b = int(input())
k = int(input())

print(max_squares(a, b, k))
