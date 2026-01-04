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
import argparse
import time
from colorama import init as colorama_init

# Import Modules
from ui.banner import show_banner, show_header, show_footer
from ui.display import ui_print, loading_animation
from core import downloader, utils

# Inisialisasi warna untuk Windows
colorama_init(autoreset=True)

def main():
    # 1. Setup Argument Parser
    parser = argparse.ArgumentParser(
        prog="voidrip",
        description="VOIDRIP - High Speed Terminal Downloader",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
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

    # Jika dijalankan tanpa argumen
    if len(sys.argv) == 1:
        show_banner()
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    # 2. Tampilan Awal
    show_banner()
    show_header()
    
    # 3. System Check & Info
    os_info = utils.get_os_info()
    ui_print(f"HOST: {os_info['node']:<20} OS: {os_info['system']:<10}", "info")
    print("\033[38;5;51m" + "─" * 58 + "\033[0m")

    # Cek apakah FFmpeg ada (Penting untuk Windows/Linux)
    missing_deps = utils.check_system_deps()
    if missing_deps:
        ui_print(f"Warning: {', '.join(missing_deps)} not found!", "warn")
        ui_print("Beberapa fitur (convert mp3/merge video) mungkin gagal.", "warn")
        time.sleep(2)

    try:
        # 4. Eksekusi
        ui_print(f"Processing {args.cmd.upper()} request...", "step")
        loading_animation("Initializing connection...")
        
        success = False
        print("\033[38;5;51m" + "─" * 58 + "\033[0m")
        
        if args.cmd == "video":
            success = downloader.download_video(args.url, args.res, args.output)
        elif args.cmd == "audio":
            success = downloader.download_audio(args.url, args.bitrate, args.output)
        elif args.cmd == "playlist":
            success = downloader.download_playlist(args.url, args.output, args.start, args.end)
            
        show_footer(success)

    except KeyboardInterrupt:
        print("\n")
        ui_print("Process interrupted", "error")
        show_footer(False)
    except Exception as e:
        ui_print(f"Unexpected Error: {e}", "error")
        show_footer(False)

if __name__ == "__main__":
    main()