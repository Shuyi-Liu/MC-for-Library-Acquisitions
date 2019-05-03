import random
import numpy as np
import pandas as pd
import math


def labor_costs(annual_work_hour):
    """
    This function get hourly labor costs from annual wages. The formulae is from the book.
    :param annual_work_hour: integer.
    :return: float which indicates hourly wage.
    >>> a = labor_costs(1950)
    >>> 50000 < benefit_rate < 70000
    True
    >>> 10 < a < 50
    True
    """
    annual_wages = random.randint(50000, 70000)
    benefit_rate = random.uniform(0, 0.3)
    paid_off_hour = random.randint(0, 42)
    average_cost = (annual_wages + (annual_wages * benefit_rate)) / (annual_work_hour - paid_off_hour)
    return round(average_cost, 2)
# print(labor_costs(1950))


def maintenance_cost(annual_work_hour, total_volume):
    """
    This function is to get annual maintenance cost from total volumes library houses and hourly labor costs.
    :param annual_work_hour: integer
    :param total_volume: integer
    :return: float indicates maintenance cost
    >>> maintenance_cost(1950, 50000)
    156000.0
    """
    maintenance_time = annual_work_hour * 0.04
    volumes_per_box = math.ceil(total_volume / 25)
    maintenance_cost = volumes_per_box * maintenance_time
    return round(maintenance_cost, 2)


print(maintenance_cost(1950, 50000))


def cataloging_cost(annual_work_hour):
    """
    This function calculate the cataloging cost of each book. The cost is random in a range.
    :param annual_work_hour: Integer. a cataloger's annual total work hours in general.
    :return: Float. a cataloging cost of each book.
    >>> cataloging_cost(1950)
    30
    """
    day_cataloging = random.randint(8, 12)
    daily_labor = labor_costs(annual_work_hour) * 8
    cost_per_book = daily_labor / day_cataloging
    return round(cost_per_book, 2)


print(cataloging_cost(1950))


def get_book_list(num_book, annual_work_hour):
    """
    This function generates a list of books that are randomly selected in pages, page thickness, price, and demand level.
    :param num_book: Integer. the number of books that a random book list contains. a librarian will purchase books from it.
    :param annual_work_hour: Integer. a cataloger's annual total work hours in general.
    :return: DataFrame. the columns are thickness, price, demand, and cataloging cost.
    >>> a = get_book_list(10, 1950)
    >>> len(a)
        10
    >>> 10 <= pages <= 2000
    True
    >>> 0.01 <= page_thickness < 0.05
    True
    >>> 0.1 <= thickness < 100
    True
    >>> 0.01 <= page_price < 0.1
    True
    >>> 0.1 <= price < 200
    True
    """
    cost_per_book = cataloging_cost(annual_work_hour)
    pages = np.random.randint(10, 2000, size=num_book)
    page_thickness = np.random.uniform(0.01, 0.05, size=num_book)
    thickness = np.around(page_thickness * pages, decimals=2)
    page_price = random.uniform(0.01, 0.1)
    price = np.around(page_price * pages, decimals=2)
    # Three types of demand indicates 3 is high, 2 medium, and 1 low.
    demand_list = ['1', '2', '3']
    demands = []
    for i in range(num_book):
        demand = random.choice(demand_list)
        # print(demand)
        demands.append(demand)

    df = pd.DataFrame(data={'Thickness': thickness,
                            'Price': price,
                            'Demands': demands,
                            'cataloging_cost': cost_per_book})
    return df


print(get_book_list(10, 1950))


