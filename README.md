
# ⚡ VOIDRIP v2.0 :: High Speed Terminal Downloader

![Python](https://img.shields.io/badge/Language-Python%203.8%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-brightgreen)
![License](https://img.shields.io/badge/License-Apache%202.0-orange)
![Version](https://img.shields.io/badge/Version-2.0.0-purple)

**Repository:** [https://github.com/Alghifari888/VOIDRIP](https://github.com/Alghifari888/VOIDRIP)

---

## 📖 Penjelasan Singkat
**VOIDRIP** adalah alat pengunduh media berbasis CLI (Command Line Interface) yang dirancang untuk kecepatan, kestabilan, dan estetika. Dibangun menggunakan Python modern dengan engine `yt-dlp`, alat ini mampu mengunduh video, audio (MP3), hingga seluruh playlist dari YouTube dengan efisiensi tinggi tanpa membebani sistem.

### ✨ Kutipan
> "Aku tidak berilmu; yang berilmu hanyalah DIA. Jika tampak ilmu dariku, itu hanyalah pantulan dari Cahaya-Nya."

---

## 📑 Ringkasan Singkat
* **Nama Project:** VOIDRIP
* **Versi:** 2.0 (Neon Cyberpunk Update)
* **Fokus:** Download Video & Audio High Quality via Terminal.
* **Target Pengguna:** Pengguna Linux (Kali/Ubuntu) & Windows yang menyukai efisiensi terminal.

---

## 🚀 Penjelasan Fitur
1.  **High Speed Engine:** Menggunakan multithreading untuk download maksimal.
2.  **Neon Glitch UI:** Tampilan antarmuka terminal yang estetik dan rapi.
3.  **Smart Auto-Path:** Otomatis membuat folder output jika belum ada.
4.  **Auto-Installer:** Script instalasi otomatis untuk Linux (`.sh`) dan Windows (`.bat`).
5.  **Global Command:** Bisa dijalankan dari folder mana saja (setelah install).
6.  **Format Support:**
    * **Video:** Hingga 4K (2160p), otomatis merge video+audio (MP4).
    * **Audio:** Otomatis convert ke MP3 High Quality dengan Cover Album.
7.  **Playlist Downloader:** Download satu album/playlist sekali perintah.

---

## 🧩 Komponen & Penjelasan Detail

### Komponen Program
Program ini dibangun secara modular (terpisah-pisah) agar mudah dikelola dan dikembangkan:
* **Core Logic:** Menangani proses download dan interaksi sistem.
* **User Interface (UI):** Menangani tampilan banner, warna, dan animasi loading.
* **Installer:** Script untuk memasang dependencies secara otomatis.

### 📂 Struktur Folder & File
Berikut adalah hierarki file dalam project ini:

```text
VOIDRIP/
├── core/                  # [Logika Utama]
│   ├── downloader.py      # Mengatur engine download (yt-dlp & ffmpeg)
│   └── utils.py           # Fungsi bantuan (cek os, cek ffmpeg, auto-folder)
│
├── ui/                    # [Tampilan Antarmuka]
│   ├── banner.py          # Menampilkan logo ASCII Neon & Header status
│   └── display.py         # Menangani output pesan warna-warni & animasi
│
├── setup/                 # [Installer Otomatis]
│   ├── install.sh         # Script instalasi untuk Linux (Debian/Kali)
│   └── install.bat        # Script instalasi untuk Windows
│
├── main.py                # [Launcher Utama] Titik awal program berjalan
├── requirements.txt       # Daftar pustaka Python yang dibutuhkan
├── .gitignore             # Mengabaikan file sampah/hasil download saat upload
└── README.md              # Dokumentasi ini

```

### 📝 Penjelasan File (Detail)

1. **`main.py`**: Gerbang utama. Mengatur argumen input user (seperti `video`, `audio`) dan memanggil fungsi yang sesuai dari folder `core`.
2. **`core/downloader.py`**: Otak dari program. Berisi fungsi `download_video`, `download_audio`, dan `download_playlist`. Menggunakan `subprocess` untuk memerintah `yt-dlp`.
3. **`core/utils.py`**: Asisten pintar. Bertugas mengecek apakah FFmpeg terinstall, membuat folder output otomatis, dan mendeteksi OS.
4. **`ui/banner.py`**: Seniman. Menggambar logo VOIDRIP dengan gradasi warna presisi agar terlihat keren.
5. **`setup/install.*`**: Teknisi. Script ini yang bekerja keras saat pertama kali Anda menginstall tools ini (download library, setting path, dll).

---

## 💻 Persyaratan Sistem (System Requirements)

Sebelum menginstall, pastikan perangkat Anda memiliki:

* **Sistem Operasi:**
* Linux (Kali Linux, Ubuntu, Debian, Mint).
* Windows 10 / 11.


* **Software Pendukung:**
* **Python 3.8** atau lebih baru.
* **FFmpeg** (Wajib untuk convert MP3 & gabung video 1080p).
* **Git** (Untuk clone repository).


* **Koneksi Internet:** Stabil.

---

## 🛠️ Panduan Instalasi & Menjalankan

### 🐧 Untuk Linux (Kali / Ubuntu / Debian)

1. **Clone Repository:**
```bash
git clone [https://github.com/Alghifari888/VOIDRIP.git](https://github.com/Alghifari888/VOIDRIP.git)
cd VOIDRIP

```


2. **Jalankan Installer (Otomatis):**
```bash
cd setup
chmod +x install.sh
sudo ./install.sh

```


*Tunggu hingga proses selesai. Script akan otomatis mendaftarkan perintah global.*
3. **Cara Menjalankan:**
Buka terminal baru, lalu ketik:
```bash
voidrip

```



### 🪟 Untuk Windows

1. **Persiapan:**
* Install Python dari [python.org](https://www.python.org/) (Centang **"Add Python to PATH"**).
* (Disarankan) Download [FFmpeg](https://ffmpeg.org/download.html) dan taruh `ffmpeg.exe` di folder project.


2. **Install:**
* Masuk ke folder `VOIDRIP/setup`.
* Klik 2x file **`install.bat`**.
* Jika diminta akses Administrator, klik **Yes**.


3. **Cara Menjalankan:**
* Buka CMD (Command Prompt) di mana saja.
* Ketik: `voidrip`



---

## 📖 Cara Penggunaan (Usage Examples)

**1. Download Video (MP4)**

```bash
voidrip video "[https://youtu.be/contoh123](https://youtu.be/contoh123)"

```

*Custom Resolusi & Nama File:*

```bash
voidrip video "URL" --res 720 -o "VideoBaru.mp4"

```

**2. Download Audio (MP3)**

```bash
voidrip audio "[https://youtu.be/contohMusik](https://youtu.be/contohMusik)"

```

*Custom Output Folder (Otomatis dibuatkan):*

```bash
voidrip audio "URL" -o "Musik/LaguFavorit.mp3"

```

**3. Download Playlist Full**

```bash
voidrip playlist "[https://youtube.com/playlist?list=](https://youtube.com/playlist?list=)..."

```

---

## 🤝 Panduan Kontribusi (Fork)

Kami sangat terbuka untuk kontribusi! Jika Anda ingin menambahkan fitur:

1. **Fork** repository ini (klik tombol Fork di pojok kanan atas GitHub).
2. **Clone** hasil fork Anda ke komputer lokal.
3. Buat **Branch** baru untuk fitur Anda:
```bash
git checkout -b fitur-baru-keren

```


4. Lakukan perubahan kode dan **Commit**:
```bash
git commit -m "Menambahkan fitur X"

```


5. **Push** ke repository GitHub Anda:
```bash
git push origin fitur-baru-keren

```


6. Buat **Pull Request** (PR) di repository asli VOIDRIP.

---

## 🧪 Testing (Cara Menjalankan Testing)

Karena tools ini berbasis CLI dan bergantung pada koneksi internet ke server YouTube, pengujian dilakukan secara **Manual (Integration Testing)**:

1. **Test Koneksi:** Jalankan `voidrip` tanpa argumen. Pastikan Banner muncul.
2. **Test Download Video:** Coba download 1 video pendek. Pastikan file `.mp4` muncul dan bisa diputar.
3. **Test Convert Audio:** Coba download mode `audio`. Pastikan file `.mp3` muncul dan memiliki cover album (thumbnail).
4. **Test Folder:** Coba download dengan flag `-o "FolderBaru/test.mp4"`. Pastikan folder otomatis terbuat.

---

## ⚖️ Peringatan Legal & Etis

### Lisensi

Project ini dilisensikan di bawah **Apache License 2.0**.
Anda bebas menggunakan, memodifikasi, dan mendistribusikan ulang, selama Anda menyertakan lisensi asli dan hak cipta author.

### Disclaimer

* Tools ini dibuat untuk tujuan **Edukasi** dan penggunaan pribadi (backup media sendiri).
* Author (**Alghifari888**) tidak bertanggung jawab atas penyalahgunaan alat ini untuk pelanggaran hak cipta (Copyright Infringement).
* Harap patuhi *Terms of Service* dari platform yang Anda download.

---

<div align="center">
<p>✍️ <b>Author</b></p>
<p>Dikembangkan dengan ❤️ dan ☕ oleh <b>Alghifari888</b>.</p>
<p><i>Licensed under Apache-2.0</i></p>
</div>

```

```
