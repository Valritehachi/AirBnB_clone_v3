#!/usr/bin/python3
"""
W3C validator for Holberton School

"""
import sys
import requests


def __print_stdout(msg):
    """Print out the  STDOUT function
    """
    sys.stdout.write(msg)


def __print_stderr(msg):
    """Print out the STDERR function
    """
    sys.stderr.write(msg)


def __analyse_html(file_path):
    """Start analyse of HTML file function
    """
    h = {'Content-Type': "text/html; charset=utf-8"}
    d = open(file_path, "rb").read()
    u = "https://validator.w3.org/nu/?out=json"
    r = requests.post(u, headers=h, data=d)
    res = []
    messages = r.json().get('messages', [])
    for m in messages:
        res.append("[{}:{}] {}".format(file_path, m['lastLine'], m['message']))
    return res


def __analyse_css(file_path):
    """Start analyse of CSS file
    """
    d = {'output': "json"}
    f = {'file': (file_path, open(file_path, 'rb'), 'text/css')}
    u = "http://jigsaw.w3.org/css-validator/validator"
    r = requests.post(u, data=d, files=f)
    res = []
    errors = r.json().get('cssvalidation', {}).get('errors', [])
    for e in errors:
        res.append("[{}:{}] {}".format(file_path, e['line'], e['message']))
    return res


def __analyse(file_path):
    """a function to Start file analysis
    """
    nb_errors = 0
    try:
        result = None
        if file_path.endswith('.css'):
            result = __analyse_css(file_path)
        else:
            result = __analyse_html(file_path)

        if len(result) > 0:
            for msg in result:
                __print_stderr("{}\n".format(msg))
                nb_errors += 1
        else:
            __print_stdout("{}: OK\n".format(file_path))

    except Exception as e:
        __print_stderr("[{}] {}\n".format(e.__class__.__name__, e))
    return nb_errors


def __files_loop():
    """Loop that analyses for each file from input arguments
    """
    nb_errors = 0
    for file_path in sys.argv[1:]:
        nb_errors += __analyse(file_path)

    return nb_errors


if __name__ == "__main__":
    """Main
    """
    if len(sys.argv) < 2:
        __print_stderr("usage: w3c_validator.py file1 file2 ...\n")
        exit(1)

    """execute tests, then exit. Exit status = # of errors (0 on success)
    """
    sys.exit(__files_loop())
