#!/bin/bash/python3 
from datetime import datetime, timedelta 
import json
import requests, psycopg2
from psycopg2 import Error
from termcolor import colored

API_ID = "d54b6d212cf142caaa7ac1c28b1c260c"
SYMBOLS = "ARS%2CPEN%2CUYU%2CPYG"

try:
    # Connect to database
    connection = psycopg2.connect(user="postgres",
                                    password="postgres",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="globalnet")

    initial_date = datetime.strptime('2019-01-01', '%Y-%m-%d')
    for value in range(0, 694):
        initial_date += timedelta(days = 1)
        date_str = initial_date.strftime('%Y-%m-%d')
        URL = f"""https://openexchangerates.org/api/historical/{date_str}.json?app_id={API_ID}&symbols={SYMBOLS}"""
        
        result = requests.get(URL)
        result_dict = result.json()

        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO rates values ('{date_str}', 'USD', {result_dict['rates']['ARS']}, {result_dict['rates']['PEN']}, {result_dict['rates']['PYG']}, {result_dict['rates']['UYU']})")
        connection.commit()
        print( f"""DATE: {colored(date_str, 'green')} ARS: {colored(result_dict['rates']['ARS'], 'yellow')}  PEN: {colored(result_dict['rates']['PEN'], 'yellow')}  PYG: {colored(result_dict['rates']['PYG'], 'yellow')}  UYU: {colored(result_dict['rates']['UYU'], 'yellow')}""")

except (Exception, Error) as error:
    print(colored(error, 'cyan'))
finally:
    if (connection):
        cursor.close()
        connection.close()
        print(colored("PostgreSQL connection is closed", 'cyan'))
