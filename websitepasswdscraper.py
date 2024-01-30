import requests
from bs4 import BeautifulSoup
import re

url = input("Enter the URL: ")
min_length = int(input("Enter the minimum character length for words: "))
max_length = int(input("Enter the maximum character length for words: "))
output_file = input("Please enter the name of the output file (e.g., 'output.txt'): ")

response = requests.get(url)
if response.status_code != 200:
    print("Error fetching the URL!")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')
text = soup.get_text()

words = re.findall(r'\b\w+\b', text)

filtered_words = [word for word in words if min_length < len(word) < max_length]

with open(output_file, 'w') as file:
    for word in filtered_words:
        file.write(word + '\n')
