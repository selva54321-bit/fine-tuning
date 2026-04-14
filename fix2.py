import json
import re

with open('liquird.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code' and 'dataset = [' in ''.join(cell['source']):
        source = ''.join(cell['source'])
        # Add comma after } if next non-whitespace character is {
        source = re.sub(r'\}(\s*)\{', r'},\1{', source)
        # Restore as list of lines with trailing newlines
        lines = source.split('\n')
        cell['source'] = [line + '\n' for line in lines[:-1]] + ([lines[-1]] if lines[-1] else [])
        
with open('liquird.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print('Fixed with precise regex!')
