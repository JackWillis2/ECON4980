import urllib.request
import os
import time
import datetime

if not  os.path.exists("html_files"):
	os.mkdir("html_files")

for i in range(5):
	current_time_step=datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	
	response = urllib.request.urlopen("https://finance.yahoo.com/quote/%5EGSPC?p=^GSPC")
	
	html = response.read()

	print(html)
	f=open("html_files/sandp" + current_time_step +".html","wb")

	f.write(html)

	f.close()
	print("requesting coinmarketcap")
	time.sleep(5)



