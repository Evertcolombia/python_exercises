#!/usr/bin/python3

import bs4, sys

if len(sys.argv) > 0:

    new_file = open(sys.argv[1])
    file_soup = bs4.BeautifulSoup(new_file.read())
    
    try:
        elements  = file_soup.select('PRE')
        print("Elements were stored")
        
        print(str(elements[0]))
        
        a = elements[0].getText()
        print(a)

        b = elements[0].attrs
        print(b)
    except:
        print("Error")

    new_file.close()

# You can see the corect selector form the css element in a we bage 
# selecting the element from the  inpect console and typing secondary
# click on the element that you want -> copy -> copy selector
