#!/usr/bin/python3

import requests, sys, os


def create_folder():

        cwd = os.getcwd()
        path = cwd + '/' + sys.argv[4]

        try:
            os.makedirs(path)
            return path
        except:
            print("Can't Create the folder {}".format(sys.argv[4]))
            sys.exit(1)


def create_file(res):

    try:
        with open(path + '/' + filename, 'wb') as f:
            for chunk in res.iter_content(100000):
                f.write(chunk)
    except:
        print("Can't create file {}".format(filename))

def get_page(n):

    try:
        res = requests.get(sys.argv[1] + str(n))
        res.raise_for_status()
        print("Got the chapter {}".format(sys.argv[1] + str(n)))

    except:
        print("Cant do request to {}".format(url))
        sys.exit(1)

    create_file(res)


if len(sys.argv) > 3:
   
    path = create_folder()
    
    for n in range(1, int(sys.argv[3])):
        try:
            filename = sys.argv[2] + str(n) + '.html'
            get_page(n)
        except:
            pass
