from bs4 import BeautifulSoup
import requests

site = 'https://www.havan.com.br/esporte-e-lazer/piscinas/'

response = requests.get(site)
html = BeautifulSoup(response.text, 'html.parser')
produtos = []
valores = []
for produto in html.select('.product-item-name'):
    produtos.append(produto.text.lstrip().rstrip())

for valor in html.select('.price-wrapper .price , .no-sprecial:nth-child(1) .product-item-link'):
    valores.append(valor.text)

for i in range(len(produtos)):
    print(f'Produto: {produtos[i]} - valor: {valores[i]}')
