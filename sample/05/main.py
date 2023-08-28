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

def forEach(list, function):
    for i, v in enumerate(list):
        function(v, i, ' '.join([str(urlName) for urlName in list]))
      
def ExceptSizeArrayBookmarks(thisArrayNow, valueSizeBookmarks):
  arrays = []
  for i in range(0, len(thisArrayNow), valueSizeBookmarks):
    arrays.append(thisArrayNow[i:i+size])
 return forEach(arrays)

def listURLS(array_bookmark):
  if len(array_bookmark)>3000:
    viewPost('id_table', 'add_token', listToString(ExceptSizeArrayBookmarks(array_bookmark, 100))) # 100.000 or 10.000 or 30.000 or 5.000  bookmarks /100 to table
  else:
    return array_bookmark

def listToString(array):
  return ' '.join([str(urlName) for urlName in array])

def viewPost(idTable, token, arrayMap):
  return postBase(idTable, token, arrayMap)

viewGet('id_table', 'add_token', 'add_property')
viewPost('id_table', 'add_token', listToString(listURLS(chrome_bookmarks.urls))
