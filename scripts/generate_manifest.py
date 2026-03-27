"""
Run this script after adding or removing images:
  python misc/generate_manifest.py

It scans static/images/ and writes static/images/manifest.json,
which the website fetches at runtime to build the gallery dynamically.
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
IMAGES_DIR = os.path.join(PROJECT_ROOT, "static", "images")
MANIFEST_PATH = os.path.join(IMAGES_DIR, "manifest.json")

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".JPG", ".JPEG", ".PNG", ".GIF", ".WEBP"}

def main():
    images = sorted(
        f for f in os.listdir(IMAGES_DIR)
        if os.path.splitext(f)[1] in IMAGE_EXTENSIONS
    )
    with open(MANIFEST_PATH, "w", encoding="utf-8") as fh:
        json.dump({"images": images}, fh, ensure_ascii=False, indent=2)
    print(f"manifest.json updated: {len(images)} images listed.")

if __name__ == "__main__":
    main()
