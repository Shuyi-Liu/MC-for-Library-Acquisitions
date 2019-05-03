"""
Simulation for Library Acquisitions.
This program is to simulate to buy "printed books" in a library. The purpose of the simulation program is to help librarian's desicion making for acquisitions.
This program considers two limited condition: budget and space.
This program considers two possible factors that impact the librarian's making decision for acquisitions: users' demands and expansion of volumes of collections.

IS590PR by Professor John Weible
"""
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
    >>> type(a)
    <class 'float'>
    >>> 10 < a < 50
    True
    '''
    annual_wages = random.randint(50000, 70000)
    benefit_rate = random.uniform(0, 0.3)
    paid_off_hour = random.randint(0, 42)
    average_cost = (annual_wages + (annual_wages * benefit_rate)) / (annual_work_hour - paid_off_hour)
    return round(average_cost, 2)


def maintenance_cost(annual_work_hour, total_volume):
    '''
    This function is to get annual maintenance cost from total volumes library houses and hourly labor costs.
    :param annual_work_hour: integer
    :param total_volume: integer
    :return: float indicates maintenance cost
    >>> cost = maintenance_cost(1950, 45000)
    >>> type(cost)
    <class 'float'>
    >>> cost < 50000
    True
    '''
    maintenance_labor = labor_costs(annual_work_hour) * 0.04
    volumes_per_box = math.ceil(total_volume / 25)
    maintenance_cost = volumes_per_box * maintenance_labor
    return round(maintenance_cost, 2)


def cataloging_cost(annual_work_hour):
    '''
    This functions is to calculate cataloging cost per a book. A cataloger can catalog books between 8 and 12 a day. The function randomly choose a catalog's capacity. Based on labor costs, the function caculates a cataloging cost per a book.
    :param annual_work_hour: integer
    :return: float.
    >>> a = cataloging_cost(1950)
    >>> 20 < a < 50
    True
    >>> 50 < a < 100
    False
    '''
    day_cataloging = random.randint(8, 12)
    daily_labor = labor_costs(annual_work_hour) * 8
    cost_per_book = daily_labor / day_cataloging
    return round(cost_per_book, 2)


def get_book_list(num_of_titles, annual_work_hour):
    '''
    This is getting attributes of books, thickness and prices. The price will caculate randomly depedning on its thickness.
    :param num_of_titles: Integer. a number of titles a librarian would like to purchase.
    :return: DataFrame, columns are thickness and price.
    >>> a = get_book_list(10, 1950)
    >>> a.count()
    Thickness          10
    Price              10
    Demands            10
    cataloging_cost    10
    dtype: int64
    >>> 10 * 0.01 < a['Thickness'][0] < 2000 * 0.05
    True
    >>> 10 * 0.01 < a['Price'][0] < 2000 * 0.1
    True
    '''
    cost_per_book = cataloging_cost(annual_work_hour)
    pages = np.random.randint(10, 2000, size=num_of_titles)
    page_thickness = np.random.uniform(0.01, 0.05, size=num_of_titles)
    thickness = np.around(page_thickness * pages, decimals=2)
    page_price = np.random.uniform(0.01, 0.1, size=num_of_titles)
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
    '''
    Select books from the book list generated "get book list" function based on budget and space.
    :param plan: Data Frame
    :param budget: integer. A Library's annual budget for acuiqisionts including cataloging and maintenance consts.
    :param space: integer. Available shelf space.
    :return: Data Frame for possible purchasing books.
    >>> plan = get_book_list(10, 1950)
    >>> a = select_book(plan, 1000, 500)
    >>> a.isnull().values.any()
    False
    '''
    select_plan = plan.copy(deep=True)
    select_plan['total_cost_per_book'] = select_plan['Price'] + select_plan['cataloging_cost']

    select_plan['cost_accumulate'] = select_plan['total_cost_per_book'].cumsum().where(lambda x: x <= budget)

    select_plan['Total_thickness'] = select_plan['Thickness'].cumsum().where(lambda x:x <= space)

    acquisitions = select_plan.dropna()
    return acquisitions


def MonteCarloSimulation(annual_work_hour, total_volume, budget, space, num_of_titles) -> list:
    '''
    This function an MC simulation for acquisitions. There are two stragegies for getting books: users' demands and number of books as many as possible in a budget and space.
    :param annual_work_hour: integer
    :param total_volume: integer
    :param budget: float
    :param space: float
    :param num_of_titles: integer
    :return: list which contains number of books, costs, and thickness of both users' demand and expansion of volumes of collection (considering book price at first)
    >>> list = MonteCarloSimulation(1950, 50000, 1000000000, 10000, 100000)
    >>> len(list)
    6
    >>> list[0] < 100000
    True
    >>> list[3] < 100000
    True
    '''
    acquisition_budget = budget - maintenance_cost(annual_work_hour, total_volume)

    plan = get_book_list(num_of_titles, annual_work_hour)

    demand_order = plan.sort_values(by='Demands', ascending=False)
    price_order = plan.sort_values(by='Price', ascending=True)

    demand_acquisition = select_book(demand_order, acquisition_budget, space)
    price_acquisition = select_book(price_order, acquisition_budget, space)

    demand_book = demand_acquisition['Price'].count()
    demand_cost = round(demand_acquisition['total_cost_per_book'].sum() * (1 - vendor_discount(demand_book)), 2)
    demand_thickness = math.ceil(demand_acquisition['Thickness'].sum())

    price_book = price_acquisition['Price'].count()
    price_cost = round(price_acquisition['total_cost_per_book'].sum() * (1 - vendor_discount(price_book), 2))
    price_thickness = math.ceil(price_acquisition['Thickness'].sum())

    sim_data = [demand_book, demand_cost, demand_thickness, price_book, price_cost, price_thickness]

    return sim_data


if __name__ == '__main__':


    data = []
    for i in range(100):
        list = MonteCarloSimulation(1950, 50000, 1000000000, 10000, 100000)
        data.append(list)
    simulation_result = pd.DataFrame(data, columns=['num_of_books_by_demand',
                                                     'total_cost_by_demand',
                                                     'total_thickness_by_demand',
                                                     'num_of_books_by_price',
                                                     'total_cost_by_price',
                                                     'total_thickness_by_price'])
    print(simulation_result)
