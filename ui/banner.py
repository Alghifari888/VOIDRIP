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
import random
from datetime import datetime

# --- PALET WARNA ---
C_MAIN    = "\033[38;5;39m"   
C_ACCENT  = "\033[38;5;51m"   
C_WHITE   = "\033[38;5;255m"  
C_GREY    = "\033[38;5;240m"  
C_DARK    = "\033[38;5;234m"  
C_GREEN   = "\033[38;5;46m"   
C_RED     = "\033[38;5;196m"  
C_RESET   = "\033[0m"

# ASCII Art "VOIDRIP" - Font: Standard Block (Sangat Jelas)
BANNER_LINES = [
    f"{C_MAIN}__      __  ____   {C_ACCENT} _____   {C_MAIN} ____    {C_ACCENT} ____    {C_MAIN} _____   {C_ACCENT} _____  ",
    f"{C_MAIN}\ \    / / / __ \  {C_ACCENT}|_   _|  {C_MAIN}|  _ \   {C_ACCENT}|  _ \  {C_MAIN} |_   _|  {C_ACCENT}|  __ \ ",
    f"{C_MAIN} \ \  / / | |  | | {C_ACCENT}  | |    {C_MAIN}| | | |  {C_ACCENT}| |_) | {C_MAIN}   | |    {C_ACCENT}| |__) |",
    f"{C_MAIN}  \ \/ /  | |  | | {C_ACCENT}  | |    {C_MAIN}| | | |  {C_ACCENT}|  _ <  {C_MAIN}   | |    {C_ACCENT}|  ___/ ",
    f"{C_MAIN}   \  /   | |__| | {C_ACCENT} _| |_   {C_MAIN}| |_| |  {C_ACCENT}| | \ \ {C_MAIN}  _| |_   {C_ACCENT}| |     ",
    f"{C_MAIN}    \/     \____/  {C_ACCENT}|_____|  {C_MAIN}|____/   {C_ACCENT}|_|  \_\ {C_MAIN}|_____|  {C_ACCENT}|_|     "
]

def show_banner():
    # 1. Garis Pembuka (Booting Effect)
    print(f"\n{C_DARK}   {'//' * 30}{C_RESET}")
    
    # 2. Tampilkan Banner Baris per Baris (Animasi Cepat)
    for line in BANNER_LINES:
        print("   " + line) # Indentasi biar rapi
        time.sleep(0.09)    # Delay sedikit

    # 3. Info Meta (Rapi & Minimalis)
    print(f"{C_DARK}   {'-' * 60}{C_RESET}")
    # Format: Label (Grey) : Value (White)
    print(f"   {C_GREY}PROJECT :{C_WHITE} HIGH SPEED DOWNLOADER {C_ACCENT}v2.0")
    print(f"   {C_GREY}AUTHOR  :{C_WHITE} alghifari888")
    print(f"   {C_GREY}GITHUB  :{C_WHITE} github.com/alghifari888")
    print(f"   {C_GREY}LICENSE :{C_WHITE} Apache License 2.0")
    print(f"{C_DARK}   {'//' * 30}{C_RESET}\n")

def show_header():
    t = datetime.now().strftime("%H:%M:%S")
    
    # --- ANIMASI LOADING AKTIF ---
    # Teks muncul: "Initializing..." lalu berubah jadi Header
    loading_text = f"   {C_MAIN}[SYSTEM]{C_RESET} Establishing secure connection"
    sys.stdout.write(loading_text)
    
    # Animasi titik (...)
    for _ in range(3):
        sys.stdout.write(f"{C_ACCENT}.")
        sys.stdout.flush()
        time.sleep(0.2)
    
    # Hapus loading text (Timpa dengan spasi kosong lalu kembali ke awal)
    sys.stdout.write("\r" + " " * 70 + "\r")
    
    # Tampilkan HEADER Final (Box Style)
    print(f"   {C_MAIN}┌{'─'*65}┐{C_RESET}")
    # Isi Header: Waktu | User | Status Aktif
    print(f"   {C_MAIN}│ {C_WHITE}TIME: {C_ACCENT}{t} {C_GREY}| {C_WHITE}SERVER: {C_ACCENT}MAIN {C_GREY}| {C_WHITE}STATUS: {C_GREEN}● ONLINE {C_MAIN}{' '*18}│{C_RESET}")
    print(f"   {C_MAIN}└{'─'*65}┘{C_RESET}")

def show_footer(success=True):
    t = datetime.now().strftime("%H:%M:%S")
    
    # Icon status yang jelas
    if success:
        status = f"{C_GREEN}[✓] SUCCESS{C_RESET}"
        msg = f"Task completed at {t}"
    else:
        status = f"{C_RED}[✗] FAILED {C_RESET}"
        msg = f"Error occurred at {t}"

    # Footer simpel tapi informatif
    print(f"\n   {C_DARK}{'='*67}{C_RESET}")
    print(f"   {status} {C_GREY}>> {C_WHITE}{msg}{C_RESET}")
    print(f"   {C_DARK}{'='*67}{C_RESET}\n")