from pathlib import Path
import markdown
base = Path(r'C:/Users/techf/Documents/Vectra-Core-Systems-LLC')
files = [
    ('past_performance.md', 'Past_Performance.html'),
    ('Manse_Soura_Resume.md', 'Manse_Soura_Resume.html'),
    ('resume_template.md', 'Resume_Template.html'),
    ('cover_letter_subcontractor.md', 'Cover_Letter_Subcontractor.html'),
]
css = '''
body{font-family: Arial, sans-serif; margin:40px; color:#0a1628}
h1,h2{color:#00b4d8}
code, pre{background:#f3f4f6;padding:6px;border-radius:4px}
'''
for mdname, htmlname in files:
    mdpath = base / mdname
    if not mdpath.exists():
        print('Missing', mdpath)
        continue
    text = mdpath.read_text(encoding='utf-8')
    html = markdown.markdown(text, extensions=['extra','sane_lists'])
    full = f"""<!doctype html><html><head><meta charset='utf-8'><title>{mdname}</title><style>{css}</style></head><body>{html}</body></html>"""
    out = base / htmlname
    out.write_text(full, encoding='utf-8')
    print('Wrote', out)
