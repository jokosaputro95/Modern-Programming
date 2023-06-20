# Validasi Data
Validasi data adalah proses memastikan bahwa data yang diterima atau diproses sesuai dengan aturan atau persyaratan yang telah ditentukan. Validasi data penting dalam pengembangan API karena beberapa alasan:

1. Keamanan: Validasi data membantu mencegah serangan keamanan seperti injeksi SQL atau serangan skrip silang (cross-site scripting) dengan memastikan bahwa data yang diterima atau ditampilkan tidak berisi kode berbahaya.

2. Integritas data: Validasi data membantu memastikan bahwa data yang masuk ke sistem sesuai dengan format yang diharapkan atau persyaratan bisnis. Ini membantu menjaga integritas data dan mencegah kesalahan atau kerusakan data.

3. Konsistensi: Validasi data membantu memastikan bahwa data yang diterima memiliki tipe yang benar, nilai yang valid, dan format yang sesuai. Hal ini memastikan bahwa data yang diproses secara konsisten dan dapat diandalkan.

4. Penggunaan sumber daya yang efisien: Dengan memvalidasi data sejak awal, API dapat menghindari pemrosesan data yang tidak valid atau tidak perlu, menghemat waktu dan sumber daya.

5. Pesan kesalahan yang jelas: Dengan validasi data, API dapat memberikan pesan kesalahan yang informatif kepada pengguna jika ada masalah dengan data yang diberikan. Hal ini membantu pengguna memperbaiki masalah dengan cepat dan mengurangi kesalahan dalam penggunaan API.

# Pydantic
## Apa itu Pydantic?
Pydantic adalah sebuah pustaka Python yang digunakan untuk memvalidasi dan mengurai data, dengan dukungan untuk serialisasi, deserialisasi, dan dokumentasi otomatis. Dalam konteks FastAPI, Pydantic digunakan untuk mendefinisikan model data dan aturan validasi untuk data yang diterima atau dikirimkan melalui API.

## Bagaimana cara kerja Pydantic?
Pydantic bekerja dengan cara melakukan validasi otomatis berdasarkan anotasi tipe data yang ditentukan dalam model. Anotasi tipe data Pydantic mendefinisikan tipe data dan aturan validasi untuk setiap field dalam model. Saat data diterima atau dikirimkan melalui API, Pydantic akan memeriksa apakah data tersebut sesuai dengan aturan validasi yang telah ditentukan. Jika data tidak valid, Pydantic akan menghasilkan pesan kesalahan yang sesuai.

Perhatikan baris kode berikut ini:
```python
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
```

Penjelasan kode:
Dalam kode yang diberikan, terdapat beberapa blok yang dapat dijelaskan diantaranya:

1. Deklarasi model User sebagai subkelas dari BaseModel Pydantic. Model ini mendefinisikan struktur dan aturan validasi untuk data pengguna.

2. Fungsi `get_all_users` yang mengembalikan daftar pengguna saat melakukan permintaan GET ke `/users`.

3. Fungsi `get_user_by_id` yang mencari pengguna berdasarkan **ID** saat melakukan permintaan GET ke `/user/{id}`.

4. Fungsi `create_user` yang menambahkan pengguna baru ke dalam daftar USERS saat melakukan permintaan POST ke `/user`. Data pengguna yang diterima divalidasi menggunakan model User yang telah didefinisikan sebelumnya.

5. Fungsi `updated_user_by_id` yang memperbarui pengguna berdasarkan **ID** saat melakukan permintaan PUT ke `/user/{id}`. Data pengguna yang diterima divalidasi menggunakan model User.

6. Fungsi `delete_user_by_id` yang menghapus pengguna berdasarkan **ID** saat melakukan permintaan DELETE ke `/user/{id}`.

Pada bagian komentar di bawah fungsi `create_user`, terdapat dua pendekatan yang disorot untuk menerima data pengguna melalui parameter. Yang pertama menggunakan `Form` untuk mendefinisikan parameter sebagai bagian dari permintaan `form-encoded`, dan yang kedua menggunakan `path parameter` untuk mengambil nilai dari path URL.

Bagian terakhir menggunakan `uvicorn.run` untuk menjalankan aplikasi FastAPI dengan mengimpor aplikasi dari modul main dan mengaktifkan mode reload untuk pengembangan.