import cv2
import numpy as np
from PIL import Image

def image_to_ascii(image_path, output_width=100):
    # Read and convert image to grayscale
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = img.shape
    aspect_ratio = height / width
    new_height = int(output_width * aspect_ratio)
    img = cv2.resize(img, (output_width, new_height), interpolation=cv2.INTER_AREA)

    # Define ASCII characters (darker to lighter)
    ascii_chars = "@%#*+=-:. "
    ascii_scale = 256 / len(ascii_chars)

    # Convert image to ASCII
    ascii_art = ""
    for i in range(new_height):
        for j in range(output_width):
            pixel = img[i, j]
            ascii_art += ascii_chars[int(pixel // ascii_scale)]
        ascii_art += "\n"

    return ascii_art

# Usage
if __name__ == "__main__":
    image_path = "your_image.jpg"  # Replace with your image path
    ascii_art = image_to_ascii(image_path)
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_art)
