coins = [1, 5, 7, 10, 15]


def calculate_change(product, payment):
    price = products[product]
    change = payment - price
    change_coins = {}

    while change > 0:
        max_coin = max([coin for coin in coins if coin <= change])
        if max_coin in change_coins:
            change_coins[max_coin] += 1
        else:
            change_coins[max_coin] = 1
        change -= max_coin

    return change_coins


products = {
    "молоко": 20,
    "хлеб": 15,
    "яблоки": 30,
    "сырок": 25,
    "вода": 10,
    "сухарики": 18,
    "кириешки": 22,
    "вкусняшки": 12,
    "чипсы": 35,
    "салат": 40
}
print("\nДоступные продукты и их цены:")
for product, price in products.items():
    print(f"{product}: {price}р.")

product = input("Выберите продукт из списка: ")
payment = products.get(product)

if payment is None:
    print("Такого продукта нет в списке.")
else:
    payment = int(input("Введите сумму, которую вы дали: "))
    change_coins = calculate_change(product, payment)

    print("Сдача:")
    for coin, count in change_coins.items():
        print(f"{count} монет номиналом {coin}р")
