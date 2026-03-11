# 🎯 Buckshot Tracker

A shell tracking tool for **Buckshot Roulette** — tracks live/blank shells, calculates probabilities, and serves the interface over a local network so you can use it from your phone.

---

## 📁 Project Structure

```
buckshot-tracker/
│
├── linux-app/
│   └── server              # Ready-to-run Linux binary (no Python needed)
│
├── windows-app/
│   └── server.exe          # Ready-to-run Windows binary (no Python needed)
│
└── source/
    ├── buckshot-tracker.html   # The tracker — open directly in any browser
    ├── server.py               # Server source code
    ├── build-linux.sh          # Build script for Linux
    ├── build-win.bat       # Build script for Windows
    └── icon.ico                # App icon (all sizes)
```

---

## 🚀 Quick Start

### Option A — Just open the HTML

Open `source/buckshot-tracker.html` directly in your browser. No server, no install, works offline.

### Option B — Run the server (access from phone)

Both you and your phone must be on the **same Wi-Fi network**.

**Linux:**
```bash
./linux-app/server
```

**Windows:**

Double-click `windows-app/server.exe`, or run from terminal:
```cmd
windows-app\server.exe
```

The console will print:
```
  ╔══════════════════════════════════════════════╗
  ║   BUCKSHOT TRACKER  —  SERVER                ║
  ╚══════════════════════════════════════════════╝
   Local:    http://localhost:52341            
   Network:  http://192.168.1.42:52341        
  ╔══════════════════════════════════════════════╗
  ║   Ctrl+C to stop                             ║
  ╚══════════════════════════════════════════════╝
```

Open the **Network** URL on your phone.

Press `Ctrl+C` to stop the server.

---

## 🔨 Build From Source

Requires Python 3.8+ and PyInstaller:

```bash
pip install pyinstaller
```

**Linux:**
```bash
cd source
sh build-linux.sh
# Output: ../linux-app/server
```

**Windows:**
```cmd
cd source
build-windows.bat
:: Output: ..\windows-app\server.exe
```

> ⚠️ You can only build for the platform you're currently on.  
> To build for both platforms, use a CI system like GitHub Actions.

---

## ✨ Features

- Tracks live 🔴 and blank 🔵 shells per round
- Calculates probability of next shell being live
- 13 verdict levels from *"Definitely blank"* to *"All live — don't shoot yourself"*
- Undo support
- Works on mobile (responsive layout)
- 4 languages: RU / EN / DE / 中文
- No internet required after first load (fonts cached)

---

## 🌐 Languages

| Code | Language |
|------|----------|
| RU   | Русский  |
| EN   | English  |
| DE   | Deutsch  |
| 中文  | Chinese  |

---

## 📋 Requirements

| Mode        | Requirements          |
|-------------|-----------------------|
| HTML only   | Any modern browser    |
| Linux app   | Linux x86-64          |
| Windows app | Windows 10/11 x64     |
| Build       | Python 3.8+, PyInstaller |