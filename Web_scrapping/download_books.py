#!/usr/bin/python3
import requests, sys, os

"""
    This script download cotent from webpages using arguments
    from the user command line to get th resuls

    sys.argv:
        [1] = Url to rquest
        [2] = File names
        [3] = File extension
        [4] = limit to request to do example (17)
        [5] = Folder name for the Donwloaded content
"""

def create_folder():
    """
        Create a new folder at the current working directory

        cwd: current working directory
        path: the (cwd + sys.argv[4]) argv[4] folder name by user
    """
    cwd = os.getcwd()
    path = cwd + '/' + sys.argv[5]

    try:
        os.makedirs(path)
        return path
    except:
        print("Can't Create the folder {}".format(sys.argv[5]))
        sys.exit(1)


def create_file(res):
    """
        Create a file in the path

        filename: the filename from the user argv[3]
    """
    try:
        with open(path + '/' + filename, 'wb') as f:
            for chunk in res.iter_content(100000):
                f.write(chunk)
    except:
        print("Can't create file {}".format(filename))


def get_page(n):
    """
        Make a request from the user page on argv[1]

        res: response of the request to the url in argv[1]
    """
    try:
        res = requests.get(sys.argv[1] + str(n))
        res.raise_for_status()
        print("Got the chapter {}".format(sys.argv[1] + str(n)))

    except:
        print("Cant do request to {}".format(url))
        sys.exit(1)

    create_file(res)


def validator():
    """
        This function validates the file extension and the
        range for the downloads sequence
    """
    if sys.argv[3][0] != '.':
        print("File ext use '.' ex: .{}".format(sys.argv[3]))
        sys.exit(1)

    try:
        d_range = int(sys.argv[4])
        return d_range
    except:
        st = 'Range Download must be integer {}'
        raise ValueError(st.format(sys.argv[4]))


if len(sys.argv) > 4:
    """
        This part runs the program

        path: the return folder create path
        filename: name by user argv[2] .argv[3] as extension
    """
    d_range = validator()
    path = create_folder()
    file_ext = sys.argv[3]

    for n in range(0, d_range):
        try:
            filename = sys.argv[2] + str(n) + file_ext
            get_page(n)
        except:
            print("File {} wasn't created".format(filename))
else:
    s1 = "Error No arguments to use the program example"
    s2 = "[url] [file_names] [file extension] [range] [folder_name]"
    print("{} {}".format(s1, s2))
    sys.exit(1)
