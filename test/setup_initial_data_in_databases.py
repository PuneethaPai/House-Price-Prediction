import csv

import psycopg2

connection = psycopg2.connect(database='house_features', user='surajus', host='localhost', port='5432')
cursor = connection.cursor()

csv_data = csv.reader(file('train_data.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO train_dataset(bedrooms,bathrooms,sqft_living,sqft_lot,floors,yr_built,zipcode,price) VALUES(%s, %s, %s,%s, %s, %s,%s, %s)',row)
# close the connection to the database.
connection.commit()
cursor.close()
print "Done"
