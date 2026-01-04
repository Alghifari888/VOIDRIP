@echo off
TITLE VOIDRIP Installer (Windows) - github.com/alghifari888
CLS
color 0b

:: --- HEADER ---
ECHO ==========================================================
ECHO      VOIDRIP v2.0 - ULTIMATE WINDOWS INSTALLER
ECHO      Created by: github.com/alghifari888
ECHO ==========================================================
ECHO.

:: --- 1. CEK ADMIN (AUTO ELEVATE) ---
:: Script ini butuh Admin untuk mendaftarkan PATH
NET SESSION >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    ECHO [INFO] Administrator privileges detected. Good.
) ELSE (
    ECHO [WARN] Meminta akses Administrator untuk setup sistem...
    ECHO.
    PowerShell -Command "Start-Process '%~dpnx0' -Verb RunAs"
    EXIT
)

:: --- 2. CEK PYTHON ---
ECHO [*] Mengecek instalasi Python...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    color 0c
    ECHO [!] ERROR: Python tidak ditemukan!
    ECHO.
    ECHO Solusi:
    ECHO 1. Download Python di python.org
    ECHO 2. PENTING: Centang "Add Python to PATH" saat install.
    PAUSE
    EXIT
) ELSE (
    ECHO [OK] Python terdeteksi.
)

:: --- 3. INSTALL REQUIREMENTS ---
ECHO.
ECHO [*] Menginstall Library Python...
pip install -r ..\requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    color 0c
    ECHO [!] Gagal download library. Cek internet Anda!
    PAUSE
    EXIT
)

:: --- 4. CEK FFMPEG (FITUR PINTAR) ---
ECHO.
ECHO [*] Mengecek FFmpeg (Wajib untuk Audio/MP3)...
where ffmpeg >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    color 0e
    ECHO [!] WARNING: FFmpeg belum terinstall!
    ECHO     Fitur convert MP3 mungkin tidak jalan.
    ECHO.
    ECHO [*] Membuka halaman download FFmpeg otomatis...
    timeout /t 3 >nul
    start https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z
    ECHO.
    ECHO [TIPS] Extract file tadi, lalu copy 'ffmpeg.exe' ke folder ini.
) ELSE (
    ECHO [OK] FFmpeg sudah terinstall. Mantap!
)

:: --- 5. SETUP GLOBAL PATH & SHORTCUT ---
ECHO.
ECHO [*] Mengkonfigurasi Global Command...

:: Masuk ke folder root project (Mundur satu langkah dari setup)
cd ..
SET "PROJECT_DIR=%CD%"

:: Buat wrapper batch file
(
ECHO @echo off
ECHO python "%PROJECT_DIR%\main.py" %%*
) > "%PROJECT_DIR%\voidrip.bat"

:: Tambahkan Folder Project ke User Environment PATH (PowerShell Magic)
:: Ini yang bikin user bisa ketik 'voidrip' dari mana saja
ECHO [*] Mendaftarkan '%PROJECT_DIR%' ke System PATH...
PowerShell -Command "[Environment]::SetEnvironmentVariable('Path', [Environment]::GetEnvironmentVariable('Path', 'User') + ';%PROJECT_DIR%', 'User')"

ECHO.
ECHO ==========================================================
ECHO    INSTALASI SELESAI - SUKSES!
ECHO ==========================================================
ECHO.
ECHO PENTING:
ECHO Agar perintah 'voidrip' bisa dipakai global:
ECHO 1. Tutup jendela CMD ini.
ECHO 2. Buka CMD baru.
ECHO 3. Ketik 'voidrip'.
ECHO.
ECHO Regards, github.com/alghifari888
PAUSE