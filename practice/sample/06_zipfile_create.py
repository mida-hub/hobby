import zipfile

with zipfile.ZipFile('dummy_dir/test.zip', 'w') as zf:
    zf.write('dummy_dir/test1.txt')
    zf.write('dummy_dir/test2.txt')
