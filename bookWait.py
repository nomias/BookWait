import requests
import smtplib
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

headers={
    "User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}
#URL='https://www.barnesandnoble.com/w/spy-x-family-vol-9-tatsuya-endo/1141652264?ean=9781974736287'
bookList=pd.read_csv('bookList.csv')
ISBN=bookList.ISBN.to_numpy()
#print(ISBN)
URL='https://www.barnesandnoble.com/'
options=webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)
driver.get(URL)
for i in ISBN:
    searchBar=driver.find_element(By.XPATH,"//input[@placeholder='Search by Title, Author, Keyword or ISBN']")
    searchBtn=driver.find_element(By.XPATH,"//button[@class='btn btn-outline-secondary rhf-search-btn']")
    searchBar.send_keys(f'{i}')
    searchBtn.click()
    bookUrl=driver.current_url
    row_num=bookList[bookList['ISBN']==i].index.values
    row_num_val=row_num.item(0)
    bookList.loc[row_num_val,'URL']=bookUrl
    page=requests.get(bookUrl,headers=headers)
    #print(page)

    soup=BeautifulSoup(page.text,'html.parser')
    val=soup.find("input",value="ADD TO CART")
    if val is None:
        print("Book not available to cart!")
        bookList.loc[row_num_val,'Status']=0
    else:
        print("Book is available to cart!")
        bookList.loc[row_num_val,'Status']=1
    bookList.to_csv('bookList.csv',index=False)