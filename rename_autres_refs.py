import os

with open("index.html", "r") as f:
    html = f.read()

# Replace Image/Autres../ with Image/Autres/
html = html.replace('Image/Autres../', 'Image/Autres/')

with open("index.html", "w") as f:
    f.write(html)

print("Updated index.html references.")
