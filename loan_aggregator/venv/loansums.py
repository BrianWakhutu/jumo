'''Read CSV, process and give aggregate data of loans/products'''

import csv
import pprint

def read_csv():
    '''
    Read the CSv
    '''
    csv_file = open('loans.csv')
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    return csv_reader


result = read_csv()

lines = []
networks = []
products = []
for each in result:
    lines.append(each)
    networks.append(each['Network'])
    products.append(each['Product'])
unique_networks = list(set(networks))
unique_products = list(set(products))
# print(unique_networks)
# print(unique_products)
# print(lines)

groups = {}
for line in lines:
    for network in unique_networks:
        if line['Network'] == network:
            if network not in groups:
                groups[str(network)] = [line]
            else:
                groups[str(network)].append(line)




for network in unique_networks:
    categories = {}
    print(network)
    for item in groups[network]:
        for product in unique_products:
            if item['Product'] == product:
                if product not in categories:
                    categories[str(product)] = float(item['Amount'])
                else:
                    k = categories[str(product)]
                    categories[str(product)] = k+float(item['Amount'])
    pprint.pprint(categories)
