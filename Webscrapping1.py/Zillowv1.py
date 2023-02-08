#Libraries
import requests
import re
import json
import pandas as pd
from time import sleep

import warnings
warnings.filterwarnings('ignore')

#Lista de Ciudades
#city = ["nyc","Los-Angeles","chicago","boston","San-Francisco","washington-dc"]
city = 'Chicago/' #Cambia la ciudad

#URLs hardcoded
url1 = 'https://www.zillow.com/homes/for_rent/'+city
url2 = 'https://www.zillow.com/homes/for_rent/'+city+'/2_p/'
url3 = 'https://www.zillow.com/homes/for_rent/'+city+'/3_p/'
url4 = 'https://www.zillow.com/homes/for_rent/'+city+'/4_p/'
url5 = 'https://www.zillow.com/homes/for_rent/'+city+'/5_p/'
url6 = 'https://www.zillow.com/homes/for_rent/'+city+'/6_p/'
url7 = 'https://www.zillow.com/homes/for_rent/'+city+'/7_p/'
url8 = 'https://www.zillow.com/homes/for_rent/'+city+'/8_p/'
url9 = 'https://www.zillow.com/homes/for_rent/'+city+'/9_p/'
url10 = 'https://www.zillow.com/homes/for_rent/'+city+'/10_p/'

#Not used due to blocked response
"""
url11 = 'https://www.zillow.com/homes/for_rent/'+city+'/11_p/'
url12 = 'https://www.zillow.com/homes/for_rent/'+city+'/12_p/'
url13 = 'https://www.zillow.com/homes/for_rent/'+city+'/13_p/'
url14 = 'https://www.zillow.com/homes/for_rent/'+city+'/14_p/'
url15 = 'https://www.zillow.com/homes/for_rent/'+city+'/15_p/'
url16 = 'https://www.zillow.com/homes/for_rent/'+city+'/16_p/'
url17 = 'https://www.zillow.com/homes/for_rent/'+city+'/17_p/'
url18= 'https://www.zillow.com/homes/for_rent/'+city+'/18_p/'
url19 = 'https://www.zillow.com/homes/for_rent/'+city+'/19_p/'
url20 = 'https://www.zillow.com/homes/for_rent/'+city+'/20_p/'
"""

#Headers make GET the requests, some should be updated every 20 20 calls or 2 cities.
# if required to avoid being banned.
#change user-agent to avoid ip block.
#maybe a multiple user-agent is required.
req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.5',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

with requests.Session() as s:
    r1 = s.get(url1, headers=req_headers)
    r2 = s.get(url2, headers=req_headers)
    r3 = s.get(url3, headers=req_headers)
    r4 = s.get(url4, headers=req_headers)
    r5 = s.get(url5, headers=req_headers)
    r6 = s.get(url6, headers=req_headers)
    r7 = s.get(url7, headers=req_headers)
    r8 = s.get(url8, headers=req_headers)
    r9 = s.get(url9, headers=req_headers)
    r10 = s.get(url10, headers=req_headers)

    data1 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r1.text).group(1))
    data2 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r2.text).group(1))
    data3 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r3.text).group(1))
    data4 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r4.text).group(1))
    data5 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r5.text).group(1))
    data6 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r6.text).group(1))
    data7 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r7.text).group(1))
    data8 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r8.text).group(1))
    data9 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r9.text).group(1))
    data10 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r10.text).group(1))


data_list = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]
            #MORE:  ,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20]

df = pd.DataFrame()

def to_dataframe(dataframe):
    for i in data_list:
        #JSON location
        for item in i['cat1']['searchResults']['listResults']:
            dataframe = dataframe.append(item, ignore_index=True)
    return dataframe

df = to_dataframe(df)
#Save Dataframe to a csv file
df.to_csv('data_Chicago.csv', index=False)