def get_ebook_list(num_ebook, annual_work_hour):
    """
    This function generates a list of ebooks that are randomly selected in pages, prices, demand level, and contract type.
    :param num_ebook: Integer. the number of ebooks that a random ebook list contains. a librarian will purchase ebooks from it.
    :param annual_work_hour: Integer. a cataloger's annual total work hours in general.
    :return: DataFrame. the columns are price of printed version, demand level, contract type, ebook price, and cataloging cost.
    """
    cost_per_book = cataloging_cost(annual_work_hour)
    pages = np.random.randint(10, 2000, size=num_ebook)
    page_price = np.random.uniform(0.01, 0.1, size=num_ebook)
    printed_price = np.around(page_price * pages, decimals=2)
    demand_list = [1, 2, 3]
    demand_select = []
    high_demand_contract = [3, 2]
    mid_demand_contract = [2, 1]
    contract_price_1 = 1.3
    contract_price_2 = 1.3 * 1.5
    contract_price_3 = 1.3 * 2
    contract_select = []
    price_select = []
    for i in range(num_ebook):
        demand = random.choice(demand_list)
        demand_select.append(demand)
        if demand == 3:
            contract = random.choice(high_demand_contract)
            contract_select.append(contract)
            if contract == 3:
                price_select.append(contract_price_3)
            elif contract == 2:
                price_select.append(contract_price_2)
        elif demand == 2:
            contract = random.choice(mid_demand_contract)
            contract_select.append(contract)
            if contract == 2:
                price_select.append(contract_price_2)
            elif contract == 1:
                price_select.append(contract_price_1)
        elif demand == 1:
            contract_select.append(1)
            price_select.append(contract_price_1)

    df = pd.DataFrame(data={'Printed Price': printed_price,
                            'Demand': demand_select,
                            'Contract': contract_select,
                            'Contract rate': price_select,
                            'Ebook Price': np.round(printed_price * price_select, decimals=2),
                            'cataloging cost': cost_per_book})
    return df


print(get_ebook_list(20, 1950))


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


