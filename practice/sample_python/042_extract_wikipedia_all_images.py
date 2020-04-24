import time
from pathlib import Path
from bs4 import BeautifulSoup
import requests

output_folder = Path('hunting_cats')
output_folder.mkdir(exist_ok=True)

page_data = requests.get('https://commons.wikimedia.org/wiki/Category:Hunting_cats').text
page = BeautifulSoup(page_data, 'lxml')
for img in page.select('img'):
    # img.attrs['alt]: 画像のキャプション(代替テキスト)、img.attrs['src']: 画像のURL
    print(f"見出し: {img.attrs['alt']}")
    print(f"URL: {img.attrs['src']}")
    save_path = output_folder.joinpath(img.attrs['alt'])
    image = requests.get(img.attrs['src'])
    open(save_path, 'wb').write(image.content)
    time.sleep(1.0)