#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
import os
import argparse
import time
from colorama import init as colorama_init

# Import Modules
try:
    from ui.banner import show_banner, show_header, show_footer
    from ui.display import ui_print, loading_animation
    from core import downloader, utils
except ImportError as e:
    print(f"Error: Module corrupt ({e}). Harap install ulang.")
    sys.exit(1)

# Inisialisasi warna Windows
colorama_init(autoreset=True)

# --- CONFIGURATION & HELP ---
CUSTOM_HELP_TEXT = """
\033[1;33mCARA MENGGUNAKAN:\033[0m
 
  # Download video dengan resolusi 720p (Recommended)
  voidrip video "URL_VIDEO" --res 720

  # Download dengan nama custom
  voidrip video "URL_VIDEO" --res 720 -o "test.mp4"

\033[1;33mDOWNLOAD AUDIO (MP3):\033[0m
  # Download audio default quality
  voidrip audio "URL_VIDEO"

  # Download audio dengan nama custom
  voidrip audio "URL_VIDEO" -o "lagu_favorit.mp3"

\033[1;33mPERINTAH BANTU:\033[0m
  voidrip --help
  voidrip video --help
  voidrip --version
"""

def get_save_location(out_arg):
    """Menghitung lokasi penyimpanan absolut untuk info user"""
    if "%" in out_arg:
        # Jika pakai template (default), file ada di folder output/working dir
        d = os.path.dirname(out_arg)
        return os.path.abspath(d) if d else os.getcwd()
    else:
        # Jika nama file fix, return full path filenya
        return os.path.abspath(out_arg)

def main():
    parser = argparse.ArgumentParser(
        prog="voidrip",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=CUSTOM_HELP_TEXT
    )
    
    parser.add_argument('--version', action='version', version='VOIDRIP v2.0')
    sub = parser.add_subparsers(dest="cmd", metavar="<command>")
    
    # Video Command
    v = sub.add_parser("video", help="Download Video (MP4)")
    v.add_argument("url", help="Target URL")
    v.add_argument("--res", default="1080", choices=["360", "480", "720", "1080", "1440", "2160"], help="Resolution")
    v.add_argument("-o", "--output", default="%(title)s.%(ext)s", help="Output filename")

    # Audio Command
    a = sub.add_parser("audio", help="Download Audio (MP3)")
    a.add_argument("url", help="Target URL")
    a.add_argument("--bitrate", default="192", help="Bitrate (kbps)")
    a.add_argument("-o", "--output", default="%(title)s.%(ext)s", help="Output filename")

    # Playlist Command
    p = sub.add_parser("playlist", help="Download Playlist")
    p.add_argument("url", help="Target URL")
    p.add_argument("-o", "--output", default="%(playlist_title)s/%(title)s.%(ext)s", help="Output directory")
    p.add_argument("--start", type=int, help="Start item")
    p.add_argument("--end", type=int, help="End item")

    # Tampilkan Banner jika tanpa argumen
    if len(sys.argv) == 1:
        show_banner()
        print(CUSTOM_HELP_TEXT)
        sys.exit(0)

    args = parser.parse_args()

    show_banner()
    show_header()
    
    try:
        # System Info
        os_info = utils.get_os_info()
        ui_print(f"HOST: {os_info['node']:<20} OS: {os_info['system']:<10}", "info")
        print("\033[38;5;51m" + "─" * 65 + "\033[0m")

        missing = utils.check_system_deps()
        if missing:
            ui_print(f"Warning: {', '.join(missing)} not found!", "warn")
            time.sleep(2)
            
        ui_print(f"Processing {args.cmd.upper()} Request...", "step")
        loading_animation("Establishing connection...")
        
        success = False
        print("\033[38;5;51m" + "─" * 65 + "\033[0m")
        
        # Eksekusi Download
        if args.cmd == "video":
            success = downloader.download_video(args.url, args.res, args.output)
        elif args.cmd == "audio":
            success = downloader.download_audio(args.url, args.bitrate, args.output)
        elif args.cmd == "playlist":
            success = downloader.download_playlist(args.url, args.output, args.start, args.end)
            
        # Info Lokasi File (Fitur Baru)
        if success:
            save_path = get_save_location(args.output)
            print(f"\n   \033[1;38;5;46m[SAVED TO] >\033[0m {save_path}")

        show_footer(success)

    except KeyboardInterrupt:
        print("\n")
        ui_print("Process interrupted by user", "error")
        show_footer(False)
    except Exception as e:
        ui_print(f"Unexpected Error: {e}", "error")
        show_footer(False)

if __name__ == "__main__":
    main()