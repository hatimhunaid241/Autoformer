#!/usr/bin/env python3
"""
Script to download Autoformer datasets.

The datasets are hosted on Google Drive. Due to Google Drive's limitations,
automatic download of large files requires special handling.

For easier download, please manually download from:
https://drive.google.com/drive/folders/1ZOYpTUa82_jCcxIdTmyr0LXQfvaM9vIy?usp=sharing

Alternatively, you can use gdown to download from Google Drive.
"""

import os
import sys

def download_with_gdown():
    """Download using gdown library for Google Drive files."""
    try:
        import gdown
    except ImportError:
        print("gdown is not installed. Installing...")
        os.system(f"{sys.executable} -m pip install gdown")
        import gdown
    
    os.makedirs('dataset', exist_ok=True)
    
    print("=" * 60)
    print("Autoformer Dataset Downloader")
    print("=" * 60)
    print("\nNote: Google Drive has limits on automated downloads.")
    print("If this fails, please manually download from:")
    print("https://drive.google.com/drive/folders/1ZOYpTUa82_jCcxIdTmyr0LXQfvaM9vIy")
    print("=" * 60)
    print()
    
    # Google Drive folder ID for the datasets
    folder_url = 'https://drive.google.com/drive/folders/1ZOYpTUa82_jCcxIdTmyr0LXQfvaM9vIy'
    
    print(f"Downloading from: {folder_url}")
    print("This will download all datasets to ./dataset/ folder")
    print()
    
    try:
        gdown.download_folder(folder_url, output='dataset/', quiet=False, use_cookies=False)
        print("\n✓ Download complete!")
        print("You can now run the experiments.")
    except Exception as e:
        print(f"\n✗ Download failed: {e}")
        print("\nPlease manually download the datasets:")
        print("1. Visit: https://drive.google.com/drive/folders/1ZOYpTUa82_jCcxIdTmyr0LXQfvaM9vIy")
        print("2. Download the required datasets (ETT-small, weather, etc.)")
        print("3. Extract them to the ./dataset/ folder")
        print("\nExpected structure:")
        print("  dataset/")
        print("    ETT-small/")
        print("      ETTm1.csv")
        print("      ETTm2.csv")
        print("      ...")
        print("    weather/")
        print("      weather.csv")
        print("    ...")
        return False
    
    return True

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("IMPORTANT: Manual download recommended")
    print("=" * 60)
    print("\nThe easiest way to get the datasets:")
    print("1. Visit: https://drive.google.com/drive/folders/1ZOYpTUa82_jCcxIdTmyr0LXQfvaM9vIy")
    print("2. Download the datasets you need")
    print("3. Extract to ./dataset/ folder")
    print("\nPress Enter to try automatic download, or Ctrl+C to cancel...")
    
    try:
        input()
        download_with_gdown()
    except KeyboardInterrupt:
        print("\n\nDownload cancelled. Please download manually from Google Drive.")
