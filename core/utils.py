# Copyright 2026 github.com/alghifari888
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Author  : alghifari888
# GitHub  : https://github.com/alghifari888
# Project : High Speed Terminal Downloader
# Version : 2.0

import shutil
import platform
import os
import sys

# Kita import ui_print agar pesan warning terlihat rapi
try:
    from ui.display import ui_print
except ImportError:
    # Fallback jika ui belum siap
    def ui_print(msg, type="info"): print(msg)

def check_system_deps():
    """
    Mengecek apakah dependencies sistem (ffmpeg) sudah terinstall.
    Support Windows & Linux.
    """
    missing = []
    is_windows = os.name == 'nt'
    
    # Cek FFmpeg
    if not shutil.which("ffmpeg"):
        missing.append("FFmpeg")
        
        # KHUSUS WINDOWS: Berikan instruksi jelas jika FFmpeg tidak ada
        if is_windows:
            print("\n\033[38;5;208m" + "="*60)
            ui_print("FFMPEG TIDAK DITEMUKAN DI WINDOWS ANDA!", "warn")
            print("\033[38;5;208m" + "="*60 + "\033[0m")
            print(" Agar fitur convert MP3 berjalan, lakukan langkah ini:")
            print(" 1. Download FFmpeg: \033[1;36mhttps://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z\033[0m")
            print(" 2. Extract file tersebut.")
            print(" 3. Copy file 'ffmpeg.exe' dari folder 'bin'.")
            print(" 4. Paste ke folder 'C:\\Windows\\System32\\' atau folder VOIDRIP ini.")
            print("\033[38;5;208m" + "="*60 + "\033[0m\n")
    
    return missing

def get_os_info():
    """Mengambil informasi Sistem Operasi"""
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release()
    }

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    