#!/bin/bash/python3 
import requests

API_ID = "d54b6d212cf142caaa7ac1c28b1c260c"
SYMBOLS = "ARS%2CPEN%2CUYU%2CPYG"
URL = f"""https://openexchangerates.org/api/historical/2021-01-28.json?app_id={API_ID}&symbols={SYMBOLS}"""

result = requests.get(URL)
result_dict = result.json()
print(result_dict)
