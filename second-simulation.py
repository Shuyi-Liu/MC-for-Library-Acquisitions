import random
import numpy as np
import pandas as pd
import math


def labor_costs(annual_work_hour):
    """
    This function calculates the hourly wage of a cataloger. The formulae is from the reference book.
    The annual wage is randomly selected from a wage range.
    Paid off hours are the hours that a cataloger does not work but still get payments.
    :param annual_work_hour: integer. A cataloger's annual work hours.
    :return: float. A cataloger's hourly wage.
    >>> 50000 <= annual_wages <= 70000
    True
    >>> 0 <= benefit_rate < 0.3
    True
    >>> 0<= paid_off_hour <= 42
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
    This function calculates an annual maintenance cost of the total collections in a library.
    The maintenance cost is calculated from the labor cost and the volume of collections.
    :param annual_work_hour: integer. A cataloger's annual work hours.
    :param total_volume: integer. The total collections in a library.
    :return: float. The maintenance cost.
    >>> maintenance_cost(1950, 50000)
    156000.0
    """
    maintenance_fee = labor_costs(annual_work_hour) * 0.04
    volumes_per_box = math.ceil(total_volume / 25)
    maintenance_total = volumes_per_box * maintenance_fee
    return round(maintenance_total, 2)


# print(maintenance_cost(1950, 50000))


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


def get_price(num_of_titles):
    """

    :param num_of_titles:
    :return:
    """
    pages = np.random.randint(10, 2000, size=num_of_titles)
    page_price = random.uniform(0.01, 0.1)
    price = np.around(page_price * pages, decimals=2)
    return price


print(get_price(20))


def get_book_list(num_of_titles, annual_work_hour):
    """
    This function generates a list of books that are randomly selected in pages, page thickness, price, and demand level.
    :param num_of_titles: Integer. the number of books that a random book list contains. a librarian will purchase books from it.
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
    >>> 0.1 <= price < 200
    True
    """
    cost_per_book = cataloging_cost(annual_work_hour)
    pages = np.random.randint(10, 2000, size=num_of_titles)
    page_thickness = np.random.uniform(0.01, 0.05, size=num_of_titles)
    thickness = np.around(page_thickness * pages, decimals=2)
    price = get_price(num_of_titles)
    # Three types of demand indicates 3 is high, 2 medium, and 1 low.
    demand_list = [1, 2, 3]
    demands = []
    for i in range(num_of_titles):
        demand = random.choice(demand_list)
        # print(demand)
        demands.append(demand)

    df = pd.DataFrame(data={'Thickness': thickness,
                            'Price': price,
                            'Demand': demands,
                            'cataloging cost': cost_per_book})
    return df


print(get_book_list(10, 1950))


def get_ebook_list(num_of_titles, annual_work_hour):
    """
    This function generates a list of ebooks that are randomly selected in pages, prices, demand level, and contract type.
    :param num_of_titles: Integer. the number of ebooks that a random ebook list contains. a librarian will purchase ebooks from it.
    :param annual_work_hour: Integer. a cataloger's annual total work hours in general.
    :return: DataFrame. the columns are price of printed version, demand level, contract type, ebook price, and cataloging cost.
    True
    >>> 0.1 <= printed_price < 200
    True
    >>> 0.13<= contract_price_1 < 260
    True
    >>> 0.195 <= contract_price_2 < 390
    True
    >>> 0.26 <= contract_price_3 < 520
    True
    """
    cost_per_book = cataloging_cost(annual_work_hour)
    printed_price = get_price(num_of_titles)
    demand_list = [1, 2, 3]
    demand_select = []
    high_demand_contract = [3, 2]
    mid_demand_contract = [2, 1]
    contract_price_1 = 1.3
    contract_price_2 = 1.3 * 1.5
    contract_price_3 = 1.3 * 2
    contract_select = []
    price_select = []
    for i in range(num_of_titles):
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


def vendor_discount(num_book_buy):
    """
    This function calculates the percentage of discount that a vendor will offer based on how many books you purchase.
    :param num_book_buy: Integer. A number of books that a librarian will purchase.
    :return: float.
    >>> vendor_discount(1000)
    0.05
    >>> vendor_discount(280)
    0.02
    >>> vendor_discount(50)
    0.01
    """
    if num_book_buy < 100:
        return 0.01
    elif 100 <= num_book_buy < 500:
        return 0.02
    elif num_book_buy >= 500:
        return 0.05


print(vendor_discount(280))


book_plan = get_book_list(1000, 1950)
ebook_plan = get_ebook_list(1000, 1950)
book_demand_order = book_plan.sort_values(by='Demand', ascending=False)
book_price_order = book_plan.sort_values(by='Price', ascending=True)
ebook_demand_order = ebook_plan.sort_values(by='Demand', ascending=False)
ebook_price_order = ebook_plan.sort_values(by='Ebook Price', ascending=True)


