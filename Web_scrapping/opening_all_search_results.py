#!/usr/bin/python3
import sys, requests, webbrowser, bs4
"""Simple script to open the first 5th web pages that contains
    the refered user looks
"""

def simple_request():
    """ 
        Do simple request based in the search string
    """
    print('Googling...')
    browser_url = 'https://google.com/search?q='
    res = requests.get(browser_url + ''.join(search_string))
    res.raise_for_status()
    return res


def link_elements(res):
    """
        get the elements html <a> with the refer url por the pages

        [0] res: response of the request
    """
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElems = soup.select('.ZINbbc>div.kCrYT a')

    if (linkElems  == []):
        print("Can't find any url to go")
        sys.exit(1)
    return linkElems


def open_tabs():
    """
        open the links in tabs in the mozilla browser
    """
    numOpen = min(5, len(linkElems))

    try:
        for i in range(numOpen):
            url = 'https://google.com' + linkElems[i].get('href')
            webbrowser.open_new_tab(url)
    except:
        raise ValueError('The url can be opened')
        pass


if len(sys.argv) > 0:
    """
        Main part of the program

        sys.argv[1]: search_string
    """
    try:
        search_string = sys.argv[1:]
        res = simple_request()
    except:
        print("request error")
        sys.exit(1)

    linkElems = link_elements(res)
    open_tabs()
