import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    data = []
    for page_num in range(0, 80, 10):  # scrape up to 2 pages (assuming each page has 10 results)
        page_url = url + f'&start={page_num}'
        page = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('div', class_='gs_r gs_or gs_scl')
        for r in results:
            title = r.find('h3', class_='gs_rt').find('a')
            link = title['href'] if title else None
            title = title.get_text().strip() if title else None
            author_year_publi_info = r.find('div', class_='gs_a').get_text().strip()
            description = r.find('div', class_='gs_rs').get_text().strip()
            data.append({
                'title': title,
                'link': link,
                'author_year_publi_info': author_year_publi_info,
                'description': description,
            })
    return data

url = 'https://scholar.google.com.sg/scholar?hl=en&as_sdt=0%2C5&as_vis=1&q=drug+effects&btnG='
data = scrape_website(url)
print(data)

with open("drug_effects.json", "w") as outfile:
    json.dump(data, outfile)
