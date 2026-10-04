import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Hero Slideshow
hero_old = """<img src="Image/IMG_9233.JPG" alt="Intérieur contemporain" class="hero-bg parallax-img" data-speed="0.3">"""
hero_new = """<div class="hero-slideshow">
        <img src="Image/image1-salon.JPG" class="hero-bg slide active">
        <img src="Image/image2-cuisine.JPG" class="hero-bg slide">
        <img src="Image/image3-%20decoration-.JPG" class="hero-bg slide">
        <img src="Image/image4-dressing.jpg" class="hero-bg slide">
      </div>"""
html = html.replace(hero_old, hero_new)

# 2. Realisations block
# Find the portfolio grid and replace it
portfolio_start = html.find('<div class="portfolio-filters">')
portfolio_end = html.find('<!-- CHIFFRES -->')
if portfolio_start != -1 and portfolio_end != -1:
    portfolio_new = """<div class="portfolio-filters">
        <button class="filter-btn active">TOUT</button>
        <button class="filter-btn">CUISINES</button>
        <button class="filter-btn">DRESSINGS</button>
        <button class="filter-btn">SALONS</button>
        <button class="filter-btn">CHAMBRES</button>
        <button class="filter-btn">BUREAUX</button>
      </div>

      <div class="portfolio-masonry">
        <a href="#contact" class="port-card reveal"><img src="Image/photo1-decoration.JPG"><div class="port-overlay"><h3 class="t-h3">Décoration</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo2-coiffeuse.JPG"><div class="port-overlay"><h3 class="t-h3">Coiffeuse</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo4-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo5-douche.JPG"><div class="port-overlay"><h3 class="t-h3">Douche</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo6-douche2.JPG"><div class="port-overlay"><h3 class="t-h3">Salle de bain</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo7-dressing.JPG"><div class="port-overlay"><h3 class="t-h3">Dressing</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo8-coiffeuse.JPG"><div class="port-overlay"><h3 class="t-h3">Coiffeuse Moderne</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo9-%20cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine Épurée</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo10-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine Contemporaine</h3></div></a>
        <a href="#contact" class="port-card reveal"><img src="Image/photo11-cuisine.JPG"><div class="port-overlay"><h3 class="t-h3">Cuisine Design</h3></div></a>
      </div>

      <div class="reveal" style="text-align: center; margin-top: 5rem;">
        <a href="realisations.html" class="btn-primary" style="background:var(--c-espresso); color:var(--c-blanc);">Voir toutes les réalisations</a>
      </div>
    </section>

    """
    html = html[:portfolio_start] + portfolio_new + html[portfolio_end:]

# 3. Chiffres & Pourquoi Nous Redesign
chiffres_old = """<!-- CHIFFRES -->
    <section class="section chiffres-section">
      <div class="container chiffres-grid reveal">
        <div class="chiffre-item">
          <h4>2020</h4>
          <span class="t-label">ANNÉE DE CRÉATION</span>
        </div>
        <div class="chiffre-item">
          <h4>100%</h4>
          <span class="t-label">SUR MESURE</span>
        </div>
        <div class="chiffre-item">
          <h4>360°</h4>
          <span class="t-label">ACCOMPAGNEMENT</span>
        </div>
        <div class="chiffre-item">
          <h4>∞</h4>
          <span class="t-label">GARANTIE</span>
        </div>
      </div>
    </section>

    <!-- POURQUOI NOUS -->
    <section class="section container">
      <div class="pourquoi-grid">
        <div class="reveal">
          <h2 class="t-h2">Pourquoi Meilleure Menuiserie du Bénin ?</h2>
          <div class="pourquoi-list">
            <div class="pourquoi-item">
              <span>01</span>
              <div>FABRICATION SUR MESURE</div>
            </div>
            <div class="pourquoi-item">
              <span>02</span>
              <div>MATÉRIAUX DE QUALITÉ</div>
            </div>
            <div class="pourquoi-item">
              <span>03</span>
              <div>ACCOMPAGNEMENT PERSONNALISÉ</div>
            </div>
            <div class="pourquoi-item">
              <span>04</span>
              <div>INSTALLATION PROFESSIONNELLE</div>
            </div>
            <div class="pourquoi-item">
              <span>05</span>
              <div>GARANTIE ILLIMITÉE</div>
            </div>
          </div>
        </div>
        <div class="reveal" style="transition-delay: 0.2s;">
          <img src="Image/PDG_new.jpg" alt="La Fondatrice" style="border-radius: 0.5rem; height: 100%; width: 100%; object-fit:cover;">
        </div>
      </div>
    </section>"""

new_chiffres_pourquoi = """<!-- CHIFFRES -->
    <section class="section chiffres-section" style="background: url('Image/image2-cuisine.JPG') center/cover no-repeat; position: relative;">
      <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(25,24,23,0.85); z-index:1;"></div>
      <div class="container reveal" style="position:relative; z-index:2;">
        <div class="chiffres-flex">
          <div class="chiffre-card">
            <h4 class="t-display">2020</h4>
            <div class="c-line"></div>
            <span class="t-label">ANNÉE DE CRÉATION</span>
          </div>
          <div class="chiffre-card">
            <h4 class="t-display">100<span style="font-size:0.5em">%</span></h4>
            <div class="c-line"></div>
            <span class="t-label">SUR MESURE</span>
          </div>
          <div class="chiffre-card">
            <h4 class="t-display">360<span style="font-size:0.5em">°</span></h4>
            <div class="c-line"></div>
            <span class="t-label">ACCOMPAGNEMENT</span>
          </div>
          <div class="chiffre-card">
            <h4 class="t-display">∞</h4>
            <div class="c-line"></div>
            <span class="t-label">GARANTIE</span>
          </div>
        </div>
      </div>
    </section>

    <!-- POURQUOI NOUS -->
    <section class="section light-theme" style="padding-top: 8rem; padding-bottom: 8rem;">
      <div class="container">
        <div class="reveal" style="text-align: center; margin-bottom: 5rem;">
          <h2 class="t-display">L'Excellence<br><span class="t-italic" style="color:var(--c-bois-chaud);">notre standard.</span></h2>
        </div>
        
        <div class="pq-grid">
          <div class="pq-card reveal">
            <div class="pq-icon">01</div>
            <h3 class="t-h3">Fabrication sur mesure</h3>
            <p class="t-body">Chaque meuble est pensé spécifiquement pour votre espace, s'intégrant parfaitement à votre intérieur.</p>
          </div>
          <div class="pq-card reveal" style="transition-delay: 0.1s;">
            <div class="pq-icon">02</div>
            <h3 class="t-h3">Matériaux de qualité</h3>
            <p class="t-body">Nous sélectionnons rigoureusement nos bois et matériaux pour garantir une longévité exceptionnelle au Bénin.</p>
          </div>
          <div class="pq-card reveal" style="transition-delay: 0.2s;">
            <div class="pq-icon">03</div>
            <h3 class="t-h3">Design Premium</h3>
            <p class="t-body">Une esthétique raffinée, contemporaine et intemporelle pour sublimer chaque pièce de votre maison.</p>
          </div>
          <div class="pq-card reveal" style="transition-delay: 0.3s;">
            <div class="pq-icon">04</div>
            <h3 class="t-h3">Garantie illimitée</h3>
            <p class="t-body">Une confiance totale en notre savoir-faire qui nous permet de vous offrir une tranquillité d'esprit absolue.</p>
          </div>
        </div>
      </div>
    </section>"""
html = html.replace(chiffres_old, new_chiffres_pourquoi)

with open("index.html", "w") as f:
    f.write(html)
