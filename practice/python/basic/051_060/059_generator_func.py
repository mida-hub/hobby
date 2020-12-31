# ジェネレーター関数

def generator(max):
    print('ジェネレーター作成')
    for i in range(max):
        yield i
        print('yield実行')

gen = generator(10)
for x in gen:
    print(x)

"""
    next
    send
    throw
    close
"""
