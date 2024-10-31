def show_products_buy():
    print('=' * 64 + '\n|| Products available for purchase:' + ' ' * 28 + '||')
    print('|| 1) Category: Sport | Product: Football T-Shirt | Price: 100 ||')
    print('|| 2) Category: Food | Product: Ramen | Price: 1.5 ' + ' ' * 12 + '||')
    print('|| 3) Category: Sport | Product: Ball | Price: 50 ' + ' ' * 13 + '||')
    print('|| 4) Category: Food | Product: Fish | Price: 20 ' + ' ' * 14 + '||')
    print('|| 5) Category: Sport | Product: Bike | Price: 400 ' + ' ' * 12 + '||')
    print('|| 6) Category: Food | Product: Protein | Price: 70.5 ' + ' ' * 9 + '||')
    print('=' * 64)


from models import store, history, manager


def options():
    print('''Choice the option:
        Balance
        Sale
        Buy
        Bank account
        Warehouse inventory
        Product Inventory
        Set discount
        Request history
        Clear history
        Store history
        End''')


def main():
    while True:
        options()
        command = input("Enter command to execute: ").lower()
        try:
            history.set_history(command)
            if command == 'end':
                break
            result = manager.execute(command, store)
            if result is not None:
                print("Result:", result)
        except AttributeError as e:
            print(e)
