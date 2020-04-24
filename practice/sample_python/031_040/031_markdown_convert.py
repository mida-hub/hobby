import locale
import os
import webbrowser
import markdown2

md_file = 'input/sample1.md'
html_file = 'output/sample1_from_module.html'
html_enc = locale.getpreferredencoding()

with open(md_file, 'r', encoding='utf-8') as md,\
     open(html_file, 'w', encoding=html_enc) as html:
     md_format = md.read()
     html_format = markdown2.markdown(md_format)
     html.write(html_format)

current_dir = os.getcwd()
uri = f'file://{current_dir}/{html_file}'
webbrowser.open_new_tab(uri)
