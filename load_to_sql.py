import pandas as pd
import mysql.connector
from mysql.connector import Error

# Load CSV using pandas
df = pd.read_csv("SuperStoreOrders.csv")

# Convert date columns to MySQL compatible format
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True, errors='coerce')

# Remove commas from numeric columns & convert to proper data types
df['sales'] = df['sales'].replace({',': ''}, regex=True).astype(float)
df['profit'] = df['profit'].replace({',': ''}, regex=True).astype(float)
df['shipping_cost'] = df['shipping_cost'].replace({',': ''}, regex=True).astype(float)
df['discount'] = df['discount'].astype(float)
df['quantity'] = df['quantity'].astype(int)
df['year'] = df['year'].astype(int)
try:
    connection = mysql.connector.connect(
        host="localhost",
        database="sales_insights",
        user="root",
        password="@Arun9110"
    )

    if connection.is_connected():
        print("Connected to MySQL Server")
        cursor = connection.cursor()

        # Create table
        cursor.execute("DROP TABLE IF EXISTS sales_data")

        create_table_query = """
        CREATE TABLE sales_data (
            order_id VARCHAR(50),
            order_date DATE,
            ship_date DATE,
            ship_mode VARCHAR(50),
            customer_name VARCHAR(100),
            segment VARCHAR(50),
            state VARCHAR(50),
            country VARCHAR(50),
            market VARCHAR(50),
            region VARCHAR(50),
            product_id VARCHAR(50),
            category VARCHAR(50),
            sub_category VARCHAR(50),
            product_name VARCHAR(200),
            sales DECIMAL(10,2),
            quantity INT,
            discount DECIMAL(5,2),
            profit DECIMAL(10,2),
            shipping_cost DECIMAL(10,2),
            order_priority VARCHAR(50),
            year INT
        );
        """
        cursor.execute(create_table_query)

        # Insert data row-by-row
        insert_query = """
        INSERT INTO sales_data (
            order_id, order_date, ship_date, ship_mode, customer_name,
            segment, state, country, market, region, product_id,
            category, sub_category, product_name, sales, quantity,
            discount, profit, shipping_cost, order_priority, year
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for _, row in df.iterrows():
            cursor.execute(insert_query, tuple(row))

        connection.commit()
        print("Data inserted successfully ✔")

except Error as e:
    print("Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed")
