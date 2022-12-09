# importing FastAPI
from fastapi import FastAPI


# creating an instance of FastAPI
app = FastAPI()

@app.get('/')
def index():
    return {'data':'bloag list'}


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