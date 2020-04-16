import pathlib

def show_recursive(path):
    for po in path.iterdir():
        if po.is_dir():
            show_recursive(po)
        elif po.is_file():
            print(po)

path = pathlib.Path('.')
show_recursive(path)