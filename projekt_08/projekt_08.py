from rich.console import Console
import rich.traceback
import requests
from bs4 import BeautifulSoup
import os
import multiprocessing as mp
import concurrent.futures
from PIL import Image
from io import BytesIO
from pathlib import Path

console = Console()
console.clear()
rich.traceback.install()

def get_links(url):
    links = []

    try:
        req = requests.get(url)
    except requests.exceptions.HTTPError:
        console.print("HTTP error.")
    except requests.exceptions.ConnectionError:
        console.print("Connection error.")
    else:
        soup = BeautifulSoup(req.text, 'html.parser')
        images = soup.find_all('a')

        for image in images:
            if '.png' in image.text:
                links.append(image['href'])
        
        return links

def worker(link):
    console.print(f'Process {os.getpid()} working on {link}')

    path = os.getcwd()+f"\\images"
    Path(path).mkdir(parents=True, exist_ok=True)  

    url = 'http://www.if.pw.edu.pl/~mrow/dyd/wdprir/'

    data = Image.open(BytesIO(requests.get(url+link).content)).convert("L")
    data.save(f"{path}\\{link}")

links = get_links(url = 'http://www.if.pw.edu.pl/~mrow/dyd/wdprir/')

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(worker, links)