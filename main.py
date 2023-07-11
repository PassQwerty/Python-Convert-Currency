def currency_converter(amount, from_currency, to_currency):
    # Данные для конвертации
    currencies = {
        'USD': 1.0,
        'EUR': 0.9,
        'RUB': 75.4323
    }
    # Вычисляем сумму в долларах (сумма/ 1 USD)
    amount_in_usd = amount / currencies[from_currency]
    # Вычисляем сумму в нужной валюте (сумма в долларах * текущий курс)
    converted_amount = amount_in_usd * currencies[to_currency]
    # Выводим результат
    print(f"{amount} {from_currency} {round(converted_amount, 3)} {to_currency}")


def main():
    amount = float(input("Введите сумму: "))
    from_currency = input("Введите вашу валюту(USD, EUR, RUB): ")
    to_currency = input("Введите будущую валюту(USD, EUR, RUB): ")

    # 1000 RUB = 12.47 EUR
    currency_converter(amount, from_currency, to_currency)


if __name__ == main():
    main()
