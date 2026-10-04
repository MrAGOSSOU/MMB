import os
import shutil

categories = {
    'cuisines': 'Image/cuisines',
    'dressings': 'Image/dressings',
    'salons': 'Image/saloon',
    'chambres': 'Image/chambre',
    'bureaux': 'Image/bureaux',
    'salles-de-bain': 'Image/salle de bain'
}

with open("index.html", "r") as f:
    base_html = f.read()

# Extract the header/nav part and footer part to reuse
# We will just replace the "portfolio-masonry" content, and the parallax background
for cat_name, folder_path in categories.items():
    if not os.path.exists(folder_path):
        continue
    
    images = [img for img in os.listdir(folder_path) if img.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4'))]
    if not images:
        continue
    
    bg_img = f"{folder_path}/{images[0]}"
    
    grid_html = '<div class="portfolio-masonry" style="margin-top: 4rem; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">\n'
    
    for i, img in enumerate(images):
        span = 30 if i % 2 == 0 else 45
        img_path = f"{folder_path}/{img}"
        grid_html += f"""
          <a href="#contact" class="port-card reveal" style="grid-row-end: span {span};">
            <img src="{img_path}">
            <div class="port-overlay">
              <span style="color: var(--c-beige); font-size: 0.8rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem;">{cat_name}</span>
            </div>
          </a>\n"""
    grid_html += '</div>'
    
    # Create the new HTML page based on index.html
    page_html = base_html
    
    # Change active state on filters
    page_html = page_html.replace('class="filter-btn active"', 'class="filter-btn"')
    page_html = page_html.replace(f'href="{cat_name}.html" class="filter-btn"', f'href="{cat_name}.html" class="filter-btn active"')
    
    # Replace the masonry grid
    port_start = page_html.find('<div class="portfolio-masonry"')
    port_end = page_html.find('</div>\n      </section>', port_start)
    if port_start != -1 and port_end != -1:
        page_html = page_html[:port_start] + grid_html + page_html[port_end:]
        
    # Replace the parallax background for realisations wrapper
    realisations_wrapper_start = page_html.find('<!-- REALISATIONS WRAPPER -->')
    if realisations_wrapper_start != -1:
        bg_start = page_html.find("background: url('", realisations_wrapper_start) + 17
        bg_end = page_html.find("')", bg_start)
        if bg_start != -1 and bg_end != -1:
            page_html = page_html[:bg_start] + bg_img + page_html[bg_end:]
            
    with open(f"{cat_name}.html", "w") as f:
        f.write(page_html)

print("Generated category pages")
