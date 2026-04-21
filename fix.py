import json
import re

with open('liquird.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code' and 'dataset = [' in ''.join(cell['source']):
        source = ''.join(cell['source'])
        
        # Replace } followed by \n or whitespace and then { with },\n{
        source = re.sub(r'\}\s*\n\s*\{', '},\n\t{', source)
        
        # Also handle } followed immediately by { just in case
        source = re.sub(r'\}\s*\{', '}, {', source)
        
        # Update the cell source
        lines = source.split('\n')
        cell['source'] = [line + '\n' for line in lines[:-1]] + ([lines[-1]] if lines[-1] else [])

with open('liquird.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print('Successfully added commas between all dicts in the dataset list in liquird.ipynb!'
 
      print("and ijdi, nch. mm"if(nb
