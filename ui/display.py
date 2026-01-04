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

import sys
import time

def ui_print(msg, type="info"):
    """Mencetak pesan dengan ikon berwarna"""
    marks = {
        "info": "\033[1;38;5;117m[ℹ]\033[0m", 
        "ok":   "\033[1;38;5;46m[✓]\033[0m", 
        "warn": "\033[1;38;5;208m[!]\033[0m", 
        "load": "\033[1;38;5;141m[↻]\033[0m", 
        "error":"\033[1;38;5;196m[✗]\033[0m",
        "step": "\033[1;38;5;51m[→]\033[0m"
    }
    # Mengambil icon berdasarkan tipe, default ke 'info'
    icon = marks.get(type, marks["info"])
    print(f"{icon} \033[38;5;252m{msg}\033[0m")

def loading_animation(text, duration=0.5):
    """Animasi loading sederhana agar tidak terlihat freeze"""
    ui_print(text, "load")
    time.sleep(duration)