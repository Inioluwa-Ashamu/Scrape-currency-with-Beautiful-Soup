from bs4 import BeautifulSoup
import requests

def get_currency(from_currency, to_currency):
  url = f'https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find('span', class_='ccOutputRslt').get_text()
  rate = float(rate[:-4])
  return rate

final_rslt = get_currency('INR', 'USD')
print(final_rslt)

  