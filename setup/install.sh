#!/bin/bash
# VOIDRIP Ultimate Installer for Linux
# Created by: github.com/alghifari888
# License: Apache 2.0


# --- WARNA & VISUAL ---
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# --- FUNGSI SPINNER (ANIMASI) ---
spinner() {
    local pid=$!
    local delay=0.1
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

clear
echo -e "${CYAN}======================================================${NC}"
echo -e "${CYAN}   VOIDRIP v2.0 :: ULTIMATE LINUX INSTALLER           ${NC}"
echo -e "${CYAN}   Created by: github.com/alghifari888                ${NC}"
echo -e "${CYAN}   LICENSE: Apache 2.0                                ${NC}"
echo -e "${CYAN}======================================================${NC}\n"

# 1. CEK ROOT
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}[X] ERROR: Script ini butuh akses ROOT.${NC}"
    echo -e "    Silakan jalankan: ${YELLOW}sudo ./install.sh${NC}"
    exit 1
fi

# 2. CEK KONEKSI INTERNET
echo -ne "${BLUE}[*] Mengecek koneksi internet...${NC}"
wget -q --spider http://google.com
if [ $? -eq 0 ]; then
    echo -e "${GREEN} [CONNECTED]${NC}"
else
    echo -e "${RED} [OFFLINE]${NC}"
    echo -e "${RED}[!] Harap sambungkan perangkat ke internet!${NC}"
    exit 1
fi

# 3. DETEKSI LOKASI PROJECT
SETUP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_DIR="$(dirname "$SETUP_DIR")"
MAIN_FILE="$PROJECT_DIR/main.py"

echo -e "${BLUE}[*] Lokasi Project:${NC} $PROJECT_DIR"

# 4. INSTALL DEPENDENCIES (DENGAN ANIMASI)
echo -ne "${BLUE}[*] Mengupdate repository & install System Deps...${NC}"
(apt-get update -qq && apt-get install -y python3 python3-pip ffmpeg > /dev/null 2>&1) &
spinner
echo -e "${GREEN} [DONE]${NC}"

echo -ne "${BLUE}[*] Menginstall Python Libraries (requirements.txt)...${NC}"
(pip3 install -r "$PROJECT_DIR/requirements.txt" --break-system-packages > /dev/null 2>&1) &
spinner
echo -e "${GREEN} [DONE]${NC}"

# 5. BUAT LAUNCHER GLOBAL
echo -ne "${BLUE}[*] Membuat Shortcut Global 'voidrip'...${NC}"
cat > /usr/local/bin/voidrip <<EOF
#!/bin/bash
# Launcher VOIDRIP by github.com/alghifari888
cd "$PROJECT_DIR"
exec python3 main.py "\$@"
EOF
chmod +x /usr/local/bin/voidrip
chmod +x "$MAIN_FILE"
sleep 0.5
echo -e "${GREEN} [DONE]${NC}"

# 6. SELESAI
echo -e "\n${GREEN}======================================================${NC}"
echo -e "${GREEN}   INSTALASI SUKSES! SIAP DIGUNAKAN.                    ${NC}"
echo -e "${GREEN}   VOIDRIP v2.0 - ULTIMATE LINUX INSTALLER              ${NC}"
echo -e "${GREEN}   Created by: github.com/alghifari888                  ${NC}"
echo -e "${GREEN}   LICENSE: Apache 2.0                                  ${NC}"
echo -e "${GREEN}========================================================${NC}"
echo -e "Ketik perintah ini di mana saja:"
echo -e "   ${CYAN}voidrip${NC}          (Untuk bantuan)"
echo -e "   ${CYAN}voidrip video ...${NC} (Untuk download)"
echo -e "\n${YELLOW}Enjoy the tools! - alghifari888${NC}"