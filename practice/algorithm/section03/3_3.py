an = list(map(int, input().split()))

if an[0] < an[1]:
  a_min_first = an[0]
  a_min_second = an[1]
else:
  a_min_first = an[1]
  a_min_second = an[0]

for a in an[2:]:
  if a < a_min_first:
    a_min_second = a_min_first
    a_min_first = a
  elif a < a_min_second:
    a_min_second = a
  # print(a_min_first, a_min_second)

print(a_min_second)
