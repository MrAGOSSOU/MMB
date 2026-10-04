with open("index.html", "r") as f:
    html = f.read()

pourquoi_nous = """    <!-- POURQUOI NOUS CHOISIR -->
    <section id="pourquoi-nous" class="section container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 4rem; align-items: center;">
        <div class="reveal">
          <h2 class="t-display" style="margin-bottom: 2rem;">Pourquoi<br><span class="t-italic">nous choisir ?</span></h2>
          <p class="t-body-large" style="margin-bottom: 2rem; color: var(--c-bois-chaud);">L'excellence et la confiance, notre priorité.</p>
          <p class="t-body" style="margin-bottom: 1.5rem;">Faire appel à la Meilleure Menuiserie du Bénin, c'est choisir un artisanat d'exception. Nous mettons un point d'honneur à respecter vos délais tout en garantissant des finitions parfaites.</p>
          <ul style="list-style: none; padding: 0; margin-bottom: 2rem; color: var(--c-blanc);">
            <li style="margin-bottom: 1rem;">✓ <span style="margin-left: 1rem;">Matériaux nobles et durables</span></li>
            <li style="margin-bottom: 1rem;">✓ <span style="margin-left: 1rem;">Accompagnement 100% personnalisé</span></li>
            <li style="margin-bottom: 1rem;">✓ <span style="margin-left: 1rem;">Respect strict des délais d'installation</span></li>
          </ul>
        </div>
        <div class="reveal" style="position: relative; border-radius: 1rem; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
          <img src="Image/image-pdg.JPG" alt="PDG Meilleure Menuiserie du Bénin" style="width: 100%; height: auto; object-fit: cover;">
        </div>
      </div>
    </section>
"""

if "POURQUOI NOUS CHOISIR" not in html:
    # Insert before NOUVEAU PROCESSUS
    proc_start = html.find('<!-- NOUVEAU PROCESSUS -->')
    if proc_start != -1:
        html = html[:proc_start] + pourquoi_nous + "\n" + html[proc_start:]
        with open("index.html", "w") as f:
            f.write(html)
        print("Restored Pourquoi Nous")
    else:
        print("NOUVEAU PROCESSUS not found")
else:
    print("POURQUOI NOUS already exists")
