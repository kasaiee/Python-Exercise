# pip install beautifulsoup4
from urllib.request import urlopen
from bs4 import BeautifulSoup

internal_links = []

def sitemap(domain='python.org'):
    global internal_links
    if not (domain.startswith('http://') or domain.startswith('https://')):
        domain = 'http://' + domain
    html = urlopen(domain).read()
    soup = BeautifulSoup(html)
    for link in soup.find_all('a'):
        internal_links += [link.get('href')]

print(internal_links)