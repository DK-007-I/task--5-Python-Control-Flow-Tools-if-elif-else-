plane = {
    (0, 0): ('blue', 5),
    (0, 1): ('green', 3),
    (0, 2): ('grey', 0),
    (1, 0): ('green', 7),
    (1, 1): ('blue', 2),
    (1, 2): ('grey', 0)
}

def check_square(x, y):
    square = plane.get((x, y))
    if square:
        color, value = square
        if color == 'grey':
            return "Площадь пуста."
        else:
            return f"На площади есть {color} попугай со значением {value}."
    else:
        return "Неверные координаты."

x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))
result = check_square(x, y)
print(result)