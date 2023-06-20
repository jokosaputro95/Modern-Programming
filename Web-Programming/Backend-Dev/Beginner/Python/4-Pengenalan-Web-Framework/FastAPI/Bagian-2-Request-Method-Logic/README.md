# Table of Contents
- [GET HTTP Request Method](#get-http-request-method)
- [POST HTTP Request Method](#post-http-request-method)

# GET HTTP Request Method
## Creating a FastAPI Application
Perhatikan kode berikut ini:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/api-endpoint')
async def first_api():
    return {"message": "Welcome to FastAPI Web Framework Python"} 
```

Bedah Kode:

```python
from fastapi import FastAPI
```
Kode tersebut kita lakukan untuk mengimpor kelas FastAPI dari modul fastapi. Ini memungkinkan kita untuk membuat instance aplikasi FastAPI.

```python
app = FastAPI()
```
Kode tersebut memberikan informasi kita membuat instance FastAPI dengan menjalankan kelas FastAPI(). Instance ini mewakili kelas aplikasi kita.

```python
@app.get('/api-endpoint')
```
Kode tersebut memberikan informasi bahwa kita menggunakan dekorator `@app` untuk mendefinisikan API endpoint dengan metode `GET`. API endpoint ini akan diakses melalui path `'/api-endpoint`.

```python
async def first_api():
```
Kode tersebut menunjukan kita mendefinisikan sebuah fungsi dengan nama **first_api()**. Fungsi ini akan dihubungkan dengan API endpoint yang telah kita definisikan sebelumnya. Fungsi ini akan dipanggil ketika API endpoint diakses. Disana kita juga pengguna fungsi `aync` kita juga bisa membuat sebuah fungsi biasa tanpa menggunakan `async`.

```python
return {"message": "Welcome to FastAPI Web Framework Python"}
```
Kode tersebut memberikan informasi bahwa kita menggunakan pernyataan `return` untuk mengembalikan respons dari API. Dalam contoh ini, kita mengembalikan sebuah tipe data dictionary yang berisi pesan **"Welcome to FastAPI Web Framework Python"**. selain tipe data dictionary kita juga bisa mengembalikan nilai dalam bentuk tipe data lainnya seperti: list, str, int, dan sebagainya.

Jika di Recap, step by step:
1. Import `FastAPI`
2. Create a `FastAPI` "instance" (app)
3. Create a path operation (http://127.0.0.1:8000/api-endpoint) atau (/api-endpoint) Operation HTTP Method GET
4. Define a path operation decorator (@app)
5. Define the path operation function `async def first_api():`
6. Return the content 

atau

Recap
1. Impor FastAPI.
2. Buat instance aplikasi.
3. Tulis dekorator operasi jalur seperti @app.get('/').
4. Tulis fungsi operasi jalur seperti first_api():
5. Jalankan server pengembangan

Secara keseluruhan, kode di atas membuat sebuah API endpoint dengan path '/api-endpoint' yang dapat diakses melalui metode GET. Ketika endpoint diakses, fungsi first_api() akan dipanggil dan akan mengembalikan sebuah pesan dalam bentuk JSON. Dengan menggunakan FastAPI, kita dapat dengan mudah membuat API dengan lebih sedikit kode dan dengan dukungan async/await untuk menjalankan operasi yang asinkron.

Menjalankan server pengembangan pada FastAPI:
```bash
uvicorn main:app --reload
```
Maka Ouput pada terminal :
```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12890] using WatchFiles
INFO:     Started server process [12892]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
Informasi tersebut menandakan server FastAPI sudah berjalan dengan baik, selanjutnya anda bisa buka browser kesayangan Anda lalu copy & paste link http://127.0.0.1:8000/api-endpoint di browser Anda.

## Interactive API docs
- Untuk melihat atau mengakses dokumentasi API interaktif otomatis yang disediakan oleh Swagger UI dengan mengakses http://127.0.0.1:8000/docs
- Alternatif API docs, Anda dapat mengakses API API interaktif otomatis yang disediakan oleh ReDoc dengan mengakses http://127.0.0.1:8000/redoc

# Path Parameter
## Apa itu Path Paramter?
Path parameter adalah bagian dari URL yang digunakan untuk menyampaikan data spesifik ke sebuah API endpoint. Dalam FastAPI, path parameter didefinisikan sebagai bagian dari path URL yang diapit oleh tanda kurung kurawal `{}`. Path parameter digunakan untuk mengambil nilai dinamis dari URL dan digunakan dalam logika pemrosesan API. Perlu **diingat** FastAPI memiliki fitur Konfersi Data Otomatis, jika Anda tidak mendefinisikan dengan jelas pada tipe data inputan apa yang diharapkan maka FastAPI akan mengkonversi inputan dan mengembalikan nilai dengan tipe data `String`: Sebagai Contoh perhatikan kode berikut:
```bash
USERS = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "phone": "08771xxxxxxx", "city": "US"},
    {"id": 2, "name": "Jane Jannet", "email": "jane@example.com", "phone": "08772xxxxxxx", "city": "US"},
    {"id": 3, "name": "Calisa Jannet", "email": "calisa@example.com", "phone": "08773xxxxxxx", "city": "Kanada"},
    {"id": 4, "name": "Mark James", "email": "mark@example.com", "phone": "08774xxxxxxx", "city": "Tiongkok"},
    {"id": 5, "name": "Roby Elison", "email": "robyl@example.com", "phone": "08775xxxxxxx", "city": "Kanada"}
]
```
Pada blok kode diatas kita memiliki sekumpulan data user, yang ditampung ke dalam variable `USERS` bertipekan data List. Anda fokus ke bagian field ID. disana ada 2 tipe data yang digunakan sebagai contoh yakni tipe data int, dan string. Jika anda membuat fungsi dan menetapkan path parameter seperti ingin mencari id yang tipe datanya int. maka anda perlu `async def read_user_by_id(id: int):` tetapi jika Anda tidak mendefinisikan secara spesifik misal seperti ini: `async def read_user_by_id(id):` maka yang anda inputkan berupa int return value nya akan menampilkan string. hal itu akan secara otomatis dilakukan oleh FastAPI.

Perhatikan kode berikut ini:
```python
# Urutan 1:
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Urutan 2:
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}
```
Dari kode diatas coba Anda jalankan dan coba execute pada Docs API nya.

Bedah Kode:

Pasti Anda akan menemukan ke janggalan pada Outputnya, dimana jika Bagian I dan II dijalankan, hal ini dikarenakan pada framework FastAPI, urutan deklarasi route handlers sangat penting. Ketika Anda mendefinisikan beberapa fungsi route handler dengan jalur yang sama (misalnya, `"/users"`), FastAPI akan menggunakan urutan deklarasi tersebut untuk menentukan fungsi mana yang harus digunakan. 

Jika Bagian II dijalankan maka FastAPI sekarang melihat `read_user()` terlebih dahulu dan menggunakannya sebagai penangan untuk rute `"/users/{user_id}"`. Kemudian, saat Anda mengakses `"/users/me"`, FastAPI melihat `read_user_me()` dan menggunakan fungsi tersebut sebagai penangan untuk rute itu.

Kemudian perhatikan kode berikut ini:
```python
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/users")
async def read_users2(): # fungsi ini yang akan tampil di Docs API
    return ["Bean", "Elfo"] 
