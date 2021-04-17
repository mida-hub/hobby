# cf. https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0

# 1. argparseをインポート
import argparse

# 2. パーサを作る
parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')

# 3. parser.add_argumentで受け取る引数を追加していく
# 必須の引数を追加
parser.add_argument('arg1', help='この引数の説明（なくてもよい）')
parser.add_argument('arg2', help='foooo')
# オプション引数（指定しなくても良い引数）を追加
parser.add_argument('--arg3', default='3')
# よく使う引数なら省略形があると使う時に便利
parser.add_argument('-a', '--arg4', type=int, default=4)

args = parser.parse_args()    # 4. 引数を解析

print('arg1='+args.arg1)
print('arg2='+args.arg2)
print('arg3='+args.arg3)
print('arg4='+str(args.arg4))
