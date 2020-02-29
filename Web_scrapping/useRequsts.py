#!/usr/bin/python3

import requests, sys

def book_and_filename():
    res = requests.get(sys.argv[1])
    res.raise_for_status()
        
    playFile =  open(filename, 'wb')        
    for chunk in res.iter_content(100000):
    playFile.write(chunk)
    playFile.close()


if len(sys.argv) > 2:
   
    filename = sys.argv[2]
    try:
        book_and_filename()
    except Exception as exc:
        print('there was a problem %s' % (exc))

else:
    print("Must passs url and filename")
