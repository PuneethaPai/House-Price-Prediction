import pickle
import threading

import psycopg2

with open(
        '/Users/surajus/Shanbhag/House Price Prediction/PredictionApp/HousePricePredicton/myapp/house_price_prediction_model.sav',
        'rb') as fl:
    model = pickle.load(fl)
connection = psycopg2.connect(database='house_features', user='surajus', host='localhost', port='5432')


def processRequest(house_features):
    update = threading.Thread(target=updateHousePrice, args=(house_features))
    update.start()
    return predictHousePrice(house_features)


def add_batch_to_training_set(cursor):
    query="""select * from features_with_price"""
    query_to_insert="""INSERT INTO train_dataset VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(query)
    data=cursor.fetchall()
    print data
    for row in data:
        cursor.execute(query_to_insert,row)
    query_to_check="""select count(*) from train_dataset"""
    cursor.execute(query_to_check)
    print cursor.fetchall()


def updateHousePrice(house_features):
    cursor = connection.cursor()
    insertRecord(cursor, house_features)
    query_to_check_batch_size = """SELECT count(*) from features_with_price"""
    cursor.execute(query_to_check_batch_size)
    result = cursor.fetchall()[0][0]
    if (result >= 50):
        add_batch_to_training_set(cursor)
        trainAndUpdateModel()
    connection.commit()
    connection.close()
    return


def insertRecord(cursor, house_features):
    sql_query = """INSERT INTO features_with_price VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql_query, tuple(house_features))

def trainAndUpdateModel():
    return

def predictHousePrice(input):
    return model.predict(input)


if __name__ == '__main__':
    # updateHousePrice([1, 2, 3, 3, 4, 6, 7, 3])
    add_batch_to_training_set(connection.cursor())
