import sys,requests,httpx
arg=sys.argv
http_methods=['GET','POST','PUT','DELETE','HEAD','OPTIONS','PATH','TRACE','CONNECT']
def http_requests(URL):
    for method in http_methods:
        http=httpx.Client()
        response = http.request(method,URL)
        print(f"[~]{method} {response.status_code} {response.reason_phrase}") 
    
if len(sys.argv)==1:
    print('[~]Enter in valid format :\n\t>> python verb-tamper.py <URL>')
else:
    url=arg[1]
    http_requests(url)
