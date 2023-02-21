import pandas as pd
import sqlite3


def rellenar():

    c = sqlite3.connect('example.db') #connect to db

    data = pd.read_csv('alerts.csv')  #read data from csv
    data.to_sql('Alerts', c, if_exists='replace', index=False) #add data to db

    c.commit() #commit changes
    c.close()  #close connection to db



def show_db():
    c = sqlite3.connect('example.db')
    cursor = c.cursor()

    cursor.execute('SELECT * FROM Alerts')
    rows = cursor.fetchall()

    for row in rows:
            print(row)
    cursor.close()
    c.close()

if __name__ == '__main__':
    rellenar()
    #show_db()






