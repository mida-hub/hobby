from PIL import Image

img = Image.open('image/caffee.png')
resized_img = img.resize((200, 200))

resized_img.save('image/caffee_small.png')