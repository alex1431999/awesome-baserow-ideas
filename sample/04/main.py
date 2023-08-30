import requests
import json 
import pandas as pd
import numpy as np

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

def ExportJson(filename):
  with open(filename, 'w') as f:
    json.dump(listDatabase('results'), f)
  
def ExportCSV(filename):
  return pd.DataFrame(ArrayMap()).to_csv(filename)
  
ExportCSV("my_data_baserow.csv")
ExportJSON("my_data_baserow.json")
