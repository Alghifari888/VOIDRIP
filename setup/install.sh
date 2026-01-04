#!/bin/bash
# VOIDRIP Auto-Installer

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}:: VOIDRIP Installer v2.0${NC}"

# 1. Cek Root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}[!] Please run as root (sudo)${NC}"
    exit 1
fi

# 2. Install System Deps
echo -e "\n${CYAN}:: Installing System Dependencies...${NC}"
apt update && apt install -y python3 python3-pip python3-venv ffmpeg

# 3. Install Python Libs
echo -e "\n${CYAN}:: Installing Python Libraries...${NC}"
# Mundur satu folder ke root untuk cari requirements.txt
pip3 install -r ../requirements.txt --break-system-packages

# 4. Setup Global Command
echo -e "\n${CYAN}:: Setting up shortcut...${NC}"
# Mencari path absolut ke main.py dari folder setup
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
MAIN_FILE="$ROOT_DIR/main.py"

chmod +x "$MAIN_FILE"
ln -sf "$MAIN_FILE" /usr/local/bin/voidrip

echo -e "\n${GREEN}[✓] Installation Complete!${NC}"
echo -e "Run using command: ${CYAN}voidrip${NC}"