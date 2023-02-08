import requests
import re
import json
import pandas as pd
from time import sleep


import warnings
warnings.filterwarnings('ignore')

city = ["nyc","Los-Angeles","chicago","boston","San-Francisco","washington-dc"]
#'austin/'


req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

}

def make_frame(frame):
    for i in data_list:
        for item in i['cat1']['searchResults']['listResults']:
            frame = frame.append(item, ignore_index=True)
    return frame

#just grabbing the first 10 pages per city
data_list=[]
for index in range(len(city)):
    print("City List: ", city[index])
    url='https://www.zillow.com/homes/for_rent/'+city[index]
    #pagina=1
    paginas=11
    for pagina in range (1,paginas,1):
        #print("City List: ", city[index],
        #print("pagina/paginas: ", pagina, "/", paginas)
        if(pagina!=1):
            urls = url+'/'+str(pagina)+'_p/'
        else:
            urls = url
        print("Url formada:",urls)
        sleep(3)
        with requests.Session() as s:
            r1 = s.get(urls, headers=req_headers)
            data1 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r1.text).group(1))
            print("Response data:", data)
        data_list.append(data)
        print("Longitud data_list:", len(data_list))
    df = pd.DataFrame()
    df = make_frame(df)
    #Save df in a csv
    filename='ZillowWebScrapped_'+city[index]+'.csv'
    print("filename: ", filename)
    df.to_csv(filename, index=False)