```
Bedah Kode:

Anda mendefinisikan `read_users()` terlebih dahulu, kemudian diikuti oleh `read_users2()`, FastAPI hanya akan melihat fungsi terakhir yang didefinisikan dan menganggapnya sebagai penangan untuk rute tersebut. Oleh karena itu, saat Anda membuka dokumentasi API, yang terlihat hanyalah `async def read_users2()`. Namun itu akan menjadi konflik dan tidak menimbulkan pesan Error tetapi hanya outputnya saja yang janggal, karena Anda menggunakan (`path`) untuk dua fungsi route handler yang berbeda. Untuk menghindari konflik tersebut Anda disarankan merubah pathnya menjadi `"/users"` untuk satu fungsi dan `"/users2"` untuk fungsi lainnya.

- Kesimpulannya adalah: Pastikan Anda tidak menggunakan `PATH` yang sama untuk dua fungsi dua fungsi route handler yang berbeda. Sangat disarankan lebih baik Anda buat PATH yang berbeda di Fungsi yang berbeda.

Perhatikan kode berikut ini:
```python
@app.get('/users/{name}')
async def read_user(name: str):
    for user in USERS:
        if user.get("name").casefold() == name.casefold():
            return user
```
Bedah Kode:

```python
@app.get('/users/{name}')
async def read_user(name: str):
```
Dalam kode tersebut terdapat endpoint API `/users/{name}` yang menggunakan path parameter `name` untuk mengambil nama pengguna sebagai input. `@app.get('/users/{name}')` adalah decorator `@app.get` yang mendefinisikan metode HTTP GET untuk endpoint `/users/{name}`. Ini menunjukkan bahwa endpoint ini akan merespons permintaan GET.

`async def read_user(name: str):` mendefinisikan fungsi `read_user()` yang akan dipanggil ketika endpoint `/users/{name}` diakses. Fungsi ini memiliki parameter `name` yang bertipe data string dan akan menerima nilai dari path parameter `name`.

```python
for user in USERS:
        if user.get("name").casefold() == name.casefold():
            return user
