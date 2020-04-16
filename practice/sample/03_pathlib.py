import pathlib

path = pathlib.Path('.')
for po in path.iterdir():
    if not po.is_dir():
        print(po)
