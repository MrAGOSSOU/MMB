import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Update Portfolio Realisations (Remove photo11, rearrange layout, maybe grid 5 items)
port_start = html.find('<div class="portfolio-masonry">')
port_end = html.find('</div>\n      \n      <div class="reveal" style="text-align: center; margin-top: 5rem;">')
if port_end == -1: # fallback
    port_end = html.find('</div>\n      \n      <div class="reveal" style="text-align: center; margin-top: 4rem;">')
if port_end == -1:
    port_end = html.find('</div>\n      <div class="reveal" style="text-align: center; margin-top: 5rem;">')

new_port = """<div class="portfolio-masonry" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
        <a href="#contact" class="port-card reveal" style="grid-row-end: span 45;"><img src="Image/photo4-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine</h3></div></a>
        <a href="#contact" class="port-card reveal" style="grid-row-end: span 30;"><img src="Image/photo1-decoration.JPG"><div class="port-overlay"><h3 class="t-h3">Décoration</h3></div></a>
        <a href="#contact" class="port-card reveal" style="grid-row-end: span 40;"><img src="Image/photo6-douche2.JPG"><div class="port-overlay"><h3 class="t-h3">Salle de bain</h3></div></a>
        <a href="#contact" class="port-card reveal" style="grid-row-end: span 30;"><img src="Image/photo2-coiffeuse.JPG"><div class="port-overlay"><h3 class="t-h3">Coiffeuse</h3></div></a>
        <a href="#contact" class="port-card reveal" style="grid-row-end: span 45;"><img src="Image/photo9-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine Épurée</h3></div></a>"""

if port_start != -1 and port_end != -1:
    html = html[:port_start] + new_port + html[port_end:]

# 2. Add Parallax Backgrounds to Services and Realisations
# Services section
services_start = html.find('<!-- SERVICES -->')
services_section_tag = html.find('<section id="services"', services_start)
services_end = html.find('</section>', services_section_tag) + 10

# Wrap services in parallax
services_content = html[services_section_tag:services_end]
# Add parallax wrapper
services_wrapper = f"""
    <!-- SERVICES WRAPPER -->
    <div style="position: relative; background: url('Image/photo7-dressing.JPG') center/cover fixed; overflow: hidden;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(25,24,23,0.85); backdrop-filter: blur(5px);"></div>
      <div style="position: relative; z-index: 2;">
        {services_content}
      </div>
    </div>
"""
if services_start != -1:
    html = html[:services_start] + services_wrapper + html[services_end:]


# Realisations section
realisations_start = html.find('<!-- REALISATIONS -->')
realisations_section_tag = html.find('<section id="realisations"', realisations_start)
realisations_end = html.find('</section>', realisations_section_tag) + 10

# Wrap realisations in parallax
realisations_content = html[realisations_section_tag:realisations_end]
realisations_wrapper = f"""
    <!-- REALISATIONS WRAPPER -->
    <div style="position: relative; background: url('Image/photo8-coiffeuse.JPG') center/cover fixed; overflow: hidden;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to right, rgba(25,24,23,0.95), rgba(25,24,23,0.7)); backdrop-filter: blur(8px);"></div>
      <div style="position: relative; z-index: 2;">
        {realisations_content}
      </div>
    </div>
"""
if realisations_start != -1:
    html = html[:realisations_start] + realisations_wrapper + html[realisations_end:]


# 3. Pourquoi Nous - use PDG image and reassuring arguments
pq_start = html.find('<!-- POURQUOI NOUS -->')
pq_end = html.find('<!-- PROCESSUS -->')

new_pq = """<!-- POURQUOI NOUS -->
    <section class="section light-theme container">
      <div class="savoir-grid" style="gap: 4vw; margin-top: 1rem; align-items: flex-start;">
        <div class="savoir-img-wrap reveal" style="height: 600px; border-radius: 1rem; overflow: hidden;">
          <img src="Image/PDG_new.jpg" class="savoir-img parallax-img" data-speed="0.05" style="height: 110%; object-fit: cover;">
        </div>
        <div class="savoir-content reveal" style="transition-delay: 0.2s;">
          <h2 class="t-display" style="margin-bottom: 2rem; font-size: clamp(2rem, 4vw, 3.5rem);">L'Excellence & La Confiance,<br><span class="t-italic" style="color:var(--c-bois-chaud);">notre priorité.</span></h2>
          <div class="pourquoi-list" style="margin-top: 2rem;">
            <div class="pourquoi-item" style="padding: 1rem 0;">
              <span style="font-size: 1.5rem; color: var(--c-bois-chaud);">01</span>
              <div>
                <h3 class="t-h3" style="margin: 0 0 0.25rem 0;">Accompagnement de A à Z</h3>
                <p class="t-body">Nous sommes à vos côtés depuis la première idée jusqu'à l'installation finale. Un seul interlocuteur de confiance pour tout votre projet.</p>
              </div>
            </div>
            <div class="pourquoi-item" style="padding: 1rem 0;">
              <span style="font-size: 1.5rem; color: var(--c-bois-chaud);">02</span>
              <div>
                <h3 class="t-h3" style="margin: 0 0 0.25rem 0;">Durabilité Garantie</h3>
                <p class="t-body">Conscient des réalités climatiques, chaque bois est traité et sélectionné rigoureusement pour défier le temps.</p>
              </div>
            </div>
            <div class="pourquoi-item" style="padding: 1rem 0; border-bottom: none;">
              <span style="font-size: 1.5rem; color: var(--c-bois-chaud);">03</span>
              <div>
                <h3 class="t-h3" style="margin: 0 0 0.25rem 0;">SAV Ultra-Réactif</h3>
                <p class="t-body">Notre garantie ne s'arrête pas à la livraison. Notre équipe reste à votre entière disposition pour tout ajustement.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    """

if pq_start != -1 and pq_end != -1:
    html = html[:pq_start] + new_pq + html[pq_end:]


# Reduce spacing further in css if needed
with open("css/style.css", "r") as f:
    css = f.read()

css = css.replace("--section-py: 5vw;", "--section-py: 3vw;")
css = css.replace("margin-top: 5rem;", "margin-top: 2rem;")
css = css.replace("margin-top: 4rem;", "margin-top: 2rem;")
css = css.replace("margin-bottom: 4rem;", "margin-bottom: 2rem;")
css = css.replace("margin-bottom: 5rem;", "margin-bottom: 2.5rem;")

with open("css/style.css", "w") as f:
    f.write(css)

with open("index.html", "w") as f:
    f.write(html)

print("Updates successful")
