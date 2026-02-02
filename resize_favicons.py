
import sys
from PIL import Image

def resize_image(input_path, output_path, size):
    try:
        with Image.open(input_path) as img:
            img = img.resize((size, size), Image.Resampling.LANCZOS)
            img.save(output_path)
            print(f"Successfully created {output_path}")
    except Exception as e:
        print(f"Error creating {output_path}: {e}")

input_image = r"C:\Users\User\.gemini\antigravity\brain\bac7711f-e762-4f9d-9ddc-8f30ec6ef458\uploaded_media_0_1769972183886.png"

resize_image(input_image, "c:/mickaportifolio/public/favicon-32x32.png", 32)
resize_image(input_image, "c:/mickaportifolio/public/favicon-16x16.png", 16)
resize_image(input_image, "c:/mickaportifolio/public/apple-touch-icon.png", 180)
resize_image(input_image, "c:/mickaportifolio/public/android-chrome-192x192.png", 192)
