from PIL import Image
from pathlib import Path

target_width = 500

input_folder = Path('images')
output_folder = Path('resize_ratio')
output_folder.mkdir(exist_ok=True)

for f in input_folder.glob('*.png'):
    img = Image.open(f)
    ratio = target_width / img.size[0]
    resized_img = img.resize((target_width, int(img.size[1] * ratio)))
    save_path = output_folder.joinpath(f.name)
    resized_img.save(save_path)
    img.close()