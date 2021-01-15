
# Puddleify is the Transaction Learning aspect. 
We'll create a a large dataset to train on and use that initially to create a standardized model. 

(find_puddles.py)\
    1. take an input of a customer's {past month's} bank transactions.\
    2. record the puddle each item was placed\
    3. train model\
    4. use model to recommend a puddle.\
    5. retrain model to compensate accuracy and loss\

Further Breakdown:

## 1. take an input of a customer's {past month's} bank transactions.
    a. Customer's bank transactions are received via plaid as JSON\
    b. Transaction as JSON is placed into database\

## 2. record the puddle each item was placed
    a. Given bank account's transactions are displayed from the database\
    b. Customer creates labelled puddles\
    c. Customer places transaction into puddle\
    d. Puddle is recorded along with the transaction in database\

## 3. train model
    a. Pull all data with puddles from database into model\
    b. Observe features and acknowledge relevant ones\
        i. Changes may be necessary - break down text into individual words as a feature.\
        ii. Remove numbers?\
        iii. Incorporate as many features as possible / relevant/
    c. Choose ML models\
        i. Test on dummy data - Generate large dummy datasets\
        ii. Which models work better and with which features? Too many or too less.\
    d. Large model to work for anyone and individual brand new models. (different types of consumers?)\

## 4. use model to help speed up puddleing process by recommending a puddle.
    a. Once we have a working trained model\
    b. The next months transactions will roll in\
    c. As each new transaction is observed that has not been placed into a puddle,\
    d. Predict a puddle on it and display that to the user.\

## 5. retrain model to compensate accuracy and loss
    a. Observe the predicted value vs actual value\
    b. retrain model with new puddle data ???\


Resources:\
Plaid data: https://plaid.com/blog/making-sense-of-messy-data/
