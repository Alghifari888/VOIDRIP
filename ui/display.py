import sys
from colorama import Fore, Style

def ui_print(msg, type="info"):
    marks = {
        "info": "\033[1;38;5;117m[ℹ]\033[0m", 
        "ok": "\033[1;38;5;46m[✓]\033[0m", 
        "warn": "\033[1;38;5;208m[!]\033[0m", 
        "load": "\033[1;38;5;141m[↻]\033[0m",
        "error": "\033[1;38;5;196m[✗]\033[0m",
        "step": "\033[1;38;5;51m[→]\033[0m"
    }
    print(f"{marks.get(type, '[ℹ]')} \033[38;5;252m{msg}\033[0m")

def progress_bar(progress, width=40):
    filled = int(width * progress)
    bar = f"\033[38;5;51m[\033[1;38;5;46m{'█' * filled}\033[38;5;240m{'░' * (width - filled)}\033[38;5;51m]\033[0m"
    percent = f"{progress*100:.1f}%"
    return f"{bar} {percent}"

def loading_animation(text, duration=3):
    """loading sederhana"""
    import time
    ui_print(text, "load")
    for i in range(1, duration + 1):
        time.sleep(0.2)
        prog = i / duration
        print(f"   {progress_bar(prog, 30)}", end="\r")
    print() # Newline