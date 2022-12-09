# importing FastAPI
from fastapi import FastAPI

# creating an instance of FastAPI
app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Harshit Kashyap'}}