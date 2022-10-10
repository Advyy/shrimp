import requests
from io import BytesIO

response = requests.get("https://media.tenor.com/2691oFJizwUAAAAC/chorando-triste.gif")

print(response.text)