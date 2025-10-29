from bs4 import BeautifulSoup
import requests as req
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait

def setdriver():
    geckodriver_path = "./geckodriver"
    service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=service)

    return driver


def nirf_data():
    url="https://www.nirfindia.org/Rankings/2025/UniversityRanking.html"
    res=req.get(url)
    if res.status_code == 200:
        soup=BeautifulSoup(res.text, 'html.parser')
        table=soup.find(id="tbl_overall")
        rows=table.find_all('tr')
        dic={'Id':[], 'Name':[], 'City':[], 'State':[], 'Score':[], 'Rank':[]}
        for i in range(1, len(rows), 3):
            tds=rows[i].find_all('td')
            dic['Id'].append(tds[0].text)
            dic['Name'].append(tds[1].text.split('More')[0])
            dic['City'].append(tds[-4].text)
            dic['State'].append(tds[-3].text)
            dic['Score'].append(tds[-2].text)
            dic['Rank'].append(tds[-1].text)
        
        df=pd.DataFrame(dic)
        df.to_csv('top_100_nirf_colleges.csv')    
# nirf_data()

def iit_delhi_tenders():
    url='https://home.iitd.ac.in/tenders-archive.php'
    res=req.get(url)
    if res.status_code==200:
        soup=BeautifulSoup(res.text, 'html.parser')
        table=soup.find(id="tenders")
        rows=table.find_all('tr')
        dic={'Nit No.':[], 'Title':[], 'Last Date':[], 'Published On':[]}
        for i in range(1, len(rows)):
            tds=rows[i].find_all('td')
            dic['Nit No.'].append(tds[1].text)
            dic['Title'].append(tds[2].text)
            dic['Last Date'].append(tds[3].text)
            dic['Published On'].append(tds[4].text)
        
        df=pd.DataFrame(dic)
        df.to_csv('iit_delhi_tenders.csv')
# iit_delhi_tenders()


print('hello')











