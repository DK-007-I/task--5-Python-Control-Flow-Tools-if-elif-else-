purchase_price = float(input("Введите цену покупки в рублях: "))

if purchase_price < 1000:
    discount = 0  # Без скидки
elif 1000 <= purchase_price <= 5000:
    discount = purchase_price * 0.05  # 5%  скидка
else:
    discount = purchase_price * 0.10  # 10%  скидка

final_price = purchase_price - discount

print(f"Скидка: {discount:.2f} рублей")
print(f"Окончательная цена после скидки: {final_price:.2f} рублей")