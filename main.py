# importing FastAPI
from fastapi import FastAPI
from typing import Optional


# creating an instance of FastAPI
app = FastAPI()

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs list'}    
    else:
        return {'data':f'{limit} non published blogs list'}    


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id :int):
    # fetch blog with id = id
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data':{'comments':['abc','xyz','pqr']}}