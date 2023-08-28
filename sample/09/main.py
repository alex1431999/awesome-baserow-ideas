import requests
import json
from cryptography.fernet import Fernet

def apiHeader(token):
  return {"Authorization": "Token " + token, "Content-Type": "application/json"}
  
def apiGet(id):
  return "https://api.baserow.io/api/database/rows/table/"+id+"/?user_field_names=true"

def getBase(id, token):
  return requests.get(apiGet(id), headers=apiHeader(token))

def postBase(id, token, string):
  return requests.post(apiGet(id), headers=apiHeader(token), json={"encryptedMessage":string})

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
  
main("test text with encrypt")
