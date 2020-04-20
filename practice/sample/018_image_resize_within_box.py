from PIL import Image
from pathlib import Path

box_size = 500

input_folder = Path('images')
output_folder = Path('resize_in_box')
output_folder.mkdir(exist_ok=True)

for f in input_folder.glob('*.png'):
    img = Image.open(f)
    width, height = img.size
    ratio = box_size / max(img.size)
    resized_img = img.resize((int(width * ratio), int(height * ratio)))
    save_path = output_folder.joinpath(f.name)
    resized_img.save(save_path)
    img.close()