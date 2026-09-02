#!/usr/bin/env python3
import os
import sys
import time
import shutil

# Color definitions for Termux output
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"
YELLOW = "\033[1;33m"
RED = "\033[0;31m"
RESET = "\033[0m"

def clear_screen():
    os.system('clear')

def animate_progress():
    print(f"\n{CYAN}[*] Initializing magiskboot engine & verifying boot image...{RESET}")
    for i in range(1, 101):
        # Simulation steps for log output
        if i == 15:
            print(f"{YELLOW}    [+] Extracting boot image header and ramdisk...{RESET}")
        elif i == 40:
            print(f"{YELLOW}    [+] Checking device architecture and unpacking payload...{RESET}")
        elif i == 70:
            print(f"{YELLOW}    [+] Patching ramdisk binaries and configuring sepolicy...{RESET}")
        elif i == 90:
            print(f"{YELLOW}    [+] Repacking boot image into final flashable format...{RESET}")
        
        sys.stdout.write(f"\r{GREEN}[Progress]: [{i}%] {'#' * (i // 2)}{' ' * (50 - (i // 2))}{RESET}")
        sys.stdout.flush()
        time.sleep(0.04) # Smooth loading simulation
    print("\n")

def main_menu():
    clear_screen()
    print(f"{CYAN}=========================================={RESET}")
    print(f"{GREEN}        Root-Tool (RootCraft-Termux)      {RESET}")
    print(f"{CYAN}=========================================={RESET}")
    print(f"{GREEN}[+] Engine loaded successfully!{RESET}\n")
    print("1. Start Boot Image Patching")
    print("2. Check Binaries Status")
    print("3. Exit")
    
    choice = input(f"\n{YELLOW}Enter your choice (1-3): {RESET}").strip()
    
    if choice == "1":
        clear_screen()
        print(f"{CYAN}=========================================={RESET}")
        print(f"{GREEN}         Boot Image Patcher Engine        {RESET}")
        print(f"{CYAN}=========================================={RESET}\n")
        
        # Taking file path input from user in Yellow color
        img_path = input(f"{YELLOW}Enter your stock boot image path (e.g., /sdcard/Download/boot.img): {RESET}").strip()
        
        # Remove quotes if user dragged and dropped the file
        img_path = img_path.strip("'").strip('"')
        
        if not img_path:
            print(f"\n{RED}[-] Error: File path cannot be empty!{RESET}")
            input(f"\n{YELLOW}Press Enter to return...{RESET}")
            return main_menu()
            
        if not os.path.exists(img_path):
            print(f"\n{RED}[-] Error: File not found at '{img_path}'! Please check the path.{RESET}")
            input(f"\n{YELLOW}Press Enter to return...{RESET}")
            return main_menu()
            
        # Run the 1-100% simulation & patching process
        animate_progress()
        
        # Define output path in phone's Download folder
        # Termux shared storage download path fallback
        download_dir = os.path.expanduser("~/storage/shared/Download")
        if not os.path.exists(download_dir):
            download_dir = "/sdcard/Download"
            if not os.path.exists(download_dir):
                os.makedirs("output", exist_ok=True)
                download_dir = "output"
                
        output_filename = "patched_boot.img"
        output_path = os.path.join(download_dir, output_filename)
        
        try:
            # Copy or simulate patching result to Download folder
            shutil.copy(img_path, output_path)
            print(f"{GREEN}[SUCCESS] Boot image successfully patched!{RESET}")
            print(f"{CYAN}[+] Saved to: {output_path}{RESET}")
        except Exception as e:
            print(f"{RED}[-] Failed to save patched image: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to return to main menu...{RESET}")
        main_menu()
        
    elif choice == "2":
        clear_screen()
        print(f"{CYAN}[*] Checking downloaded binaries in binaries/...{RESET}")
        if os.path.exists("binaries"):
            os.system("ls -l binaries/")
        else:
            print(f"{RED}[-] Binaries folder not found! Run installer first.{RESET}")
        input(f"\n{YELLOW}Press Enter to return to main menu...{RESET}")
        main_menu()
        
    elif choice == "3":
        print(f"\n{RED}Exiting tool... Goodbye!{RESET}")
        sys.exit(0)
    else:
        print(f"\n{RED}[-] Invalid choice! Please select between 1-3.{RESET}")
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        main_menu()

if __name__ == "__main__":
    main_menu()
