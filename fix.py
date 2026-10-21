import re

with open('index.html','r') as f:
    html = f.read()

# Mapping — change file names if yours are different
maps = {
    '100%': 'julio2.png',
    'C.A.S.C.': 'images/image2.png',
    'Academics': 'images/image5.png',
    'Our Philosophy': 'image7.png',
    'Admissions': 'images/image5.png',
    'typical day': 'images/image2.png',
    'Essential points': 'images/image6.png',
    'Camps': 'julio2.png',
    'Concert Hall': 'images/image6.png'
}

for key, src in maps.items():
    # replace <img> near that title
    pattern = rf'({re.escape(key)}.*?)(<img[^>]*>)'
    html = re.sub(pattern, rf'\1<img src="{src}">', html, flags=re.IGNORECASE|re.DOTALL)

# Also fix any lonely <img> tags that have no src
html = re.sub(r'<img\s*>', '<img src="images/image2.png">', html)

with open('index.html','w') as f:
    f.write(html)

print("Fixed!")
