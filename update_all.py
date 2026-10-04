import os
import re
import shutil
import json

# 1. Copy the new image
src_img = "/Users/aaaaaaaa/.gemini/antigravity-ide/brain/05a0eb02-3425-4fa9-bf58-55fa90fb6632/media__1791155442395.jpg"
dest_img = "Image/chambre_new_v2.jpg"
if os.path.exists(src_img):
    shutil.copy(src_img, dest_img)

# 2. Update index.html
with open("index.html", "r") as f:
    html = f.read()

# Replace Image/Lit_new.jpg with Image/chambre_new_v2.jpg
html = html.replace('Image/Lit_new.jpg', 'Image/chambre_new_v2.jpg')

with open("index.html", "w") as f:
    f.write(html)

# 3. Update galleryData in js/main.js
# Folder mapping
folders = {
    "cuisines": "Image/cuisines",
    "dressings": "Image/dressings",
    "salons": "Image/saloon",
    "chambres": "Image/chambre",
    "bureaux": "Image/bureaux",
    "salles-de-bain": "Image/salle de bain"
}

gallery_data = {}
for cat, folder_path in folders.items():
    if os.path.exists(folder_path):
        # List all valid images
        images = [f"{folder_path}/{f}" for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        gallery_data[cat] = images
    else:
        gallery_data[cat] = []

# Replace inside js/main.js
with open("js/main.js", "r") as f:
    js_content = f.read()

# Find the galleryData object and replace it
json_str = json.dumps(gallery_data, indent=2)
js_content = re.sub(r'const galleryData = \{.*?\};', f'const galleryData = {json_str};', js_content, flags=re.DOTALL)

with open("js/main.js", "w") as f:
    f.write(js_content)

print("Updates applied successfully.")
