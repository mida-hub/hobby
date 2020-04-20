from PIL import Image

img = Image.open('image/caffee.png')
cropped_img = img.crop(box=(0, 0, 500, 500))

cropped_img.save('image/caffee_cropped.png')