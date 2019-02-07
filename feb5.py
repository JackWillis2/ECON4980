import urllib.request
import ssl

response = urllib.request.urlopen("http://www.stockx.com")
page =response.read()

print(page)