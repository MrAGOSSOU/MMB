import os

with open("index.html", "r") as f:
    html = f.read()

# We want to replace everything from <!-- PROCESSUS --> down to </main>
start_replace = html.find('<!-- PROCESSUS -->')
end_replace = html.find('</main>')

new_bottom = """<!-- NOUVEAU PROCESSUS -->
    <section id="processus" class="section light-theme">
      <div class="container">
        <div class="reveal" style="text-align: center; margin-bottom: 4rem;">
          <h2 class="t-display">Comment nous travaillons.</h2>
          <p class="t-body-large" style="color: var(--c-bois-chaud);">Un processus clair, sans surprise.</p>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
          <div class="reveal" style="padding: 2rem; border: 1px solid rgba(25,24,23,0.1); border-radius: 1rem; background: var(--c-blanc);">
            <div style="font-family: var(--f-heading); font-size: 3rem; color: var(--c-bois-chaud); margin-bottom: 1rem;">01</div>
            <h3 class="t-h3" style="margin-bottom: 1rem;">L'Écoute</h3>
            <p class="t-body" style="color: var(--c-espresso);">Nous analysons vos besoins, votre espace et vos goûts lors d'une première consultation détaillée.</p>
          </div>
          
          <div class="reveal" style="padding: 2rem; border: 1px solid rgba(25,24,23,0.1); border-radius: 1rem; background: var(--c-blanc); transition-delay: 0.1s;">
            <div style="font-family: var(--f-heading); font-size: 3rem; color: var(--c-bois-chaud); margin-bottom: 1rem;">02</div>
            <h3 class="t-h3" style="margin-bottom: 1rem;">La Conception</h3>
            <p class="t-body" style="color: var(--c-espresso);">Réalisation des plans, choix des matériaux nobles et validation du devis sur-mesure.</p>
          </div>
          
          <div class="reveal" style="padding: 2rem; border: 1px solid rgba(25,24,23,0.1); border-radius: 1rem; background: var(--c-blanc); transition-delay: 0.2s;">
            <div style="font-family: var(--f-heading); font-size: 3rem; color: var(--c-bois-chaud); margin-bottom: 1rem;">03</div>
            <h3 class="t-h3" style="margin-bottom: 1rem;">La Fabrication</h3>
            <p class="t-body" style="color: var(--c-espresso);">Vos meubles prennent vie dans notre atelier, avec une finition artisanale irréprochable.</p>
          </div>
          
          <div class="reveal" style="padding: 2rem; border: 1px solid rgba(25,24,23,0.1); border-radius: 1rem; background: var(--c-bois-chaud); color: var(--c-blanc); transition-delay: 0.3s;">
            <div style="font-family: var(--f-heading); font-size: 3rem; color: var(--c-beige); margin-bottom: 1rem;">04</div>
            <h3 class="t-h3" style="margin-bottom: 1rem;">L'Installation</h3>
            <p class="t-body" style="color: rgba(255,255,255,0.9);">Livraison et pose experte chez vous, pour un résultat clé en main exceptionnel.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- NOUVEAU CONTACT / CTA MINIMALISTE -->
    <section id="contact" class="section container" style="padding-top: 8rem; padding-bottom: 8rem;">
      <div class="reveal" style="background: var(--c-espresso); border-radius: 2rem; padding: 4rem 2rem; text-align: center; position: relative; overflow: hidden; border: 1px solid rgba(255,255,255,0.1);">
        <div style="position: relative; z-index: 2;">
          <h2 class="t-display" style="color: var(--c-blanc); margin-bottom: 1rem;">Prêt à transformer<br><span class="t-italic" style="color: var(--c-beige);">votre intérieur ?</span></h2>
          <p class="t-body-large" style="color: rgba(255,255,255,0.7); max-width: 600px; margin: 0 auto 3rem;">Discutons ensemble de vos idées. Nous sommes à votre écoute pour concevoir l'espace qui vous ressemble parfaitement.</p>
          
          <div style="display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
            <a href="https://wa.me/22967585650" target="_blank" class="btn-primary" style="background: var(--c-bois-chaud); color: white; border: none; padding: 1.2rem 2.5rem; font-size: 0.9rem;">PARLER SUR WHATSAPP</a>
            <a href="tel:0167585650" class="btn-secondary" style="padding: 1.2rem 2.5rem; font-size: 0.9rem;">APPELER DIRECTEMENT</a>
          </div>
        </div>
      </div>
    </section>
    """

if start_replace != -1 and end_replace != -1:
    html = html[:start_replace] + new_bottom + "\n  "
    with open("index.html", "w") as f:
        f.write(html)
    print("Updated bottom of index.html")
else:
    print("Could not find PROCESSUS tags.")
