import requests
import json 
import pandas as pd
import numpy as np
import json

def Connect(add_id_table, add_token_baserow):
  return requests.get("https://api.baserow.io/api/database/rows/table/"+add_id_table+"/?user_field_names=true", headers={"Authorization": "Token "+add_token_baserow})

def listDatabase(add_property_name):
  viewList = json.loads(json.dumps(Connect('add_id_table','add_token_baserow').json()))
  return viewList[add_property_name]

def ArrayMap():
  testTitleName = []
  for index, item in enumerate(listDatabase('add_property_name')):
    testTitleName.append(item['testTitleName'])
  return testTitleName

def ExportJson():
  with open('my_data_baserow.json', 'w') as f:
    json.dump(listDatabase('results'), f)
  
def ExportCSV():
  # arr = np.arange(testTitleName).reshape(testTitleLastName)  # arr = np.arange(1,11).reshape(2,5)
  dataFrame  = pd.DataFrame(ArrayMap()) # pd.DataFrame(testTitleName)
  dataFrame.to_csv("my_data_baserow.csv")
  
ExportCSV()
ExportJSON()
