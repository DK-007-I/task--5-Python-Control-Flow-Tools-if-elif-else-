preset_password = "securePassword123"

entered_password = input("Введите свой пароль: ")

if entered_password == preset_password:
    print("Доступ предоставлен.")
else:
    print("Неверный пароль.")