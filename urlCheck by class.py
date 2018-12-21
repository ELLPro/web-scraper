from urllib.request import urlopen
from bs4 import BeautifulSoup 
import requests 
import csv 
from openpyxl import Workbook
import xlsxwriter
import pprint 
import re 
import pyperclip 
import time
from datetime import datetime
import string


urls = [
#a list of URLs to check
]

text_file = open("Output_Clear.txt", "w")

for url in urls:
    response = requests.get(url,timeout=None) 
    soup = BeautifulSoup(response.content, "html.parser") 

    
    if (soup.find_all("",{"class":""}) or soup.find_all("",{"class":""})): # Here write the class of a "wrong" page
        print ("Wrong")
    else:
        print ("True one:"+url)
        text_file.write(', "'+url+'" \n')
        
text_file.close()





