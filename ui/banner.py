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

from datetime import datetime

BANNER_TEXT = r"""
\033[38;5;51m ┌─────────────────────────────────────────────────────────────────────────┐
\033[38;5;51m ║ \033[1;38;5;87m██╗   ██╗ ██████╗ ██╗██████╗ ██████╗ ██╗██████╗ ║\033[38;5;51m║
\033[38;5;51m ║ \033[1;38;5;87m██║   ██║██╔═══██╗██║██╔══██╗██╔══██╗██║██╔══██╗║\033[38;5;51m║
\033[38;5;51m ║ \033[1;38;5;87m██║   ██║██║   ██║██║██║  ██║██████╔╝██║██████╔╝║\033[38;5;51m║
\033[38;5;51m ║ \033[1;38;5;87m╚██╗ ██╔╝██║   ██║██║██║  ██║██╔══██╗██║██╔═══╝ ║\033[38;5;51m║
\033[38;5;51m ║ \033[1;38;5;87m ╚████╔╝ ╚██████╔╝██║██████╔╝██║  ██║██║██║     ║\033[38;5;51m║
\033[38;5;51m ║ \033[1;38;5;87m  ╚═══╝   ╚═════╝ ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ║\033[38;5;51m║ 
\033[38;5;51m ├─────────────────────────────────────────────────────────────────────────┤
\033[38;5;51m │                                                                         │
\033[38;5;51m │ \033[0;38;5;195m  High Speed Terminal Downloader • v2.0 \033[38;5;51m   │
\033[38;5;51m │ \033[0;38;5;195m        by: alghifari888 \033[38;5;51m                  │
\033[38;5;51m │ \033[0;38;5;117m     github.com/alghifari888 \033[38;5;51m              │
\033[38;5;51m │                   http://www.apache.org/licenses/LICENSE-2.0            │
\033[38;5;51m └─────────────────────────────────────────────────────────────────────────┘\033[0m
"""

def show_banner():
    print(BANNER_TEXT)

def show_header():
    current_time = datetime.now().strftime("%H:%M:%S")
    print("\033[38;5;51m╔══════════════════════════════════════════════════════════╗\033[0m")
    print(f"\033[38;5;51m║ \033[38;5;195mSESSION STARTED: {current_time} | STATUS: \033[1;38;5;46mACTIVE\033[0;38;5;51m          ║")
    print("\033[38;5;51m╚══════════════════════════════════════════════════════════╝\033[0m")

def show_footer(success=True):
    current_time = datetime.now().strftime("%H:%M:%S")
    print("\n\033[38;5;51m╔══════════════════════════════════════════════════════════╗\033[0m")
    if success:
        print(f"\033[38;5;51m║ \033[1;38;5;46m✓ OPERATION COMPLETED\033[0;38;5;195m at {current_time}                \033[38;5;51m║")
    else:
        print(f"\033[38;5;51m║ \033[1;38;5;196m✗ OPERATION FAILED\033[0;38;5;195m at {current_time}                   \033[38;5;51m║")
    print("\033[38;5;51m╚══════════════════════════════════════════════════════════╝\033[0m")