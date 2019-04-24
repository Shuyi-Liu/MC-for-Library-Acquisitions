import random
import numpy as np
import pandas as pd

class acquisitions:

    def __init__(self, type, price, contract):
        self.type = type
        self.price = price
        self.contract = contract

    def price_decision(self):
        type = ['printed_book', 'e-book']
        if type == 'printed_book':
            price = self.price
        else:
            price = self.price * 130

    def contract(self):
        contract_option = ['one_user', 'three_user', 'unlimited']
        if contract_option == 'one_user':
            price = self.price
        elif contract_option == 'three_user':
            price = self.price * 150
        elif contract_option == 'unlimited':
            price = self.price * 200

def get_types(num_of_titles):
    pb = input("right percentage of printed_book:" )
    eb = input("right percentage of e-book:" )
    both = input("right percentage of both pb and -ebook:" )
    numprinted = num_of_titles * pb // 100
    numebook = num_of_titles * eb // 100
    both = num_of_titles * both // 100
    if acquisitions.type == 'printed_book':
        pages_list = []
        for i in range(numprinted):
            page = round(random.randint(10, 2000), 2)
            pages_list.append(page)
        print("This is the random pages:", pages_list)
        thickness_list = []
        for i in pages_list:
            thickness1 = round(random.uniform(0.1, 2), 2)  # thickness measurement is centimeter.
            thickness2 = round(random.uniform(2, 6), 2)
            thickness3 = round(random.uniform(6, 10), 2)
            if i <= 300:
                thickness_list.append(thickness1)
            elif 300 < i <= 1000:
                thickness_list.append(thickness2)
            elif 1000 < i:
                thickness_list.append(thickness3)
        print("thickness_list", thickness_list)
        price_list = []
        for i in pages_list:
            price1 = round(random.uniform(1, 40), 2)
            price2 = round(random.uniform(40, 100), 2)
            price3 = round(random.uniform(100, 200), 2)
            if i <= 100:
                price_list.append(price1)
            elif 100 < i <= 400:
                price_list.append(price2)
            elif i > 400:
                price_list.append(price3)
        print("This is the random price", price_list)
    elif acquisitions.type == 'e_book':
        pages_list = []
        for i in range(numprinted):
            page = round(random.randint(10, 2000), 2)
            pages_list.append(page)
        print("This is the random pages:", pages_list)
        e_price_list = []
        for i in pages_list:
            price1 = round(random.uniform(1, 40), 2)
            price2 = round(random.uniform(40, 100), 2)
            price3 = round(random.uniform(100, 200), 2)
            if i <= 100:
                e_price_list.append(price1)
            elif 100 < i <= 400:
                e_price_list.append(price2)
            elif i > 400:
                e_price_list.append(price3)
        for i in e_price_list:
            option = acquisitions.contract
        print("This is the random price", price_list)

    df = pd.DataFrame(data={'Thickness': thickness_list,
                                'Price': price_list})
        # print("This is the random book\n", df)
    return df


def vendor_discount(self):
    if self.num_of_titles < 100:
        return 0.01
    elif 100 <= self.num_of_titles < 500:
        return 0.02
    elif self.num_of_titles >= 500:
        return 0.05










