from bs4 import BeautifulSoup

f = open("sample.html","r")

soup = BeautifulSoup(f.read(),'html.parser')

results = soup.find_all('td',attrs={'class': "user"}

for r in results:
		print(c.text)