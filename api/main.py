import requests
import json
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import json
import chrome_bookmarks
import todotxtio

def apiHeader(token):
  return {"Authorization": "Token " + token, "Content-Type": "application/json"}
  
def apiGet(id):
  return "https://api.baserow.io/api/database/rows/table/"+id+"/?user_field_names=true"

def getBase(id, token):
  return requests.get(apiGet(id), headers=apiHeader(token))

def postBase(id, token, string):
  return requests.post(apiGet(id), headers=apiHeader(token), json={"urlName":string})

def listToString(array):
  return ' '.join([str(urlName) for urlName in array])

def Connect(add_id_table, add_token_baserow):
  return requests.get("https://api.baserow.io/api/database/rows/table/"+add_id_table+"/?user_field_names=true", headers={"Authorization": "Token "+add_token_baserow})

def dataList(value):
  return enumerate(value)
  
def apiHeader(token):
  return {"Authorization": "Token " + token, "Content-Type": "application/json"}
  
def apiGet(id):
  return "https://api.baserow.io/api/database/rows/table/"+id+"/?user_field_names=true"

def getBase(id, token):
  return requests.get(apiGet(id), headers=apiHeader(token))

def postBase(id, token, string):
  return requests.post(apiGet(id), headers=apiHeader(token), json={"cyphertext":string})

def listDatabase(id, token, property):
  viewList = json.loads(json.dumps(getBase(id, token).json()))
  return viewList[property]

def ArrayMap():
  testTitleName = []
  for index, item in enumerate(listDatabase('add_property_name')):
    testTitleName.append(item['testTitleName'])
  return testTitleName

def ExportJson():
  with open('my_data_baserow.json', 'w') as f:
    json.dump(listDatabase('results'), f)
  
def ExportCSV(filename): # ExportCSV("my_data_baserow.csv")
  return pd.DataFrame(ArrayMap()).to_csv(filename)

def graph(firt_array, end_array):    
  plt.plot(firt_array, end_array)
  plt.xlabel('title')
  plt.ylabel('dataTitle')
  plt.title('My first graph with baserow-api, matplotlib, json, requests!')
  plt.show()


getBase('id_table', 'add_token', 'add_property')
postBase('id_table', 'add_token', listToString(chrome_bookmarks.urls))
