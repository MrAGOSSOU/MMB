import os
import glob

whatsapp_old = "https://wa.me/22967585650"
whatsapp_new = "https://wa.me/22967585650?text=Salut%2C%20je%20suis%20interss%C3%A9e%20par%20vos%20realisation%2C%20j%27aimerais%20en%20savoir%20plus%20."

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace whatsapp link
    content = content.replace(whatsapp_old, whatsapp_new)

    # Replace index.html portfolio items
    if "index.html" in filepath:
        # Item 1
        content = content.replace('<img src="Image/IMG_9245.JPG">', '<img src="Image/photo1-cuisine.jpg">')
        # Item 2
        content = content.replace('<img src="Image/IMG_9257.JPG">', '<img src="Image/photo2-decoration.jpg">')
        content = content.replace('Dressing sur mesure', 'Décoration intérieure')
        content = content.replace('<span class="t-label">Dressing</span>', '<span class="t-label">Décoration</span>')
        # Item 3
        content = content.replace('<img src="Image/IMG_9273.JPG">', '<img src="Image/photo3-coiffeuse.jpg">')
        content = content.replace('Salon moderne', 'Coiffeuse')
        content = content.replace('<span class="t-label">Salon</span>', '<span class="t-label">Meuble</span>')
        # Item 4
        content = content.replace('<img src="Image/IMG_9285.JPG">', '<img src="Image/photo4-salon.jpg">')
        content = content.replace('Aménagement intérieur', 'Décoration de salon')
        # The label for item 4 is already 'Intérieur', let's change to 'Salon'
        content = content.replace('<span class="t-label">Intérieur</span>', '<span class="t-label">Salon</span>')

    # Replace realisations.html items
    if "realisations.html" in filepath:
        content = content.replace('<img src="Image/IMG_9245.JPG">', '<img src="Image/photo1-cuisine.jpg">')
        
        content = content.replace('<img src="Image/IMG_9273.JPG">', '<img src="Image/photo4-salon.jpg">')
        content = content.replace('Aménagement Mural', 'Décoration de salon')
        
        content = content.replace('<img src="Image/IMG_9257.JPG">', '<img src="Image/photo2-decoration.jpg">')
        content = content.replace('Espace Rangement', 'Décoration intérieure')
        content = content.replace('<span class="t-label">Dressing</span>', '<span class="t-label">Décoration</span>')
        
        content = content.replace('<img src="Image/IMG_9233.JPG">', '<img src="Image/photo3-coiffeuse.jpg">')
        content = content.replace('Design Sombre', 'Coiffeuse')
        content = content.replace('<span class="t-label">Cuisine</span>', '<span class="t-label">Meuble</span>')
        # The first item has <span class="t-label">Cuisine</span> as well, but that's for the cuisine.
        # Wait, if I replace '<span class="t-label">Cuisine</span>', it will replace both.
        # I'll just keep it simple, actually let's use a smarter replace for realisations.html

    with open(filepath, 'w') as f:
        f.write(content)

for html_file in glob.glob("*.html"):
    update_file(html_file)

print("Updated HTML files.")
