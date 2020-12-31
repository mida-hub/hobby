with open('input/postage.txt', encoding='utf-8') as f:
    for line in f:
        text = line.strip()
        # print(text)
        if text.startswith('50g'):
            print(text)
        if text.endswith(('郵便物', '規格外')):
            print(text)