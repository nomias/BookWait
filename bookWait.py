import requests
import smtplib
from bs4 import BeautifulSoup

headers={
    "User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}
URL='https://www.barnesandnoble.com/w/spy-x-family-vol-9-tatsuya-endo/1141652264?ean=9781974736287'
page=requests.get(URL,headers=headers)
#print(page)

soup=BeautifulSoup(page.text,'html.parser')
val=soup.find("input",value="ADD TO CART")
if val is None:
    print("Book not available to cart!")
else:
    print("Book is available to cart!")