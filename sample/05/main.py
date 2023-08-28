import requests
import json
import chrome_bookmarks

def apiHeader(token):
  return {"Authorization": "Token " + token, "Content-Type": "application/json"}
  
def apiGet(id):
  return "https://api.baserow.io/api/database/rows/table/"+id+"/?user_field_names=true"

def getBase(id, token):
  return requests.get(apiGet(id), headers=apiHeader(token))

def postBase(id, token, string):
  return requests.post(apiGet(id), headers=apiHeader(token), json={"urlName":string})
  
def listURLS():
   return chrome_bookmarks.urls

def listToString(array):
  return ' '.join([str(urlName) for urlName in array])

def viewPost(idTable, token):
  return postBase(idTable, token, listToString(listURLS()))

viewGet('id_table', 'add_token', 'add_property')
viewPost('id_table', 'add_token')
