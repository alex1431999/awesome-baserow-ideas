import requests
import json
from pynostr.key import PrivateKey

private_key = PrivateKey()
public_key = private_key.public_key

def apiHeader(token):
  return {"Authorization": "Token " + token, "Content-Type": "application/json"}
  
def apiGet(id):
  return "https://api.baserow.io/api/database/rows/table/"+id+"/?user_field_names=true"

def getBase(id, token):
  return requests.get(apiGet(id), headers=apiHeader(token))

def postBase(id, token, string):
  return requests.post(apiGet(id), headers=apiHeader(token), json={"public_key":string})

def listDatabase(id, token, property):
  viewList = json.loads(json.dumps(getBase(id, token).json()))
  return viewList[property]

def viewGet(idTable, token, property):
  public_key = []
  for index, item in enumerate(listDatabase(idTable, token, property)):
    public_key.append(item['public_key'])
  print('public_key: ', public_key)

def main():
  array_map = [private_key.bech32(), public_key.bech32()] 
  for key in in array_map:
    postBase('add_table_id', 'add_token', key)
  print({'public_key': key[0], 'private_key': key[1]})

main()
