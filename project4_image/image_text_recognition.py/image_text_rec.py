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

    # Preprocess image for better OCR accuracy
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Upscale to improve small-text recognition
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # Reduce noise while keeping edges
    gray = cv2.bilateralFilter(gray, 9, 75, 75)
    # Use Otsu's thresholding to get a clean binary image
    _, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # Optional morphology to remove tiny specks
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    processed = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)

    # Tesseract config: use LSTM engine, assume a single uniform block of text (psm 6)
    # and restrict the character set to common printable characters to reduce mistakes.
    config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?()[]%$@:/+-'

    # Run OCR on preprocessed image
    text = pytesseract.image_to_string(processed, config=config)

    print("\nRecognized Text")
    print("-" * 30)
    print(text)

    with open("recognized_text.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("\nText saved successfully in recognized_text.txt")


if __name__ == "__main__":
    main()
