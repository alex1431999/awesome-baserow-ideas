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
 return objFernet().encrypt(message.encode())

def decMessage(encMessage):
 return objFernet().decrypt(encMessage).decode()

def cryptMessage(message):
 return {"original":message, "encyptedMessage": encMessage(message), "decrypted": decMessage(encMessage)}

def EchoPrintln(message):
  return print(cryptMessage(message))
  
def main(message):
  EchoPrintln(message)
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
  return {'public_keybench32': public_key.bech32(), 'private_keybench32': private_key.bech32()}

def api_header(token):
  return {"Authorization": "Token " + token, "Content-Type": "application/json"}
  
def api_get(id):
  return "https://api.baserow.io/api/database/rows/table/"+id+"/?user_field_names=true"

def api_http_get(id, token):
  return requests.get(api_get(id), headers=api_header(token))

def json_property(nameProperty, typeProperty):
  return {nameProperty:type}
  
def api_http_post(id, token, string):
  return requests.post(api_get(id), headers=api_header(token), json=json_property('nameProperty', string))

def listToString(array):
  return ' '.join([str(urlName) for urlName in array])

def ListThis(value):
  return enumerate(value)
    
def ListOf(id, token, property):
  return json.loads(json.dumps(getBase(id, token).json()))[property]

def ArrayMap():
  array = []
  for index, item in enumerate(listDatabase('add_property_name')):
    array.append(item['testTitleName'])
  return array

def ExportJson(filename):
  with open(filename, 'w') as f:
    json.dump(ListOf('results'), f)
  
def ExportCSV(filename):
  return pd.DataFrame(ArrayMap()).to_csv(filename)

def graph(firt_array, end_array):    
  plt.plot(firt_array, end_array)
  plt.xlabel('title')
  plt.ylabel('dataTitle')
  plt.title('My first graph with baserow-api, matplotlib, json, requests!')
  return plt.show()

api_http_get('id_table', 'add_token', 'add_property')
api_http_post('id_table', 'add_token', listToString(chrome_bookmarks.urls))
