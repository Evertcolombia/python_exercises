#!/usr/bin/python3

import bs4, sys

if len(sys.argv) > 0:

    new_file = open(sys.argv[1])
    file_soup = bs4.BeautifulSoup(new_file.read())
    
    try:
        elements  = file_soup.select('PRE')
        print("Elements were stored")
        print()
        print(str(elements[0]))
        a = elements[0].getText()
        print(a)
    except:
        print("Error")

    new_file.close()
