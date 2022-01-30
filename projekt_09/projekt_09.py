import asyncio, aiofiles
from aiohttp import ClientSession
from pathlib import Path
import os

async def download_image(session, url, link):
    print(f'Session started: {url+link}')

    async with session.get(url+link) as response:

        path = os.getcwd()+f"\\images"
        Path(path).mkdir(parents = True, exist_ok = True)  

        file = await aiofiles.open(path+f'\\{link}', mode='wb')
        await file.write(await response.read())
        await file.close()
        
        print(f'Session finished: {url+link}')

async def main():
    links = [f'img{i}.png' for i in range(10)]
    url = 'http://www.if.pw.edu.pl/~mrow/dyd/wdprir/'
    tasks = []
    async with ClientSession() as session:
        for link in links:
            tasks.append(asyncio.create_task(download_image(session, url, link)))
    
        await asyncio.gather(*tasks) #gather łączy wszystkie taski w jeden task 
                                        #i await czeka na wszystkie taski

asyncio.run(main())

