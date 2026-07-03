# ==========================================
# DecodeLabs AI Project 4
# Image Text Recognition using OCR
# Developed by: Nadendla Sai Vyshnavi
# ==========================================

import os
import shutil
from pathlib import Path

import cv2
import pytesseract


def find_tesseract():
    # Use an explicit Tesseract path if present in the environment
    explicit_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    ]

    for path in explicit_paths:
        if Path(path).is_file():
            return str(path)

    found = shutil.which("tesseract")
    if found:
        return found

    return None


def main():
    tesseract_path = find_tesseract()
    if not tesseract_path:
        print("Error: Tesseract OCR executable not found.")
        print("Install Tesseract from https://github.com/tesseract-ocr/tesseract or add it to your PATH.")
        return

    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    print("=" * 60)
    print("      AI IMAGE TEXT RECOGNITION")
    print("=" * 60)

    image_path = input("Enter image file name (example: sample_image.png): ")
    image_file = Path(image_path)

    if not image_file.is_file():
        print("Error: Image not found! Please check the file name and location.")
        return

    image = cv2.imread(str(image_file))
    if image is None:
        print("Error: Unable to read the image. The file may be corrupted or invalid.")
        return

    text = pytesseract.image_to_string(image)

    print("\nRecognized Text")
    print("-" * 30)
    print(text)

    with open("recognized_text.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("\nText saved successfully in recognized_text.txt")


if __name__ == "__main__":
    main()
