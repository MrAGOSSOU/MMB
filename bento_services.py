import re

with open("index.html", "r") as f:
    html = f.read()

services_bento = """    <section id="services" class="section container">
      <div class="services-header reveal">
        <h2 class="t-display">Des espaces pensés<br>dans les <span class="t-italic">moindres détails.</span></h2>
      </div>
      
      <style>
        .services-bento {
          display: grid;
          grid-template-columns: repeat(4, 1fr);
          grid-auto-rows: 250px;
          gap: 1.5rem;
        }
        .bento-card {
          position: relative;
          border-radius: 1.5rem;
          overflow: hidden;
          display: block;
          background: var(--c-espresso);
        }
        .bento-card img {
          width: 100%;
          height: 100%;
          object-fit: cover;
          transition: transform 0.8s var(--ease);
        }
        .bento-card:hover img {
          transform: scale(1.05);
        }
        .bento-overlay {
          position: absolute;
          inset: 0;
          background: linear-gradient(to top, rgba(25,24,23,0.9) 0%, rgba(25,24,23,0.2) 50%, rgba(25,24,23,0) 100%);
          display: flex;
          flex-direction: column;
          justify-content: flex-end;
          padding: 1.5rem;
          pointer-events: none;
        }
        
        .bento-card:nth-child(1) { grid-column: span 2; grid-row: span 2; }
        .bento-card:nth-child(2) { grid-column: span 1; grid-row: span 1; }
        .bento-card:nth-child(3) { grid-column: span 1; grid-row: span 1; }
        .bento-card:nth-child(4) { grid-column: span 2; grid-row: span 1; }
        .bento-card:nth-child(5) { grid-column: span 1; grid-row: span 2; }
        .bento-card:nth-child(6) { grid-column: span 1; grid-row: span 1; }
        .bento-card:nth-child(7) { grid-column: span 2; grid-row: span 1; }
        .bento-card:nth-child(8) { grid-column: span 1; grid-row: span 1; }
        .bento-card:nth-child(9) { grid-column: span 2; grid-row: span 1; }

        @media (max-width: 900px) {
          .services-bento {
            grid-template-columns: repeat(2, 1fr);
            grid-auto-rows: 200px;
          }
          .bento-card:nth-child(1) { grid-column: span 2; grid-row: span 2; }
          .bento-card:nth-child(n+2) { grid-column: span 1; grid-row: span 1; }
          .bento-card:nth-child(4) { grid-column: span 2; grid-row: span 1; }
          .bento-card:nth-child(7) { grid-column: span 2; grid-row: span 1; }
          .bento-card:nth-child(9) { grid-column: span 2; grid-row: span 1; }
        }
        @media (max-width: 600px) {
          .services-bento {
            grid-template-columns: 1fr;
          }
          .bento-card:nth-child(n) { grid-column: span 1; grid-row: span 1; }
          .bento-card:nth-child(1) { grid-row: span 2; }
        }
      </style>

      <div class="services-bento">
        <a href="#contact" class="bento-card reveal">
          <img src="Image/image2-cuisine.JPG">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">01 — CUISINES SUR MESURE</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Cuisines</h3>
          </div>
        </a>
        <a href="#contact" class="bento-card reveal" style="transition-delay: 0.1s;">
          <img src="Image/image4-dressing.jpg">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">02 — DRESSINGS</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Dressings</h3>
          </div>
        </a>
        <a href="#contact" class="bento-card reveal" style="transition-delay: 0.2s;">
          <img src="Image/Salon_new.jpg">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">03 — SALONS</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Salons</h3>
          </div>
        </a>
        <a href="#contact" class="bento-card reveal">
          <img src="Image/Lit_new.jpg">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">04 — CHAMBRES</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Chambres</h3>
          </div>
        </a>
        <a href="#contact" class="bento-card reveal" style="transition-delay: 0.1s;">
          <img src="Image/Bureau_new.jpg">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">05 — BUREAUX</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Bureaux</h3>
          </div>
        </a>
        <a href="#contact" class="bento-card reveal" style="transition-delay: 0.2s;">
          <img src="Image/IMG_9230.JPG">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">06 — RANGEMENTS</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Rangements</h3>
          </div>
        </a>
        <a href="#contact" class="bento-card reveal">
          <img src="Image/IMG_9227.JPG">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">07 — MEUBLES TV</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Meubles TV</h3>
          </div>
        </a>
        <a href="#contact" class="bento-card reveal" style="transition-delay: 0.1s;">
          <img src="Image/IMG_9285.JPG">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">08 — DÉCORATION</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Intérieurs</h3>
          </div>
        </a>
        <a href="#contact" class="bento-card reveal" style="transition-delay: 0.2s;">
          <img src="Image/photo6-douche2.JPG">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">09 — SALLES DE BAIN</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Salles de bain</h3>
          </div>
        </a>
      </div>
    </section>"""

# Replace the old <section id="services"> completely
start_idx = html.find('<!-- SERVICES -->')
end_idx = html.find('<!-- SAVOIR-FAIRE -->')

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + "<!-- SERVICES -->\n" + services_bento + "\n\n    " + html[end_idx:]
    with open("index.html", "w") as f:
        f.write(html)
    print("Updated Services to Bento Grid")
else:
    print("Could not find SERVICES section bounds.")
