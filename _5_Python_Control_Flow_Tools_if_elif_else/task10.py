king = "Враги приближаются! Готовы ли лучники?"
warrior = "Для Альянса!"
magician = "Заклинание готовоy."

def check_punctuation(phrase):
    if phrase.endswith('?'):
        return "Это вопрос."
    elif phrase.endswith('!'):
        return "Это восклицание."
    elif phrase.endswith('.'):
        return "Это заявление."
    else:
        return "В конце нет распознанных знаков препинания."

print("Король:", check_punctuation(king))
print("Воин:", check_punctuation(warrior))
print("Волшебник:", check_punctuation(magician))
