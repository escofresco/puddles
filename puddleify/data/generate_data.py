
# We use this to generate datasets to train on!

# Let's generate some data in a csv to train our model on

# the dataset will have 12 attributes per item

class Dataset:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.dataset = None

    def create_empties():
        ''' generate an empty dataset of rows r and columns c '''
        empty_array = [[0]*self.columns]*self.rows
        self.dataset = empty_array
        print(self.dataset)
        # for index, item in enumerate(self.dataset):
        #     print(index, item)
        return self.dataset




if __name__ == '__main__':
    empties(10, 12)     