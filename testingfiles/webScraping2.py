from bs4 import BeautifulSoup
import requests

linkedin_url = "https://www.linkedin.com/in/rudrax/"

url2 = "https://www.etsy.com/in-en/listing/1098108470/keycap-oreo?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=outemu&ref=sr_gallery-1-24&frs=1"
url3 = "https://kbdfans.com/collections/oem-profile/products/oem-black-backlit-arrow-keycaps?variant=39604701921419"

result = requests.get(url3)
doc = BeautifulSoup(result.text , 'html.parser')

scr0 = doc.findAll('script')[2]
print(scr0.string)
#print(scr0.find(text = "$"))

#print(scr0.findAll(theme))