import zipfile

with zipfile.ZipFile('dummy_dir/test.zip', 'a') as zf:
    zf.write('dummy_dir/test3.txt')
