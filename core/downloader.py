import subprocess
import sys
from ui.display import ui_print

def run_yt(args, verbose=False):
    """Wrapper untuk menjalankan yt-dlp"""
    base_cmd = ["yt-dlp", "--no-warnings"]
    
    if not verbose:
        base_cmd.append("--progress")
    else:
        base_cmd.append("--verbose")
    
    cmd = base_cmd + args
    
    try:
        # Menggunakan shell=False untuk keamanan
        # capture_output=False agar progress bar yt-dlp terlihat langsung
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        ui_print(f"Download Error (Code: {e.returncode})", "error")
        return False
    except FileNotFoundError:
        ui_print("yt-dlp tidak ditemukan. Pastikan sudah install requirements.txt", "error")
        return False
    except KeyboardInterrupt:
        ui_print("Download dibatalkan user.", "warn")
        return False

def download_video(url, res, out_pattern):
    format_str = f"bv*[height<={res}][ext=mp4]+ba[ext=m4a]/b[height<={res}]"
    
    args = [
        "-f", format_str,
        "--merge-output-format", "mp4",
        "--convert-thumbnails", "jpg",
        "--embed-thumbnail",
        "--embed-metadata",
        "--restrict-filenames", # Penting untuk Windows
        "-o", out_pattern,
        url
    ]
    return run_yt(args)

def download_audio(url, bitrate, out_pattern):
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