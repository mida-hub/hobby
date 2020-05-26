# inner関数 / ノンローカル関数

def outer():
    outer_var = '外側の変数'
    def inner():
        nonlocal outer_var
        outer_var = '内側の変数'
        print('inner')
        print(f'outer_var = {outer_var}, id = {id(outer_var)}')

    inner()
    print('outer')
    print(f'outer_var = {outer_var}, id = {id(outer_var)}')

outer()