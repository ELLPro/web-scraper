from bs4 import BeautifulSoup 
import requests 



number = 0
text_file = open("Output.txt", "w")



for i in range (30000,53001):
    string=' ,"Blablabla/'+str(i)+'/blabla''"' # generates us URLs with ID's we need
    text_file.write(string+'\n')
    print (string)

text_file.close()
