import requests 
import colorama
import logging

from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

url = input("URL To Scan: ")
urlReplaced = url.replace("https://", "")
logging.basicConfig(filename=f"{urlReplaced}",level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
RED = colorama.Fore.RED

internalUrls = set()
externalUrls = set()

def isValidUrl(url):
    
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def getAllWebLinks(url):
    urls = set()
    domainName = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for aTag in soup.findAll("a"):
        href = aTag.attrs.get("href")
        if href == "" or str(href).startswith("tel") or str(href).startswith("mailto")  or href is None:
            continue
        try: 

            href = urljoin(url, href)
            parsedHref = urlparse(href)
            href = parsedHref.scheme + "://" + parsedHref.netloc + parsedHref.path
            if not isValidUrl(href):
                continue
            if href in internalUrls:
                continue
            if domainName not in href:
                if href not in externalUrls:
                    print(f"{GRAY}[!] External Link: {href}{RESET}")
                    logging.info(f"[!] External Link: {href}{RESET}")
                    externalUrls.add(href)
                    continue
            print(f"{GREEN}[*] Internal Link: {href}{RESET}")
            logging.info(f"[*] Internal Link: {href}{RESET}")
            urls.add(href)
            internalUrls.add(href)
        except requests.exceptions.InvalidSchema:
            continue
    return urls

totalUrlsVisited = 0
def crawl(url, maxUrls=40):
    global totalUrlsVisited
    totalUrlsVisited += 1
    print(f"{YELLOW}[*] Crawling: {url}{RESET}")
    links = getAllWebLinks(url)
    for link in links:
        if totalUrlsVisited > maxUrls:
            break
        crawl(link, maxUrls=maxUrls)

if __name__ == "__main__":
    try: 
        crawl(f"{url}")
    except KeyboardInterrupt: 
        print("[+] Total Internal links:", len(internalUrls))
        print("[+] Total External links:", len(externalUrls))
        print("[+] Total URLs:", len(externalUrls) + len(internalUrls))
        # if "Invalid" in e:
        #     print(f"{RED} ERROR - InvalidSchema {RESET}")
        # if "KeyboardInterrupt" in e: 
        print(f"{RED} KeyboardInterrupt - Ended Program {RESET}")
        quit()
    # print("[+] Total crawled URLs:", maxUrls)