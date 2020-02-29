#!/usr/bin/python3

import requests, sys, os


def get_page(n):
    
    try:
        res = requests.get(sys.argv[1] + str(n))
        res.raise_for_status()
        print("Got the chapter {}".format(sys.argv[1] + str(n)))

        playFile =  open(filename, 'wb')
        for chunk in res.iter_content(100000):
            playFile.write(chunk)
            print("Writting")
        playFile.close()
    
    except:
        print("Cant do request to {}".format(url))
        sys.exit(1)

    
if len(sys.argv) > 1: 

    my_files = []
   
    for n in range(1, int(sys.argv[3])):
        try:
            filename = sys.argv[2] + str(n) + '.html'
            get_page(n)
        except:
            pass
    print(my_files)
