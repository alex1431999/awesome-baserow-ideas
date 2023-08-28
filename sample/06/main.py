import requests
import json
import todotxtio

def apiHeader(token):
  return {"Authorization": "Token " + token, "Content-Type": "application/json"}
  
def apiGet(id):
  return "https://api.baserow.io/api/database/rows/table/"+id+"/?user_field_names=true"

def getBase(id, token):
  return requests.get(apiGet(id), headers=apiHeader(token))

def postBase(id, token, string):
  return requests.post(apiGet(id), headers=apiHeader(token), json={"taskName":string})
  
def listDatabase(id, token, property):
  viewList = json.loads(json.dumps(getBase(id, token).json()))
  return viewList[property]

def viewGet(idTable, token, property):
  taskName = []
  for index, item in enumerate(listDatabase(idTable, token, property)):
    taskName.append(item['taskName'])
  print('taskName: ', taskName)

def listTodos():
  list_of_todos = todotxtio.from_file('todo.txt')
  return list_of_todos

def listToString(array):
  return ' '.join([str(elem) for elem in array])

def viewPost(idTable, token):
  return postBase(idTable, token, listToString(listTodos()))

viewGet('id_table', 'add_token', 'add_property')
viewPost('id_table', 'add_token')
