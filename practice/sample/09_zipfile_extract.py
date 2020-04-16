import zipfile

with zipfile.ZipFile('dummy_dir/test.zip', 'r') as zf:
    zf.extractall('./extract_dir')
