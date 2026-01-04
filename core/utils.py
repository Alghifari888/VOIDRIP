import shutil
import platform
import os
import sys

def check_system_deps():
    """
    Mengecek apakah dependencies sistem (ffmpeg) sudah terinstall.
    Support Windows & Linux.
    """
    missing = []
    
    # Cek FFmpeg
    if not shutil.which("ffmpeg"):
        missing.append("FFmpeg")
    
    # Cek yt-dlp (opsional karena kita import via python, tapi bagus jika ada di path)
    # Kita skip yt-dlp check karena kita pakai module internal di requirements.txt
    
    return missing

def get_os_info():
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release()
    }

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')