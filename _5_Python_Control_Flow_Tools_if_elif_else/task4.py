number = int(input("Введите номер: "))

if number % 2 == 0 and (str(number).endswith('2') or str(number).endswith('6')):
    print(True)
else:
    print(False)