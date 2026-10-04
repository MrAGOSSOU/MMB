import re

with open("css/style.css", "r") as f:
    css = f.read()

css = css.replace("--section-py: 10vw;", "--section-py: 5vw;")
css = css.replace("font-size: clamp(2.5rem, 6vw, 7rem);", "font-size: clamp(2rem, 5vw, 4.5rem);")
css = css.replace("font-size: clamp(2rem, 4vw, 4rem);", "font-size: clamp(1.75rem, 3.5vw, 3rem);")
css = css.replace("font-size: clamp(1.25rem, 2.5vw, 2.5rem);", "font-size: clamp(1.1rem, 2vw, 1.75rem);")

# Also, the user might complain about padding in specific sections, let's just write back the CSS
with open("css/style.css", "w") as f:
    f.write(css)

with open("index.html", "r") as f:
    html = f.read()

# Fix dressing image in Services section
html = html.replace('src="Image/Dressing_new.jpg"', 'src="Image/image4-dressing.jpg"')

# Reorganize Realisations (keep 6 best, e.g., photo11, photo4, photo1, photo2, photo6, photo9)
# Currently it's a portfolio-masonry with 10 items.
port_start = html.find('<div class="portfolio-masonry">')
port_end = html.find('</div>\n      \n      <div class="reveal" style="text-align: center; margin-top: 5rem;">')

new_port = """<div class="portfolio-masonry">
        <a href="#contact" class="port-card reveal"><img src="Image/photo11-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine Design</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo1-decoration.JPG"><div class="port-overlay"><h3 class="t-h3">Décoration</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo4-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo6-douche2.JPG"><div class="port-overlay"><h3 class="t-h3">Salle de bain</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo2-coiffeuse.JPG"><div class="port-overlay"><h3 class="t-h3">Coiffeuse</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo9-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine Épurée</h3></div></a>"""

if port_start != -1 and port_end != -1:
    html = html[:port_start] + new_port + html[port_end:]

# Restore Pourquoi Nous section to a side-by-side
pq_start = html.find('<!-- POURQUOI NOUS -->')
pq_end = html.find('<!-- PROCESSUS -->')

new_pq = """<!-- POURQUOI NOUS -->
    <section class="section light-theme container">
      <div class="savoir-grid" style="gap: 4vw; margin-top: 2rem;">
        <div class="savoir-img-wrap reveal" style="height: 600px;">
          <img src="Image/image1-salon.JPG" class="savoir-img parallax-img" data-speed="0.1" style="height: 120%;">
        </div>
        <div class="savoir-content reveal" style="transition-delay: 0.2s;">
          <h2 class="t-display" style="margin-bottom: 2rem;">L'Excellence<br><span class="t-italic" style="color:var(--c-bois-chaud);">notre standard.</span></h2>
          <div class="pourquoi-list">
            <div class="pourquoi-item">
              <span style="font-size: 1.5rem;">01</span>
              <div>
                <h3 class="t-h3" style="margin: 0 0 0.5rem 0;">Fabrication sur mesure</h3>
                <p class="t-body">Chaque meuble est pensé spécifiquement pour votre espace, s'intégrant parfaitement à votre intérieur.</p>
              </div>
            </div>
            <div class="pourquoi-item">
              <span style="font-size: 1.5rem;">02</span>
              <div>
                <h3 class="t-h3" style="margin: 0 0 0.5rem 0;">Matériaux de qualité</h3>
                <p class="t-body">Nous sélectionnons rigoureusement nos bois et matériaux pour garantir une longévité exceptionnelle au Bénin.</p>
              </div>
            </div>
            <div class="pourquoi-item">
              <span style="font-size: 1.5rem;">03</span>
              <div>
                <h3 class="t-h3" style="margin: 0 0 0.5rem 0;">Garantie illimitée</h3>
                <p class="t-body">Une confiance totale en notre savoir-faire qui nous permet de vous offrir une tranquillité d'esprit absolue.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    """

if pq_start != -1 and pq_end != -1:
    html = html[:pq_start] + new_pq + html[pq_end:]

with open("index.html", "w") as f:
    f.write(html)
print("Updated index.html and style.css")
