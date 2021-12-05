import argparse
from rich.console import Console
import rich.traceback
import requests
from bs4 import BeautifulSoup
import os
import json

parser = argparse.ArgumentParser()
parser.add_argument('name', help = 'name of file to return')
args = parser.parse_args()

console = Console()
console.clear()
rich.traceback.install()

try:
    req = requests.get('https://www.filmweb.pl/serial/Biuro-2005-202887/cast/actors')
except requests.exceptions.HTTPError:
    console.print("HTTP error.")
except requests.exceptions.ConnectionError:
    console.print("Connection error.")
else:
    soup = BeautifulSoup(req.text, 'html.parser')
    divs = soup.find_all('div', class_ = 'castRoleListElement__info')

    listt = [{'Aktor/ka': div.find('a').text, 'Postac': div.find('span').text} for div in divs]

    with open(os.getcwd()+f'\\{args.name}', 'w', encoding="utf-8") as file:
        json.dump(listt, file, indent=2)

    console.print('Saved to file.')

    