# def book_price_solution(book_plan):
#     """
#     A function for drop books from a list because of limited budget.
#     :param book_plan: Data Frame. A book list with thickness and price
#     :return: Data Frame excluding the book whose cost is the highest from the plan.
#     """
#     drop = book_plan['Book_Price'].max()
#     # print(drop)
#     new_plan = book_plan.loc[book_plan['Book_Price'] != drop]
#     # print('This is the new book plan:\n', new_plan)
#     return new_plan
# # price_solution(all_book(20))
#
#
# def book_thickness_solution(book_plan):
#     """
#
#     :param book_plan:
#     :return:
#     """
#     drop = book_plan['Book_Thickness'].max()
#     new_plan = book_plan.loc[book_plan['Book_Thickness'] != drop]
#     return new_plan
#
#
# def ebook_price_solution(ebook_plan):
#     """
#
#     :param ebook_plan:
#     :return:
#     """
#     drop = ebook_plan['ePrice_with_contract'].max()
#     new_plan = ebook_plan.loc[ebook_plan['ePrice_with_contract'] != drop]
#     return new_plan
#
#
# def both_thickness_solution(both_plan):
#     """
#     A function for dropping books from a list because of limited space
#     :param both_plan: Data Frame. A book list with thickness and price
#     :return: Data Frame, excluding the book whose space is the largest from the plan.
#     """
#     if len(both_plan.index) != 0:
#         drop = both_plan['Book_Thickness'].max()
#         new_plan = both_plan.loc[both_plan['Book_Thickness'] != drop]
#         return new_plan
#     else:
#         print("We have removed all physical books in 'Both' type. Now the space should be OK.\n")
#         return both_plan
#
#
# def both_price_solution(both_plan):
#     df = both_plan.loc[both_plan.ne(0).all(axis=1)]
#     if len(df.index) != 0:
#         p_price = df['Book_Price'].max()
#         e_price = df['ePrice_with_contract'].max()
#         if p_price > e_price:
#             df['Book_Price'].replace(p_price, 0)
#             df.loc[df['Book_Price'] == p_price, 'Book_Thickness'] = 0
#         elif p_price <= e_price:
#             df['ePrice_with_contract'].replace(e_price, 0)
#         return df
#     else:
#         print("We have no more can remove from 'Both' type.\n")
#         return both_plan
#
#
# def Monte(budget, space, num_of_titles, num_book, num_ebook, num_both, simulation):
#     final_num_books = []
#     final_prices = []
#     final_space = []
#     for i in range(simulation):
#         book_plan = book_select(num_book)
#         ebook_plan = ebook_select(num_ebook)
#         both_plan = both_select(num_both)
#         num_physical = num_book + num_both
#         all_physical_price = (book_plan['Book_Price'].sum() +
#                               both_plan['Book_Price'].sum()) * (1 - vendor_discount(num_physical))
#         all_ebook_price = ebook_plan['ePrice_with_contract'].sum() + both_plan['ePrice_with_contract'].sum()
#         both_thickness = both_plan['Book_Thickness'].sum()
#         book_thickness = book_plan['Book_Thickness'].sum()
#         total_price = all_physical_price + all_ebook_price
#         total_thickness = book_thickness + both_thickness
#         if total_price <= budget:
#             if total_thickness <= space:
#                 print('The plan is fine:')
#             elif total_thickness > space:
#                 if book_thickness > space:
#                     print("The budget is enough, but we don't have enough space.\n"
#                           "We will remove all the physical book from 'Both', and some books. The new plan is:\n")
#                     both_plan[both_plan['Book_Price']] = 0
#                     both_plan[both_plan['Book_Thickness']] = 0
#                     while book_thickness > space:
#                         book_plan = book_thickness_solution(book_plan)
#                         book_thickness = book_plan['Book_Thickness'].sum()
#                 elif book_thickness <= space:
#                     print("The budget is enough, but we don't have enough space.\n"
#                           "We will remove physical books from 'Both'. The new plan is:\n")
#                     while total_thickness > space:
#                         both_plan = both_thickness_solution(both_plan)
#                         total_thickness = both_plan['Book_Thickness'].sum() + book_thickness
#         elif total_price > budget:
#             print("Our budget is NOT enough.\nWe will remove the higher price copy from 'Both'.\n")
#             while total_price > budget and len(both_plan.index) != 0:
#                 both_plan = both_price_solution(both_plan)
#                 num_physical = (both_plan['Book_Price'] != 0).sum() + num_book
#                 all_physical_price = (book_plan['Book_Price'].sum() +
#                               both_plan['Book_Price'].sum()) * (1 - vendor_discount(num_physical))
#                 total_price = all_physical_price + ebook_plan['ePrice_with_contract'].sum() \
#                               + both_plan['ePrice_with_contract'].sum()
#             if total_price > budget and len(both_plan.index) == 0:
#                 print("We will remove a highest price copy from 'Book' and 'e-book'.\n")
#                 while total_price > budget:
#                     book_plan = book_price_solution(book_plan)
#                     ebook_plan = ebook_price_solution(ebook_plan)
#                     num_physical = len(book_plan.index) + (both_plan['Book_Price'] != 0).sum()
#                     all_physical_price = (book_plan['Book_Price'].sum() +
#                                           both_plan['Book_Price'].sum()) * (1 - vendor_discount(num_physical))
#                     total_price = all_physical_price + ebook_plan['ePrice_with_contract'].sum()
#             total_thickness = book_plan['Book_Thickness'].sum() + both_plan['Book_Thickness'].sum()
#             if total_thickness <= space:
#                 print('This is the final plan:\n')
#             elif total_thickness > space:
#                 print("We will remove some books from 'Book' to save space.\n")
#                 while total_thickness > space:
#                     book_plan = book_thickness_solution(book_plan)
#                     total_thickness = book_plan['Book_Thickness'].sum() + both_plan['Book_Thickness'].sum()
#                     if len(book_plan.index) == 0:
#                         print("We have no way to relief more space. The plan needs to be changed.\n"
#                               "Please reenter your plan.\n")
#                 total_num_book = len(book_plan.index) + (both_plan['Book_Price'] != 0).sum()
#                 final_num_books.append(total_num_book)
#                 final_prices.append(total_price)
#                 final_space.append(total_thickness)
#                 final_plan = pd.DataFrame({'total_books': final_num_books, 'final_price': final_prices, 'final_space': final_space})
#                 return final_plan


# print(Monte(50000, 40000, 1000, 500, 300, 200, 5))


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









