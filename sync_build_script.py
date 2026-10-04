import os

with open("index.html", "r") as f:
    html_content = f.read()

with open("css/style.css", "r") as f:
    css_content = f.read()

with open("js/main.js", "r") as f:
    js_content = f.read()

script_content = f'''import os

css_content = """{css_content}"""

html_content = """{html_content}"""

js_content = """{js_content}"""

os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
os.makedirs("Image", exist_ok=True)

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("js/main.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Site généré avec succès !")
'''

with open("build_site_v6.py", "w") as f:
    f.write(script_content)

print("Updated build_site_v6.py with current code")
