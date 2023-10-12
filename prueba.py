import requests
from lxml import html

url = 'http://158.69.119.209/data/index.php?view=mostrar&cod=71637153'
response = requests.get(url)
html_source = response.content
busqueda_elementos = html.fromstring(html_source)
nombre = busqueda_elementos.xpath('//h2[@class="name"]/text()')

if nombre:
    print(nombre[0])
else:
    message = "estado fallido"
