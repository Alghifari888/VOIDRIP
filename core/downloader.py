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

import subprocess
import sys
import os
from ui.display import ui_print

def ensure_directory(path_pattern):
    """
    Fitur User Friendly: Otomatis membuat folder jika belum ada.
    Contoh: User set output ke 'Musik/Lagu.mp3', maka folder 'Musik' dibuatkan.
    """
    try:
        # Ambil nama folder dari path output
        directory = os.path.dirname(path_pattern)
        
        # Hanya buat folder jika pathnya bukan kosong dan bukan template yt-dlp (yang ada %)
        # yt-dlp biasanya handle template folder sendiri, tapi untuk path statis kita bantu.
        if directory and "%" not in directory:
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
                ui_print(f"Membuat folder otomatis: {directory}/", "info")
    except Exception as e:
        # Jangan stop program cuma gara-gara gagal bikin folder, biarkan yt-dlp coba lanjut
        pass

def run_yt(args, verbose=False):
    """Wrapper untuk menjalankan yt-dlp"""
    base_cmd = ["yt-dlp", "--no-warnings"]
    
    if not verbose:
        base_cmd.append("--progress")
    else:
        base_cmd.append("--verbose")
    
    cmd = base_cmd + args
    
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        # Error code biasa yt-dlp (misal skip video)
        return False
    except FileNotFoundError:
        ui_print("yt-dlp tidak ditemukan. Pastikan requirements.txt sudah diinstall.", "error")
        return False
    except KeyboardInterrupt:
        ui_print("Download dibatalkan user.", "warn")
        return False

def download_video(url, res, out_pattern):
    # Cek dan buat folder dulu
    ensure_directory(out_pattern)
    
    format_str = f"bv*[height<={res}][ext=mp4]+ba[ext=m4a]/b[height<={res}]"
    
    args = [
        "-f", format_str,
        "--merge-output-format", "mp4",
        "--convert-thumbnails", "jpg",
        "--embed-thumbnail",
        "--embed-metadata",
        "--restrict-filenames",
        "-o", out_pattern,
        url
    ]
    return run_yt(args)

def download_audio(url, bitrate, out_pattern):
    # Cek dan buat folder dulu
    ensure_directory(out_pattern)
    
    args = [
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--embed-thumbnail",
        "--embed-metadata",
        "--restrict-filenames",
        "--prefer-ffmpeg",
        "-o", out_pattern,
        url
    ]
    return run_yt(args)

def download_playlist(url, out_pattern, start, end):
    # Cek dan buat folder dulu
    ensure_directory(out_pattern)
    
    args = [
        "--yes-playlist",
        "--merge-output-format", "mp4",
        "--restrict-filenames",
        "--download-archive", "downloaded.txt",
        "-o", out_pattern,
        url
    ]
    
    if start:
        args.extend(["--playlist-start", str(start)])
    if end:
        args.extend(["--playlist-end", str(end)])
        
    return run_yt(args)