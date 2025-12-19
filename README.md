# Game Billiard

Panduan lengkap untuk instalasi dan menjalankan Game Billiard di komputer lokal.

## Persyaratan Sistem

Sebelum memulai, pastikan Anda telah memiliki:

1. **Python** - versi 3.8 atau lebih baru
2. **pip** - package manager untuk Python

## Panduan Instalasi dan Menjalankan Program

### Step 1: Clone atau Download Repository

Jika menggunakan Git:
```bash
git clone https://github.com/Dhimasekaputraa/billiard-game.git
```

Atau download file ZIP dari repository dan ekstrak di komputer Anda.

### Step 2: Buka Folder Proyek di VSCode

1. Buka Visual Studio Code
2. Pilih menu `File` > `Open Folder`
3. Navigasi ke folder tempat penyimpanan program Game Billiard
4. Klik `Select Folder` untuk membuka folder proyek

### Step 3: Buat Virtual Environment (venv)

Virtual environment digunakan untuk mengisolasi dependensi proyek agar tidak konflik dengan paket Python lainnya.

#### Windows:
Buka terminal VSCode dan ketik:
```bash
python -m venv venv
```

Aktivasi virtual environment:
```bash
venv\Scripts\activate
```

#### macOS / Linux:
Buka terminal VSCode dan ketik:
```bash
python3 -m venv venv
```

Aktivasi virtual environment:
```bash
source venv/bin/activate
```

Setelah aktivasi, Anda akan melihat `(venv)` di awal baris terminal, yang menandakan virtual environment sudah aktif.

### Step 4: Install Library yang Dibutuhkan

Pastikan virtual environment sudah aktif, kemudian install semua library yang diperlukan:

```bash
pip install Zope.event
pip install numpy
pip install pygame
```

Atau Anda bisa install semuanya sekaligus:
```bash
pip install Zope numpy pygame
```

### Step 5: Verifikasi Instalasi

Untuk memastikan semua library terinstall dengan benar, ketik:
```bash
pip list
```

Pastikan output menunjukkan `Zope`, `numpy`, dan `pygame` dalam daftar library yang terinstall.

### Step 6: Jalankan Program

Setelah semua library terinstall, jalankan program dengan mengetik:
```bash
python main.py
```

Jika menggunakan Python 3, Anda juga bisa menggunakan:
```bash
python3 main.py
```

Program Game Billiard akan terbuka dan siap dimainkan.