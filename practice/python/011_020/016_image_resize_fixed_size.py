from PIL import Image
from pathlib import Path

input_folder = Path('images')
output_folder = Path('resize_fixed')
output_folder.mkdir(exist_ok=True)

for f in input_folder.glob('*.png'):
    img = Image.open(f)
    resized_img = img.resize((500, 500))
    save_path = output_folder.joinpath(f.name)
    resized_img.save(save_path)
    img.close()