# yt-2-mp4 🎬

A lightweight Python script to download YouTube videos and Shorts in the highest possible quality using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).

---

## 📋 Features

- Downloads video and audio at the best available resolutions (1080p, 4K, 60fps, etc.).
- Automatically merges separate video and audio streams into a single playable MP4 file.
- Works with standard YouTube URLs and Shorts.

---

## ⚙️ Prerequisites & Setup

YouTube delivers modern high-definition streams with separate video and audio tracks. To merge them properly and avoid extraction errors, ensure the dependencies below are installed.

### 1. Install Python Dependencies

Install the `yt-dlp` package using `pip`:

```bash
pip install -U yt-dlp
```

---

### 2. Install FFmpeg (Required for Merging Video & Audio)

If you see the error:
> `ERROR: You have requested merging of multiple formats but ffmpeg is not installed.`

`yt-dlp` needs **FFmpeg** to merge the downloaded audio and video streams together.

#### On Windows:
Run this command in PowerShell or Command Prompt (as Administrator):
```powershell
winget install Gyan.FFmpeg
```
*Note: Restart your terminal or code editor after installation so the `PATH` environment variable updates.*

#### On macOS:
```bash
brew install ffmpeg
```

#### On Linux (Ubuntu/Debian):
```bash
sudo apt update && sudo apt install ffmpeg -y
```

---

### 3. Optional: Install a JavaScript Runtime (Deno)

If you see a warning about a missing JavaScript runtime:
> `WARNING: [youtube] No supported JavaScript runtime could be found.`

YouTube uses JavaScript challenges to verify requests. Installing Deno resolves this warning:

#### Windows:
```powershell
winget install DenoLand.Deno
```

#### macOS / Linux:
```bash
curl -fsSL https://deno.land/install.sh | sh
```

---

## 🚀 Usage

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/saksham17-tech/yt-2-mp4.git
   cd yt-2-mp4
   ```

2. Run the script:
   ```bash
   python yt-2-mp4.py
   ```

3. Paste your video or Shorts URL when prompted:
   ```text
   Enter URL: https://www.youtube.com/watch?v=...
   ```

The downloaded file will be saved in the directory where the script is executed.

---

## 🛠️ Script Overview

```python
import yt_dlp

url = input("Enter URL: ")

ydl_opts = {
    "format": "bestvideo+bestaudio/best",
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).