import os

with open("index.html", "r") as f:
    html = f.read()

# 1. Update filter buttons to links
filters_start = html.find('<div class="portfolio-filters reveal">')
filters_end = html.find('</div>', filters_start) + 6

new_filters = """<div class="portfolio-filters reveal">
        <a href="realisations.html" class="filter-btn active">TOUT</a>
        <a href="cuisines.html" class="filter-btn">CUISINES</a>
        <a href="dressings.html" class="filter-btn">DRESSINGS</a>
        <a href="salons.html" class="filter-btn">SALONS</a>
        <a href="chambres.html" class="filter-btn">CHAMBRES</a>
        <a href="bureaux.html" class="filter-btn">BUREAUX</a>
      </div>"""

if filters_start != -1:
    html = html[:filters_start] + new_filters + html[filters_end:]

# 2. Update masonry grid to 3 items
port_start = html.find('<div class="portfolio-masonry"')
port_end = html.find('</div>\n      </section>', port_start)

new_port = """<div class="portfolio-masonry" style="margin-top: 4rem; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
          <a href="#contact" class="port-card reveal" style="grid-row-end: span 40;">
            <img src="Image/photo1-decoration.JPG">
            <div class="port-overlay">
              <span style="color: var(--c-beige); font-size: 0.8rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem;">Intérieur</span>
              <h3 class="t-h3" style="color: white; margin: 0;">Décoration</h3>
            </div>
          </a>
          <a href="#contact" class="port-card reveal" style="grid-row-end: span 45;">
            <img src="Image/photo2-coiffeuse.JPG">
            <div class="port-overlay">
              <span style="color: var(--c-beige); font-size: 0.8rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem;">Meuble</span>
              <h3 class="t-h3" style="color: white; margin: 0;">Coiffeuse</h3>
            </div>
          </a>
          <a href="#contact" class="port-card reveal" style="grid-row-end: span 35;">
            <img src="Image/photo23-cuisine.jpg">
            <div class="port-overlay">
              <span style="color: var(--c-beige); font-size: 0.8rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem;">Sur mesure</span>
              <h3 class="t-h3" style="color: white; margin: 0;">Cuisine</h3>
            </div>
          </a>"""

if port_start != -1 and port_end != -1:
    html = html[:port_start] + new_port + html[port_end:]

with open("index.html", "w") as f:
    f.write(html)


# Do the same for realisations.html
with open("realisations.html", "r") as f:
    r_html = f.read()

r_port_start = r_html.find('<div class="portfolio-masonry"')
r_port_end = r_html.find('</div>\n      </section>', r_port_start)

if r_port_start != -1 and r_port_end != -1:
    r_html = r_html[:r_port_start] + new_port + r_html[r_port_end:]
    with open("realisations.html", "w") as f:
        f.write(r_html)

print("Updated index.html and realisations.html")
