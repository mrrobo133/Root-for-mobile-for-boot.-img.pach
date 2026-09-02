#!/bin/bash

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
RESET='\033[0m'

clear
echo -e "${CYAN}==========================================${RESET}"
echo -e "${GREEN}    Root-Tool Secure Engine Installer     ${RESET}"
echo -e "${CYAN}==========================================${RESET}"

cd "$(dirname "$0")"

ZIP_PATH="/sdcard/Download/main.py.zip"
TARGET_DIR="./binaries"
PASSWORD="123456789"

if [ ! -f "$ZIP_PATH" ]; then
    echo -e "${RED}[-] Critical Error: main.py.zip not found in Download folder!${RESET}"
    echo -e "${YELLOW}[*] Please download main.py.zip from the Releases page and place it in /sdcard/Download/.${RESET}"
    exit 1
fi

echo -e "${YELLOW}[*] Creating binaries workspace...${RESET}"
mkdir -p "$TARGET_DIR"

echo -e "${YELLOW}* Extracting engines securely using password...${RESET}"
unzip -P "$PASSWORD" -o "$ZIP_PATH" -d "$TARGET_DIR"

if [ $? -ne 0 ]; then
    echo -e "${RED}[-] Extraction Failed! Incorrect password or corrupted file.${RESET}"
    exit 1
fi

# Fix if a nested folder was created during extraction
if [ -d "$TARGET_DIR/main.py" ]; then
    echo -e "${YELLOW}[*] Flattening nested directory structure...${RESET}"
    cp -r "$TARGET_DIR/main.py/"* "$TARGET_DIR/"
    rm -rf "$TARGET_DIR/main.py"
fi

# Setting up executable permissions for all binaries
echo -e "${YELLOW}[*] Setting execution permissions...${RESET}"
chmod +x "$TARGET_DIR"/*

if [ -f "tool.py" ]; then
    chmod +x tool.py
fi

if [ -f "main.py" ]; then
    chmod +x main.py
fi

echo -e "${GREEN}[+] Installation & Engine Setup 100% Complete!${RESET}"
echo -e "${CYAN}[*] You can now launch your tool using: python3 tool.py${RESET}"
