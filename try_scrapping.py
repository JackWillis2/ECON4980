import urllib.request
import ssl

unverified_context = ssl._create_unverified_context()
response = urllib.request.urlopen("http://coinmarketcap.com/", context=unverified_context)

page = response.read()

print(page)

f= open("coinmarketcap.html","wb")

f.write(page)

f.close()






