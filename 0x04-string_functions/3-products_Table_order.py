#!/usr/bin/python3

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PRODUCTS ORDER'.center(leftWidth + rightWidth, '-'))

    for key, value in itemsDict.items():
        print(key.ljust(leftWidth, '.') + str(value).rjust(rightWidth))

productItems = {'Sandwiches': 4, 'apples': 12,
        'cups': 4, 'cookies': 8000}

printPicnic(productItems, 12, 5)
printPicnic(productItems, 20, 6)
