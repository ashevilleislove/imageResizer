
from PIL import Image
import os

def resize_image(input_path, output_path, size):
    '''Resize the image to the specified size and save it to the output path.'''
    with Image.open(input_path) as img:
        img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)
        print(f"Image saved to {output_path}")

if __name__ == "__main__":
    input_path = "input.jpg"  # Path to the input image
    output_path = "output.jpg"  # Path to save the resized image
    size = (800, 600)  # New size
    resize_image(input_path, output_path, size)
