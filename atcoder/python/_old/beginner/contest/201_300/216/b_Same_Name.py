n = int(input())

st = []
for i in range(n):
    s, t = input().split(' ')
    st.append([s, t])

st = sorted(st)

result = 'No'
for i in range(n-1):
    si, ti = st[i][0], st[i][1]
    for j in range(i+1, n):
        # print(i , j)
        sj, tj = st[j][0], st[j][1]

        if si == sj and ti == tj:
            result = 'Yes'

print(result) 
