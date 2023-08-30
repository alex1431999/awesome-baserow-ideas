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
from pynostr.key import PrivateKey
from csv import DictReader
from cryptography.fernet import Fernet

def keyFernetGenerator():
  return Fernet.generate_key()

def objFernet():
 return Fernet(keyFernetGenerator())

def encMessage(message):
 msg = message
 return objFernet().encrypt(msg.encode())

def decMessage(encMessage):
 return objFernet().decrypt(encMessage).decode()

def cryptMessage(message):
 encMessage = encMessage(message)
 obj = {"original":message, "encyptedMessage":encMessage, "decrypted":decMessage(encMessage)}
 return obj

def main(message):
  print(cryptMessage(message))
  return postBase('add_table_id', 'add_token_id', str(cryptMessage['encyptedMessage']))

def writeFile(public_keybench32, private_keybench32):
    with open('password.csv','wb') as file:
        for line in text:
            file.write(public_keybench32)
            file.write(private_keybench32)
    file.close()

def readFile():
    with open('password.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            print(row['public_key'], row['private_key'])
          
def Keys():
  private_key = PrivateKey()
  public_key = private_key.public_key
  public_keybench32 = public_key.bech32()
  private_keybench32 = private_key.bech32()

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

def ExportJson(filename):
  with open(filename, 'w') as f:
    json.dump(listDatabase('results'), f)
  
def ExportCSV(filename):
  return pd.DataFrame(ArrayMap()).to_csv(filename)

def graph(firt_array, end_array):    
  plt.plot(firt_array, end_array)
  plt.xlabel('title')
  plt.ylabel('dataTitle')
  plt.title('My first graph with baserow-api, matplotlib, json, requests!')
  plt.show()


getBase('id_table', 'add_token', 'add_property')
postBase('id_table', 'add_token', listToString(chrome_bookmarks.urls))
