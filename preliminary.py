import random
import numpy as np
import pandas as pd
import math


def labor_costs(annual_work_hour):
    '''
    This function get hourly labor costs from annual wages. The formulae is from the book.
    :param annual_work_hour: integer.
    :return: float which indicates hourly wage.
    >>> a = labor_costs(1950)
    >>> 50000 < benefit_rate < 70000
    True
    >>> 10 < a < 50
    True
    '''
    annual_wages = random.randint(50000, 70000)
    benefit_rate = random.uniform(0, 0.3)
    paid_off_hour = random.randint(0, 42)
    average_cost = (annual_wages + (annual_wages * benefit_rate)) / (annual_work_hour - paid_off_hour)
    return round(average_cost, 2)
# print(labor_costs(1950))

def maintenance_cost(annual_work_hour, total_volume):
    '''
    This function is to get annual maintenance cost from total volumes library houses and hourly labor costs.
    :param annual_work_hour: integer
    :param total_volume: integer
    :return: float indicates maintenance cost
    >>> maintenance_cost(1950, 45000)
    volumes_per_box =
    '''
    maintenance_time = annual_work_hour * 0.04
    volumes_per_box = math.ceil(total_volume / 25)
    maintenance_cost = volumes_per_box * maintenance_time
    return round(maintenance_cost, 2)
# print(maintenance_cost(1950, 50000))

def cataloging_cost(annual_work_hour):
    day_cataloging = random.randint(8, 12)
    daily_labor = labor_costs(annual_work_hour) * 8
    cost_per_book = daily_labor / day_cataloging
    return round(cost_per_book, 2)
# print(cataloging_cost(1950))

def get_book_list(num_of_titles, annual_work_hour):
    '''
    This is getting attributes of books, thickness and prices. The price will caculate randomly depedning on its thickness.
    :param num_of_titles: Integer. a number of titles a librarian would like to purchase.
    :return: DataFrame, columns are thickness and price.
    >>> a = all_book(10)
    >>> len(a)
        10
    >>> 20 < thickness_list < 50000
    True
    >>> 1 < price_list < 200
    True

    '''
    cost_per_book = cataloging_cost(annual_work_hour)
    pages = np.random.randint(10, 2000, size=num_of_titles)
    page_thickness = random.uniform(0.01, 0.05)
    thickness = np.around(page_thickness * pages, decimals=2)
    page_price = random.uniform(0.01, 0.1)
    price = np.around(page_price * pages, decimals=2)
    # Three types of demand indicates 3 is high, 2 medium, and 1 low.
    demand_list = ['1', '2', '3']
    demands = []
    for i in range(num_of_titles):
        demand = random.choice(demand_list)
        # print(demand)
        demands.append(demand)

    df = pd.DataFrame(data={'Thickness': thickness,
                            'Price': price,
                            'Demands': demands,
                            'cataloging_cost': cost_per_book})
    return df

# print(get_book_list(10, 1950))

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
budget = 1000
space = 500
plan = get_book_list(10, 1950)
print('This is plan \n\n', plan, '\n')
# def select_book(plan, space, budget):
select_plan = plan.copy(deep=True)
select_plan['Total_cost_per_book'] = select_plan['Price'] + select_plan['cataloging_cost']
print('This is select plan\n\n', select_plan, '\n')

select_plan[['cost_accumulate', 'Total_thickness']] = select_plan[['Total_cost_per_book', 'Thickness']].cumsum().where(lambda x: x <= budget).where(lambda x: x <= space)
acquisition

print('newplan\n\n', select_plan)
    # print(space_plan)
    # acquisitions = select_plan.dropna()
    # print(thick_acquisitions)
#     return acquisitions
# a = get_book_list(10, 1950)
# print(select_book(a, 100, 1000))

