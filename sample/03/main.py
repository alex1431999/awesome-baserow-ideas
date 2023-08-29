import requests
import json 
import matplotlib.pyplot as plt

def Connect(add_id_table, add_token_baserow):
  return requests.get("https://api.baserow.io/api/database/rows/table/"+add_id_table+"/?user_field_names=true", headers={"Authorization": "Token "+add_token_baserow})

def listDatabase(add_property_name):
  viewList = json.loads(json.dumps(Connect('add_id_table','add_token_baserow').json()))
  return viewList[add_property_name]

def dataList(value):
  return enumerate(value)

def graph():
  testTitleName = []
  testTitleLastName = []
  
  for index, item in dataList(listDatabase('add_property_name')):
    testTitleName.append(item['testTitleName'])
    testTitleLastName.append(item['testTitleLastName']) 
  
  plt.plot(testTitleName, testTitleLastName)
  plt.xlabel('title')
  plt.ylabel('dataTitle')
  plt.title('My first graph with baserow-api, matplotlib, json, requests!')
  plt.show()

graph()
