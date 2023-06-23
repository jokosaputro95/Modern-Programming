from fastapi import Body, FastAPI

app = FastAPI() # * Membuat instance dari kelas FastAPI

# * Inisialisasi Path dengan tanda ("/")
@app.get("/") # * http://127.0.0.1:8000/ default akses url
async def root():
    return {"message": "Hello World, Welcome to FastAPI Web Framework"}

@app.get("/api-endpoint") # * http://127.0.0.1:8000/api-endpoint
async def first_api():
    return {"message": "Welcome to path '/api-endpoint', Response HTTP GET Method"} 

# * Membuat list users
USERS = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "phone": "08771xxxxxxx", "country": "US"},
    {"id": 2, "name": "Jane Jannet", "email": "jane@example.com", "phone": "08772xxxxxxx", "country": "US"},
    {"id": 3, "name": "Calisa Jannet", "email": "calisa@example.com", "phone": "08773xxxxxxx", "country": "Kanada"},
    {"id": 4, "name": "Mark James", "email": "mark@example.com", "phone": "08774xxxxxxx", "country": "Tiongkok"},
    {"id": 5, "name": "Roby Elison", "email": "robyl@example.com", "phone": "08775xxxxxxx", "country": "Kanada"}
]

# Todo: Creating endpoint API users
# * HTTP GET Method
@app.get("/users") # * http://127.0.0.1:8000/users
async def read_all_users():
    return USERS

# * HTTP GET Using PATH Parameters
"""
# Todo: example path dynamic pamaters, will be open Docs API url http://127.0.0.1:8000/docs
@app.get("/users/{dynamic_param}") # * http://127.0.0.1:8000/users/{dynamic_param}?dynamic_params=good%21
async def read_all_dynamic_params(dynamic_params: str):
    return {"dynamic_params": dynamic_params}
"""

"""
# TODO: Kemudian Anda jalankan juga yang kode ini Bagian I:
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# TODO: Kemudian anda tukar posisi nya menjadi seperti ini Bagian II:
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}
"""

@app.get("/users/{user_name}") # * http://127.0.0.1:8000/users/Mark%20James
async def read_user_by_name(user_name: str):
    for user in USERS:
        if user.get("name").casefold() == user_name.casefold():
            return user

# * HTTP GET Using Query Parameters
@app.get("/users/")
async def read_user_email_by_query_params(user_email: str): # * http://127.0.0.1:8000/users/?user_email=calisa%40example.com
    user_email_to_return = []
    for user in USERS:
        if user.get("email").casefold() == user_email.casefold():
            user_email_to_return.append(user)

    return user_email_to_return

# Todo: Mendapatkan semua pengguna dari kota tertentu menggunakan Query atau Path Parameter
@app.get("/users/bycountry/")
async def read_user_by_country_path(user_country: str): # * http://127.0.0.1:8000/users/bycountry/?user_country=kanada
    user_city_to_return = []
    for user in USERS:
        if user.get("country").casefold() == user_country.casefold():
            user_city_to_return.append(user)

    return user_city_to_return

@app.get("/users/{user_id}/")
async def read_user_email_country_by_query(user_id: int, email: str, country: str): # * http://127.0.0.1:8000/users/1/?email=john%40example.com&country=US
    user_to_return = []
    for user in USERS:
        if (
            user.get("id") == user_id and
            user.get("email").casefold() == email.casefold() and
            user.get("country").casefold() == country.casefold()
        ):
            user_to_return.append(user)
    
    return user_to_return

# * HTTP POST Method
@app.post("/users/create_user")
async def create_user(new_user: dict = Body(...)): # * http://127.0.0.1:8000/users/create_user
    USERS.append(new_user)

# * HTTP PUT Method
@app.put("/users/update_country")
async def update_phone(updated_country: dict = Body(...)): # * http://127.0.0.1:8000/users/update_phone
    for i, user in enumerate(USERS):
        if user["country"].lower() == updated_country["country"].lower():
            USERS[i] = updated_country

# * HTTP DELETE Method
@app.delete("/users/delete_user/{user_name}")
async def delete_user(user_name: str): # * http://127.0.0.1:8000/users/delete_user/Jane%20Jannet
    for i, user in enumerate(USERS):
        if user.get("name").casefold() == user_name.casefold():
            USERS.pop(i)
            break

# @app.delete('/users/{user_id}')
# async def delete_user(user_id: int):
#     for i in range(len(USERS)):
#         if USERS[i]['id'] == user_id:
#             del USERS[i]
#             return {"message": "User deleted successfully."}
#     return {"message": "User not found."}
"""
# * Menggunakan model list comprehension
@app.delete('/user/{id}')
async def delete_user_by_id(id: int):
    pengguna_terhapus = [pengguna for pengguna in USERS if pengguna["id"] == id]
    if not pengguna_terhapus:
        return f"ID pengguna {id} tidak ditemukan!"
    else:
        pengguna_tersisa = [pengguna for pengguna in USERS if pengguna["id"] != id]
        USERS[:] = pengguna_tersisa  # Memperbarui daftar USERS untuk menghapus pengguna yang terhapus
        return {"pesan": f"Pengguna dengan ID {id} telah dihapus", "pengguna_terhapus": pengguna_terhapus, "pengguna_tersisa": pengguna_tersisa}
    
# * Tidak menggunakan model list comprehension
@app.delete('/user/{id}')
async def delete_user_by_id(id: int):
    pengguna_terhapus = []
    for pengguna in USERS:
        if pengguna["id"] == id:
            pengguna_terhapus.append(pengguna)
            USERS.remove(pengguna)
            break
    if not pengguna_terhapus:
        return f"ID pengguna {id} tidak ditemukan!"
    else:
        pengguna_tersisa = USERS
        return {"pesan": f"Pengguna dengan ID {id} telah dihapus", "pengguna_terhapus": pengguna_terhapus, "pengguna_tersisa": pengguna_tersisa}

"""