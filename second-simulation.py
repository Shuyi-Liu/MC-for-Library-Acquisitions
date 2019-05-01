import random
import numpy as np
import pandas as pd
from itertools import groupby


def book_select(num_book):
    """
    This is getting attributes of books, thickness and prices.
    The price will calculate randomly depending on its thickness.
    :param num_book: Integer. a number of titles a librarian is going to purchase.
    :return: DataFrame, columns are thickness and price.
    >>> a = all_book(10)
    >>> len(a)
        10
    >>> 20 < thickness_list < 50000
    True
    >>> 1 < price_list < 200
    True

    """
    book_page_list = []
    for i in range(num_book):
        page = round(random.randint(10, 2000), 2)
        book_page_list.append(page)
    print("This is the random book pages:", book_page_list)
    thickness_list = []
    for i in book_page_list:
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
    for i in book_page_list:
        price1 = round(random.uniform(1, 40), 2)
        price2 = round(random.uniform(40, 100), 2)
        price3 = round(random.uniform(100, 200), 2)
        if i <= 100:
            price_list.append(price1)
        elif 100 < i <= 400:
            price_list.append(price2)
        elif i > 400:
            price_list.append(price3)
    print("This is the random book price", price_list)

    df = pd.DataFrame(data={'Pages': book_page_list,
                            'Book_Thickness': thickness_list,
                            'Book_Price': price_list})
    print("This is the random book\n", df)
    return df


# print(book_select(20))


def ebook_select(num_ebook):
    """

    :param num_ebook:
    :return:
    """
    ebook_page_list = []
    for i in range(num_ebook):
        page = round(random.randint(10, 2000), 2)
        ebook_page_list.append(page)
    print("This is the random pages:", ebook_page_list)
    price_list = []
    for i in ebook_page_list:
        price1 = round(random.uniform(1, 10), 2)
        price2 = round(random.uniform(10, 20), 2)
        price3 = round(random.uniform(20, 50), 2)
        if i <= 100:
            price_list.append(price1)
        elif 100 < i <= 500:
            price_list.append(price2)
        elif i > 500:
            price_list.append(price3)
    price_with_contract = []
    contract_list = [1, 1.5, 2, 3, 5]  # contract indicates how many people can access the book at the same time.
    for i in price_list:
        price_contract = i * random.choice(contract_list)
        price_with_contract.append(price_contract)
    print("This is the random ebook price", price_with_contract)
    df = pd.DataFrame(data={'Pages': ebook_page_list,
                            'ebook_Price': price_list,
                            'ePrice_with_contract': price_with_contract})
    print("This is the random ebook\n", df)
    return df


print(ebook_select(20))


def both_select(num_both):
    """

    :param num_both:
    :return:
    """
    both_page_list = []
    for i in range(num_both):
        page = round(random.randint(10, 2000), 2)
        both_page_list.append(page)
    print("This is the random Both pages:", both_page_list)
    thickness_list = []
    for i in both_page_list:
        thickness1 = round(random.uniform(0.1, 2), 2)  # thickness measurement is centimeter.
        thickness2 = round(random.uniform(2, 6), 2)
        thickness3 = round(random.uniform(6, 10), 2)
        if i <= 300:
            thickness_list.append(thickness1)
        elif 300 < i <= 1000:
            thickness_list.append(thickness2)
        elif 1000 < i:
            thickness_list.append(thickness3)
    print("both_thickness_list", thickness_list)
    price_list1 = []
    price_list2 = []

    for i in both_page_list:
        price1 = round(random.uniform(1, 40), 2)
        price2 = round(random.uniform(40, 100), 2)
        price3 = round(random.uniform(100, 200), 2)
        price4 = round(random.uniform(1, 10), 2)
        price5 = round(random.uniform(10, 20), 2)
        price6 = round(random.uniform(20, 50), 2)
        if i <= 100:
            price_list1.append(price1)
            price_list2.append(price4)
        elif 100 < i <= 400:
            price_list1.append(price2)
            price_list2.append(price5)
        elif i > 400:
            price_list1.append(price3)
            price_list2.append(price6)
    price_with_contract = []
    contract_list = [1, 1.5, 2, 3, 5]
    for i in price_list2:
        price_contract = i * random.choice(contract_list)
        price_with_contract.append(price_contract)
    print("This is the random Both price", price_list1, '\n', price_list2)
    df = pd.DataFrame(data={'Pages': both_page_list,
                            'Book_Thickness': thickness_list,
                            'Book_Price': price_list1,
                            'ebook_Price': price_list2,
                            'ePrice_with_contract': price_with_contract})
    print("This is the random Both\n", df)
    return df


