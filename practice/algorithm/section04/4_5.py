def sft(n, l, output):
    # print(output)
    # 3桁以上
    if l >= 3:
        if all([n >= int(output),
                '3' in output,
                '5' in output,
                '7' in output]):
            # print(output)
            output_list.append(output)
        # 最大桁数までいったら終わり
        if len(str(n)) == l:
            return

    sft(n, l+1, output+'3')
    sft(n, l+1, output+'5')
    sft(n, l+1, output+'7')
    
    return

n = int(input())
output = ""
output_list = []

if n < 100:
    print(0)
else:
    sft(n, 0, output)

    # print(output_list)
    print(len(output_list))
