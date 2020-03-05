#!/usr/bin/python3
import sys, requests, webbrowser, bs4

def simple_request(browser_url):
    print('Googling...')
    browser_url = 'https://google.com/search?q='
    res = requests.get(browser_url + ''.join(search_string))
    res.raise_for_status()
    return res


def link_elements(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElems = soup.select('.ZINbbc>div.kCrYT a')

    if (linkElems  == []):
        print("Can't find any url to go")
        sys.exit(1)
    return linkElems


if len(sys.argv) > 0:

    try:
        search_string = sys.argv[1:]
        res = simple_request(search_string)
    except:
        print("request error")
        sys.exit(1)

    linkElems = link_elements(res)
    numOpen = min(5, len(linkElems))

    for i in range(numOpen):
        url = 'https://google.com' + linkElems[i].get('href')
        webbrowser.open_new_tab(url)
