import pandas as pd
import sqlite3


def rellenar():

    c = sqlite3.connect('example.db') #connect to db
    data = pd.read_csv('alerts.csv')  #read data from csv

    data.to_sql('example.db', c, if_exists='replace', index=False) #add data to db

    c.commit() #commit changes
    c.close()  #close connection to db










if __name__ == '__main__':
    rellenar()







