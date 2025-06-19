import requests
from bs4 import BeautifulSoup
import os

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

clean()

# Fetching data from tutorialspoint.com
res = requests.get('https://www.tutorialspoint.com/tutorialslibrary.htm')
print("The status code is ", res.status_code)

print(res.headers)
soup_data = BeautifulSoup(res.text, 'html.parser')
title = str(soup_data.title.text)
print(title.strip())
print("\n")

# Printing all <h2> tags
for i, j in enumerate(soup_data.find_all('h2')):
    print(f'{i+1}. {j.text}')

# Example with parameters
payload = {'id': '9', 'username': 'Delphine'}
res = requests.get('https://jsonplaceholder.typicode.com/users', params=payload)
print(res.text)

# Example without parameters
res = requests.get('https://jsonplaceholder.typicode.com/users')
status_code = res.status_code
data = {'id': '11', 'username': 'Savvy'}
print(f"Successfully added the user {data['username']} and the status code is {status_code}")
