from bs4 import BeautifulSoup
import requests

website_path = r'websites/index.html'

with open(website_path) as f :
    doc = BeautifulSoup(f,"html.parser")

#print(doc)

#print(doc.findAll("p"))

#print(doc.findAll("p")[0])

para0 = doc.findAll("p")[0]

#print(para0.find("b"))

text0 = para0.find("b").string
print(text0)

para0.find("b").string = "This is changed to Hola !!"
print(para0)


#print(para0.findAll("b"))
