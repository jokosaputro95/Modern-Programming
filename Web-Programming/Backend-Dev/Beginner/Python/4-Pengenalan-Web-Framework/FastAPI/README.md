# Hallo **everyone!** Selamat datang di kelas FastAPI Web Framework.

Kelas ini membahas tentang Pengenalan FastAPI berikut Dokumentasi Otomatis, Routing, Model Tipe Data, dan Validasi Data.

# Table of Contents
- [Pre-Test dan Post-Test](#exam)
- [Pengenalan FastAPI](#pengenalan-fastapi)
- [Routing Overview](#routing)
- [Model Tipe Data Overview](#model-tipe-data)
- [Validasi Data Overview](#validasi-data)
- [Persiapan Belajar](#persiapan-belajar)
- [Prasyarat Tools](#prasyarat-tools)
- [Mekanisme Belajar](#mekanisme-belajar)
- [Forum Diskusi](#forum-diskusi)
- [Materi Pembahasan](#materi-yang-akan-dibahas)

# Exam
Sebelum Anda memulai pembelajaran pada kelas ini, terlebih dahulu Anda dianjurkan untuk menyelesaikan/Mengerjakan soal pre-test. Soal pre-test dapat diakses melalui url ini: [pre-test](https://forms.gle/Ccs4SVPi2SubU1JZ8).

Setelah Anda mempelajari seluruh topik pembahasan pada kelas ini, Anda dianjurkan untuk menyelesaikan/mengerjakan soal post-test, hal ini diperlukan untuk mengevaluasi pemahaman Anda. Soal post-test dapat diakses melalui link url ini: [post-test](https://forms.gle/pFf3D5jfM2XD7QoE8).

# Pengenalan FastAPI

> FastAPI framework, high performance, easy to learn, fast to code, ready for production

## Apa itu FastAPI dan mengapa itu penting?
FastAPI adalah kerangka kerja (*Framework*) Python modern dan cepat untuk membangun web API. FastAPI didukung oleh konsep-konsep dari kerangka kerja [Starlette](https://www.starlette.io/) dan [Pydantic](https://docs.pydantic.dev/latest/). 

FastAPI dirancang untuk memberikan performa tinggi dengan dukungan penuh terhadap *asynchronous programming*, tidak hanya itu FastAPI juga mendukung dokumentasi otomatis dan validasi data yang kuat. FastAPI juga memiliki basis pengguna yang luas dan aktif dalam komunitas pengembangan Python.

## Fitur dan Keunggulan FastAPI
Mengenai fitur apa saja yang terdapat pada FastAPI mungkin Anda dapat melihat nya di situs [resmi](https://fastapi.tiangolo.com/features/). Namun disini akan sedikit dijelaskan singkat terkait keunggulan FastAPI jika dibandingkan dengan kerangka kerja (*Framework*) Python web lainnya:

- Kecepatan eksekusi yang tinggi dengan dukungan untuk *asynchronous programming*.
- Validasi data yang kuat dengan menggunakan model tipe data Pydantic.
- Dukungan untuk dokumentasi otomatis melalui integrasi dengan Swagger UI dan Redoc.
- Kemudahan dalam menangani parameter jalur, parameter query, dan parameter lainnya dalam rute.
- Kode yang mudah dibaca dan dipahami berkat adopsi dari Python type hints.
- Kemudahan dalam instalasi dan konfigurasi awal FastAPI.

## Pengguna FastAPI
FastAPI telah menjadi populer dikalangan banyak perusahaan dan platform diseluruh dunia. Berikut adalah beberapa contoh perusahaan dan platform yang telah menggunakan FastAPI.

1. Netflix: Netflix menggunakan FastAPI untuk beberapa bagian dari infrastruktur dan layanan internal mereka.
2. Microsoft: Microsoft telah mengadopsi FastAPI dalam beberapa proyek internal dan layanan Azure Functions.
3. Uber: Uber menggunakan FastAPI untuk mengembangkan dan mengelola sejumlah layanan API internal mereka.
4. TransferWise (sekarang Wise): TransferWise, sebuah perusahaan fintech global, telah menggunakan FastAPI dalam pengembangan API mereka.
5. Square: Square, sebuah perusahaan pembayaran digital, telah mengimplementasikan FastAPI dalam sejumlah proyek mereka.
6. HubSpot: HubSpot, platform pemasaran dan penjualan terkemuka, telah menggunakan FastAPI dalam beberapa komponen infrastruktur mereka.
7. MyFitnessPal: MyFitnessPal, sebuah platform untuk manajemen kebugaran dan nutrisi, telah mengadopsi FastAPI untuk pengembangan API mereka.
8. Mercado Libre: Mercado Libre, perusahaan e-commerce terbesar di Amerika Latin, menggunakan FastAPI dalam beberapa layanan API mereka.
9. Namecheap: Namecheap, sebuah perusahaan penyedia layanan hosting dan registrasi domain, telah mengimplementasikan FastAPI dalam pengembangan beberapa fitur API mereka.
10. TiDB: TiDB, sebuah database terdistribusi open-source, telah menggunakan FastAPI dalam beberapa komponen manajemen dan monitoring mereka.

Itu hanya beberapa contoh dari banyak perusahaan dan platform yang telah mengadopsi FastAPI. Penggunaan FastAPI terus berkembang seiring dengan peningkatan popularitasnya sebagai kerangka kerja (*Framework*) yang efisien dan produktif untuk pengembangan API Python.

# Routing
## Apa itu Routing?
Routing dalam konteks FastAPI mengacu pada proses menghubungkan URL atau endpoint tertentu dengan fungsi tertentu dalam aplikasi web. Routing memungkinkan Anda untuk menentukan bagaimana aplikasi Anda merespons permintaan HTTP yang masuk.

Analogi sederhananya seperti ini:
> Bayangkan Anda sedang mengendarai mobil dan ingin mencapai tujuan Anda. Untuk mencapai tujuan tersebut, Anda harus mengikuti rute atau jalur yang ditentukan di jalan. Setiap rute atau jalur memiliki tujuan atau destinasi tertentu. Dalam hal ini, Anda sebagai pengemudi adalah server aplikasi, mobil Anda adalah aplikasi web, dan tujuan Anda adalah fungsi atau penanganan yang sesuai untuk setiap URL atau endpoint.

## Bagaimana cara mendefinisikan dan menggunakan rute (route) dengan FastAPI?
Mendefinisikan Rute (Route) dengan FastAPI:
- Anda dapat mendefinisikan rute menggunakan dekorator `@app.get`, `@app.post`, `@app.put`, dan lainnya pada instance aplikasi FastAPI.
- Dekorator ini menghubungkan fungsi tertentu dengan metode HTTP yang sesuai seperti **GET, POST, PUT**, dll.

Menggunakan Dekorator `@app.get`, `@app.post`, `@app.put`, dan Sebagainya:
- Anda dapat menggunakan dekorator `@app.get` untuk menghubungkan fungsi ke metode HTTP **GET**, `@app.post` untuk metode HTTP **POST**, dan seterusnya.
- Misalnya, `@app.get("/items/{item_id}")` akan menghubungkan fungsi tertentu dengan URL **"/items/{item_id}"** dan akan merespons permintaan **GET** pada URL tersebut.

## Bagaimana menangani Parameter Jalur(Path Parameters), Parameter Query(Query Parameters), dan Parameter Lainnya dalam Rute?
FastAPI mendukung penanganan parameter jalur (path parameters), parameter query (query parameters), dan parameter lainnya dalam rute.

> - Parameter jalur adalah bagian dari URL yang digunakan untuk mengidentifikasi sumber daya tertentu, seperti **"/items/{item_id}"**.
> - Parameter query adalah bagian dari URL yang digunakan untuk mengirim data opsional ke server melalui URL, seperti **"/items?category=books"**.

FastAPI memungkinkan Anda mendefinisikan parameter-parameter ini langsung dalam deklarasi fungsi, menggunakan tipe data dan anotasi khusus.

Dengan menggunakan routing dalam FastAPI, Anda dapat mengarahkan permintaan HTTP ke fungsi yang sesuai, menangani parameter yang diberikan dalam URL, dan mengontrol respons yang dikirimkan kembali ke klien. Ini memungkinkan Anda untuk membangun API yang kuat dan fleksibel dengan mudah.

# Model Tipe Data
## Apa itu Model Tipe Data?
Model Tipe Data dalam konteks FastAPI merujuk/mengacu pada penggunaan model tipe data Pydantic untuk mendefinisikan struktur data/schema data yang akan digunakan dalam API Anda. Model tipe data ini memungkinkan Anda untuk menentukan tipe data untuk setiap field dalam model, melakukan validasi data, dan mengatur data yang opsional atau memiliki nilai default yang diterima dan dikirim oleh API.

Secara garis besar Model Tipe Data:
- Model tipe data adalah representasi struktur data yang digunakan dalam API Anda.
- Model tipe data mendefinisikan skema data yang harus diterima atau dikirim oleh API.
- Model tipe data membantu dalam validasi data masukan, konversi tipe data, dan memberikan dokumentasi yang jelas.

Analogi sederhananya seperti ini:
> Bayangkan Anda ingin membuat formulir pendaftaran untuk acara, dan setiap peserta harus mengisi beberapa informasi seperti nama, alamat email, dan usia. Formulir ini berfungsi sebagai schema data untuk pendaftaran peserta acara. Setiap field pada formulir memiliki tipe data tertentu, seperti string untuk nama, string untuk alamat email, dan integer untuk usia. Selain itu, ada juga aturan validasi tertentu, misalnya, usia harus di atas 18 tahun. Dalam hal ini, formulir pendaftaran adalah model tipe data, dan setiap field pada formulir adalah field dalam model.

## Menggunakan Model Tipe Data Pydantic untuk Mendefinisikan Schema Data
1. Anda dapat menggunakan Pydantic, Pydantic adalah library Python yang digunakan untuk mendefinisikan model tipe data dan validasi data.
2. Anda dapat membuat kelas model menggunakan Pydantic untuk mendefinisikan struktur data yang diharapkan dalam API. Model tipe data Pydantic menyediakan validasi data otomatis dan pengubahan tipe data.
3. Model tipe data adalah kelas Python yang diturunkan dari kelas `pydantic.BaseModel` dan memiliki deklarasi field-field dengan tipe data yang sesuai.

## Menentukan Tipe Data untuk Field dalam Model
- Setiap field dalam model tipe data harus memiliki tipe data yang ditentukan. Tipe data dapat berupa tipe Python seperti `str`, `int`, `float`, `bool` dan lain sebagainya. 

- Pydantic juga mendukung penggunaan tipe data Pydantic lainnya, tipe data kustom, dan tipe data kompleks seperti `List`, `Dict`, dan `datetime`.

## Validasi Data Menggunakan Anotasi Tipe Data dan Aturan Validasi Pydantic
Dengan menggunakan anotasi tipe data dan aturan validasi Pydantic, Anda dapat mendefinisikan aturan validasi untuk setiap field dalam model. Validasi data akan secara otomatis dilakukan oleh Pydantic berdasarkan aturan yang telah ditentukan.

- Contoh aturan validasi meliputi panjang minimal/maksimal string, nilai minimal/maksimal numerik, regex, dan banyak lagi.

## Menangani Data yang Opsional atau Data Default dalam Model
Anda dapat menentukan/mendefinisikan field dalam model sebagai opsional dengan menambahkan tanda tanya (?)/(`Optional`) setelah tipe data atau memberikan nilai default untuk field tersebut atau dengan menggunakan argumen default. Data yang opsional atau default memberikan fleksibilitas dalam pengiriman data ke API.

## Penggunaan Model Tipe Data dalam Rute FastAPI
Anda dapat menggunakan model tipe data Pydantic dalam deklarasi fungsi rute FastAPI sebagai **parameter path, query, body atau header**. FastAPI akan secara otomatis membaca/mengambil dan memvalidasi data masukan berdasarkan struktur model tipe data yang ditentukan. Anda juga dapat menggunakan model tipe data sebagai parameter fungsi untuk mengakses data yang diterima dari permintaan HTTP.

Dengan menggunakan model tipe data dalam FastAPI, Anda dapat mendefinisikan skema data yang jelas, melakukan validasi data otomatis, dan mengonversi tipe data dengan mudah. Hal ini membantu dalam memastikan bahwa data yang diterima dan dikirim oleh API Anda sesuai dengan ekspektasi dan aturan validasi yang telah ditentukan.

# Validasi Data
Validasi data adalah proses memeriksa data yang masuk atau keluar dari suatu sistem untuk memastikan bahwa data tersebut memenuhi aturan dan kriteria tertentu. Tujuan validasi data adalah untuk menjaga integritas data, mencegah kesalahan, dan memastikan bahwa data yang diterima atau dikirim oleh sistem sesuai dengan harapan.

Analogi sederhananya seperti ini:
> Bayangkan Anda adalah seorang penjaga keamanan di pintu masuk suatu gedung. Tugas Anda adalah memeriksa setiap orang yang masuk untuk memastikan bahwa mereka memiliki kartu akses yang valid dan sesuai dengan aturan gedung. Anda memeriksa identitas mereka, memeriksa apakah kartu akses mereka berlaku, dan memastikan bahwa mereka memenuhi persyaratan tertentu sebelum memperbolehkan mereka masuk. Jika ada yang tidak memenuhi persyaratan atau kartu akses mereka tidak valid, Anda akan menolak masuk dan memberikan respons yang sesuai.

## Penjelasan Singkat Validasi Data
### Menggunakan Pydantic untuk Memvalidasi Data Masukkan
- Pydantic adalah library Python yang kuat untuk validasi data dan serialisasi. Dalam FastAPI, Anda dapat menggunakan Pydantic untuk memvalidasi data masukan yang diterima oleh API Anda.
- Pydantic memeriksa tipe data, aturan validasi, dan struktur data untuk memastikan bahwa data masukan memenuhi persyaratan yang ditentukan.

### Menentukan Aturan Validasi Menggunakan Anotasi Tipe Data Pydantic
- Dengan menggunakan anotasi tipe data Pydantic, Anda dapat menentukan aturan validasi untuk setiap field dalam model. Aturan validasi dapat mencakup panjang minimal/maksimal string, nilai minimal/maksimal numerik, regex, format tanggal, dan banyak lagi.
- Pydantic secara otomatis akan menerapkan validasi berdasarkan anotasi tipe data yang ditentukan.

### Mengatasi Kesalahan Validasi dan Memberikan Respons yang Sesuai
- Jika terjadi kesalahan validasi, FastAPI akan secara otomatis menghasilkan respons HTTP yang sesuai dengan informasi kesalahan yang terperinci.
- Respons akan berisi status kode yang sesuai (misalnya, 400 Bad Request) dan pesan kesalahan yang menjelaskan mengapa validasi gagal.
- Anda juga dapat menangani kesalahan validasi secara manual menggunakan try-except untuk menangkap kesalahan dan memberikan respons yang ditentukan.
### Menggunakan Pydantic's Field untuk Aturan Validasi Kustom
- Pydantic menyediakan kelas Field yang memungkinkan Anda mendefinisikan aturan validasi kustom.
- Anda dapat menggunakan Field untuk menentukan aturan validasi tambahan seperti nilai default, data opsional, nilai yang diterima, dan lainnya.

Dengan melakukan validasi data, Anda dapat memastikan bahwa data yang diterima oleh API Anda memenuhi kriteria dan aturan yang telah ditentukan. Hal ini membantu mencegah kesalahan dan memastikan integritas data. Dalam konteks FastAPI, Pydantic memudahkan validasi data dengan memberikan respons yang jelas dan terperinci ketika terjadi kesalahan validasi, sehingga Anda dapat mengambil tindakan yang tepat dalam menangani data yang tidak valid.

# Persiapan Belajar
## Persyaratan Kemampuan
Sebelum mengikuti/mempelajari kelas ini, idealnya Anda harus memiliki bekal kemampuan dalam dasar bahasa pemrograman Python untuk membangun RESTful API sederhana.

# Prasyarat Tools
Selain kemampuan prasyarat yang sudah Anda ketahui di materi sebelumnya, kelas ini juga memiliki prasyarat tools yang perlu Anda penuhi terlebih dahulu. 

## Text Editor
Selama mengikuti kelas ini tentu Anda akan banyak sekali menuliskan kode. Kami merekomendasikan Anda untuk menggunakan VSCode. Text editor ini sangat populer dan gratis untuk digunakan. Selain itu, text editor ini memiliki plugin berlimpah yang dapat membuat fungsionalitas menjadi lebih kaya lagi. Visual Studio Code dapat dijalankan pada sistem operasi Windows, macOS, ataupun Linux. Untuk mengunduhnya, silakan kunjungi halaman unduh [Visual Studio Code](https://code.visualstudio.com/download).

## Python
Pastikan komputer Anda sudah terpasang Python dengan minimal versi 3.7 atau lebih tinggi. Untuk mengetahui versi Python yang terpasang, silakan tulis perintah ini pada Terminal atau CMD.
```bash
python -V
```

## Postman
Tools ini akan digunakan menguji fungsionalitas dari RESTful API yang kita buat. Pastikan Anda sudah memasang Postman pada komputer Anda. Jika belum, silakan unduh Postman melalui tautan  yang kami sediakan di bawah ini.

> Catatan: Agar dapat mengikuti materi dengan baik, kami sarankan Anda untuk mengunduh Postman versi 9 stabil. Link unduh di bawah ini kami sudah sesuaikan dengan versi tersebut. jika Anda ingin menggunakan yang versi terbaru unduh melalui link ini [Postman](https://www.postman.com/downloads/)

- [Windows](https://go.pstmn.io/dl-win64-v9-latest)
- [Linux](https://go.pstmn.io/dl-linux64-v9-latest)
- [MacOS-Intel chip](https://go.pstmn.io/dl-osx64-v9-latest)
- [MacOS-Apple silicon](https://go.pstmn.io/dl-osxarm64-v9-latest)

# Mekanisme Belajar
Sebelum memulai belajar di kelas ini, Anda perlu tahu tahapan dan cara belajar beserta fasilitas yang tersedia agar proses belajar lebih efektif.
## Materi Pembelajaran
- Materi Bacaan Elektornik: Materi yang ada dalam kelas ini mayoritas berupa teks atau tulisan. Mengapa demikian? Karena kami menemukan bahwa dalam proses belajar di bidang pemrograman, bentuk materi pembelajaran yang paling efektif untuk diingat, dimengerti, dan yang terpenting, dipraktikkan, adalah dalam bentuk teks.

- Forum Diskusi: Setiap kelas memiliki sebuah forum diskusi yang dapat Anda gunakan untuk bertanya (dan menjawab) mengenai materi kelas. Tidak hanya sebatas itu Anda pun dapat berpartisipasi. Untuk meningkatkan retensi ilmu yang Anda punya, berbagi adalah salah satu kuncinya. Jadi, silakan aktif dan saling membantu di dalam forum.

## Evaluasi Pembelajaran
- Exam (Knowledge Check): Terdapat ujian atau Knowledge Check di kelas guna mengecek pemahaman Anda pada materi pembelajaran. Ketersediaan ujian beserta jenis ujian yang tersedia pada setiap kelas dapat berbeda-beda. Setiap pertanyaan dalam ujian pasti mencakup materi yang telah dibahas. Sehingga jika ada pertanyaan yang tidak dapat Anda jawab, pastikan Anda mengulang kembali pembelajaran. 

- Submission (Proyek, Tugas, Codelab, Proyek Akhir): Praktik Pembelajaran Siswa, biasanya berupa hasil coding Anda sendiri yang perlu diunggah ke platform GitHub Anda dan mengirimkan link/urlnya untuk membuktikan bahwa Anda telah mengerti materi dan dapat mengimplementasikannya.

# Forum Diskusi
Silahkan bertanya dan berkontribusi pada Forum Diskusi. Anda dapat mengakses dan bergabung ke forum diskusi dengan url berikut: [College Struggles](https://discord.gg/rgvWDCZKSb)

# Materi yang akan dibahas
Kelas ini terdiri dari 3 (dua) modul atau pembahasa pokok. Berikut rincian materi yang akan dipelajari:

1. FastAPI Setup & Installation:
Materi ini akan membahas tentang langkah-langkah untuk mengatur dan menginstal FastAPI di lingkungan pengembangan Anda. Ini akan mencakup persyaratan sistem, instalasi Python, serta pengaturan proyek FastAPI awal.
    - Isi Materi:
        - Persyaratan sistem untuk menjalankan FastAPI
        - Instalasi Python dan pip (Python Package Installer
        - Pembuatan virtual environment untuk proyek FastAPI
        - Pengenalan tentang dependency management menggunakan pipenv atau pip
        - Menginstal FastAPI menggunakan pip
        - Inisialisasi proyek FastAPI dan pengaturan struktur dasar
2. FastAPI Request Method Logic
Materi ini akan menjelaskan logika dan penggunaan metode permintaan (request methods) dalam FastAPI. Anda akan belajar bagaimana menentukan metode permintaan yang digunakan oleh klien (GET, POST, PUT, DELETE) dan menghubungkannya dengan fungsi penanganan yang sesuai.
    - Isi Materi:
        - Pengenalan tentang metode permintaan HTTP (GET, POST, PUT, DELETE)
        - Menggunakan dekorator @app.get untuk menangani permintaan GET
        - Menggunakan dekorator @app.post untuk menangani permintaan POST
        - Menggunakan dekorator @app.put untuk menangani permintaan PUT
        - Menggunakan dekorator @app.delete untuk menangani permintaan DELETE
        - Penanganan permintaan dengan parameter jalur (path parameters), parameter query (query parameters), dan parameter lainnya
        - Mengembalikan respons HTTP yang sesuai berdasarkan metode permintaan
3. Data Validation
Materi ini akan menjelaskan tentang validasi data dalam FastAPI menggunakan Pydantic. Anda akan mempelajari bagaimana menggunakan anotasi tipe data dan aturan validasi Pydantic untuk memvalidasi input data dari klien.
    - Isi Materi:
        - Pengenalan tentang validasi data dan kepentingannya dalam pengembangan API
        - Menggunakan Pydantic untuk memvalidasi data masukan
        - Menentukan aturan validasi menggunakan anotasi tipe data Pydantic
        - Mengatasi kesalahan validasi dan memberikan respons yang sesuai
        - Menggunakan Pydantic's Field untuk aturan validasi kustom
        - Menangani data opsional atau data default dalam model Pydantic

Materi-materi ini akan memberikan pemahaman yang mendalam tentang pengaturan dan instalasi FastAPI, logika metode permintaan dalam FastAPI, serta validasi data menggunakan Pydantic. Anda akan belajar cara menginstal FastAPI, menentukan metode permintaan yang tepat, dan memvalidasi data yang diterima oleh API Anda.

# Daftar Referensi
1. [Dokumentasi FastAPI](https://fastapi.tiangolo.com/)