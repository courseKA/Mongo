import json
from re import U
import pymongo
from pymongo import MongoClient
import pprint
from mongoengine import connect


class MongoDB:
    def __init__(self):
        client = pymongo.MongoClient('mongodb://localhost:27017')
        db = client.pythondb 
        self.users = db.user
        
    
    def insert_many_documents(self, users):
        self.db.pythondb.insert_many(users)        

    
    def show_collections():
        collection = db['python_collection']
        
    def get_data_from_jason(users):
        with open(users, 'r') as f:
            return f.read()   
    

class Bankomat():
    def __init__(self, name):
        self.name = name
        
    def check_balance(self):
        return f"Your current balance is {self.balance}."    
        
    def check_pin(self, pin):
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount
        return f"You have deposited {amount}. Your new balance is {self.balance}."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Sorry, you do not have enough funds in your account."
        self.balance -= amount
        return f"You have withdrawn {amount}. Your new balance is {self.balance}."


if __name__ == "__main__":

    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client.pythondb 
    collection = db['python_collection']
    name = input('Enter your name: ')
    exist_name = collection.count_documents({"name":f'{name}'})
    if exist_name >0:
        print("'Your name is accepted'")

    else:
        print("Wrong name. Try again")  
        
for i in range(3):
    pin_input = int(input('Enter your pin: '))
    exist_pin = collection.count_documents({"pin":f'{pin_input}'}) >0
    
    if True:
        print('Login Successful')
        print("Make a choice - 1 to 3 or exit")
        print('1  Balance Inquiry')
        print('2  Withdraw')
        print('3  Deposit')
        pass

            

    
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['python-db']    
    collection = db.python_collection
    collection = db['python_collection']
    connect(db="python-db", host="localhost", port=27017)
    print(db)
    print(collection)    
print("Available databases:", client.list_database_names())    
   
    
 

                 
  
    
