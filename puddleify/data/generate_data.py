
# We use this to generate datasets to train on!

# Let's generate some data in a csv to train our model on

# the dataset will have 12 attributes per item

import pandas
import random
import string
import decimal
import datetime

class Dataset:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.features = ["amount", "category", "date", "name", "orginal_description", "address", "city", "lat", "lon", "state", "zip"]
        self.dataset = []

    def rand_amount(self):
        ''' generates a random amount between $2 and $250 '''
        amount = float(decimal.Decimal(random.randrange(200, 25000))/100)
        return float(amount)
    
    def rand_category(self):
        ''' generates random categories '''
        categories = ['Toy', 'Grocery', 'Furniture', 'Auto', 'Loan', 'Shops', 'Computer Electronics', 'Food', 'Home Goods', 'Candy', 'Laundry', 'Rent']
        category = random.choice(categories)
        return str(category)
    
    def rand_date(self):
        start = datetime.datetime.now()
        end = start + datetime.timedelta(days=365)
        random_date = start + (end - start) * random.random()
        return random_date
    
    def rand_name(self):
        names = ["Safeway", "Albertsons", "Kroger's", "Ralphs", "Best Buy", "Micro Center", "Pizza My Heart", "Veggie Grill", "Car Wash Classic", "7 Eleven"]
        name = random.choice(names)
        return str(name)
    
    def rand_description(self):
        description = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        return str(description)
    
    def rand_address(self):
        addy = random.choice(["555 Post Street", '''123 nowhere street''', '''229 asdfjk drive''', '''1234 woot street'''])
        return str(addy)
    
    def rand_city(self):
        city = random.choice(["San Francisco", "Berkeley", "Los Angeles", "New York", "Philadelphia", "Boston"])
        return str(city)
    
    def rand_lat(self):
        lat = random.randint(1, 100)
        return int(lat)
    
    def rand_lon(self):
        lat = random.randint(1, 100)
        return str(lat)
    
    def rand_state(self):
        state = random.choice(["CA", "TX", "OR", "NV", "FL", "NY", "WY"])
        return str(state)
    
    def rand_zip(self):
        zip = ''.join(random.randint(1, 10) for _ in range(5))
        return int(zip)
    
    def fill_dataset(self):
    
        for j in range(self.rows):
            for i in range(self.columns):
                the_row = []
                the_row.append(self.rand_amount())
                the_row.append(self.rand_category())
                the_row.append(self.rand_date())
                the_row.append(self.rand_name())
                the_row.append(self.rand_description())
                the_row.append(self.rand_address())
                the_row.append(self.rand_city())
                the_row.append(self.rand_lat())
                the_row.append(self.rand_lon())
                the_row.append(self.rand_state())
                the_row.append(self.rand_zip())
                self.dataset.append(the_row)

        for index, item in enumerate(self.dataset):
            print(index, item)

        return
             
    def dataset_to_csv(self, name):
        ''' save dataset to a csv '''
        if len(self.dataset) < 1:
            print("create dataset")
            return
        df = pd.DataFrame(self.dataset)
        df.to_csv(name+'.csv')
        return    
    
        
        
        
        
        