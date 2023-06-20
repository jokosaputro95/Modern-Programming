# Table of Contents
- [Virtual Enironment](#virtual-environment-overview)
- [FastAPI Setup & Installation](#instalasi-fastapi-dan-virtual-environtment)

# Virtual Environment Overview
Virtual environment adalah sebuah lingkungan terisolasi yang terpisah dari lingkungan Python global pada sistem operasi Anda. 

Analogi sederhananya seperti ini:
> Bayangkan ada sedang berada didalam sebuah komplek perumahan, Anda melihat dan bahwa disana banyak sekali rumah-rumah terpisah dalam satu komplek perumahan. Setiap rumah mewakili sebuah proyek atau aplikasi yang sedang Anda kembangkan. Dalam setiap rumah, Anda memiliki kontrol penuh atas pengaturan, desain, dan peralatan yang ada di dalamnya. Jika Anda perlu melakukan renovasi atau membuat perubahan tertentu pada satu rumah, itu tidak akan mempengaruhi rumah-rumah lain dalam kompleks.

Dalam konteks pengembangan perangkat lunak, virtual environment adalah lingkungan terisolasi yang mirip dengan rumah-rumah tersebut. Setiap lingkungan virtual mewakili proyek atau aplikasi yang sedang Anda kerjakan. Anda dapat mengatur/menginstal dependensi, versi Python, dan konfigurasi lainnya secara bebas di dalam lingkungan virtual tanpa mempengaruhi lingkungan global atau proyek lain.

## Manfaat dan Kegunaan Virtual Environment
1. Mencegah Konflik Dependensi: Analoginya, setiap rumah memiliki pasokan air dan listrik tersendiri. Jika ada masalah dengan pasokan air di satu rumah, itu tidak akan mempengaruhi pasokan air di rumah-rumah lainnya. Dalam pengembangan perangkat lunak, virtual environment mencegah konflik dependensi antara proyek-proyek yang berbeda. Setiap proyek memiliki dependensi dan versi paket yang dapat ditentukan secara independen.

2. Eksperimen Aman: Analoginya, Anda dapat melakukan percobaan dengan tata letak dan perabotan di dalam rumah Anda tanpa mempengaruhi rumah-rumah tetangga. Dalam lingkungan virtual, Anda dapat melakukan eksperimen dengan instalasi paket, menguji versi Python yang berbeda, atau mengubah konfigurasi tanpa khawatir tentang dampaknya pada proyek-proyek lain.

3. Bersih dan Terkelola: Analoginya, setiap rumah memiliki kebersihan dan tata letak yang teratur sesuai kebutuhan pemiliknya. Dalam lingkungan virtual, Anda dapat menjaga kebersihan dan keteraturan dengan mengelola dependensi proyek secara terpisah. Anda dapat menghapus, menambahkan, atau mengubah dependensi dalam lingkungan virtual tanpa mengganggu proyek lain.

4. Skalabilitas: Analoginya, Anda dapat memperluas rumah atau menambahkan ruangan sesuai kebutuhan dan anggaran Anda. Dalam lingkungan virtual, Anda dapat dengan mudah menambahkan atau menghapus dependensi proyek, mengganti versi Python, atau melakukan perubahan lainnya sesuai kebutuhan tanpa mempengaruhi proyek-proyek lain.

Dengan menggunakan virtual environment, Anda dapat mengisolasi dan mengelola lingkungan pengembangan proyek dengan lebih baik, mirip dengan rumah-rumah terpisah dalam kompleks perumahan. Setiap proyek memiliki lingkungan yang terisolasi dan dapat dikonfigurasi sesuai kebutuhan, mencegah konflik dependensi dan memastikan keteraturan serta kebersihan dalam pengembangan perangkat lunak.

# Instalasi FastAPI dan Virtual Environtment
## Instalasi FastAPI & Virtual Environment Windows
- Instalasi Python:
    - Kunjungi situs resmi Python di https://www.python.org/downloads/.
    - Unduh installer Python untuk Windows sesuai dengan versi yang Anda inginkan (misalnya, Python 3.9) atau unduh versi terbaru.
    - Jalankan installer yang telah diunduh dan ikuti langkah-langkah instalasi yang disediakan.
    - Pastikan instalasi Python berhasil. Anda bisa cek melalui Command Prompt atau PowerShell dengan mengetik `python -V`
- Download & Install Virtualenv using pip or pip3
    ```bash
    pip3 install virtualenv
    # or
    pip install virtualenv
    # or
    py -m pip install --user virtualenv
    ```
    Ini dilakukan jika virtualenv tidak ikut serta dalam installasi Python. biasanya versi terbaru Python sudah include. maka step ini bisa dilewati langsung ke step selanjutnya
- Membuat Virtual Environment menggunakan venv:
    - Buka Command Prompt atau PowerShell.
    - Pindah ke direktori proyek Anda menggunakan perintah "cd" (misalnya, "cd C:\Users\NamaUser\Projects").
    - Buat virtual environment baru dengan perintah berikut: `python -m venv nama_env` atau `py -m venv nama_env` (ganti "nama_env" dengan nama yang Anda inginkan untuk virtual environment).
    - Aktifkan virtual environment dengan menjalankan perintah: `nama_env\Scripts\activate`.
    - Nonaktifkan virtual environment dengan perintah: `deactivate` (Unix/Mac/Windows)
    - Setelah Virtual Environment aktif Anda bisa melihan python package dengan mengetikan perintah `pip list` pada Command Prompt atau PowerShell
- Instalasi FastAPI:
    - Ketikan perintah `pip install fastapi` untuk menginstal FastAPI demi bagian, hal mungkin diperlukan Anda ketika hendak men-deploy aplikasi Anda ke tahap produksi.
    - Ketikan perintah `pip install "fastapi[all]"` jika kamu ingin menginstall seluruh fitur dan dependensinya.
    - Ketikan perintah `pip install "uvicorn[standard]"`, hal ini dilakukan untuk melakukan menjalankan server FastAPI

## Instalasi FastAPI & Virtual Environment MacOS
- Instalasi Python:
    - MacOS biasanya sudah dilengkapi dengan Python terbaru. Untuk memverifikasi, buka Terminal dan jalankan perintah `python --version` atau `python3 --version` atau `python -V` atau `python3 -V`.
    - Jika Python tidak terinstal atau versi yang diinginkan tidak ada, Anda dapat mengunduh installer Python dari situs resmi di https://www.python.org/downloads/.
- Download & Install Virtualenv using pip or pip3
    ```bash
    pip3 install virtualenv
    # or
    pip install virtualenv
    # or
    py -m pip install --user virtualenv
    ```
    Ini dilakukan jika virtualenv tidak ikut serta dalam installasi Python. biasanya versi terbaru Python sudah include. maka step ini bisa dilewati langsung ke step selanjutnya
- Membuat Virtual Environment menggunakan venv:
    - Buka Terminal.
    - Pindah ke direktori proyek Anda menggunakan perintah "cd" (misalnya, "cd /Users/NamaUser/Projects").
    - Buat virtual environment baru dengan perintah berikut: `python3 -m venv nama_env` (ganti "nama_env" dengan nama yang Anda inginkan untuk virtual environment).
    - Aktifkan virtual environment dengan menjalankan perintah: `source nama_env/bin/activate`.
    - Nonaktifkan virtual environment dengan perintah: `deactivate` (Unix/Mac/Windows)
    - Setelah Virtual Environment aktif Anda bisa melihan python package dengan mengetikan perintah `pip list` pada Terminal.
- Instalasi FastAPI:
    - Ketikan perintah `pip install fastapi` untuk menginstal FastAPI demi bagian, hal mungkin diperlukan Anda ketika hendak men-deploy aplikasi Anda ke tahap produksi.
    - Ketikan perintah `pip install "fastapi[all]"` jika kamu ingin menginstall seluruh fitur dan dependensinya.
    - Ketikan perintah `pip install "uvicorn[standard]"`, hal ini dilakukan untuk melakukan menjalankan server FastAPI

## Instalasi FastAPI & Virtual Environment Linux
- Instalasi Python:
    - Buka Terminal dan jalankan perintah berikut untuk memeriksa apakah Python sudah terinstal: `python --version` atau `python3 --version`.
    - Jika Python tidak terinstal, Anda dapat menginstalnya dengan perintah berikut:
        - Untuk Ubuntu/Debian: `sudo apt-get install python3 python3-venv python3-pip`.- Untuk Fedora: `sudo dnf install python3 python3-venv python3-pip`.
- Membuat Virtual Environment menggunakan venv:
    - Buka Terminal.
    - Pindah ke direktori proyek Anda menggunakan perintah "cd" (misalnya, "cd /home/NamaUser/Projects").
    - Buat virtual environment baru dengan perintah berikut: `python3 -m venv nama_env` (ganti "nama_env" dengan nama yang Anda inginkan untuk virtual environment).
    - Aktifkan virtual environment dengan menjalankan perintah: `source nama_env/bin/activate`.
    - Nonaktifkan virtual environment dengan perintah: `deactivate` (Unix/Mac/Windows)
    - Setelah Virtual Environment aktif Anda bisa melihan python package dengan mengetikan perintah `pip list` pada Terminal.
- Instalasi FastAPI:
    - Ketikan perintah `pip install fastapi` untuk menginstal FastAPI demi bagian, hal mungkin diperlukan Anda ketika hendak men-deploy aplikasi Anda ke tahap produksi.
    - Ketikan perintah `pip install "fastapi[all]"` jika kamu ingin menginstall seluruh fitur dan dependensinya.
    - Ketikan perintah `pip install "uvicorn[standard]"`, hal ini dilakukan untuk melakukan menjalankan server FastAPI