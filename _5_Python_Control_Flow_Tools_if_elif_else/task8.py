def check_mission_status(level, health):
    if level < 0 or health < 0 or health > 100:
        return "Неверные данные."

    if level < 5:
        return "Ваш уровень слишком низок, чтобы выполнить миссию."
    else:
        if health > 50:
            return "Вы готовы к выполнению задания!"
        elif 20 <= health <= 50:
            return "Ваше здоровье на исходе, будьте осторожны."
        else:  # health < 20
            return "У вас слишком мало здоровья, чтобы выполнить миссию."


try:
    player_level = int(input("Введите свой уровень: "))
    player_health = int(input("Войдите в свое здоровье: "))

    result = check_mission_status(player_level, player_health)
    print(result)
except ValueError:
    print("Неверные данные.")