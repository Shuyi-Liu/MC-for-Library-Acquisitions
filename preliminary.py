import random
import numpy as np
import pandas as pd
import math


def labor_costs(annual_work_hour):
    annual_wages = random.randint(50000, 70000)
    benefit_rate = random.uniform(0, 0.3)
    paid_off_hour = random.randint(0, 42)
    average_cost = (annual_wages + (annual_wages * benefit_rate)) / (annual_work_hour - paid_off_hour)
    return round(average_cost, 2)
# print(labor_costs(1950))

def maintenance_cost(annual_work_hour, total_volume):
    maintenance_time = annual_work_hour * 0.04
    volumes_per_box = math.ceil(total_volume / 25)
    maintenance_cost = volumes_per_box * maintenance_time
    return round(maintenance_cost, 2)
# print(maintenance_cost(1950, 50000))

def cataloging_cost(num_of_titles, annual_work_hour):
    hourly_cataloging_items = math.ceil(num_of_titles / random.randint(10, 12))
    labor_cost = labor_costs(annual_work_hour) * hourly_cataloging_items
    return round(labor_cost, 2)
# print(cataloging_cost(100, 1950))

def get_attributes(num_of_titles):
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

    pages = np.random.randint(10, 2000, size=num_of_titles)
    page_thickness = random.uniform(0.01, 0.05)
    thickness = np.around(page_thickness * pages, decimals=2)
    page_price = random.uniform(0.01, 0.1)
    price = np.around(page_price * pages, decimals=2)
    demand_list = ['1', '2', '3']
    demands = []
    for i in range(num_of_titles):
        demand = random.choice(demand_list)
        # print(demand)
        demands.append(demand)

    df = pd.DataFrame(data={'Thickness': thickness,
                            'Price': price,
                            'Demands': demands})
    return df

# print(get_attributes(10))

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


def MonteCarloSimulation(annual_work_hour, total_volume, budget, space, num_of_titles):
    acquisition_budget = budget - maintenance_cost(annual_work_hour, total_volume) - cataloging_cost(num_of_titles, annual_work_hour)
    # print(acquisition_budget)

    plan = get_attributes(num_of_titles)
    plan = plan.sort_values(by='Demands', ascending=False)
    print(plan)

    if num_of_titles > 100:
        plan['Price'] = plan['Price'] * (1 - vendor_discount(num_of_titles))
        plan['Total_price'] = plan['Price'].cumsum().where(lambda x: x <= acquisition_budget)
        plan['Total_thickness'] = plan['Thickness'].cumsum().where(lambda x: x <= space)
        acquisitions = plan.dropna()
    else:
        plan['Total_price'] = plan['Price'].cumsum().where(lambda x: x <= acquisition_budget)
        plan['Total_thickness'] = plan['Thickness'].cumsum().where(lambda x: x <= space)
        acquisitions = plan.dropna()
        print(acquisitions)

    return acquisitions

a = MonteCarloSimulation(1950, 500000, 3000000, 300, 150)
print(a)
print(a.count())


if __name__ == '__main__':

    data = MonteCarloSimulation(1950, 500000, 3000000, 300, 150)
    print(data)
    nums = []
    total_costs = []
    total_thickness = []
    for i in range(30):
        num_purchase_book = data['Price'].count()
        total_price = data['Price'].sum()
        all_thickness = data['Thickness'].sum()
        nums.append(num_purchase_book)
        total_costs.append(total_price)
        total_thickness.append(all_thickness)
    simulation = pd.DataFrame({'total_purchase_book': nums, 'app_price': total_costs, 'app_space': total_thickness})

    print(simulation)

