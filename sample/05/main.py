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

def listToString(array):
  return ' '.join([str(urlName) for urlName in array])
  
def forEach(list, function):
    for i, v in enumerate(list):
        function(v, i, listToString(list))

def ExceptSizeArrayBookmarks(thisArrayNow, valueSizeBookmarks):
  arrays = []
  for i in range(0, len(thisArrayNow), valueSizeBookmarks):
    arrays.append(thisArrayNow[i:i+size])
 return forEach(arrays)

def listURLS(id_table, add_token, array_bookmark):
  if len(array_bookmark)>3000:
    viewPost(id_table, add_token, listToString(ExceptSizeArrayBookmarks(array_bookmark, 100))) # 100.000 or 10.000 or 30.000 or 5.000  bookmarks /100 to table
  else:
    return array_bookmark

getBase('id_table', 'add_token', 'add_property')
postBase('id_table', 'add_token', listToString('id_table', 'add_token', listURLS(chrome_bookmarks.urls))
