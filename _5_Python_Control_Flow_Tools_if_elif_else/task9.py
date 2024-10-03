def check_inventory(inventory):
    has_key = "key" in inventory
    has_flashlight = "flashlight" in inventory

    if has_key and has_flashlight:
        return "Ты можешь пройти через дверь."
    elif not has_key and not has_flashlight:
        return "У вас нет ни ключа, ни фонарика, вы не можете войти в дверь."
    elif not has_key:
        return "У тебя нет ключа, ты не можешь открыть дверь.."
    else:   
        return "У тебя нет фонарика, здесь слишком темно, чтобы пройти.."


inventory = ["apple", "ballpoint pen"]


result = check_inventory(inventory)
print(result)