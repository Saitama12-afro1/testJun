import asyncio
import requests
import aiohttp
import bs4
import wikipedia
import pprint
#сделать ассинхронным
#нужно переписать так что бы фукнция заполняла одну стриацу 

all_animals = {}

def get_letters():
    url = "https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from=A"
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, "lxml")
    letters = soup.find("table", class_="plainlinks").find_all("td")
    all_letters = []
    for i in letters:
        try:
            if 1040 <= ord(a := i.text) <=1071:
                all_letters.append(i.text)
        except TypeError:
            pass
    return all_letters

def get_pagination(all_letters):
    all_pages = []
    for i in all_letters:
        url = f"https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from={i}"
        all_pages.append(url)
    return all_pages
lock = asyncio.Lock()     
async def get_page_data(session, page, letters):
    async with session.get(page) as response:
        response_text = await response.text()
        soup = bs4.BeautifulSoup(response_text, "lxml")
        current_latters = soup.find("div", {"id": "mw-pages"}).find("ul")
        buff = []
        for i in current_latters:
            if i.text != '\n':
                buff.append(i.text)

            async with lock:
                all_animals.update({f"{letters}":buff})
    

async def gettt():
    all_letters = get_letters()
    all_pages = get_pagination(all_letters)
    async with aiohttp.ClientSession() as session:
        for ind, page in enumerate(all_pages):
            req =  await session.get(page)
            soup = bs4.BeautifulSoup(await req.text(), "lxml")
            tasks = []

            for page in all_pages:
                await asyncio.sleep(1)
                task = asyncio.create_task(get_page_data(session, page, all_letters[ind]))
                tasks.append(task)
  
        await asyncio.gather(*tasks)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gettt())
    pprint.pprint(all_animals)



if __name__ == "__main__":
    main()