from bs4 import BeautifulSoup
import requests
import csv

alljobs = []

def writetocsv(alljobs):

    with open('joblist.csv', 'w', newline="", encoding='utf-8') as f:
        keys = alljobs[0].keys()
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(alljobs)

url = 'https://www.indeed.com/jobs?q=ios+developer&l=Remote'
htmldata = requests.get(url)
soupdata = BeautifulSoup(htmldata.text, "html.parser")
jobcard = soupdata.find_all('div', 'jobsearch-SerpJobCard')
for onecard in jobcard:
    dic = {}
    try:
        titetag = onecard.h2.a
        jobtile = titetag.get('title')
        companyname = onecard.find('span', 'company').text.strip()
        joblocation = onecard.find('div', 'location').text.strip()
        #print(joblocation)
        #print(onecard)
        #print("Title : {}   Company:{} Location : {}".format(jobtile, companyname, joblocation))
        dic['tile'] = jobtile
        dic['company'] = companyname
        dic['location'] = joblocation
        alljobs.append(dic)
    except Exception as e:
        joblocation = onecard.find('span', 'location').text.strip()
        #print("Title : {}   Company:{} Location : {}".format(jobtile, companyname, joblocation))
        dic['tile'] = jobtile
        dic['company'] = companyname
        dic['location'] = joblocation
        alljobs.append(dic)
        #print(e)
        #print(onecard)
        #print("Title : {}   Company:{}".format(jobtile, companyname))

writetocsv(alljobs)

