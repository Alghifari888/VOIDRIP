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
    """Memastikan folder tujuan tersedia sebelum download."""
    try:
        directory = os.path.dirname(path_pattern)
        # Hanya buat folder jika path valid dan bukan template
        if directory and "%" not in directory:
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
                ui_print(f"Auto-create directory: {directory}/", "info")
    except Exception:
        pass

def run_yt(args, verbose=False):
    """Wrapper eksekusi yt-dlp dengan konfigurasi High Speed."""
    # --- TURBO MODE: 16 FRAGMENTS ---
    # Memaksa download 16 bagian sekaligus untuk max speed
    base_cmd = ["yt-dlp", "--no-warnings", "--concurrent-fragments", "16"]
    
    if not verbose:
        base_cmd.append("--progress")
    else:
        base_cmd.append("--verbose")
    
    cmd = base_cmd + args
    
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        ui_print("Error: yt-dlp/FFmpeg not found. Check requirements.", "error")
        return False
    except KeyboardInterrupt:
        ui_print("Download cancelled by user.", "warn")
        return False

def download_video(url, res, out_pattern):
    ensure_directory(out_pattern)
    
    # Format: Video Best + Audio Best -> Merge MP4
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
    ensure_directory(out_pattern)
    
    args = [
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0", # 0 = Best Quality (VBR)
        "--embed-thumbnail",
        "--embed-metadata",
        "--restrict-filenames",
        "-o", out_pattern,
        url
    ]
    return run_yt(args)

def download_playlist(url, out_pattern, start, end):
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
