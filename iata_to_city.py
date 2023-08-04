from bs4 import BeautifulSoup
import requests


def get_city_name(iata_code: str):
    url = f'https://www.iata.org/en/publications/directories/code-search/?airport.search={iata_code}'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find('table', class_='datatable')
    cell = table.find('td', string='City Name').next.next.next.next.next.next.next.next.next.next.next.next.next
    city_name = cell.find('td').text
    return city_name
