import requests
url1 = 'https://www.msit.in/'
url2 = 'https://cloudbreeze.vercel.app/'

def fetchdata(url , path):
    html_doc = requests.get(url)
    with open(path , 'w') as f:
        f.write(html_doc.text)

fetchdata(url2 , 'sahil.html')
