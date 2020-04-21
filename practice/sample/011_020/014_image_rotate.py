from PIL import Image

img = Image.open('image/caffee.png')
rotated_img = img.rotate(90)

rotated_img.save('image/caffee_rotated.png')