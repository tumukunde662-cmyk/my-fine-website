import pathlib, re
html = pathlib.Path("home.html").read_text()

# Map each DRAG tile to a real image you have
replacements = [
    ("Main Campus", "images/image5.png"),
    ("100%.*Boarding", "images/julio2.png"),
    ("C\\.A\\.S\\.C\\.", "images/julio3.png"),
    ("Academics", "images/julio5.jpg"),
    ("Philosophy", "images/julio12.png"),
    ("Admissions", "images/julio2.png"),
    ("A typical day", "images/julio3.png"),
    ("Essential points", "images/image5.png"),
    ("Camps", "images/julio9.png"),
    ("Concert Hall", "images/julio9.png"),
]

for pattern, src in replacements:
    # find <div class="hint">...+ pattern +...</div><img>
    # and inject src into that img
    html = re.sub(
        rf'(<div class="hint">[^<]*{pattern}[^<]*</div>)<img>',
        rf'\1<img src="{src}">',
        html,
        flags=re.IGNORECASE
    )

pathlib.Path("home.html").write_text(html)
print("DONE - injected src into all tiles")python3 fix.py

