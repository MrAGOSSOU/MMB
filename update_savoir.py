import os
import re

html_filepath = "index.html"
with open(html_filepath, "r") as f:
    html = f.read()

# 1. Clean the messy savoir-img-wrap and replace it with the new fading images
# We will find the div class="savoir-img-wrap and replace it up to </section>

savoir_images = [
    "Image/Autres../30af9e8b28b889719b75a378cf36a958.jpg",
    "Image/Autres../415aa88df9f7460bd2f377ea8b50adc5.jpg",
    "Image/Autres../50f0d86238313db7515d854b8b6307b7.jpg",
    "Image/Autres../6314c1a8f4a29acfe488645eb605eba5.jpg",
    "Image/Autres../67644d0c557ce1fe318e5a42877c40cd.jpg",
    "Image/Autres../ab8f039197ad7b740125543be97870d4.jpg"
]

images_html = ""
for i, img in enumerate(savoir_images):
    active_class = "active" if i == 0 else ""
    opacity = "1" if i == 0 else "0"
    images_html += f'          <img src="{img}" class="savoir-img parallax-img fade-img {active_class}" data-speed="0.1" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity: {opacity}; transition: opacity 0.8s ease;">\n'

new_savoir_wrap = f"""        <div class="savoir-img-wrap reveal" id="savoir-fader" style="position: relative; height: 800px; border-radius: 1rem; overflow: hidden;">
{images_html}        </div>
      </div>
    </section>"""

# Find the start of savoir-img-wrap
start_idx = html.find('<div class="savoir-img-wrap reveal"')
end_idx = html.find('</section>', start_idx) + len('</section>')

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_savoir_wrap + html[end_idx:]
    with open(html_filepath, "w") as f:
        f.write(html)
    print("Updated index.html")
else:
    print("Could not find savoir-img-wrap in index.html")

# 2. Add JS logic for the scroll crossfade
js_filepath = "js/main.js"
with open(js_filepath, "r") as f:
    js = f.read()

js_addition = """
  // Savoir-Faire Scroll Fade
  const fader = document.getElementById('savoir-fader');
  const fadeImgs = document.querySelectorAll('.fade-img');
  if(fader && fadeImgs.length > 0) {
    window.addEventListener('scroll', () => {
      const rect = fader.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      // If fader is in viewport
      if (rect.top < windowHeight && rect.bottom > 0) {
        // Calculate scroll progress (0 to 1) over the fader element
        const totalScrollDistance = windowHeight + rect.height;
        const currentScroll = windowHeight - rect.top;
        const progress = Math.max(0, Math.min(1, currentScroll / totalScrollDistance));
        
        const total = fadeImgs.length;
        // Find which image index corresponds to the progress
        const index = Math.min(total - 1, Math.floor(progress * total));
        
        fadeImgs.forEach((img, i) => {
          if (i === index) {
            img.style.opacity = 1;
            img.style.zIndex = 2;
          } else {
            img.style.opacity = 0;
            img.style.zIndex = 1;
          }
        });
      }
    });
  }
"""
if "savoir-fader" not in js:
    # Insert it inside DOMContentLoaded
    dom_idx = js.find('// Custom Cursor')
    if dom_idx != -1:
        js = js[:dom_idx] + js_addition + "\n  " + js[dom_idx:]
        with open(js_filepath, "w") as f:
            f.write(js)
        print("Updated js/main.js")
    else:
        print("Could not find // Custom Cursor inside js")
