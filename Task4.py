# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Введите номер четверти: '))
str_coord = ''
if num == 1:
    str_coord = 'x > 0, y > 0'
elif num == 2:
    str_coord = 'x < 0, y > 0'
elif num == 3:
    str_coord = 'x < 0, y < 0'
elif num == 4:
    str_coord = 'x > 0, y < 0'

print(f'Четверть {num}: {str_coord}')