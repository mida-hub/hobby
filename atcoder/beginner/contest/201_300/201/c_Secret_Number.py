S = input()
search = {}

guess_count = 0
ng_count = 0

# print(S)
for i, s in enumerate(S):
    if s == 'o':
        search[str(i)] = 1
        ng_count += 1
    elif s == '?':
        search[str(i)] = 0
    elif s == 'x':
        search[str(i)] = -1

# print(search)

for i in range(10000):
    tmp = ('000'+str(i))[-4:] 
    guess = list(tmp)
    # print(guess)

    is_ng = False
    for key in search:
        # 暗証番号に確実に含まれていないkeyが入っていた場合break
        if key in guess and search[key] == -1:
            is_ng = True
            break

        # 暗証番号に確実に含まれているkeyが入っていない場合break
        if key not in guess and search[key] == 1:
            is_ng = True
            break
    
    if not is_ng:
        guess_count += 1
        # print(guess)


if ng_count >= 5:
    print(0)
else:
    print(guess_count)
