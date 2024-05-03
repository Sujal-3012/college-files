import bs4

with open('data.html' , 'r') as f:
    data_html = f.read()

soup = bs4.BeautifulSoup(data_html , 'html.parser')
print(soup.title)
print(soup.find_all("div"))

