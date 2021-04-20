import requests
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['ncovi']

url = "https://corona-api.kompa.ai/graphql"

payload="{\"query\":\"query trendlineVnCases {  trendlineVnCases { date    confirmed   recovered    deaths   __typename  }}\",\"variables\":{}}"
headers = {
  'authority': 'corona-api.kompa.ai',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90"',
  'accept': '*/*',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
  'content-type': 'application/json',
  'origin': 'https://corona.kompa.ai',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://corona.kompa.ai/',
  'accept-language': 'en-US,en;q=0.9'
}


response = requests.request("POST", url, headers=headers, data=payload)
print(response.json()['data']['trendlineVnCases'])

mycol = mydb['trendlineVnCases']
mycol.insert_many(response.json()['data']['trendlineVnCases'])