import psycopg2
import pandas
connection = psycopg2.connect(database='house_features', user='surajus', host='localhost', port='5432')
cursor=connection.cursor()
query_for_data="""SELECT * FROM train_dataset"""
query_for_column_names="""SELECT Column_name from information_schema.columns where table_name='train_dataset'"""
cursor.execute(query_for_column_names)
columns=[]
for i in  cursor.fetchall():
    columns += i
print columns

cursor.execute(query_for_data)
result= cursor.fetchall()
print result
dataframe=pandas.DataFrame(result,columns=columns)
print dataframe