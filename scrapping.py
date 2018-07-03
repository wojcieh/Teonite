import urllib.request
from lxml import etree
import re
from bs4 import BeautifulSoup
def download(url):
    print('Downloading:', url)
    response = urllib.request.urlopen(url).read()
    return response
posts = download('https://teonite.com/blog/sitemap-posts.xml')
parser = etree.parse(posts)
root = etree.XML(parser)
print(root.tag)
#print(root.findall("loc").tag)
#links = re.findall('<loc>(.*?)</loc>', posts)
#print(links).encode(utf-8)
