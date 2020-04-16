import zipfile

with zipfile.ZipFile('dummy_dir/test.zip', 'r') as zf:
    for info in zf.infolist():
        print(info.filename)
