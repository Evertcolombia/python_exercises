#!/usr/bin/python3
import sys, requests, webbrowser, bs4

if len(sys.argv) > 0:
    try:
        res = requests.get('https://google.com/search?q=''https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
        res.raise_for_status
        print("fine")
        print(sys.argv)

    except:
        print("Basd request")
        sys.exit(1)

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    print(soup)

    # Look for results with the selector you choose
    linkElems = soup.select('div.cOl4Id')

    numOpen = min(5, len(linkElems))

    for i in range(numOpen):
        urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
        print('Opening', urlToOpen)
        webbrowser.open(urlToOpen)
