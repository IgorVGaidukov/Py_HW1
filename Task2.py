# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = int(input('Введите z: '))

res1 = not (x or y or z)
res2 = not x and not y and not z

if res1 == res2:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")