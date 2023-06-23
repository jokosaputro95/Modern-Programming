import uvicorn
from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

# create a model
class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    country: str

USERS = []

@app.get('/users')
async def get_all_users():
    return USERS

@app.get('/user/{id}')
async def get_user_by_id(id: int):
    for user in USERS:
        if user.id == id:
            return user
    return f"user {id} is not found!"


# POST using request Body
@app.post('/user')
async def create_user(user: User):
    USERS.append(user)
    return USERS


# * POST using input paramters
"""
# Todo: Cara 1 Using Modul Form
@app.post('/user')
async def create_user(
    id: int = Form(...),
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    country: str = Form(...)
):
    user = User(id=id, name=name, email=email, phone=phone, country=country)
    USERS.append(user)
    return USERS
"""
"""
# Todo: Cara 2 Using path parameter
@app.post('/user')
async def create_user(
    user_id: int,
    user_name: str,
    user_email: str,
    user_phone: str,
    user_country: str
):
    new_user = User(id = user_id, name = user_name, email = user_email, phone = user_phone, country = user_country)
    USERS.append(new_user)
    return USERS
"""
"""
# Todo: Cara 3 Using path parameter
@app.post('/user')
async def add_user(user: User):
    new_user = {
        'id': len(USERS) + 1,
        'name': user.name,
        'email': user.email,
        'phone': user.phone,
        'country': user.country
    }
    USERS.append(new_user)
    return new_user
"""

@app.put('/user/{id}')
async def updated_user_by_id(id: int, updated_user: User):
    for i, user in enumerate(USERS):
        if user.id == id:
            USERS[i] = updated_user
            return USERS
    return f"user id {id} is not found!"

@app.delete('/user/{id}')
async def delete_user_by_id(id: int):
    user_temp = [user for user in USERS if user.id != id]
    return user_temp





if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)