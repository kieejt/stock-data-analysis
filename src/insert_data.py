import psycopg2
from psycopg2 import sql
import csv

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="investment_performance",
    user="postgres",
    password="kietnha123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Insert data to prices table
def insert_stocks_data_to_db(data):
    with open(data, 'r') as file:
        data_reader = csv.reader(file)
        next(data_reader)  # Skip the header row

        # Insert each row into the table
        for row in data_reader:
            cursor.execute("""
            INSERT INTO stocks (id, symbol, name)
            VALUES (%s, %s, %s)
            """, row)
    conn.commit()
    print("Dữ liệu đã được lưu vào PostgreSQL.")
    
def insert_prices_data_to_db(data):
    with open(data, 'r') as file:
        data_reader = csv.reader(file)
        next(data_reader)  # Skip the header row

        # Insert each row into the table
        for row in data_reader:
            cursor.execute("""
            INSERT INTO prices (id, stock_id, date, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, row)
    conn.commit()
    print("Dữ liệu đã được lưu vào PostgreSQL.")


insert_stocks_data_to_db('stocks_data.csv')
insert_prices_data_to_db('prices_data.csv')


cursor.close()
conn.close()
