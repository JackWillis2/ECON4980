from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df=pd.DataFrame

for one_file_name in glob.glob("html_files/SandP/*.html"):
	print("parsing"+one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("coinmarketcap","")
	f = open(one_file_name, "r")
	soup=BeautifulSoup(f.read(),'html.parser')
	f.close()
	number_table=soup.find("div", {"id": "quote-header-info"})
	further=number_table.find("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"})
	evenfurther=further.find("span",{"class":"Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"}).text
	print(evenfurther)