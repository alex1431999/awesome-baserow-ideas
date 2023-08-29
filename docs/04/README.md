Hi guys.

## **1. Disclaimer**
**1.1** I would like to contribute to this specific topic: Todo-txt format in Api Baserow. For example, there is a library called [todotxtio](https://epocdotfr.github.io/todotxtio/) which read todotxt files. Initially, I thought I’d respond here instead of the topic, since I’d rather do an initial demo.

**1.2** Add pip install to: requests json todotxtio

**1.3** Create a file called [todo.txt](https://github.com/todotxt/todo.txt) and an file called main.py

**1.4** Use the baserow api to send and receive data: todo.txt. By default, the Baserow API works through get and post http calls.

**1.5** txt format is a simple set of rules that make todo.txt both human and machine-readable . The format supports priorities, creation and completion dates, projects

## **2. Create a file called todo.txt and main.py**
It is important to create these files if you want to do this process automatically with a few clicks.

**2.1 filename: ./todo.txt**
Here we read a txt file with information line by line of txt tasks.

```markdown
(A) Thank Mom for the meatballs @phone
```

**2.2 filename: ./main.py**
Here is a python script that reads the todotxt file locally and imports it in a post request to Baserow.

```python
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
```

## **3. Data**
add image

## **4. Final considerations**
**4.1** What do you all think of this idea?
**4.2** This code is in the public domain, use or modify it however you want.
**4.3** The codebase of this code is the same one I developed to generate graphs in Baserow etc
**4.4** This code is something basic for demonstration purposes.
**4.5** I hope to contribute in some way to the Baserow community.
**4.6** If you all have any questions, call me here and I’ll see how I can help
