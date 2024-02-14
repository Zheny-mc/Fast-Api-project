#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi import HTTPException
from database import User
from database import database as connection
from schemas import UserRequestModel
from schemas import UserResponseModel

# uvicorn main:app --reload
# http://localhost:8000
# Documentation on: # http://localhost:8000/docs
app = FastAPI(title='Simple API',
              description='A brief description of the project',
              version='1.0.1')

# Using events to configure
@app.on_event('startup')
def starup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

# http://localhost:8000/
# use async in order to use asyncronous treads
@app.get('/')
def index():
    return 'Hello World'

# http://localhost:8000/
@app.get('/about')
async def about():
    return 'This is our about endpoint'

# http://localhost:8000/users
@app.post('/users')
async def create_user(user_request: UserRequestModel):
    user = User.create(
        username=user.username,
        email=user.email
        )
    return user_request

# http://localhost:8000/users/user_id
@app.get('/users/{user_id}')
async def get_user(user_id):
    user = User.select().where(User.id == user_id).first()
    if user:
        return UserResponseModel(id=user.id,
                                 username=user.username,
                                 email=user.email)
    else:
        return HTTPException(404, 'User Not Found')

# http://localhost:8000/users/user_id
@app.delete('/users/{user_id}')
async def delete_user(user_id):
    user = User.select().where(User.id == user_id).first()
    if user:
        return UserResponseModel(id=user.id,
                                 username=user.username,
                                 email=user.email)
    else:
        return HTTPException(404, 'User Not Found')