print(both_select(20))


def vendor_discount(num_physical):
    """
    Discount percentage vendor will offer.
    :param num_physical: Integer. A number of titles a librarian is going to purchase from a vendor
    :return: float.
    >>> vendor_discount(50)
    0.01
    >>> vendor_discount(280)
    0.02
    """
    if num_physical < 100:
        return 0.01
    elif 100 <= num_physical < 500:
        return 0.02
    elif num_physical >= 500:
        return 0.05


def book_price_solution(book_plan):
    """
    A function for drop books from a list because of limited budget.
    :param book_plan: Data Frame. A book list with thickness and price
    :return: Data Frame excluding the book whose cost is the highest from the plan.
    """
    drop = book_plan['Book_Price'].max()
    # print(drop)
    new_plan = book_plan.loc[book_plan['Book_Price'] != drop]
    # print('This is the new book plan:\n', new_plan)
    return new_plan
# price_solution(all_book(20))


def book_thickness_solution(book_plan):
    """

    :param book_plan:
    :return:
    """
    drop = book_plan['Book_Thickness'].max()
    new_plan = book_plan.loc[book_plan['Book_Thickness'] != drop]
    return new_plan


def ebook_price_solution(ebook_plan):
    """

    :param ebook_plan:
    :return:
    """
    drop = ebook_plan['ePrice_with_contract'].max()
    new_plan = ebook_plan.loc[ebook_plan['ePrice_with_contract'] != drop]
    return new_plan


def both_thickness_solution(both_plan):
    """
    A function for dropping books from a list because of limited space
    :param both_plan: Data Frame. A book list with thickness and price
    :return: Data Frame, excluding the book whose space is the largest from the plan.
    """
    if len(both_plan.index) != 0:
        drop = both_plan['Book_Thickness'].max()
        new_plan = both_plan.loc[both_plan['Book_Thickness'] != drop]
        return new_plan
    else:
        print("We have removed all physical books in 'Both' type. Now the space should be OK.\n")
        return both_plan


def both_price_solution(both_plan):
    df = both_plan.loc[both_plan.ne(0).all(axis=1)]
    if len(df.index) != 0:
        p_price = df['Book_Price'].max()
        e_price = df['ePrice_with_contract'].max()
        if p_price > e_price:
            df['Book_Price'].replace(p_price, 0)
            df.loc[df['Book_Price'] == p_price, 'Book_Thickness'] = 0
        elif p_price <= e_price:
            df['ePrice_with_contract'].replace(e_price, 0)
        return df
    else:
        print("We have no more can remove from 'Both' type.\n")
        return both_plan


