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

def select_book(plan, budget, space):

    # print('This is plan \n\n', plan, '\n')
    # def select_book(plan, space, budget):
    select_plan = plan.copy(deep=True)
    select_plan['total_cost_per_book'] = select_plan['Price'] + select_plan['cataloging_cost']
    print('This is select plan\n\n', select_plan, '\n')
    select_plan['cost_accumulate'] = select_plan['total_cost_per_book'].cumsum().where(lambda x: x <= budget)
    print('thisi is price\n\n', select_plan)
    select_plan['Total_thickness'] = select_plan['Thickness'].cumsum().where(lambda x:x <= space)
    print('This is thickness\n\n', select_plan)
    acquisitions = select_plan.dropna()
    return acquisitions



def MonteCarloSimulation(annual_work_hour, total_volume, budget, space, num_of_titles):
    acquisition_budget = budget - maintenance_cost(annual_work_hour, total_volume)


    plan = get_book_list(num_of_titles, annual_work_hour)


    demand_order = plan.sort_values(by='Demands', ascending=False)
    price_order = plan.sort_values(by='Price', ascending=True)

    demand_acquisition = select_book(demand_order, acquisition_budget, space)
    price_acquisition = select_book(price_order, acquisition_budget, space)

    demand_book = demand_acquisition['Price'].count()
    demand_cost = round(demand_acquisition['total_cost_per_book'].sum() * (1 - vendor_discount(demand_book)), 2)
    demand_thickness = demand_acquisition['Thickness'].sum()

    price_book = price_acquisition['Price'].count()
    price_cost = round(price_acquisition['total_cost_per_book'].sum() * 1 - vendor_discount(price_book), 2)
    price_thickness = price_acquisition['Thickness'].sum()

    print(demand_book, demand_cost, demand_thickness, price_book, price_cost, price_thickness)
    # print(price_acquisition)

    return demand_book, demand_cost, demand_thickness, price_book, price_cost, price_thickness

print(MonteCarloSimulation(1950, 50000, 1000000000, 10000, 100000))



if __name__ == '__main__':



    demand_book = []
    demand_cost = []
    demand_thickness = []
    price_book = []
    price_cost = []
    price_thickness = []
    a = []
    for i in range(2):
        b = MonteCarloSimulation(1950, 50000, 1000000000, 10000, 100000)
        a.append(b)
    print(a)

    #     num_purchase_book = data['Price'].count()
    #     total_price = data['Price'].sum()
    #     all_thickness = data['Thickness'].sum()
    #     nums.append(num_purchase_book)
    #     total_costs.append(total_price)
    #     total_thickness.append(all_thickness)
    # simulation = pd.DataFrame({'total_purchase_book': nums, 'app_price': total_costs, 'app_space': total_thickness})
    #
    # print(simulation)

