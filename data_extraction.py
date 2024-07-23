import os
import psycopg2
import pandas as pd
from psycopg2.extras import RealDictCursor

def connect_to_postgres():
    # Get credentials from environment variables
    host = os.getenv('host')
    port = os.getenv('port', 5432)
    database = os.getenv('database')
    user = os.getenv('user')
    password = os.getenv('password')
    table = os.getenv('table')

    # Connect to PostgreSQL
    try:
        conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return

    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Query the database
    try:
        cur.execute(f"SELECT * FROM {table}")
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
        return

    # Fetch all the records
    rows = cur.fetchall()

    # Prepare a data frame
    df = pd.DataFrame(rows)

    # Print the top 5 rows
    print(df.head())

    # Print data extraction successful
    print("Data extraction successful")

    # Store the dataframe as data.csv file
    df.to_csv('data.csv', index=False)

# Call the function
connect_to_postgres()