def Monte(budget, space, num_of_titles, num_book, num_ebook, num_both, simulation):
    final_num_books = []
    final_prices = []
    final_space = []
    for i in range(simulation):
        book_plan = book_select(num_book)
        ebook_plan = ebook_select(num_ebook)
        both_plan = both_select(num_both)
        num_physical = num_book + num_both
        all_physical_price = (book_plan['Book_Price'].sum() +
                              both_plan['Book_Price'].sum()) * (1 - vendor_discount(num_physical))
        all_ebook_price = ebook_plan['ePrice_with_contract'].sum() + both_plan['ePrice_with_contract'].sum()
        both_thickness = both_plan['Book_Thickness'].sum()
        book_thickness = book_plan['Book_Thickness'].sum()
        total_price = all_physical_price + all_ebook_price
        total_thickness = book_thickness + both_thickness
        if total_price <= budget:
            if total_thickness <= space:
                print('The plan is fine:')
            elif total_thickness > space:
                if book_thickness > space:
                    print("The budget is enough, but we don't have enough space.\n"
                          "We will remove all the physical book from 'Both', and some books. The new plan is:\n")
                    both_plan[both_plan['Book_Price']] = 0
                    both_plan[both_plan['Book_Thickness']] = 0
                    while book_thickness > space:
                        book_plan = book_thickness_solution(book_plan)
                        book_thickness = book_plan['Book_Thickness'].sum()
                elif book_thickness <= space:
                    print("The budget is enough, but we don't have enough space.\n"
                          "We will remove physical books from 'Both'. The new plan is:\n")
                    while total_thickness > space:
                        both_plan = both_thickness_solution(both_plan)
                        total_thickness = both_plan['Book_Thickness'].sum() + book_thickness
        elif total_price > budget:
            print("Our budget is NOT enough.\nWe will remove the higher price copy from 'Both'.\n")
            while total_price > budget and len(both_plan.index) != 0:
                both_plan = both_price_solution(both_plan)
                num_physical = (both_plan['Book_Price'] != 0).sum() + num_book
                all_physical_price = (book_plan['Book_Price'].sum() +
                              both_plan['Book_Price'].sum()) * (1 - vendor_discount(num_physical))
                total_price = all_physical_price + ebook_plan['ePrice_with_contract'].sum() \
                              + both_plan['ePrice_with_contract'].sum()
            if total_price > budget and len(both_plan.index) == 0:
                print("We will remove a highest price copy from 'Book' and 'e-book'.\n")
                while total_price > budget:
                    book_plan = book_price_solution(book_plan)
                    ebook_plan = ebook_price_solution(ebook_plan)
                    num_physical = len(book_plan.index) + (both_plan['Book_Price'] != 0).sum()
                    all_physical_price = (book_plan['Book_Price'].sum() +
                                          both_plan['Book_Price'].sum()) * (1 - vendor_discount(num_physical))
                    total_price = all_physical_price + ebook_plan['ePrice_with_contract'].sum()
            total_thickness = book_plan['Book_Thickness'].sum() + both_plan['Book_Thickness'].sum()
            if total_thickness <= space:
                print('This is the final plan:\n')
            elif total_thickness > space:
                print("We will remove some books from 'Book' to save space.\n")
                while total_thickness > space:
                    book_plan = book_thickness_solution(book_plan)
                    total_thickness = book_plan['Book_Thickness'].sum() + both_plan['Book_Thickness'].sum()
                    if len(book_plan.index) == 0:
                        print("We have no way to relief more space. The plan needs to be changed.\n"
                              "Please reenter your plan.\n")
                total_num_book = len(book_plan.index) + (both_plan['Book_Price'] != 0).sum()
                final_num_books.append(total_num_book)
                final_prices.append(total_price)
                final_space.append(total_thickness)
                final_plan = pd.DataFrame({'total_books': final_num_books, 'final_price': final_prices, 'final_space': final_space})
                return final_plan


print(Monte(50000, 40000, 1000, 500, 300, 200, 5))


# #--------------------------------------------------below still working on------------------
#             if book_thickness <= space:
#                 print("The new plan is:")
#                 both_price = both_plan['Price'].sum() * (1 - vendor_discount(num_of_titles))
#
#             elif book_thickness > space:
#                 print("The new plan has no enough space.\nChange it.")
#                 while book_thickness > space:
#                     book_plan = space_solution(book_plan)
#                     book_thickness = book_plan['Thickness'].sum()
#
# budget = int(input("please:" ))
# space = int(input(": "))
# number = int(input(":" ))
# simulation = int(input(": "))

# print(Monte(budget, space, number, simulation))
# print(Monte(3000, 40000, 10, 8))









