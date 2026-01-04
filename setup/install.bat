@echo off
TITLE VOIDRIP Installer for Windows
CLS
color 0b

ECHO ==================================================
ECHO      VOIDRIP v2.0 - Windows Installer
ECHO ==================================================
ECHO.

:: 1. Cek apakah Python sudah terinstall
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    color 0c
    ECHO [!] ERROR: Python tidak terdeteksi!
    ECHO     Silakan install Python dari python.org dan
    ECHO     pastikan centang "Add Python to PATH" saat install.
    PAUSE
    EXIT /B
)

:: 2. Install Library dari requirements.txt
ECHO [*] Menginstall Library Python...
pip install -r ..\requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    color 0c
    ECHO [!] Gagal menginstall library. Cek koneksi internet Anda.
    PAUSE
    EXIT /B
)

:: 3. Buat Launcher "voidrip.bat" di folder utama
ECHO.
ECHO [*] Membuat shortcut perintah...
cd ..
(
ECHO @echo off
ECHO python "%%~dp0main.py" %%*
) > voidrip.bat

ECHO [OK] Shortcut 'voidrip.bat' berhasil dibuat.
ECHO.
ECHO ==================================================
ECHO    INSTALASI SUKSES!
ECHO ==================================================
ECHO.
ECHO CARA PAKAI DI WINDOWS:
ECHO 1. Buka CMD di folder folder VOIDRIP ini.
ECHO 2. Ketik perintah: voidrip video "URL"
ECHO.
PAUSE