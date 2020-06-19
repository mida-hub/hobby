import re

txt = "I like tenis"
x = re.search(r'\bt\w+', txt) # tから始まってアルファベット、アンダースコア1回以上繰り返し
print(type(x))
print(x.group())

pattern = r'^a...s$'

test_string = 'abyss'
result = re.search(pattern, test_string)
if result:
    print(result.group())
else:
    print('Not exists')

msg = "Im 30 years old"
#Im 30 years old
#012345678901234
match = re.search(r'(\d{2}) years', msg)
print(match.group())
print(match.start())
print(match.end())
print(match.span())
print(match.re)
print(match.string)

msg = "Im 40 years, name is Jiro."
match = re.search(r'Im (\d{1,3}) years, name is (.*?)\.', msg)
print(match.group())
print(match.groups())
