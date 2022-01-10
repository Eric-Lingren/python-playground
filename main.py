import requests 
import wget
from bs4 import BeautifulSoup 

urls = [
    # Add list of URLs with images here
]

images = []  # list to store images

for url in urls:
    r = requests.get(url)   
    soup = BeautifulSoup(r.content, 'html5lib') 
    images.append(soup.find_all('div', attrs = {'class':'e-gallery-image'}) )

flattened = [val for sublist in images for val in sublist]

image_urls = []

for image in flattened:
    image_urls.append(image.attrs['data-thumbnail'])

for url in image_urls:
    filename = url.split('/')[-1]
    wget.download(url, filename)

