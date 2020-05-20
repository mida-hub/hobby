from PIL import Image

img = Image.open('image/caffee.png')
monochrome_img = img.convert('L')

monochrome_img.save('image/caffee_monochrome.png')