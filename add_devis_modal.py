import os

# 1. UPDATE index.html
with open("index.html", "r") as f:
    html = f.read()

modal_html = """
    <!-- Modal Devis -->
    <div id="devis-modal" class="modal-overlay">
      <div class="modal-content">
        <span class="modal-close" onclick="document.getElementById('devis-modal').classList.remove('active')">&times;</span>
        <h3 class="t-h3" style="color: var(--c-espresso); margin-bottom: 0.5rem;">Demander un devis</h3>
        <p style="color: rgba(25, 24, 23, 0.7); margin-bottom: 2rem; font-size: 0.9rem;">Remplissez ce formulaire. Vous serez ensuite redirigé vers notre WhatsApp pour un échange direct.</p>
        
        <form id="devis-form" onsubmit="submitDevis(event)">
          <div class="form-group">
            <label>Votre nom complet</label>
            <input type="text" id="devis-nom" required placeholder="Jean Dupont">
          </div>
          <div class="form-group">
            <label>Nature du projet</label>
            <select id="devis-projet" required>
              <option value="" disabled selected>Sélectionnez une catégorie...</option>
              <option value="Cuisine sur mesure">Cuisine sur mesure</option>
              <option value="Dressing">Dressing</option>
              <option value="Aménagement Salon">Aménagement Salon</option>
              <option value="Chambre">Chambre</option>
              <option value="Meuble TV / Rangement">Meuble TV / Rangement</option>
              <option value="Autre">Autre</option>
            </select>
          </div>
          <div class="form-group">
            <label>Détails du projet</label>
            <textarea id="devis-message" rows="4" required placeholder="Décrivez brièvement vos attentes, vos dimensions, etc."></textarea>
          </div>
          <button type="submit" class="btn-primary" style="width: 100%; text-align: center; justify-content: center;">ENVOYER ET CONTINUER SUR WHATSAPP</button>
        </form>
      </div>
    </div>
"""

if "devis-modal" not in html:
    # insert right before </body>
    html = html.replace("</body>", modal_html + "\n</body>")

# Change "Demander un devis" buttons to open the modal
html = html.replace('href="#contact" class="nav-cta"', 'href="#" onclick="document.getElementById(\'devis-modal\').classList.add(\'active\'); return false;" class="nav-cta"')

with open("index.html", "w") as f:
    f.write(html)

# 2. UPDATE style.css
with open("css/style.css", "r") as f:
    css = f.read()

modal_css = """
/* Modal Devis */
.modal-overlay {
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(25, 24, 23, 0.8);
  backdrop-filter: blur(10px);
  z-index: 10000;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.4s var(--ease), visibility 0.4s;
}
.modal-overlay.active {
  opacity: 1;
  visibility: visible;
}
.modal-content {
  background: var(--c-blanc);
  padding: 3rem;
  border-radius: 1.5rem;
  max-width: 500px;
  width: 90%;
  position: relative;
  transform: translateY(30px);
  transition: transform 0.4s var(--ease);
}
.modal-overlay.active .modal-content {
  transform: translateY(0);
}
.modal-close {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  font-size: 2rem;
  color: var(--c-espresso);
  cursor: pointer;
  line-height: 1;
}
.form-group {
  margin-bottom: 1.5rem;
  text-align: left;
}
.form-group label {
  display: block;
  font-size: 0.85rem;
  color: var(--c-espresso);
  margin-bottom: 0.5rem;
  font-weight: 600;
}
.form-group input, .form-group select, .form-group textarea {
  width: 100%;
  padding: 1rem;
  border: 1px solid rgba(25, 24, 23, 0.2);
  border-radius: 0.5rem;
  font-family: var(--f-body);
  font-size: 1rem;
  background: rgba(25, 24, 23, 0.02);
  color: var(--c-espresso);
}
.form-group input:focus, .form-group select:focus, .form-group textarea:focus {
  outline: none;
  border-color: var(--c-bois-chaud);
  background: white;
}
"""

if "modal-overlay" not in css:
    css += "\n" + modal_css

with open("css/style.css", "w") as f:
    f.write(css)

# 3. UPDATE js/main.js
with open("js/main.js", "r") as f:
    js = f.read()

js_addition = """
// Devis Form Submission
window.submitDevis = function(e) {
  e.preventDefault();
  const nom = document.getElementById('devis-nom').value;
  const projet = document.getElementById('devis-projet').value;
  const message = document.getElementById('devis-message').value;
  
  const text = `Bonjour, je suis ${nom}.\\nJe souhaite demander un devis pour un projet de type : ${projet}.\\nDétails : ${message}`;
  const whatsappUrl = `https://wa.me/22967585650?text=${encodeURIComponent(text)}`;
  
  window.open(whatsappUrl, '_blank');
  document.getElementById('devis-modal').classList.remove('active');
  document.getElementById('devis-form').reset();
};
"""

if "submitDevis" not in js:
    js += "\n" + js_addition

with open("js/main.js", "w") as f:
    f.write(js)

print("Devis feature applied successfully.")
