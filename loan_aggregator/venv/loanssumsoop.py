'''Read CSV, process and give aggregate data of loans/products'''
import csv


class Processor():
    '''Processing loans data to aggregate from networks and loans'''
    def __init__(self):
        self.in_file_location = 'loans.csv'
        self.out_file_location = 'Output.csv'
        self.unique_networks = None
        self.unique_products = None
        self.csv_file = None

    def read_csv(self):
        '''Read the CSv'''
        self.csv_file = open(self.in_file_location)
        csv_reader = csv.DictReader(self.csv_file, delimiter=',')
        return csv_reader

    def aggregate_networks(self):
        '''Aggregate to group by Networks'''
        csv_data = self.read_csv()
        lines = []
        networks = []
        products = []
        for row in csv_data:
            lines.append(row)
            networks.append(row['Network'])
            products.append(row['Product'])
        self.unique_networks = list(set(networks))
        self.unique_products = list(set(products))
        groups = {}
        for line in lines:
            for network in self.unique_networks:
                if line['Network'] == network:
                    if network not in groups:
                        groups[str(network)] = [line]
                    else:
                        groups[str(network)].append(line)
        return groups

    def aggregate_product(self, groups):
        '''Aggregate products within groups to group and total loans'''
        product_categories = []
        for network in self.unique_networks:
            categories = {}
            categories['Network'] = network
            for item in groups[network]:
                for product in self.unique_products:
                    if item['Product'] == product:
                        if product not in categories:
                            categories[str(product)] = float(item['Amount'])
                            categories[str(product) + '_count'] = 1
                        else:
                            amount = categories[str(product)]
                            count = categories[str(product)+'_count']
                            categories[str(product)] = amount + \
                                    float(item['Amount'])
                            categories[str(product)+'_count'] = count + 1
            product_categories.append(categories)
        return product_categories

    def __del__(self):
        self.csv_file.close()

if __name__ == "__main__":
    AGGREGATOR = Processor()
    AGGREGATED_NETWORKS = AGGREGATOR.aggregate_networks()
    AGGREGATED_PRODUCTS = AGGREGATOR.aggregate_product(AGGREGATED_NETWORKS)
    print(AGGREGATED_PRODUCTS)