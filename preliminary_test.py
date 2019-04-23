import random
import numpy as np
import pandas as pd


def all_book(num_of_titles):
    '''
    This is getting attributes of books, thickness and prices. The price will caculate randomly depedning on its thickness.
    :param num_of_titles: Integer. a number of titles a librarian would like to purchase.
    :return: DataFrame, columns are thickness and price.
    '''
    thickness_list = []
    for i in range(num_of_titles):
        thickness = round(random.uniform(0.1, 20), 2)
        thickness_list.append(thickness)
    # print("This is the random thickness:", thickness_list)
    price_list = []
    for i in thickness_list:
        price1 = round(random.uniform(1, 50), 2)
        price2 = round(random.uniform(50, 100), 2)
        price3 = round(random.uniform(100, 200), 2)
        if i <= 5:
            price_list.append(price1)
        elif 5 < i <= 10:
            price_list.append(price2)
        elif i > 10:
            price_list.append(price3)
    # print("This is the random price", price_list)
    df = pd.DataFrame(data={'Thickness': thickness_list,
                            'Price': price_list})
    print("This is the random book\n", df)
    return df


def vendor_discount(num_of_titles):
    '''
    Discount percentage vendor will offer.
    :param num_of_titles: Integer. A number of titles a librarian would like to purchase from a vendor
    :return: float.
    >>> vendor_discount(50)
    0.01
    >>> vendor_discount(280)
    0.02
    '''
    if num_of_titles < 100:
        return 0.01
    elif 100 <= num_of_titles < 500:
        return 0.02
    elif num_of_titles >= 500:
        return 0.05


def price_solution(plan):
    '''
    A function for drop books from a list because of limited budget.
    :param plan: Data Frame. A book list with thickness and price
    :return: Data Frame excluding the book whose cost is the highest from the plan.
    '''
    drop = plan['Price'].max()
    # print(drop)
    new_plan = plan.loc[plan['Price'] != drop]
    # print('This is the new book plan:\n', new_plan)
    return new_plan
# price_solution(all_book(20))


def space_solution(plan):
    '''
    A function for dropping books from a list because of limited space
    :param plan: Data Frame. A book list with thickness and price
    :return: Data Frame, excluding the book whose space is the largest from the plan.
    '''
    drop = plan['Thickness'].max()
    # print(drop)
    new_plan = plan.loc[plan['Thickness'] != drop]
    # print('This is the new book plan:\n', new_plan)
    return new_plan


def Monte(budget, space, num_of_titles, simulation):

    # total_price = []
    # total_thickness = []
    # for i in range(simulation):

    plan = all_book(num_of_titles)

    total_price = plan['Price'].sum() * (1 - vendor_discount(num_of_titles))
    total_space = plan['Thickness'].sum()
    # print("This is the total price", total_price, type(total_price), type(plan['Price'].sum()), type(vendor_discount(num_of_titles)))
    # print("This is the total space", total_space, type(total_space))
    if total_price <= budget:
        if total_space <= space:
            print('The plan is fine:')

        elif total_space > space:
            print("The budget is enough, but we don't have enough space.\nThe new plan is:")
            while total_space > space:
                plan = space_solution(plan)
                total_space = plan['Thickness'].sum()

    elif total_price > budget:
        print("The budget is not enough.\nWe need a new plan.")
        while total_price > budget:
            plan = price_solution(plan)
            total_price = plan['Price'].sum() * (1 - vendor_discount(num_of_titles))

        if total_space <= space:
            print("The new plan is:")

        elif total_space > space:
            print("The new plan has no enough space.\nChange it.")
            while total_space > space:
                plan = space_solution(plan)
                total_space = plan['Thickness'].sum()
    final_price = plan['Price'].sum()
    final_space = total_space
    print(final_price)
    print(total_space)

        # a = plan['Price'].sum()
        # b = plan['thickness'].sum()
        # total_price.append(a)
        # total_price.append(b)
    # total_price = new_plan['Price'].sum()
    # total_thickness = new_plan['Thickness'].sum()
    # d = {'total_cost': total_price, 'total_thickness': total_thickness}

    # final_plan = pd.DataFrame(data = d)



    # final_plan = pd.DataFrame({'final_price': final_price, 'final_space': final_space})
    # print


    return final_price, final_space


# def simulation(num_of_sim):
#     budget = input("Please write your budget for a month: ")
#     space = input("Please write available space: ")
#     num_of_titles = input("Please write number of titles you intend to purchase: ")
#     for i in range(num_of_sim):
#         Monte(budget, space, num_of_titles)


            # plan_titles = len(plan.index)
            # plan_cost = plan['Price'].sum()
            # plan_space = plan['Thickness'].sum()
            #
            # print(plan_titles)
            # final_plan = pd.DataFrame({'num': plan_titles,
            #                            'total_price': plan_cost,
            #                            'total_space': plan_space})
            # print('\nThe final plan is:', final_plan)
            # return final_plan




print(Monte(300000, 100, 20, 5))


