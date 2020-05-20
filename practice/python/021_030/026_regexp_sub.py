import re

html = """<p>
<em>re.sub()</em>関数は正規表現パターンにマッチした文字列を任意の文字列で置換します。
<em>count</em>パラメーターを指定することで文字列を置換する回数を指定できます。
</p>"""

print(f'HTMLドキュメント {html}')
print()

pattern = r'<.*?>'
result = re.sub(pattern, '', html)
print(f"正規表現: r'{pattern}'")
print(f'置換後文字列: {result}')
