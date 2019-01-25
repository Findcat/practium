a = input("Введите число:")
b = input("Введите еще одно:")
a = int(a)
b = int(b)
try:
    print(a/b)
except ValueError:
    print("Ошибка ввода.")
