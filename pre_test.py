import random
import numpy as np
import pandas as pd

# class acquisitions:
#
#     type = {'printed_book': 01, 'e-book': 02, 'Both': 03}
#
#
#     def __init__(self, type, price, thickness):
#         self.type = type
#         self.price = price
#         self.thickness = thickness
#
#     @classmethod
#     def get_attributes(cls):
#         if type == 'printed_book':
#             price = acquisitions.price[type]
#             thickness = acquisitions.thickness[type]
#         return type, price, thickness





def get_attributes(num_of_titles):

    thickness_list = []
    for i in range(num_of_titles):
        thickness = round(random.uniform(0.1, 20), 2)
        thickness_list.append(thickness)

    price_list = []
    for i in thickness_list:
        price1 = round(random.uniform(1, 50), 2)
        price2 = round(random.uniform(51, 100), 2)
        price3 = round(random.uniform(101, 200), 2)

        if i <= 5:
            price_list.append(price1)
        elif i > 5 and i <= 10:
            price_list.append(price2)
        else:
            price_list.append(price3)
    df = pd.DataFrame({'Thickness': thickness_list, 'Price': price_list})

    return df

# print(get_attributes(10))

def vendor_discount(num_of_titles):
    if num_of_titles <= 100:
        return 0.01
    elif 100 <  num_of_titles <= 500:
        return 0.02
    elif num_of_titles > 500:
        return 0.05

# space = [8, 3, 4, 6, 1]
# total = 0
# for i in space:
#     total =+ total + i
# print(total)
#
# if total > 20:
#     for i in range(len(space)):
#
#         cut_space = space[-i-1]
#         print(cut_space)
#         new_space = total - cut_space
#         if new_space < 20:
#             final_decision = new_space
# print(final_decision)

# def Monte(budget, num_of_titles, space):
num_of_titles = 10
space = 50
budget = 500
plan = get_attributes(num_of_titles)

total_price = plan['Price'].sum() * (1 - vendor_discount(num_of_titles))
total_space = plan['Thickness'].sum()
# plan.loc['total'] = plan[['Price', 'Thickness']].sum()

print(plan)
print(total_price)
# new_plan = plan.drop([3], axis = 0)
# print(new_plan)

while total_price > budget:
    # for i in range(len(plan)):
    plan = plan.drop(plan.tail(1), axis=0)
    total_price = plan['Price'].sum() * (1 - vendor_discount(num_of_titles))
    print(total_price)
    #     if total_price < budget:
    #         new_plan = plan
    # print(total_price)

# for i in range(len(plan)):
#     final_price = total_price - plan['Price'].max()
# print(final_price)

#     plan = plan.drop([i], axis= 0)
#     if i == 4:
#         new_plan = plan
#         total_price = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#         total_space = plan['Thickness'].sum()
# print(new_plan, total_price, total_space)


# finals = {}
# while total_price > budget:
#     for i in range(len(plan)):
#         plan = plan.drop([i], axis = 0)
#         print(plan)
#     if total_space < space:
#         finals['total_price'] = round(total_price, 2)
#         finals['total_space'] = round(total_space, 2)
#     elif total_space > space:
#         for i in range(len(plan)):
#             plan = plan.drop([i], axis = 0)
#             if plan['Thickness'].sum() < space:
#                 new_plan = plan
#                 finals['total_price'] = round(new_plan['Price'].sum(), 2)
#                 finals['total_space'] = round(new_plan['Thickness'].sum(), 2)
# print(finals)






# print(new_plan)
        # final_decision = total_price, total_space
