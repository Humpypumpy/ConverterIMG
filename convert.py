from PIL import Image
import os

def convert_image(input_path, output_format):
    with Image.open(input_path) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        output_file = f"{os.path.splitext(input_path)[0]}.{output_format.lower()}"
        img.save(output_file, output_format.upper())
        return output_file