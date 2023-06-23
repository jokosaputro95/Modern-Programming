from fastapi import FastAPI

app = FastAPI()

@app.get('/') # /
async def root():
    return {"message": "Hello, World!"}

USERS = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "phone": "08771xxxxxxx", "city": "US"},
    {"id": 2, "name": "Jane Jannet", "email": "jane@example.com", "phone": "08772xxxxxxx", "city": "US"},
    {"id": 3, "name": "Calisa Jannet", "email": "calisa@example.com", "phone": "08773xxxxxxx", "city": "Kanada"},
    {"id": 4, "name": "Mark James", "email": "mark@example.com", "phone": "08774xxxxxxx", "city": "Tiongkok"},
    {"id": 5, "name": "Roby Elison", "email": "robyl@example.com", "phone": "08775xxxxxxx", "city": "Kanada"}
]

@app.get('/users')
async def get_all_users():
    return USERS

@app.get('/users/{id}')
async def get_user_by_id(id: int):
    for user in USERS:
        if user["id"] == id:
            return user
    return f"user yang anda cari dengan id {id} tidak ditemukan"

@app.post('/users')
async def create_new_user(
    name: str,
    email: str,
    phone: str,
    city: str
):
    new_user = {
        "id": len(USERS) + 1,
        "name": name,
        "email": email,
        "phone": phone,
        "city": city
    }

    USERS.append(new_user)
    return new_user


@app.put('/users/{id}')
async def updated_user_by_id(
    id: int,
    name: str,
    email: str,
):
    for user in USERS:
        if user["id"] == id:
            user["name"] = name
            user["email"] = email

            return user
        
    return f"user id {id} is not found!"

@app.delete('/users/{id}')
async def delete_by_id(id: int):
    user_deleted = []
    for user in USERS:
        if user["id"] == id:
            user_deleted.append(user)
            USERS.remove(user)
            break

    if not user_deleted:
        return f"ID user {id} not found!"
    else:
        user_update = USERS
        return {
            "message": f"User dengan id {id} telah di hapus",
            "user_deleted": user_deleted,
            "user_update": user_update
        }