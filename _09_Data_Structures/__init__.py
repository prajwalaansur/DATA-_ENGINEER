'''
inp_data = [['A', 1000, 'IT'], ['C', 3000, 'IT'], ['B', 2000, 'IT'], ['D', 4000, 'HR'], ['E', 2000, 'HR'],
            ['F', 1500, 'IT'], ['G', 7000, 'HR']]

output = []

sal = {}

for each in inp_data:
    if each[2] not in sal:
        sal[each[2]] = [(each[0], each[1])]
    else:
        sal[each[2]].append((each[0], each[1]))

for key, val in sal.items():
    sal[key] = sorted(val, key=lambda s: s[1])

for each in inp_data:
    for emp_name, salary in sal[each[2]]:
        if salary > each[1]:
            each.extend([salary, emp_name])
            output.append(each)
            break
    else:
        output.append(each)

print(output)
'''

'''
REQ:
Get highest sold out product of specific month
'''
data = {'A': [100, 80], 'B': [200, 140], 'C': [150, 100], 'D': [250, 230], 'E': [225, 215]}

months = {'A': [['Jan', 10], ['Mar', 2]],
          'E': ['Feb', 5],
          'C': ['Mar', 25],
          'D': ['Jan', 5],
          'B': ['Feb', 15]
         }


def get_highest(months, data):
    # I. Get profit of each product
    di = {}
    for p, sales in data.items():
        di[p] = sales[0] - sales[1]
    print("Profit of each product            : ", di)

    # II. Get month wise product profits
    fdi = {}
    for product, sales in months.items():
        if type(sales[0]) != list:
            p_profit = di[product] * sales[1]
            if sales[0] not in fdi.keys():
                fdi[sales[0]] = [[product, p_profit]]
            else:
                fdi[sales[0]].append([product, p_profit])
        else:
            for rec in sales:
                # print("RECORD : ", rec)
                p_profit = di[product] * rec[1]
                # print("DETAILS : ", product, rec[0], p_profit)
                if rec[0] not in fdi.keys():
                    fdi[rec[0]] = [[product, p_profit]]
                else:
                    fdi[rec[0]].append([product, p_profit])
    print("Monthwise product sales           : ", fdi)
    # III. Monthly wise highest sales
    monthly = {}
    p_max_sale = 0
    p_prod = None
    for month, sales in fdi.items():
        max_sale = 0
        prod = None
        for pr, val in sales:
            if val >= max_sale:
                max_sale = val
                prod = pr
            if val >= p_max_sale:
                p_max_sale = val
                p_prod = prod
        monthly[month] = [prod, max_sale]
    print("Monthly highest sales             : ", monthly)
    # IV. Highest sold out product details of all months
    high_val = 0
    high_prod = None
    month = None
    for mon, sales in monthly.items():
        if sales[1] > high_val:
            high_prod = sales[0]
            high_val = sales[1]
            month = mon
    print("Monthly highest sold product      : ", month, high_val, high_prod)
    print("Product wise highest sold in year : ", p_max_sale, p_prod)

get_highest(months, data)

'''
for product, price in data.items():
    m_prod = months[product]
    #print("Product ", m_prod)
    for each in m_prod:
        if type(each) != list:
            print(m_prod[1], price[0], price[1])
            profit = m_prod[1] * (price[0] - price[1])
            print("Details : ", m_prod, profit)
            if m_prod[0] not in di.keys():
                di[m_prod[0]] = [profit]
            else:
                di[m_prod[0]].append(profit)
            break
   
            if profit >= high_cost:
                high_cost= profit
                h_month = m_prod[0]
            break

        else:
            pass

            for each2 in each:
                print("EACGH :", each2)
                break
            '''
l = ['a','b','c','d','e','f','g']

for x in l:
    print(l[::2])
'''
[1, 3, 5, 7]
[1, 3, 5, 7]
[1, 3, 5, 7]
[1, 3, 5, 7]
[1, 3, 5, 7]
[1, 3, 5, 7]
[1, 3, 5, 7]
'''