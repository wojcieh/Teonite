import urllib.request
import lxml.html
from lxml.cssselect import CSSSelector
import re

def download(url, user_agent="wswp, num_retries=2"):
    print('Downloading:', url)
    #headers = {'User-agent': user_agent}
    #request = urllib.request(url, headers=headers)
    html = urllib.request.urlopen(url).read().decode('utf-8')
#    except urllib.URLError as e:
#        print('Download error:', e.reason)
#        html = None
#        if num_retries > 0:
#            if hasattr(e, 'code') and 500 <= e.code < 600:
#                return download(url, user_agent, num_retries-1)
    return html

def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download(link)
        if scrape_callback:
            links.extend(scrape_callback(url, html) or [])
def scrape_callback(url, html):
        #autor = re.findall('<span>(*.?)<span>', html)
        tree = lxml.html.fromstring(html)
        #fixed_html = lxml.html.tostring(tree, pretty_print=True)
        h4span = tree.cssselect('span.author-content h4')[0]
        posttitle = tree.cssselect('h1.post-title')[0]
        #postheader = tree.cssselect('h1.post-title')[0]
        postcontent = tree.cssselect('section.post-content')[0]
        autor = h4span.text_content()
        print(autor)
        print(posttitle.text_content())
        print(postcontent.text_content())
        #row = [tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % field)[0].text_content() for field in FIELDS]
        #print(tree.findall('<span class="author-content">'))

crawl_sitemap('https://teonite.com/blog/sitemap-posts.xml')
