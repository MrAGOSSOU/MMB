import re

with open("index.html", "r") as f:
    html = f.read()

start = html.find('<div class="portfolio-grid">')
end = html.find('</div>\n\n      <div class="reveal" style="text-align: center; margin-top: 5rem;">')

new_grid = """<div class="portfolio-masonry">
        <a href="#contact" class="port-card reveal"><img src="Image/photo1-decoration.JPG"><div class="port-overlay"><h3 class="t-h3">Décoration</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo2-coiffeuse.JPG"><div class="port-overlay"><h3 class="t-h3">Coiffeuse</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo4-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo5-douche.JPG"><div class="port-overlay"><h3 class="t-h3">Douche</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo6-douche2.JPG"><div class="port-overlay"><h3 class="t-h3">Salle de bain</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo7-dressing.JPG"><div class="port-overlay"><h3 class="t-h3">Dressing</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo8-coiffeuse.JPG"><div class="port-overlay"><h3 class="t-h3">Coiffeuse Moderne</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo9-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine Épurée</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo10-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine Contemporaine</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo11-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine Design</h3></div></a>"""

if start != -1 and end != -1:
    html = html[:start] + new_grid + html[end:]
    with open("index.html", "w") as f:
        f.write(html)
    print("index.html portfolio updated")
else:
    print("index portfolio tags not found")

with open("realisations.html", "r") as f:
    r_html = f.read()

r_html = r_html.replace('photo9-%20cuisine.JPG', 'photo9-cuisine.JPG')
with open("realisations.html", "w") as f:
    f.write(r_html)
print("realisations.html updated")
