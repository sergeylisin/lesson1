def format_price(price):
    p = int(price)
    ret = f'Цена: {p} руб.'
    return ret

price = 56.24
formatted_price = format_price(price)
print(formatted_price)