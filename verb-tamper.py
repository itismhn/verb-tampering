import sys,requests
arg=sys.argv

    
if len(sys.argv)==1:
    print('[~]Enter in valid format :\n\t>> python verb-tamper.py <URL>')
else:
    url=arg[1]
    print(url)