#     elif total_space > space:
#         for i in range(len(plan)):
#             new_plan = plan.drop(plan.tail(i).index, inplace = True)
#             print(new_plan)
#             # cut_price = plan['Price'][i]
#             # new_price = (plan['Price'].sum() - cut_price) - ((plan['Price'].sum() - cut_price) * vendor_discount( - 1))
#             # cut_space = plan['Thickness'][i]
#             # new_space = plan['Thickness'].sum() - cut_space
#             # print(cut_price)
#             # new_price = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#             # new_space = plan['Thickness'].sum()
#             if new_plan['Thickness'].sum() < space:
#                 finals['total_price'] = new_plan['Price'].sum() - (new_plan['Price'].sum() * vendor_discount(num_of_titles))
#                 finals['total_space'] = plan['Thickness'].sum()
#         # print(plan['Price'][0])
#         # print(cut_price)
# elif total_price > budget:
#     if total_space < space:
#
#         for i in range(len(plan)):
#             plan = plan.drop(plan.tail(i).index, inplace=True)
#             # cut_price = plan['Price'][i]
#             # new_price = (plan['Price'].sum() - cut_price) - ((plan['Price'].sum() - cut_price) * vendor_discount( - 1))
#             # cut_space = plan['Thickness'][i]
#             # new_space = plan['Thickness'].sum() - cut_space
#             # print(cut_price)
#             # new_price = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#             # new_space = plan['Thickness'].sum()
#             if plan['Price'].sum() < space:
#                 finals['total_price'] = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#                 finals['total_space'] = plan['Thickness'].sum()
#         # print(plan['Price'][0])
#         # print(cut_price)
#
#     elif total_space > space:
#         for i in range(len(plan)):
#             plan = plan.drop(plan.tail(i).index, inplace=True)
#             # cut_price = plan['Price'][i]
#             # new_price = (plan['Price'].sum() - cut_price) - ((plan['Price'].sum() - cut_price) * vendor_discount( - 1))
#             # cut_space = plan['Thickness'][i]
#             # new_space = plan['Thickness'].sum() - cut_space
#             # print(cut_price)
#             # new_price = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#             # new_space = plan['Thickness'].sum()
#             if plan['Price'].sum() < space:
#                 finals['total_price'] = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#                 finals['total_space'] = plan['Thickness'].sum()
#         # print(plan['Price'][0])
#         # print(cut_price)

# final_decision = pd.DataFrame.from_dict(finals)

#     return finals




# def Monte(budget, num_of_titles, space):
#     plan = get_attributes(num_of_titles)
#     total_price = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#     total_space = plan['Thickness'].sum()
#
#     finals = {}
#     if total_price < budget:
#
#         if total_space < space:
#             finals['total_price'] = round(total_price, 2)
#             finals['total_space'] = round(total_space, 2)
#             # final_decision = total_price, total_space
#         elif total_space > space:
#             for i in range(len(plan)):
#                 new_plan = plan.drop(plan.tail(i).index, inplace = True)
#                 print(new_plan)
#                 # cut_price = plan['Price'][i]
#                 # new_price = (plan['Price'].sum() - cut_price) - ((plan['Price'].sum() - cut_price) * vendor_discount( - 1))
#                 # cut_space = plan['Thickness'][i]
#                 # new_space = plan['Thickness'].sum() - cut_space
#                 # print(cut_price)
#                 # new_price = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#                 # new_space = plan['Thickness'].sum()
#                 if new_plan['Thickness'].sum() < space:
#                     finals['total_price'] = new_plan['Price'].sum() - (new_plan['Price'].sum() * vendor_discount(num_of_titles))
#                     finals['total_space'] = plan['Thickness'].sum()
#             # print(plan['Price'][0])
#             # print(cut_price)
#     elif total_price > budget:
#         if total_space < space:
#
#             for i in range(len(plan)):
#                 plan = plan.drop(plan.tail(i).index, inplace=True)
#                 # cut_price = plan['Price'][i]
#                 # new_price = (plan['Price'].sum() - cut_price) - ((plan['Price'].sum() - cut_price) * vendor_discount( - 1))
#                 # cut_space = plan['Thickness'][i]
#                 # new_space = plan['Thickness'].sum() - cut_space
#                 # print(cut_price)
#                 # new_price = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#                 # new_space = plan['Thickness'].sum()
#                 if plan['Price'].sum() < space:
#                     finals['total_price'] = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#                     finals['total_space'] = plan['Thickness'].sum()
#             # print(plan['Price'][0])
#             # print(cut_price)
#
#         elif total_space > space:
#             for i in range(len(plan)):
#                 plan = plan.drop(plan.tail(i).index, inplace=True)
#                 # cut_price = plan['Price'][i]
#                 # new_price = (plan['Price'].sum() - cut_price) - ((plan['Price'].sum() - cut_price) * vendor_discount( - 1))
#                 # cut_space = plan['Thickness'][i]
#                 # new_space = plan['Thickness'].sum() - cut_space
#                 # print(cut_price)
#                 # new_price = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#                 # new_space = plan['Thickness'].sum()
#                 if plan['Price'].sum() < space:
#                     finals['total_price'] = plan['Price'].sum() - (plan['Price'].sum() * vendor_discount(num_of_titles))
#                     finals['total_space'] = plan['Thickness'].sum()
#             # print(plan['Price'][0])
#             # print(cut_price)
#
#     # final_decision = pd.DataFrame.from_dict(finals)
#
#     return finals



# print(Monte(5000000, 10, 8))


