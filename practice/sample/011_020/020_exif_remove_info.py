from PIL import Image
from pathlib import Path

file_name = 'image/IMG_5988.JPG'
img = Image.open(file_name)
output_folder = Path('exif_remove')
output_folder.mkdir(exist_ok=True)

save_path = output_folder.joinpath(file_name.split('/')[-1])
img.save(save_path)
