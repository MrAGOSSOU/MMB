import os

categories = {
    'cuisines': 'Image/cuisines',
    'dressings': 'Image/dressings',
    'salons': 'Image/saloon',
    'chambres': 'Image/chambre',
    'bureaux': 'Image/bureaux',
    'salles-de-bain': 'Image/salle de bain'
}

js_data = "const galleryData = {\n"
for cat, path in categories.items():
    if os.path.exists(path):
        images = [f for f in os.listdir(path) if f.lower().endswith(('.jpg','.jpeg','.png'))]
        images_str = ", ".join([f'"{path}/{img}"' for img in images])
        js_data += f'  "{cat}": [{images_str}],\n'
js_data += "};\n"

# Inject into main.js
with open("js/main.js", "r") as f:
    main_js = f.read()

# Add Lightbox JS
lightbox_js = """
// LIGHTBOX LOGIC
let currentCategory = [];
let currentIndex = 0;

const lightbox = document.createElement('div');
lightbox.className = 'lightbox';
lightbox.innerHTML = `
  <div class="lightbox-close">&times;</div>
  <div class="lightbox-prev">&#10094;</div>
  <div class="lightbox-next">&#10095;</div>
  <div class="lightbox-content">
    <img class="lightbox-img" src="" alt="Gallery Image">
  </div>
`;
document.body.appendChild(lightbox);

const lightboxImg = lightbox.querySelector('.lightbox-img');
const closeBtn = lightbox.querySelector('.lightbox-close');
const prevBtn = lightbox.querySelector('.lightbox-prev');
const nextBtn = lightbox.querySelector('.lightbox-next');

function openLightbox(category) {
  if (galleryData[category] && galleryData[category].length > 0) {
    currentCategory = galleryData[category];
    currentIndex = 0;
    showImage(currentIndex);
    lightbox.classList.add('active');
  } else {
    alert("Aucune image disponible pour cette catégorie.");
  }
}

function showImage(index) {
  if (index < 0) currentIndex = currentCategory.length - 1;
  else if (index >= currentCategory.length) currentIndex = 0;
  else currentIndex = index;
  
  lightboxImg.src = currentCategory[currentIndex];
}

closeBtn.addEventListener('click', () => lightbox.classList.remove('active'));
prevBtn.addEventListener('click', () => showImage(currentIndex - 1));
nextBtn.addEventListener('click', () => showImage(currentIndex + 1));

document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    const cat = btn.getAttribute('data-cat');
    if (cat === 'tout') {
      // maybe scroll to portfolio
    } else {
      openLightbox(cat);
    }
  });
});
"""

if "const galleryData =" not in main_js:
    with open("js/main.js", "a") as f:
        f.write("\n" + js_data + lightbox_js)


# Update index.html filters to use data-cat instead of href, and add Lightbox CSS
with open("index.html", "r") as f:
    html = f.read()

# 1. Update filter buttons
html = html.replace('<a href="realisations.html" class="filter-btn active">TOUT</a>', '<a href="#" data-cat="tout" class="filter-btn active">TOUT</a>')
html = html.replace('<a href="cuisines.html" class="filter-btn">CUISINES</a>', '<a href="#" data-cat="cuisines" class="filter-btn">CUISINES</a>')
html = html.replace('<a href="dressings.html" class="filter-btn">DRESSINGS</a>', '<a href="#" data-cat="dressings" class="filter-btn">DRESSINGS</a>')
html = html.replace('<a href="salons.html" class="filter-btn">SALONS</a>', '<a href="#" data-cat="salons" class="filter-btn">SALONS</a>')
html = html.replace('<a href="chambres.html" class="filter-btn">CHAMBRES</a>', '<a href="#" data-cat="chambres" class="filter-btn">CHAMBRES</a>')
html = html.replace('<a href="bureaux.html" class="filter-btn">BUREAUX</a>', '<a href="#" data-cat="bureaux" class="filter-btn">BUREAUX</a>')

# 2. Update subtitle color in showcase to be very bright #FADDAA and bold
html = html.replace('color: var(--c-beige); font-size: 0.8rem;', 'color: #FADDAA; font-weight: bold; font-size: 0.85rem;')

# 3. Add Lightbox CSS if not there
if ".lightbox {" not in html:
    css_to_add = """
      <style>
        .lightbox {
          position: fixed;
          top: 0; left: 0; width: 100%; height: 100%;
          background: rgba(10, 10, 10, 0.95);
          backdrop-filter: blur(10px);
          z-index: 9999;
          display: flex;
          align-items: center;
          justify-content: center;
          opacity: 0;
          pointer-events: none;
          transition: opacity 0.4s ease;
        }
        .lightbox.active {
          opacity: 1;
          pointer-events: auto;
        }
        .lightbox-content {
          max-width: 90%;
          max-height: 80vh;
          position: relative;
        }
        .lightbox-img {
          max-width: 100%;
          max-height: 80vh;
          object-fit: contain;
          border-radius: 5px;
          box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        }
        .lightbox-close, .lightbox-prev, .lightbox-next {
          position: absolute;
          color: white;
          font-size: 3rem;
          cursor: pointer;
          user-select: none;
          transition: color 0.3s;
        }
        .lightbox-close:hover, .lightbox-prev:hover, .lightbox-next:hover {
          color: var(--c-bois-chaud);
        }
        .lightbox-close { top: 30px; right: 40px; font-size: 4rem; }
        .lightbox-prev { left: 40px; top: 50%; transform: translateY(-50%); }
        .lightbox-next { right: 40px; top: 50%; transform: translateY(-50%); }
        
        @media (max-width: 768px) {
          .lightbox-prev { left: 10px; }
          .lightbox-next { right: 10px; }
          .lightbox-close { top: 10px; right: 20px; font-size: 3rem; }
        }
      </style>
"""
    head_end = html.find('</head>')
    if head_end != -1:
        html = html[:head_end] + css_to_add + html[head_end:]

with open("index.html", "w") as f:
    f.write(html)

print("Lightbox and buttons configured")
