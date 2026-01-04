#!/bin/bash
# VOIDRIP Auto-Installer (Ultimate Version)

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}:: VOIDRIP Installer v2.0${NC}"

# 1. Cek Root (Wajib Sudo)
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}[!] Harap jalankan menggunakan sudo!${NC}"
    echo -e "Contoh: sudo ./install.sh"
    exit 1
fi

# 2. Deteksi Lokasi Folder Secara Otomatis (DINAMIS)
# Script ini akan mencari tahu sendiri dia ada di folder mana
# Walaupun usernya bukan 'alghifari888', dia akan tetap tahu.
SETUP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_DIR="$(dirname "$SETUP_DIR")"
MAIN_FILE="$PROJECT_DIR/main.py"

echo -e "\n${CYAN}:: Mendeteksi lokasi project...${NC}"
echo -e "   Lokasi: $PROJECT_DIR"

# 3. Install Dependencies
echo -e "\n${CYAN}:: Menginstall kebutuhan sistem...${NC}"
apt update -qq
apt install -y python3 python3-pip ffmpeg > /dev/null 2>&1
pip3 install -r "$PROJECT_DIR/requirements.txt" --break-system-packages

# 4. MEMBUAT LAUNCHER (Ini Rahasianya)
# Kita buat file 'jembatan' di /usr/local/bin/voidrip
# Isinya memaksa Linux masuk ke folder project lalu panggil Python
echo -e "\n${CYAN}:: Membuat Launcher Global...${NC}"

cat > /usr/local/bin/voidrip <<EOF
#!/bin/bash
# Launcher Otomatis VOIDRIP
cd "$PROJECT_DIR"
exec python3 main.py "\$@"
EOF

# 5. Beri Izin Eksekusi
chmod +x /usr/local/bin/voidrip
chmod +x "$MAIN_FILE"

echo -e "\n${GREEN}[✓] INSTALASI BERHASIL 100%!${NC}"
echo -e "Sekarang Anda (atau siapapun) bisa menjalankannya dengan mengetik:"
echo -e "${CYAN}voidrip${NC}"