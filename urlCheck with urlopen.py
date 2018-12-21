from urllib.request import urlopen
code = urlopen('Your web page').code #url to your web-page
if (code / 100 >= 4):
   print ("Nothing there.")
