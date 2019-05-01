import random
import numpy as np
import pandas as pd
import math


# class labors:
#     def __set__(self, annual_wages, benefit_rate, work_hour, paid_vacation_hour):
#         labors.self = labors
#         labors.annual_wages = annual_wages
#         labors.benefit_rate = benefit_rate
#         labors.work_hour = work_hour
#         labors.paid_vacation_hour = paid_vacation_hour





def get_cataloging_cost(num_of_titles):
    annual_wages = random.randint(50000, 70000)
    benefit_rate = random.uniform(0, 0.3)
    paid_off_hour = random.randint(0, 42)
    average_cost = (annual_wages + (annual_wages * benefit_rate)) / (1950 - paid_off_hour)
    hourly_cataloging_items = math.ceil(num_of_titles / random.randint(10, 12))
    print(hourly_cataloging_items)
    print(average_cost)
    labor_cost = average_cost * hourly_cataloging_items
    return round(labor_cost, 2)
# print(get_cataloging_cost(10000))

# def get_circulation_cost():

def get_maintenance(total_volumes):
    maintenace_cost = total_volumes * 0.11



def get_damage_books(collection_volumes):

    circulation_rate = random.randint(0, 1)
    damage_book = collection_volumes * circulation_rate // 100
    return damage_book
# print(get_damage_books(5000000))


# def get_attributes(num_of_titles):
#     '''
#     This is getting attributes of books, thickness and prices. The price will caculate randomly depedning on its thickness.
#     :param num_of_titles: Integer. a number of titles a librarian would like to purchase.
#     :return: DataFrame, columns are thickness and price.
#     >>> a = all_book(10)
#     >>> len(a)
#         10
#     >>> 20 < thickness_list < 50000
#     True
#     >>> 1 < price_list < 200
#     True
#
#     '''
#     pages_list = []
#     for i in range(num_of_titles): #np random
#         page = round(random.randint(10, 2000), 2)
#         pages_list.append(page)
#     print("This is the random pages:", pages_list)
#     thickness_list = []
#     for i in pages_list:
#         page_thickness = random.uniform(0.01, 0.05)
#         thickness = page_thickness * i
#         thickness_list.append(thickness)
#     # print("thickness_list", thickness_list)
#     price_list = []
#     for i in pages_list:
#         price1 = round(random.uniform(1, 40), 2)
#         price2 = round(random.uniform(40, 100), 2)
#         price3 = round(random.uniform(100, 200), 2)
#         if i <= 100:
#             # price1 = round(random.uniform(1, 40), 2)
#             price_list.append(price1)
#         elif 100 < i <= 400:
#             price_list.append(price2)
#         elif i > 400:
#             price_list.append(price3)
#     # print("This is the random price", price_list)
#     df = pd.DataFrame(data={'Thickness': thickness_list,
#                             'Price': price_list})
#     # print("This is the random book\n", df)
#     return df
#
# # print(get_attributes(10))
#
# def vendor_discount(num_of_titles):
#     '''
#     Discount percentage vendor will offer.
#     :param num_of_titles: Integer. A number of titles a librarian would like to purchase from a vendor
#     :return: float.
#     >>> vendor_discount(50)
#     0.01
#     >>> vendor_discount(280)
#     0.02
#     '''
#     if num_of_titles < 100:
#         return 0.01
#     elif 100 <= num_of_titles < 500:
#         return 0.02
#     elif num_of_titles >= 500:
#         return 0.05
#
#
# def price_solution(plan):
#     '''
#     A function for drop books from a list because of limited budget.
#     :param plan: Data Frame. A book list with thickness and price
#     :return: Data Frame excluding the book whose cost is the highest from the plan.
#     '''
#     drop = plan['Price'].max()
#     # print(drop)
#     new_plan = plan.loc[plan['Price'] != drop]
#     # print('This is the new book plan:\n', new_plan)
#     return new_plan
# # price_solution(all_book(20))
#
#
# def space_solution(plan):
#     '''
#     A function for dropping books from a list because of limited space
#     :param plan: Data Frame. A book list with thickness and price
#     :return: Data Frame, excluding the book whose space is the largest from the plan.
#     '''
#     drop = plan['Thickness'].max()
#     # print(drop)
#     new_plan = plan.loc[plan['Thickness'] != drop]
#     # print('This is the new book plan:\n', new_plan)
#     return new_plan
#
#
# def Monte(budget, space, num_of_titles, simulation):
#     final_num_books = []
#     final_prices = []
#     final_space = []
#     for i in range(simulation):
#         plan = get_attributes(num_of_titles)
#
#         total_price = plan['Price'].sum() * (1 - vendor_discount(num_of_titles))
#         total_space = plan['Thickness'].sum()
#         # print("This is the total price", total_price, type(total_price), type(plan['Price'].sum()), type(vendor_discount(num_of_titles)))
#         # print("This is the total space", total_space, type(total_space))
#         if total_price <= budget:
#             if total_space <= space:
#                 print('The plan is fine:')
#                 # plan = plan
#
#             elif total_space > space:
#                 print("The budget is enough, but we don't have enough space.\nThe new plan is:")
#                 while total_space > space:
#                     plan = space_solution(plan)
#                     total_space = plan['Thickness'].sum()
#
#         elif total_price > budget:
#             print("The budget is not enough.\nWe need a new plan.")
#             while total_price > budget:
#                 plan = price_solution(plan)
#                 total_price = plan['Price'].sum() * (1 - vendor_discount(num_of_titles))
#
#             if total_space <= space:
#                 print("The new plan is:")
#
#             elif total_space > space:
#                 print("The new plan has no enough space.\nChange it.")
#                 while total_space > space:
#                     plan = space_solution(plan)
#                     total_space = plan['Thickness'].sum()
#         total_num_book = len(plan.index)
#         final_num_books.append(total_num_book)
#         final_price = plan['Price'].sum()
#         # final_space = total_space
#         final_prices.append(final_price)
#         final_space.append(total_space)
#     final_plan = pd.DataFrame({'total_books': final_num_books, 'final_price': final_prices, 'final_space': final_space})
#
#
#     return final_plan
# # budget = int(input("please:" ))
# # space = int(input(": "))
# # number = int(input(":" ))
# # simulation = int(input(": "))
# if __name__ == '__main__':
#     total_books = []
#     mean_prices = []
#     mean_spaces = []
#     for i in range(30):
#         data = Monte(10000, 40000, 20, 5)
#         # data.append(data)
#         total_book = data['total_books'].mean()
#         total_books.append(total_book)
#         mean_price = data['final_price'].mean()
#         mean_prices.append(mean_price)
#         mean_space = data['final_space'].mean()
#         mean_spaces.append(mean_space)
#         simulation = pd.DataFrame({'total_purchase_book': total_books, 'app_price': mean_prices, 'app_space': mean_spaces})
#     print(simulation)
#
#
#
# # print(Monte(budget, space, number, simulation))
# # print(Monte(100000, 40000, 20, 5))









