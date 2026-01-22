from data import entry
from fastapi import FastAPI
from database import getData ,add_data,update_data,del_data
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["http://127.0.0.1:5500"],
                   allow_methods=['*'])
entries=[
    entry(s_no=3,age=36,weight=50,height=163),
    entry(s_no=4,age=16,weight=50,height=150),
]
@app.get('/entries')
def get_entries():
    return getData()
@app.get('/entries/{s_no}')
def get_entries(id:int):
    entries=getData()
    for i in entries:
        if i.s_no== s_no:
            return i
        return "404"

@app.post('/entries')
def add_entry(entry:entry):
    return add_data(entry)
@app.put('/entries')
def update_entries(s_no:int,entry:entry):
    return update_data(s_no,entry)

@app.delete('/entry')
def del_entry(s_no:int):
    return del_data(s_no)