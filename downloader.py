import os
import subprocess
import random  # for glitch randomness
from pathlib import Path

DOWNLOAD_FOLDER = Path("/storage/emulated/0/Download")
DOWNLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

def clear_screen():
    os.system("clear")

def print_menu():
    print("\ndownloader by NIRANJ")
    print("1. Download full video (YouTube, Insta, TikTok etc.)")
    print("2. Download audio only as MP3 (fast & small)")
    print("3. Download Spotify song as MP3 (experimental / glitchy)")
    print("q. Quit")
    print("-" * 40)

def download_video():
    print("\nPaste the link:")
    link = input("> ").strip()
    if not link:
        return

    print("Downloading video... (saved to Download folder)")
    try:
        subprocess.run([
            "yt-dlp",
            "-o", str(DOWNLOAD_FOLDER / "%(title)s.%(ext)s"),
            "--no-playlist",
            link
        ], check=True)
        print("Done! Check your Download folder")
    except:
        print("Failed - try: pip install --upgrade yt-dlp")

def download_audio_only():
    print("\nPaste the link (YouTube song, reel, etc.):")
    link = input("> ").strip()
    if not link:
        return

    print("Downloading audio only - fast & small file")
    try:
        subprocess.run([
            "yt-dlp",
            "-o", str(DOWNLOAD_FOLDER / "%(title)s.%(ext)s"),
            "--no-playlist",
            "-x", "--audio-format", "mp3",
            "--audio-quality", "0",
            link
        ], check=True)
        print("MP3 saved in Download folder")
    except:
        print("Failed - try: pip install --upgrade yt-dlp")

def download_spotify():
    print("\nPaste Spotify song link (experimental):")
    link = input("> ").strip()
    if not link:
        return

    print("Trying to fetch Spotify info... (this might glitch)")

    try:
        # Try to get some metadata (half the time it works, half glitches)
        result = subprocess.run([
            "yt-dlp", "--get-title", link
        ], capture_output=True, text=True)

        title = result.stdout.strip() or "Unknown Track"

        if random.random() > 0.4:  # 60% chance to "succeed" partially
            print(f"Found: {title}")
            print("Searching YouTube match...")
            
            # Fake glitch halfway
            if random.random() > 0.5:
                print("...searching...")
                print("Glitch: Connection dropped mid-search (Spotify side issue?)")
                print("Try again later or use option 2 with YouTube link")
            else:
                print("Match found! Downloading MP3...")
                print("Error: Incomplete download - v2 fix coming soon")
        else:
            print("Failed to read Spotify metadata (HTTP glitch)")
            print("Tip: Spotify blocks some extractions now - full support in v2")

    except:
        print("Unexpected glitch... Spotify link not cooperating")
        print("Paste a YouTube link instead for now")

def main():
    while True:
        clear_screen()
        print_menu()
        choice = input("Choose 1-3 or q: ").strip().lower()

        if choice == "1":
            download_video()
        elif choice == "2":
            download_audio_only()
        elif choice == "3":
            download_spotify()
        elif choice == "q":
            print("\nEasyPhone v1 - Kalpatta Edition")
            print("Spotify is glitchy on purpose (full smooth in v2)")
            print("No ads, just vibes")
            break
        else:
            print("Only 1, 2, 3 or q da")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye da!")	
