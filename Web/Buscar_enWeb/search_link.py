import requests
import re

#Obtener url
url = input("Enter URL (include 'http://'): ")

#Conectar hacia la url
website = requests.get(url)

#leer html
html = website.text

# usa re.findall para grabar todos los links
links = re.findall("'((http|ftp)s?://.*?)'",html)

# mostrar links
for link in links:
    print(link[0])