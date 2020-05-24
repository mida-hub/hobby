try:
    b = [10, 20, 30]
    # c = b.method_a()
    # a = b[3]
    a = 10 / 0
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
    # print(e ,type(e))
except IndexError as e:
    print('index error 発生')
except Exception as e:
    print('Exception', e, type(e))
else:
    print('else 処理')
finally:
    print('finally 処理')

print('処理が完了しました。')