# def cost_consider(plan, space, budget):
#
#     # plan['Price'] = plan['Price'] * (1 - vendor_discount(num_of_titles))
#     cost_plan = plan.copy(deep=True)
#     cost_plan[['Total_price', 'Total_thickness']] = cost_plan[['Price', 'Thickness']].cumsum().where(lambda x: x <= budget).where(lambda x: x <= space)
#     cost_acquisitions = cost_plan.dropna()
#     print(cost_acquisitions)
#     return cost_acquisitions
# print('This is testing\n\n', cost_consider(a, 100, 100))

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

# def MonteCarloSimulation(annual_work_hour, total_volume, budget, space, num_of_titles):
#     # acquisition_budget = budget - maintenance_cost(annual_work_hour, total_volume) - cataloging_cost(num_of_books, annual_work_hour)
# num_of_titles = 10
# budget = 100
# space = 100
# annual_work_hour = 1950
#
# book_list = get_book_list(num_of_titles)
# print('booklist\n\n', book_list)
# plan = book_list.sort_values(by='Demands', ascending=False)
# print('plansorted\n\n', plan)
# cost_list = cost_consider(plan, budget)
# print('costcase\n\n', cost_list)
# if cost_list['Thickness'].sum() > space:
#     purchase_list = cost_list
# else:
#     purchase_list = space_consider(plan, budget)
# print('final\n\n', purchase_list)



# space_list = space_consider(plan, budget)
# print('spacecase\n\n', space_list)
# cost_list = cost_consider(plan, budget)
# cost_list = cataloging_cost(plan, budget)
# num_books = cost_list['Price'].count()
# cataloging_budget = cataloging_cost(num_books, annual_work_hour)
# remain = budget - cost_list['Price'].sum()
    # if cataloging_budget > remain:

    # result_demand = cost_consider(plan, budget)
    # result_demand = space_consider(plan, space)
    # num_of_books = result_demand['Price'].count()



    # plan1 = book_list.sort_values(by='Price', ascending=True)
    #
    # resutla = space_consider(plan, num_of_titles, space)
    # print('a\n\n', resutla)
    # resutlb = cost_consider(plan, annual_work_hour, total_volume, budget, num_of_titles)
    # print('b\n\n', resutlb)
    #
    # # result1 (price sum howmany bookcount, thickness sum)
    #
    # return resutla, resutlb





    # acquisition_budget = budget - maintenance_cost(annual_work_hour, total_volume) - cataloging_cost(num_of_titles, annual_work_hour)
    # print(acquisition_budget)
    #

    # print(plan)
    #
    # if plan['Thickness'].sum() != 0:
    #     plan['Price'] = plan['Price'] * (1 - vendor_discount(num_of_titles))
    #     plan['Total_thickness'] = plan['Thickness'].cumsum().where(lambda x: x <= space)
    #     thick_acquisitions = plan.dropna()
    #     print('thick case\n', thick_acquisitions)
    # if plan['Price'].sum() != 0:
    #     plan['Price'] = plan['Price'] * (1 - vendor_discount(num_of_titles))
    #     plan['Total_price'] = plan['Price'].cumsum().where(lambda x: x <= acquisition_budget)
    #     cost_acquisitions = plan.dropna()
    #     print('price case\n', cost_acquisitions)
    # # df = pd.DataFrame({'thick': thick_acquisitions, 'cost': cost_acquisitions})

    # return thick_acquisitions, cost_acquisitions
# annual_work_hour, total_volume, budget, space, num_of_titles
# a = MonteCarloSimulation(1950, 500000, 3000000, 30000, 100000)
# print('result\n', a)
# print(a.count())

#
# if __name__ == '__main__':
#
#     data = MonteCarloSimulation(1950, 500000, 3000000, 300, 1000)
#     print(data)
#     nums = []
#     total_costs = []
#     total_thickness = []
#     for i in range(30):
#         num_purchase_book = data['Price'].count()
#         total_price = data['Price'].sum()
#         all_thickness = data['Thickness'].sum()
#         nums.append(num_purchase_book)
#         total_costs.append(total_price)
#         total_thickness.append(all_thickness)
#     simulation = pd.DataFrame({'total_purchase_book': nums, 'app_price': total_costs, 'app_space': total_thickness})
#
#     print(simulation)

