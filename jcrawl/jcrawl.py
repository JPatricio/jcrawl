"""
A python application to extract all links from an HTML document.

Start with a seed URL and crawl every new link found, without revisiting a page.
No helper libraries allowed. Only Regex, Requests, and urllib as primary tools.

Once all the links are extracted from a website, assemble a site map in the standard format.

Note:
    A Seed URL in web crawling is a url from which a web crawler will begin to traverse a site. Once a crawler is on a
    seed URL it will extra data from the page and look for all links to additional pages. If a crawler is set to crawl
    an entire domain it will systematically follow each link on every page, extracting data from each ensuing page.
    Paths from a seed URL are often influenced by a websites Robots.txt file, which dictates how the site owner would
    like bots to traverse the site.  Source: https://blog.diffbot.com/knowledge-graph-glossary/seed-url/
"""
import argparse
import re

from urllib.parse import urlparse
from urllib.request import urlopen


def main(seed):
    domain = urlparse(seed).netloc
    web_url = urlopen(seed)
    content = web_url.read()
    print(content)
    domain_match = rf"{domain}\/"
    print(domain_match)
    links = re.findall(bytes(domain_match, 'utf-8'), content)
    print(links)


if __name__ == "__main__":
    url = "https://www.google.com/"
    main(url)
