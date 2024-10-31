from datetime import datetime
from utils import show_products_buy


class Manager:
    def __init__(self):
        self.methods = {}

    def assign(self, method_name):
        def decorate(func):
            self.methods[method_name] = func
            return func

        return decorate

    def execute(self, action, obj, *args, **kwargs):
        if action in self.methods:
            return self.methods[action](obj, *args, **kwargs)
        else:
            raise AttributeError(f'Method "{action}" not found.')


manager = Manager()


class History:
    def __init__(self):
        self.__set_history = open('history.txt', 'a')
        self.__get_history = open('history.txt', 'r')

    def set_history(self, request):
        cur_time = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M'), '%Y-%m-%d %H:%M')
        self.__set_history.write(f'Enter: {cur_time}. Request: {request}\n')

    def get_history(self):
        print('Enter the number of records required. All history(start=0;end=0):')
        start = int(input('Start: '))
        end = int(input('End: '))
        if end == 0:
            print(self.__get_history.read())
        elif end != 0:
            for i in range(start, end + 1):
                print(self.__get_history.readline())
        else:
            print('Error')

    def clear_history(self):
        open('history.txt', 'w').close()
        print('History has been cleared!')


history = History()


class Product:
    def __init__(self, category, name, price):
        self.category = category
        self.name = name
        self.price = price
        self.amount = 0
        self.discount = 0


p1 = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
p3 = Product('Sport', 'Ball', 50)
p4 = Product('Food', 'Fish', 20)
p5 = Product('Sport', 'Bike', 400)
p6 = Product('Food', 'Protein', 70.5)


class ProductStore:

    def __init__(self):
        self.product_store = []
        self.money = 10000
        self.balance = 0
        self.store_info = open('store_history.txt', 'a')
        self.cur_time = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M'), '%Y-%m-%d %H:%M')

    @manager.assign('buy')
    def add(self):
        show_products_buy()
        product_name = input('Input name product: ')
        if product_name == '1':
            product = p1
        elif product_name == '2':
            product = p2
        elif product_name == '3':
            product = p3
        elif product_name == '4':
            product = p4
        elif product_name == '5':
            product = p5
        elif product_name == '6':
            product = p6
        amount = int(input('Input quantity of products: '))

        if self.money >= amount * product.price:
            self.money -= amount * product.price
            self.balance -= amount * product.price
            self.store_info.write(f'Time change: {self.cur_time}\nCurrent balance: {self.get_balance()}\n')
            if product not in self.product_store:
                self.product_store.append(product)
            product.amount += amount
            self.store_info.write(f'Products in store:\n{self.get_all_products()}\n\n')
            print('Product is added!')
        else:
            print('You dont have enough money!')

    @manager.assign('set discount')
    def set_discount(self):
        identifier = input('Enter name or category: ')
        percent = int(input('Enter % discount: '))
        for product in self.product_store:
            if product.category == identifier or product.name == identifier:
                product.discount = percent
                product.price = product.price - (product.price * percent / 100)
        print(f'Discount {percent} for products was set')

    @manager.assign('sale')
    def sell_product(self):
        if self.product_store:
            print('Warehouse inventory: ')
            print(self.get_all_products())

            product_name = input('Input name product: ')
            amount = int(input('Input quantity of products: '))

            for product in self.product_store:
                if product.name.lower() == product_name.lower() and product.amount >= amount:
                    product.amount -= amount
                    self.money += amount * (product.price + (product.price * 30 / 100))
                    self.balance += amount * (product.price + (product.price * 30 / 100))
                    self.store_info.write(f'Time change: {self.cur_time}\nCurrent balance: {self.get_balance()}\n')
                    self.store_info.write(f'Products in store:\n{self.get_all_products()}\n\n')
                    print('Sell!')
                elif product.name == product_name and product.amount < amount:
                    print('Name or amount error!')
        else:
            print('Store is empty!')

    @manager.assign('bank account')
    def get_money(self):
        return self.money

    @manager.assign('balance')
    def get_balance(self):
        return self.balance

    @manager.assign('warehouse inventory')
    def get_all_products(self):
        all_products = []
        if self.product_store:
            for product in self.product_store:
                all_products.append(
                    {
                        'Category': product.category,
                        'Name': product.name,
                        'Price': product.price,
                        'Amount': product.amount,
                        'Discount': product.discount

                    }
                )
            return [i for i in all_products]
        else:
            print('Store is empty!')

    @manager.assign('product inventory')
    def get_product_info(self):
        product_name = input('Input product name: ')
        for product in self.product_store:
            if product_name.lower() == product.name.lower():
                return f'Name product: {product.name}, quantity: {product.amount} , price: {product.price}'
        print('We dont have this product!')

    @manager.assign('store history')
    def get_store_history(self):
        file = open('store_history.txt', 'r')
        return file.read()

    @manager.assign('request history')
    def get_history(self):
        return history.get_history()

    @manager.assign('clear history')
    def clear_history(self):
        return history.clear_history()


store = ProductStore()