```
Dalam blok kode tersebut, terdapat loop `for` yang akan iterasi melalui setiap `use`r dalam list `USERS`.

Pada setiap iterasi, kita membandingkan nilai `name` yang diterima dari path parameter dengan nama pengguna dalam objek `user`. Kami menggunakan metode `casefold()` untuk membandingkan nama dengan tidak memperhatikan perbedaan besar kecil huruf.
Jika nama pengguna yang cocok ditemukan, maka objek `user` tersebut akan dikembalikan sebagai respons dari API menggunakan pernyataan `return`. Ini akan mengakhiri eksekusi fungsi dan mengirimkan objek user sebagai respons JSON.

Dengan demikian, ketika endpoint /users/{name} diakses, fungsi read_user() akan mencari pengguna dengan nama yang cocok dari list USERS berdasarkan nilai path parameter name, dan mengembalikan objek pengguna tersebut sebagai respons.

# Query Parameter
## Apa itu Query Paramter?
Query parameter adalah komponen dari URL yang digunakan untuk mengirimkan data opsional ke sebuah API endpoint. Dalam FastAPI, query parameter didefinisikan sebagai pasangan "kunci-nilai" yang ditambahkan setelah tanda tanya `?` dalam URL. contoh: `http://127.0.0.1:8000/users?city=US` kode tersebut memberikan suatu pernyataan misalnya jika Anda mengakses `/users?city=US`, itu artinya Anda sedang ingin mencari US pada kumpulan data yang ada pada data users.

Query parameter berguna untuk memberikan fleksibilitas kepada pengguna API dalam mengatur bagaimana data harus diambil atau ditampilkan. Dengan menggunakan query parameter, pengguna dapat melakukan filter, sorting, paginasi, dan operasi lainnya pada data yang dikembalikan oleh API.

Dalam FastAPI, query parameter dapat diterima sebagai argumen fungsi dengan memberikan nilai default. Jika nilai default diberikan, maka query parameter dianggap opsional. Jika pengguna tidak menyertakan query parameter dalam URL, nilai default akan digunakan.

Perhatikan kode berikut ini, kode berikut ini meresume penggunaan query dan path parameter dengan HTTP Method GET:
```python
# Mendapatkan semua pengguna dari kota tertentu menggunakan Query atau Path Parameter
@app.get('/users/bycity')
async def read_users_by_city_path(city: str):
    users_to_return = []
    for user in USERS:
        if user.get("city").casefold() == city.casefold():
            users_to_return.append(user)

    return users_to_return

@app.get('/users/{user_name}/')
async def read_user_phone_by_query(user_name: str, user_phone: str):
    users_to_return = []
    for user in USERS:
        if user.get("name").casefold() == user_name.casefold() and \
                user.get("phone").casefold() == user_phone.casefold():
            users_to_return.append(user)
    
    return users_to_return
```

# POST HTTP Request Method