def select_book(order, book_budget, space):
    """
    This function selects the books from the book list that generated by "get_book_list" function.
    This function will select books from the fist row till the row that meets the budget and space limitations.
    :param order: Data Frame. The list we will select from.
    :param book_budget: integer. A Library's annual budget for acquisitions.
                            The budget also includes the cost of cataloging and maintenance.
    :param space: integer. Available shelf space.
    :return: Data Frame. The list of books we select for purchasing.
    >>> plan = get_book_list(10, 1950)
    >>> a = select_book(plan, 1000, 500)
    >>> a.isnull().values.any()
    False
    """
    select_plan = order.copy(deep=True)
    select_plan['total_cost_per_book'] = select_plan['Price'] + select_plan['cataloging cost']
    select_plan['cost_accumulate'] = select_plan['total_cost_per_book'].cumsum().where(lambda x: x <= book_budget)
    select_plan['Total_thickness'] = select_plan['Thickness'].cumsum().where(lambda x:x <= space)
    acquisitions = select_plan.dropna()
    return acquisitions


print(select_book(book_demand_order, 20000, 50000))
print(select_book(book_price_order, 20000, 50000))


def select_ebook(order, ebook_budget):
    """

    :param order:
    :param ebook_budget:
    :return:
    """
    select_plan = order.copy(deep=True)
    select_plan['total_cost_per_ebook'] = select_plan['Ebook Price'] + select_plan['cataloging cost']
    select_plan['cost_accumulate'] = select_plan['total_cost_per_ebook'].cumsum().where(lambda x: x <= ebook_budget)
    acquisitions = select_plan.dropna()
    return acquisitions


print(select_ebook(ebook_demand_order, 20000))
print(select_ebook(ebook_price_order, 20000))


def MonteCarloSimulation(annual_work_hour, total_volume, budget, space, num_of_titles, book_rate, ebook_rate) -> list:
    """
    This function an MC simulation for acquisitions. There are two strategies for getting books:
    1. Meet the users' demands first. (Buy resources with high demand.)
    2. Buy as many books as possible in a budget and space.
    :param annual_work_hour: integer. a cataloger's annual total work hours in general.
    :param total_volume: integer. The total collections in a library.
    :param budget: integer. The budget for purchasing books and ebooks.
                   It includes the cataloging fee and maintenance cost.
    :param space: integer. Available shelf space.
    :param num_of_titles: integer
    :param book_rate:
    :param ebook_rate:
    :return: list which contains number of books, costs, and thickness of both users' demand and expansion of volumes of collection (considering book price at first)
    """
    acquisition_budget = budget - maintenance_cost(annual_work_hour, total_volume)
    book_budget = acquisition_budget * book_rate
    ebook_budget = acquisition_budget * ebook_rate

    book_plan = get_book_list(num_of_titles, annual_work_hour)
    ebook_plan = get_ebook_list(num_of_titles, annual_work_hour)

    book_demand_order = book_plan.sort_values(by='Demand', ascending=False)
    book_price_order = book_plan.sort_values(by='Price', ascending=True)
    ebook_demand_order = ebook_plan.sort_values(by='Demand', ascending=False)
    ebook_price_order = ebook_plan.sort_values(by='Ebook Price', ascending=True)

    ebook_demand_acquisition = select_ebook(ebook_demand_order, ebook_budget)
    ebook_price_acquisition = select_ebook(ebook_price_order, ebook_budget)
    book_demand_acquisition = select_book(book_demand_order, book_budget, space)
    book_price_acquisition = select_book(book_price_order, book_budget, space)

    book_demand_num = book_demand_acquisition['Price'].count()
    book_demand_cost = round(book_demand_acquisition['total_cost_per_book'].sum() * (1 - vendor_discount(book_demand_num)), 2)
    book_demand_thickness = math.ceil(book_demand_acquisition['Thickness'].sum())
    ebook_demand_num = ebook_demand_acquisition['Ebook Price'].count()
    ebook_demand_cost = round(ebook_demand_acquisition['total_cost_per_ebook'].sum(), 2)

    book_price_num = book_price_acquisition['Price'].count()
    book_price_cost = round(book_price_acquisition['total_cost_per_book'].sum() * (1 - vendor_discount(book_price_num)), 2)
    book_price_thickness = math.ceil(book_price_acquisition['Thickness'].sum())
    ebook_price_num = ebook_price_acquisition['Ebook Price'].count()
    ebook_price_cost = round(ebook_price_acquisition['total_cost_per_ebook'].sum(), 2)

    sim_data = [book_demand_num, book_demand_cost, book_demand_thickness, book_price_num, book_price_cost, book_price_thickness,
                ebook_demand_num, ebook_demand_cost, ebook_price_num, ebook_price_cost]

    print('The Book Demand Strategic:\n',
          'Purchase amount:', book_demand_num, '\n',
          'Total Price:', book_demand_cost, '\n',
          'Total Thickness:', book_demand_thickness, '\n',
          '\n',
          'The E-book Demand Strategic:\n',
          'Purchase amount:', ebook_demand_num, '\n',
          'Total Price:', ebook_demand_cost, '\n',
          '\n\n',
          'The Book Price Strategic:\n',
          'Purchase amount:', book_price_num, '\n',
          'Total Price:', book_price_cost, '\n',
          'Total Thickness:', book_price_thickness, '\n',
          '\n',
          'The E-book Price Strategic:\n',
          'Purchase amount:', ebook_price_num, '\n',
          'Total Price:', ebook_price_cost)

    return sim_data


MonteCarloSimulation(1950, 50000, 20000, 50000, 1000, 0.5, 0.5)
# print(MonteCarloSimulation(1950, 50000, 20000, 50000, 1000, 0.5, 0.5))
