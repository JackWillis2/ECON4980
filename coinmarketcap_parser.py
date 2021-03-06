from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df=pd.DataFrame

for one_file_name in glob.glob("html_files/*.html")
	print("parsing"+one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("coinmarketcap","")
	f = open(one_file_name, "r")
	soup=BeautifulSoup(f.read(),'html.parser')
	f.close()
	currencies_table=soup.find("table",{"data-reactid":"37"})
	print(currencies_table)