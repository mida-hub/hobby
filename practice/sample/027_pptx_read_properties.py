import pptx

prs = pptx.Presentation('input/book-proposal1.pptx')
properties = prs.core_properties

print(f'作成者: {properties.author}')
print(f'件名: {properties.subject}')
print(f'タイトル: {properties.title}')
print(f'作成日時: {properties.created}')
print(f'更新日時: {properties.modified}')