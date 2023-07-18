def initial_display():
    print('''_____________________________________________________
            Sunway Bhatbhateni System
                Maitidevi,Kathmandu
______________________________________________________''')


initial_display()


def input_info():
    name = input('Enter the name:')
    id = int(input('Enter customer Id:'))
    address = input('Enter the Address:')
    num_item = int(input('Enter Item purchased:'))
    item_price = []
    quantity_item = []
    total_price = []
    for i in range(num_item):
        item_prices = int(input(f'Enter {i+1} item unit price (Rs):'))
        quantity = int(input(f'Enter quantiy of {i+1} item :'))
        item_price_quantity = item_prices * quantity
        item_price.append(item_prices)
        quantity_item.append(quantity)
        total_price.append(item_price_quantity)
    print('_____________________________________________________')
    return name, id, address, num_item, item_price, quantity_item, total_price


name, id, address, num_item, item_price, quantity_item, total_price = input_info()


def bill():
    total = sum(total_price)

    if total <= 500:
        discount = 1
        discout_amount = total*0.01
        amount_after_d = total - discout_amount
    elif total > 500 and total <= 1000:
        discount = 3
        discout_amount = 500*0.01 + (total-500)*0.03
        amount_after_d = total - discout_amount

    elif total > 1000 and total <= 1500:
        discount = 5
        discout_amount = 500*0.01 + (1000-500)*0.03+(total-1000)*0.05
        amount_after_d = total - discout_amount

    elif total > 1500 and total <= 2000:
        discount = 8
        discout_amount = 500*0.01 + \
            (1000-500)*0.03+(1500-1000)*0.05+(total-1500)*0.08
        amount_after_d = total - discout_amount
    else:
        discount = 10
        discout_amount = 500*0.01 + \
            (1000-500)*0.03+(1500-1000)*0.05+(2000-1500)*0.08+(total-2000)*0.1
        amount_after_d = total - discout_amount
    return total, discount, discout_amount, amount_after_d


total, discount, discout_amount, amount_after_d = bill()


def value_print():
    print('_________________________________________________________________')
    print('                Sunway Bhatbhatini System')
    print('                     Maitidevi,Kathmandu')
    print('_________________________________________________________________')
    print('Customer name: ', name)
    print('Customer Address:', address)
    for i in range(num_item):
        print(f'Unit price {i+1}: {item_price[i]}')
        print(f'Quantity {i+1}: {quantity_item[i]}')
        print(f'Amount {i+1}: {total_price[i]}')
    print(f'''Mr/Mrs. {name}, you have purchased {num_item} items whose
total price is {total} and discount is {discout_amount} with 
discount rate {discount}%, so, total amount to be paid after discount is {amount_after_d}''')
    print('_________________________________________________________________')


value_print()