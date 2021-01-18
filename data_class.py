
# -> trying to be able to retrieve the JSON Data 
import json
import requests

class Data:

    ''' Retrieves the Plaid JSON Data and parses it ''' 

    def __init__(self, url):

        self.url = url 
        self.response = requests.get(str(self.url))
        self.status = self.response.status_code
        self.length = len(self.response)

        self.labels = [label for label in self.response[0].keys()] # labels / columns / headers (keys of json data)
        self.trx_lists = [[item.values()] for item in self.response] # transactions as a list of lists

        return
        
    
    def __repr__(self):

        print('Type: ', type(some_url), '  ||  URL: ', some_url)
        print('Status Code: ', self.status)
        print('Labels: ', self.labels)
        print('response length: ', response_length)
        print('********** RESPONSE ***********') 
        print(self.response)

        return 
    
    # def request_length(self, response):
    #     ''' takes the large string response and breaks it up '''
    #     count = 0
    #     for item in response:
    #         count += 1

    #     print('count: ', count)
    #     print('len: ', len(response))

    #     return len(response)
    
    # def check_for_missing_values(self):
    #     ''' either create a csv or go through each json item if you know what you're looking for ''' 
    #     pass

    # def trx_lists(self):
    #     ''' uses the json response data and creates a list of lists of each transaction '''

    #     matrix = []

    #     count = 0
    #     for item in self.response: 
    #         if count == 0: 
    #             # headers 
    #             header = item.keys() 
    #             count += 1
        
    #         # appending data
    #         matrix.append([item.values()]) 
        
        
    #     return matrix
    

    def json_to_csv(self, json_f):
    # accept JSON data, turn it into a csv file
    
        with open(json_f) as json_file: 
            data = json.load(json_file) 
        
        json_data = data['emp_details'] 
        
        # now we will open a file for writing 
        data_file = open('data_file.csv', 'w') 
        
        # create the csv writer object 
        csv_writer = csv.writer(data_file) 
        
        # Counter variable used for writing  
        # headers to the CSV file 
        count = 0
        
        for item in json_data: 
            if count == 0: 
        
                # Writing headers of CSV file 
                header = item.keys() 
                csv_writer.writerow(header) 
                count += 1
        
            # Writing data of CSV file 
            csv_writer.writerow(item.values()) 
        
        data_file.close() 


