
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
        return amount
    
    def rand_category(self):
        ''' generates random categories '''
        categories = ['Toy', 'Grocery', 'Furniture', 'Auto', 'Loan', 'Shops', 'Computer Electronics', 'Food', 'Home Goods', 'Candy', 'Laundry', 'Rent']
        category = random.choice(categories)
        return category
    
    def rand_date(self):
        start = datetime.datetime.now()
        end = start + datetime.timedelta(days=365)
        random_date = start + (end - start) * random.random()
        return random_date
    
    def rand_name(self):
        names = ["Safeway", "Albertsons", "Kroger's", "Ralphs", "Best Buy", "Micro Center", "Pizza My Heart", "Veggie Grill", "Car Wash Classic", "7 Eleven"]
        name = random.choice(names)
        return name
    
    def rand_description(self):
        description = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        return description
    
    def rand_address(self):
        we_just_gonna_use_one = "555 Post Street"
        return we_just_gonna_use_one
    
    def rand_city(self):
        just_one = "San Francisco"
        return just_one
    
    def rand_lat(self):
        return 15
    
    def rand_lon(self):
        return 10
    
    def rand_state(self):
        state = "CA"
        return state
    
    def rand_zip(self):
        return 94103
    
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
                the_row.append(self.rand_zip())
                the_row.append(self.rand_state())
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
    
        
        
        
        
        