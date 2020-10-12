a, b, c, d = map(int, input().split())
cookies_list = [a, b, c, d]
# print(a, b, c, d)

is_equal = False
for i in range(2 ** 4):
  in_total = 0
  out_total = 0
  # print(i)
  for j in range(4):
    if ((i >> j) & 1):
      # print(i, j)
      in_total += cookies_list[j]
    else:
      out_total += cookies_list[j]
  
  if in_total == out_total:
    is_equal = True

if is_equal:
  print('Yes')
else:
  print('No')
