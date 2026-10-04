with open("index.html", "r") as f:
    html = f.read()

# 1. Add Salles de Bain to Services Grid (9th item)
services_end_search = html.find('<!-- REALISATIONS WRAPPER -->')
if services_end_search == -1:
    services_end_search = html.find('<!-- SAVOIR-FAIRE -->')

s_index = html.rfind('</div>\n    </section>', 0, services_end_search)
if s_index == -1:
    s_index = html.rfind('</a>\n      </div>\n    </section>', 0, services_end_search) + 4

ninth_item = """
        <a href="#contact" class="service-card reveal" style="transition-delay: 0.2s;">
          <img src="Image/photo6-douche2.JPG" class="service-img">
          <div class="service-content">
            <span class="service-num">09 — SALLES DE BAIN</span>
            <div style="display:flex; justify-content:space-between; align-items:flex-end;">
              <h3 class="service-title">Salles de bain</h3>
              <div class="service-arrow">→</div>
            </div>
          </div>
        </a>"""

# Insert before the closing div of services-grid
insert_pos = html.rfind('</div>', 0, s_index)
if insert_pos != -1:
    # double check it's closing services-grid
    html = html[:insert_pos] + ninth_item + "\n      " + html[insert_pos:]


# 2. Redesign Portfolio Showcase to be a perfectly symmetrical 3-column grid
showcase_style_start = html.find('<style>\n        .portfolio-showcase {')
showcase_style_end = html.find('</style>', showcase_style_start) + 8

new_style = """<style>
        .portfolio-showcase {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 2rem;
          margin-top: 4rem;
        }
        .showcase-item {
          position: relative;
          border-radius: 1rem;
          overflow: hidden;
          display: block;
          aspect-ratio: 3 / 4;
          background: var(--c-espresso);
        }
        .showcase-item img {
          width: 100%;
          height: 100%;
          object-fit: cover;
          transition: transform 1s var(--ease);
        }
        .showcase-item:hover img {
          transform: scale(1.05);
        }
        @media (max-width: 768px) {
          .portfolio-showcase {
            grid-template-columns: 1fr;
          }
        }
      </style>"""

if showcase_style_start != -1:
    html = html[:showcase_style_start] + new_style + html[showcase_style_end:]

with open("index.html", "w") as f:
    f.write(html)
print("Updated index.html layout")
