import plotly.express as px
from baserow.client import BaserowClient

client = BaserowClient('https://baserow.io', jwt='...')
# fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2]) # fig.show()

for db in client.list_all_applications():
  px.bar(x=[t.name for t in db.tables], y=[db]).show()
