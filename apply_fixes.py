import os
import re

# 1. Update index.html
with open("index.html", "r") as f:
    html = f.read()

# WhatsApp Button HTML
wa_html = """
    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/+22900000000?text=Salut,%20je%20suis%20interessé%20par%20ce%20que%20vous%20faites,%20puis%20en%20savoir%20plus%20?" target="_blank" class="whatsapp-btn">
      <svg viewBox="0 0 24 24" fill="white" width="30" height="30">
        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a5.22 5.22 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>
      </svg>
    </a>
"""
if "whatsapp-btn" not in html:
    html = html.replace('</body>', wa_html + '\n</body>')

# Update Bento grid classes and attributes
html = html.replace('<a href="#contact" class="bento-card reveal"', '<a href="#" data-cat="cuisines" class="bento-card reveal open-lightbox-btn"', 1)
html = html.replace('<a href="#contact" class="bento-card reveal" style="transition-delay: 0.1s;">\n          <img src="Image/image4-dressing.jpg">', '<a href="#" data-cat="dressings" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.1s;">\n          <img src="Image/image4-dressing.jpg">')
html = html.replace('<a href="#contact" class="bento-card reveal" style="transition-delay: 0.2s;">\n          <img src="Image/Salon_new.jpg">', '<a href="#" data-cat="salons" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.2s;">\n          <img src="Image/Salon_new.jpg">')
html = html.replace('<a href="#contact" class="bento-card reveal">\n          <img src="Image/Lit_new.jpg">', '<a href="#" data-cat="chambres" class="bento-card reveal open-lightbox-btn">\n          <img src="Image/Lit_new.jpg">')
html = html.replace('<a href="#contact" class="bento-card reveal" style="transition-delay: 0.1s;">\n          <img src="Image/Bureau_new.jpg">', '<a href="#" data-cat="bureaux" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.1s;">\n          <img src="Image/Bureau_new.jpg">')
html = html.replace('<a href="#contact" class="bento-card reveal" style="transition-delay: 0.2s;">\n          <img src="Image/IMG_9230.JPG">', '<a href="#" data-cat="dressings" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.2s;">\n          <img src="Image/IMG_9230.JPG">')
html = html.replace('<a href="#contact" class="bento-card reveal">\n          <img src="Image/IMG_9227.JPG">', '<a href="#" data-cat="salons" class="bento-card reveal open-lightbox-btn">\n          <img src="Image/IMG_9227.JPG">')
html = html.replace('<a href="#contact" class="bento-card reveal" style="transition-delay: 0.1s;">\n          <img src="Image/IMG_9285.JPG">', '<a href="#" data-cat="salons" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.1s;">\n          <img src="Image/IMG_9285.JPG">')
html = html.replace('<a href="#contact" class="bento-card reveal" style="transition-delay: 0.2s;">\n          <img src="Image/salle_de_bain_new.jpg">', '<a href="#" data-cat="salles-de-bain" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.2s;">\n          <img src="Image/salle_de_bain_new.jpg">')

with open("index.html", "w") as f:
    f.write(html)

# 2. Update style.css
with open("css/style.css", "r") as f:
    css = f.read()

wa_css = """
/* WhatsApp Button */
.whatsapp-btn {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background-color: #25D366;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(0,0,0,0.3);
  z-index: 9999;
  transition: transform 0.3s var(--ease), box-shadow 0.3s ease;
}
.whatsapp-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
}
"""
if ".whatsapp-btn" not in css:
    css += wa_css

# Fix scroll indicator overlap by hiding it on mobile
if "@media (max-width: 768px) {\n  .scroll-indicator {\n    display: none;\n  }" not in css:
    css += "\n@media (max-width: 768px) {\n  .scroll-indicator {\n    display: none;\n  }\n}\n"

with open("css/style.css", "w") as f:
    f.write(css)

# 3. Update main.js
with open("js/main.js", "r") as f:
    js = f.read()

js_addition = """
document.querySelectorAll('.open-lightbox-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    const cat = btn.getAttribute('data-cat');
    openLightbox(cat);
  });
});
"""
if "open-lightbox-btn" not in js:
    js += js_addition

with open("js/main.js", "w") as f:
    f.write(js)

print("Applied fixes")
