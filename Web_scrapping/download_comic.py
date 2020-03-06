#!/usr/bin/python3
"""
    Downloads every  single XKDC comic
"""

import requests, os, bs4

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print("Could't find comic image.")
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        #download the image
        print('Downloading the image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        #save the mage to the folder
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('Done.')
