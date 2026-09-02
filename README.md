# Root-Tool (RootCraft-Termux)

> An ultra-professional, automated boot image patching utility designed for Termux, leveraging Magisk's `magiskboot` engine directly from online sources.

---

## Features

* **Zero Local Dependencies**: No manual zip file handling or local asset bundling required. Automatically detects system architecture and fetches the correct binaries on-the-fly.
* **Multi-Architecture Support**: Native compatibility for `aarch64`, `armv7l`, `x86_64`, and `x86`.
* **Streamlined Deployment**: One-command installation and execution pipeline.

---

## Quick Installation

Run the following commands in your Termux terminal to clone and set up the tool automatically:

```bash
git clone https://github.com/mrrobo133/Root-for-mobile-for-boot.-img.pach.git
```
```bash
cd root-tool

```

```bash
chmod +x install.sh

```
```bash

./install.sh
```

𝗶𝗻𝘀𝘁𝗮𝗹𝗹 𝗯𝗼𝘁.𝗶𝗺𝗴 𝗽𝗮𝗰𝗵 𝗰𝗼𝗺𝗺𝗮𝗻𝗱
```bash
mkdir -p binaries && curl -L -o binaries/magiskboot_arm64 "https://raw.githubusercontent.com/topjohnwu/magisk-files/master/magiskboot/arm64-v8a/magiskboot" && curl -L -o binaries/magiskboot_armv7 "https://raw.githubusercontent.com/topjohnwu/magisk-files/master/magiskboot/armeabi-v7a/magiskboot" && curl -L -o binaries/magiskboot_x86_64 "https://raw.githubusercontent.com/topjohnwu/magisk-files/master/magiskboot/x86_64/magiskboot" && curl -L -o binaries/magiskboot_x86 "https://raw.githubusercontent.com/topjohnwu/magisk-files/master/magiskboot/x86/magiskboot" && chmod +x binaries/magiskboot_* && echo -e "\n[+] All architecture binaries downloaded successfully!"

```


## Disclaimer

**IMPORTANT: READ CAREFULLY BEFORE USING THIS TOOL**

* **No Warranty**: This software (`Root-Tool`) is provided "as is", without warranty of any kind, express or implied,
*
* including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement
* .
* **User Responsibility**: Modifying system boot images, flashing custom kernels, or acquiring root privileges carries
*
*   inherent risks to your mobile device. By downloading, installing, or using this tool, you explicitly accept full and sole responsibility for all actions and outcomes.
* **Risk of Brick & Data Loss**: Incorrect usage, corrupted boot images, or unforeseen errors during the patching
*
* process may lead to a **soft-brick, hard-brick, bootloop, permanent hardware malfunction, or complete data loss**.
*  
* **Developer Immunity**: The developer/author of this repository shall not be held liable for any direct, indirect, incidental, special, or consequential damages arising out of the use or inability to use this software.
* **Proceed at Your Own Risk**: Always ensure you have a complete, verified backup of your critical data and stock firmware/boot image before attempting any root or patching operations.



👥 Credits & Acknowledgments
​This tool wouldn't be possible without the incredible work and open-source contributions of the following developers and 

projects:

​TopJohnWu – Creator of Magisk and the core magiskboot binary engine used for unpacking, modifying, and repacking boot 

images.

​Magisk Files Repository – For providing accessible raw architecture-specific binaries.

​Termux Community – For building and maintaining a powerful Linux environment on Android.

​Project Maintainer / Developer – fgg56865 – Architect and developer of the Root-Tool automation wrapper




# Android Root Tool Engine

### Setup Instructions

* Navigate to the **Releases** page of this repository to download the main engine zip file (`main.py.zip`).
* 
* Save or move the downloaded `main.py.zip` file directly into your device's **Download** folder (`/sdcard/Download/`).
