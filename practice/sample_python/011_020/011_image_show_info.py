from PIL import Image

img = Image.open('image/caffee.png')
print(f'ファイル名: {img.filename}, フォーマット: {img.format}, サイズ: {img.size}')

img.save('image/caffee.jpg', format='jpeg')