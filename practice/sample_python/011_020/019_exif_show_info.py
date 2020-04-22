from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open('image/IMG_5988.JPG')
exif = img._getexif()
if exif is None:
    print("EXIF情報がありません")
else:
    for tagID, tagValue, in exif.items():
        tagName = TAGS[tagID] if tagID in TAGS else "NotFound"
        print(tagName, tagValue)