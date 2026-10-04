import os

css_content = """
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap');

:root {
  --c-taupe: #463D36;
  --c-taupe-light: #756A60;
  --c-ivory: #F5F0E8;
  --c-cream: #E9E0D3;
  --c-gold: #C9A66B;
  --c-gold-warm: #B59662;
  --c-oak: #B58A5A;
  --c-walnut: #634936;
  --c-white: #FFFFFF;

  --f-heading: 'Cormorant Garamond', serif;
  --f-body: 'Manrope', sans-serif;

  --space-xs: clamp(0.5rem, 1vw, 1rem);
  --space-sm: clamp(1rem, 2vw, 2rem);
  --space-md: clamp(2rem, 4vw, 4rem);
  --space-lg: clamp(4rem, 8vw, 8rem);
  --space-xl: clamp(6rem, 12vw, 12rem);
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  font-family: var(--f-body); background-color: var(--c-ivory); color: var(--c-taupe);
  -webkit-font-smoothing: antialiased; overflow-x: hidden; line-height: 1.6;
}

h1, h2, h3, h4, h5, h6 { font-family: var(--f-heading); font-weight: 400; line-height: 1.1; }
.t-huge { font-size: clamp(3rem, 8vw, 6rem); text-transform: uppercase; }
.t-xxl { font-size: clamp(2rem, 5vw, 4rem); text-transform: uppercase; }
.t-xl { font-size: clamp(1.5rem, 3vw, 2.5rem); }
.t-overline { font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--c-gold); font-weight: 600; }

.container { width: 100%; max-width: 1400px; margin: 0 auto; padding: 0 5vw; }
section { padding: var(--space-xl) 0; }
.bg-cream { background-color: var(--c-cream); }
.bg-taupe { background-color: var(--c-taupe); color: var(--c-ivory); }
.bg-white { background-color: var(--c-white); }

/* Header */
.site-header {
  position: fixed; top: 0; left: 0; width: 100%; padding: 1.5rem 5vw; z-index: 1000;
  display: flex; justify-content: space-between; align-items: center; transition: all 0.4s ease;
}
.site-header.scrolled {
  background-color: rgba(70, 61, 54, 0.95); backdrop-filter: blur(10px); padding: 1rem 5vw;
  border-bottom: 1px solid rgba(201, 166, 107, 0.2); color: var(--c-ivory);
}
.site-header a { color: inherit; text-decoration: none; }
.logo img { height: 40px; transition: filter 0.3s; }
.nav-links { display: flex; gap: 2rem; }
.nav-links a { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; transition: color 0.3s; }
.nav-links a:hover, .nav-links a.active { color: var(--c-gold); }
.mobile-toggle { display: none; font-size: 1.5rem; cursor: pointer; }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; justify-content: center; padding: 1rem 2rem; border-radius: 2px;
  font-family: var(--f-body); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em;
  text-decoration: none; transition: all 0.3s ease; border: 1px solid transparent; cursor: pointer;
}
.btn-primary { background-color: var(--c-gold); color: var(--c-white); }
.btn-primary:hover { background-color: var(--c-gold-warm); }
.btn-outline { border-color: var(--c-gold); color: var(--c-gold); }
.btn-outline:hover { background-color: var(--c-gold); color: var(--c-white); }

/* Hero */
.hero { position: relative; height: 100vh; min-height: 700px; display: flex; align-items: center; overflow: hidden; background: var(--c-taupe); color: var(--c-ivory); }
.hero-img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.5; }
.hero-content { position: relative; z-index: 2; max-width: 800px; }
.scroll-indicator { position: absolute; bottom: 40px; left: 5vw; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--c-ivory); display: flex; align-items: center; gap: 10px; z-index: 2;}
.scroll-line { width: 1px; height: 40px; background: var(--c-gold); animation: pulse-line 2s infinite; }
@keyframes pulse-line { 0% { transform: scaleY(0); transform-origin: top; } 50% { transform: scaleY(1); transform-origin: top; } 50.1% { transform: scaleY(1); transform-origin: bottom; } 100% { transform: scaleY(0); transform-origin: bottom; } }

/* Animations */
.fade-up { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease-out, transform 0.8s ease-out; }
.fade-up.is-visible { opacity: 1; transform: translateY(0); }

/* Layouts */
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-lg); align-items: center; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-md); }
.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-md); }

/* Portfolio Grid */
.portfolio-masonry { display: grid; grid-template-columns: repeat(12, 1fr); gap: var(--space-sm); }
.portfolio-item { position: relative; display: block; overflow: hidden; background: var(--c-taupe); }
.portfolio-item img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; opacity: 0.9; }
.portfolio-item:hover img { transform: scale(1.05); opacity: 0.5; }
.portfolio-overlay {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%;
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  color: var(--c-ivory); opacity: 0; transition: opacity 0.3s; text-align: center; padding: 1rem;
}
.portfolio-item:hover .portfolio-overlay { opacity: 1; }
.pi-1 { grid-column: 1 / 8; aspect-ratio: 16/9; }
.pi-2 { grid-column: 8 / 13; aspect-ratio: 4/5; }
.pi-3 { grid-column: 1 / 6; aspect-ratio: 4/5; }
.pi-4 { grid-column: 6 / 13; aspect-ratio: 16/9; }

/* Filters */
.filters { display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 3rem; justify-content: center; }
.filter-btn { background: none; border: 1px solid var(--c-taupe-light); padding: 0.5rem 1.5rem; border-radius: 50px; font-family: var(--f-body); color: var(--c-taupe); cursor: pointer; transition: all 0.3s; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; }
.filter-btn.active, .filter-btn:hover { background: var(--c-taupe); color: var(--c-ivory); border-color: var(--c-taupe); }

/* Timeline */
.timeline { position: relative; max-width: 800px; margin: 0 auto; }
.timeline::before { content: ''; position: absolute; left: 50%; top: 0; width: 1px; height: 100%; background: var(--c-gold); transform: translateX(-50%); }
.timeline-step { display: flex; justify-content: space-between; margin-bottom: var(--space-lg); position: relative; }
.timeline-step:nth-child(even) { flex-direction: row-reverse; }
.t-content { width: 45%; text-align: right; }
.timeline-step:nth-child(even) .t-content { text-align: left; }
.t-num { position: absolute; left: 50%; top: 0; transform: translateX(-50%); width: 40px; height: 40px; background: var(--c-ivory); border: 1px solid var(--c-gold); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: var(--c-gold); font-weight: bold; }

/* Values / Guarantee */
.value-box { border-top: 1px solid var(--c-gold); padding-top: 1rem; }
.value-box h3 { color: var(--c-gold); margin-bottom: 0.5rem; font-size: 1.25rem; }

/* FAQ */
.faq-item { border-bottom: 1px solid rgba(70, 61, 54, 0.2); padding: 1.5rem 0; cursor: pointer; }
.faq-q { display: flex; justify-content: space-between; align-items: center; font-family: var(--f-heading); font-size: 1.5rem; }
.faq-a { max-height: 0; overflow: hidden; transition: max-height 0.4s ease; margin-top: 0; color: var(--c-taupe-light); }
.faq-item.active .faq-a { max-height: 200px; margin-top: 1rem; }

/* Service Cards */
.service-card { border-bottom: 1px solid rgba(70, 61, 54, 0.2); padding-bottom: 2rem; }
.service-card img { width: 100%; aspect-ratio: 4/3; object-fit: cover; margin-bottom: 1.5rem; }

/* WhatsApp Float */
.wa-float { position: fixed; bottom: 30px; right: 30px; width: 60px; height: 60px; background: #25D366; border-radius: 50%; display: flex; align-items: center; justify-content: center; z-index: 1000; box-shadow: 0 10px 20px rgba(37,211,102,0.3); transition: transform 0.3s; }
.wa-float:hover { transform: scale(1.1); }
.wa-float svg { width: 30px; fill: white; }

/* Footer */
.site-footer { background: var(--c-taupe); color: var(--c-ivory); padding: var(--space-xl) 0 2rem 0; }
.site-footer a { color: inherit; text-decoration: none; opacity: 0.7; transition: opacity 0.3s; }
.site-footer a:hover { opacity: 1; color: var(--c-gold); }
.footer-divider { width: 100%; height: 1px; background: rgba(201, 166, 107, 0.2); margin: 3rem 0; }

@media(max-width: 768px) {
  .nav-links { display: none; }
  .mobile-toggle { display: block; }
  .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
  .pi-1, .pi-2, .pi-3, .pi-4 { grid-column: 1 / 13; aspect-ratio: 4/3; }
  .timeline::before { left: 20px; }
  .timeline-step, .timeline-step:nth-child(even) { flex-direction: row; padding-left: 60px; }
  .t-content { width: 100%; text-align: left; }
  .timeline-step:nth-child(even) .t-content { text-align: left; }
  .t-num { left: 20px; }
}
"""

js_content = """
document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('is-visible'); observer.unobserve(e.target); }
    });
  }, { threshold: 0.15 });
  document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

  document.querySelectorAll('.faq-item').forEach(item => {
    item.addEventListener('click', () => {
      document.querySelectorAll('.faq-item').forEach(i => { if (i !== item) i.classList.remove('active'); });
      item.classList.toggle('active');
    });
  });

  // Portfolio Filters
  const filterBtns = document.querySelectorAll('.filter-btn');
  const portfolioItems = document.querySelectorAll('.portfolio-card');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.dataset.filter;
      portfolioItems.forEach(item => {
        if (filter === 'tout' || item.dataset.category === filter) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
});
"""

def layout(title, content, dark_header=False):
    header_class = "site-header" + (" scrolled" if dark_header else "")
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Meilleure Menuiserie du Bénin | L'Excellence Sur Mesure</title>
  <meta name="description" content="Meilleure Menuiserie du Bénin conçoit et réalise des cuisines, lits, dressings, meubles et aménagements intérieurs sur mesure.">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <a href="https://wa.me/22967585650?text=Bonjour%2C%20je%20souhaite%20discuter%20d%E2%80%99un%20projet%20de%20r%C3%A9alisation%20sur%20mesure." class="wa-float" target="_blank"><svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg></a>
  <header class="{header_class}" style="color: var(--c-ivory);">
    <a href="/" class="logo"><img src="Image/LOGO.jpg" alt="MMB" style="filter: brightness(0) invert(1);"></a>
    <nav class="nav-links">
      <a href="/">Accueil</a>
      <a href="/services.html">Services</a>
      <a href="/realisations.html">Réalisations</a>
      <a href="/savoir-faire.html">Savoir-faire</a>
      <a href="/a-propos.html">À propos</a>
      <a href="/processus.html">Processus</a>
      <a href="/faq.html">FAQ</a>
      <a href="/contact.html">Contact</a>
    </nav>
    <div class="mobile-toggle">☰</div>
  </header>

  <main>
    {content}

    <!-- 11. FINAL CTA -->
    <section class="bg-cream fade-up" style="text-align: center; border-top: 1px solid var(--c-gold);">
      <div class="container">
        <h2 class="t-xxl" style="margin-bottom: 2rem;">VOTRE PROJET<br>COMMENCE ICI.</h2>
        <p style="font-size: 1.2rem; max-width: 600px; margin: 0 auto 3rem auto;">Cuisine, lit, dressing, meuble, rangement ou aménagement intérieur : imaginons ensemble une réalisation adaptée à votre espace.</p>
        <div style="display:flex; gap:1rem; justify-content:center;">
          <a href="/contact.html" class="btn btn-primary">Demander un devis gratuit</a>
          <a href="https://wa.me/22967585650" class="btn btn-outline" target="_blank">WhatsApp</a>
        </div>
      </div>
    </section>
  </main>

  <!-- 12. FOOTER -->
  <footer class="site-footer">
    <div class="container grid-4">
      <div>
        <img src="Image/LOGO.jpg" alt="MMB" style="height: 40px; filter: brightness(0) invert(1); margin-bottom: 1.5rem;">
        <h4 style="color: var(--c-gold); margin-bottom: 0.5rem; text-transform: uppercase;">Meilleure Menuiserie du Bénin</h4>
        <p class="t-overline">L'Excellence Sur Mesure</p>
      </div>
      <div>
        <h4 style="color: var(--c-gold); margin-bottom: 1.5rem;">Navigation</h4>
        <div style="display:flex; flex-direction:column; gap:0.5rem;">
          <a href="/services.html">Services</a>
          <a href="/realisations.html">Réalisations</a>
          <a href="/savoir-faire.html">Savoir-Faire</a>
          <a href="/a-propos.html">À Propos</a>
          <a href="/processus.html">Processus</a>
          <a href="/faq.html">FAQ</a>
          <a href="/contact.html">Contact</a>
        </div>
      </div>
      <div>
        <h4 style="color: var(--c-gold); margin-bottom: 1.5rem;">Contact</h4>
        <p style="margin-bottom: 0.5rem;">01 67 58 56 50</p>
        <p style="margin-bottom: 0.5rem;">01 97 47 49 58</p>
        <p style="margin-bottom: 1.5rem;">madamemelinapro@gmail.com</p>
        <a href="https://wa.me/22967585650" target="_blank" style="display: block; margin-bottom: 0.5rem;">WhatsApp</a>
        <a href="https://www.tiktok.com/@madame_melinaa" target="_blank">TikTok @madame_melinaa</a>
      </div>
      <div>
        <h4 style="color: var(--c-gold); margin-bottom: 1.5rem;">Localisation</h4>
        <p style="margin-bottom: 0.5rem;">Cotonou, Bénin</p>
        <p style="margin-bottom: 0.5rem;">Sur rendez-vous</p>
      </div>
    </div>
    <div class="container">
      <div class="footer-divider"></div>
      <p style="font-size: 0.8rem; text-align: center; opacity: 0.5;">© 2020 - 2026 Meilleure Menuiserie du Bénin. Tous droits réservés.</p>
    </div>
  </footer>
  <script src="js/data.js"></script>
  <script src="js/main.js"></script>
</body>
</html>"""

pages = {}

pages["index.html"] = layout("Accueil", """
  <!-- 01. HERO -->
  <section class="hero">
    <img src="Image/IMG_9233.JPG" alt="Cuisine Premium" class="hero-img">
    <div class="container hero-content fade-up">
      <div class="t-overline" style="margin-bottom: 1rem;">Meilleure Menuiserie du Bénin</div>
      <h1 class="t-huge" style="margin-bottom: 1.5rem;">L'EXCELLENCE<br>SUR MESURE.</h1>
      <p style="font-size: 1.2rem; margin-bottom: 2rem;">Nous concevons et réalisons des intérieurs, meubles et aménagements sur mesure pensés pour votre espace, votre style et vos besoins.</p>
      <div style="display: flex; gap: 1rem;">
        <a href="/realisations.html" class="btn btn-primary">Découvrir nos réalisations</a>
        <a href="/contact.html" class="btn btn-outline" style="color: white; border-color: white;">Demander un devis</a>
      </div>
      <div class="t-overline" style="margin-top: 2rem; font-size: 0.75rem;">Depuis 2020</div>
    </div>
    <div class="scroll-indicator">Découvrir <div class="scroll-line"></div></div>
  </section>

  <!-- 02. BRAND STATEMENT -->
  <section class="container fade-up" style="text-align: center; max-width: 900px; margin-top: 4rem;">
    <h2 class="t-xxl" style="margin-bottom: 2rem;">VOTRE ESPACE.<br>NOTRE SAVOIR-FAIRE.<br>UNE RÉALISATION QUI VOUS RESSEMBLE.</h2>
    <div style="width: 1px; height: 60px; background: var(--c-gold); margin: 0 auto 2rem auto;"></div>
    <p style="font-size: 1.2rem;">Nous ne faisons pas simplement de la menuiserie. Nous transformons les espaces intérieurs grâce au sur-mesure, avec une exigence de qualité sans compromis adaptée au climat béninois. Chaque détail est pensé, chaque fonction optimisée, chaque finition maîtrisée.</p>
  </section>

  <!-- 03. NOS SAVOIR-FAIRE -->
  <section class="bg-cream">
    <div class="container">
      <div class="t-overline fade-up" style="text-align: center;">Nos Savoir-Faire</div>
      <h2 class="t-xl fade-up" style="text-align: center; margin-bottom: 4rem;">DES SOLUTIONS PENSÉES<br>POUR VOTRE ESPACE.</h2>
      <div class="grid-4">
        <div class="service-card fade-up">
          <img src="Image/IMG_9227.JPG" alt="Cuisines">
          <div class="t-overline">01</div>
          <h3 class="t-xl" style="margin: 0.5rem 0;">Cuisines sur mesure</h3>
          <p>L'alliance de l'ergonomie et du design contemporain.</p>
        </div>
        <div class="service-card fade-up" style="transition-delay: 0.1s;">
          <img src="Image/IMG_9240.JPG" alt="Chambres">
          <div class="t-overline">02</div>
          <h3 class="t-xl" style="margin: 0.5rem 0;">Chambres & Lits</h3>
          <p>Des espaces de repos intimes et majestueux.</p>
        </div>
        <div class="service-card fade-up" style="transition-delay: 0.2s;">
          <img src="Image/IMG_9257.JPG" alt="Dressings">
          <div class="t-overline">03</div>
          <h3 class="t-xl" style="margin: 0.5rem 0;">Dressings & Rangements</h3>
          <p>L'optimisation absolue pour vos effets personnels.</p>
        </div>
        <div class="service-card fade-up" style="transition-delay: 0.3s;">
          <img src="Image/IMG_9273.JPG" alt="Salons">
          <div class="t-overline">04</div>
          <h3 class="t-xl" style="margin: 0.5rem 0;">Salons & Meubles TV</h3>
          <p>Des bibliothèques et habillages muraux d'exception.</p>
        </div>
      </div>
      <div style="text-align: center; margin-top: 4rem;" class="fade-up"><a href="/services.html" class="btn btn-outline">Voir tous nos services</a></div>
    </div>
  </section>

  <!-- 04. RÉALISATIONS -->
  <section class="container">
    <div class="t-overline fade-up">Nos Réalisations</div>
    <h2 class="t-xl fade-up" style="margin-bottom: 3rem;">DES ESPACES PENSÉS DANS LES MOINDRES DÉTAILS.</h2>
    <div class="portfolio-masonry">
      <a href="/realisations.html" class="portfolio-item pi-1 fade-up"><img src="Image/IMG_9245.JPG"><div class="portfolio-overlay"><span class="t-xl">Cuisine Contemporaine</span></div></a>
      <a href="/realisations.html" class="portfolio-item pi-2 fade-up"><img src="Image/IMG_9227.JPG"><div class="portfolio-overlay"><span class="t-xl">Salon & Tasseaux</span></div></a>
      <a href="/realisations.html" class="portfolio-item pi-3 fade-up"><img src="Image/IMG_9257.JPG"><div class="portfolio-overlay"><span class="t-xl">Aménagement Buanderie</span></div></a>
      <a href="/realisations.html" class="portfolio-item pi-4 fade-up"><img src="Image/IMG_9233.JPG"><div class="portfolio-overlay"><span class="t-xl">Cuisine Îlot Aquarium</span></div></a>
    </div>
    <div style="text-align: center; margin-top: 4rem;" class="fade-up"><a href="/realisations.html" class="btn btn-outline">Voir toutes nos réalisations</a></div>
  </section>

  <!-- 05. PERSONNALISATION -->
  <section class="bg-taupe">
    <div class="container grid-2 fade-up">
      <div>
        <h2 class="t-xxl" style="margin-bottom: 2rem;">VOTRE ESPACE.<br>VOS DIMENSIONS.<br>VOTRE STYLE.</h2>
        <p style="margin-bottom: 1rem;">Chaque projet que nous réalisons est unique car il est pensé exclusivement pour vous. Modèle, couleurs, matériaux, fonctionnalités : nous adaptons chaque paramètre à l'architecture de votre intérieur.</p>
        <p style="margin-bottom: 2rem;">La conception 3D peut être proposée selon la nature du projet pour vous projeter avant fabrication.</p>
        <a href="/contact.html" class="btn btn-primary">Parler de mon projet</a>
      </div>
      <img src="Image/IMG_9266.JPG" style="width: 100%; aspect-ratio: 4/5; object-fit: cover;">
    </div>
  </section>

  <!-- 06. LA MATIÈRE / LE GESTE / LA PRÉCISION -->
  <section class="container">
    <div class="t-overline fade-up" style="text-align: center;">Artisanat & Matériaux</div>
    <h2 class="t-xl fade-up" style="text-align: center; margin-bottom: 4rem;">LA MATIÈRE. LE GESTE. LA PRÉCISION.</h2>
    <div class="grid-3">
      <img src="Image/IMG_9285.JPG" class="fade-up" style="width: 100%; aspect-ratio: 1/1; object-fit: cover;" alt="Détail">
      <img src="Image/IMG_9256.JPG" class="fade-up" style="width: 100%; aspect-ratio: 1/1; object-fit: cover; transition-delay: 0.1s;" alt="Artisan">
      <img src="Image/IMG_9240.JPG" class="fade-up" style="width: 100%; aspect-ratio: 1/1; object-fit: cover; transition-delay: 0.2s;" alt="Bois">
    </div>
    <p class="fade-up" style="text-align: center; max-width: 700px; margin: 3rem auto 0 auto; font-size: 1.1rem;">Nous sélectionnons des bois et finitions capables de résister au climat local tout en offrant un rendu ultra-premium. Le geste de nos artisans fait la différence sur chaque poignée, chaque chant, chaque assemblage.</p>
  </section>

  <!-- 07. PROCESSUS -->
  <section class="bg-cream">
    <div class="container fade-up">
      <div class="t-overline" style="text-align: center;">Notre Approche</div>
      <h2 class="t-xl" style="text-align: center; margin-bottom: 4rem;">UN PROCESSUS CLAIR ET TRANSPARENT.</h2>
      <div class="timeline">
        <div class="timeline-step"><div class="t-num">01</div><div class="t-content"><h3>Prise de contact</h3><p>Échangeons autour de votre projet.</p></div></div>
        <div class="timeline-step"><div class="t-num">02</div><div class="t-content"><h3>Inspection</h3><p>Une inspection permet de mieux comprendre l’espace. <em>(Inspection payante)</em></p></div></div>
        <div class="timeline-step"><div class="t-num">03</div><div class="t-content"><h3>Étude du projet</h3><p>Analyse de l’espace, des besoins, et des possibilités de personnalisation.</p></div></div>
        <div class="timeline-step"><div class="t-num">04</div><div class="t-content"><h3>Validation & Devis</h3><p>Validation finale. <em>(Devis gratuit)</em></p></div></div>
        <div class="timeline-step"><div class="t-num">05</div><div class="t-content"><h3>Fabrication</h3><p>Votre projet entre en phase de réalisation dans nos ateliers.</p></div></div>
        <div class="timeline-step"><div class="t-num">06</div><div class="t-content"><h3>Installation</h3><p>Nous procédons à l’installation minutieuse de votre réalisation.</p></div></div>
      </div>
    </div>
  </section>

  <!-- 08. QUALITÉ / GARANTIE -->
  <section class="container fade-up">
    <h2 class="t-xl" style="margin-bottom: 3rem;">L'EXIGENCE SANS COMPROMIS.</h2>
    <div class="grid-4">
      <div class="value-box"><h3>Qualité</h3><p>Des standards internationaux.</p></div>
      <div class="value-box"><h3>Précision</h3><p>L'ajustement au millimètre.</p></div>
      <div class="value-box"><h3>Climat Béninois</h3><p>Des matériaux sélectionnés pour durer ici.</p></div>
      <div class="value-box"><h3>Garantie Illimitée</h3><p>Notre confiance absolue en notre travail.</p></div>
    </div>
  </section>

  <!-- 09. À PROPOS -->
  <section class="bg-taupe">
    <div class="container grid-2 fade-up">
      <img src="Image/IMG_9297.JPG" style="width: 100%; aspect-ratio: 4/5; object-fit: cover;">
      <div>
        <div class="t-overline">À Propos</div>
        <h2 class="t-xxl" style="margin: 1rem 0 2rem 0;">CRÉÉE EN 2020.</h2>
        <p style="margin-bottom: 2rem;">Meilleure Menuiserie du Bénin est née de la volonté d'apporter au Bénin un niveau de finition et d'aménagement intérieur jusque-là réservé à l'importation. Nous concevons, fabriquons et installons tout localement, avec une main-d'œuvre experte.</p>
        <a href="/a-propos.html" class="btn btn-primary">Découvrir notre histoire</a>
      </div>
    </div>
  </section>

  <!-- 10. FAQ PREVIEW -->
  <section class="container fade-up" style="max-width: 800px;">
    <div class="t-overline" style="text-align: center;">Questions Fréquentes</div>
    <h2 class="t-xl" style="text-align: center; margin-bottom: 3rem;">TOUT CE QUE VOUS DEVEZ SAVOIR.</h2>
    <div class="faq-item"><div class="faq-q">Le devis est-il gratuit ? <span>+</span></div><div class="faq-a">Oui, le devis est entièrement gratuit. Chaque projet étant unique, le prix dépend de l'espace et des matériaux.</div></div>
    <div class="faq-item"><div class="faq-q">L’inspection du site est-elle gratuite ? <span>+</span></div><div class="faq-a">Non. L’inspection du site est payante afin de garantir un relevé de cotes professionnel et engagé.</div></div>
    <div class="faq-item"><div class="faq-q">Intervenez-vous en dehors de Cotonou ? <span>+</span></div><div class="faq-a">Oui, selon l'envergure du projet, nous pouvons intervenir dans tout le Bénin.</div></div>
    <div style="text-align: center; margin-top: 3rem;"><a href="/faq.html" class="btn btn-outline">Toutes les questions</a></div>
  </section>
""")

pages["services.html"] = layout("Services", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">NOS SAVOIR-FAIRE</h1>
      <p style="font-size: 1.2rem; max-width: 600px; margin-top: 1rem;">Des solutions pensées pour votre espace.</p>
    </div>
  </section>
  <section class="container">
    <div class="grid-2 fade-up" style="margin-bottom: 6rem;">
      <img src="Image/IMG_9233.JPG" style="width:100%; aspect-ratio: 4/3; object-fit: cover;">
      <div>
        <div class="t-overline">01</div>
        <h2 class="t-xl" style="margin: 1rem 0;">Cuisines Sur Mesure</h2>
        <p style="margin-bottom: 2rem;">Le cœur de la maison. Cuisines contemporaines, îlots centraux, rangements intégrés et finitions haut de gamme.</p>
      </div>
    </div>
    <div class="grid-2 fade-up" style="margin-bottom: 6rem;">
      <div style="order: 2;">
        <div class="t-overline">02</div>
        <h2 class="t-xl" style="margin: 1rem 0;">Chambres & Lits</h2>
        <p style="margin-bottom: 2rem;">Lits capitonnés, têtes de lit sur mesure, et mobilier de chambre harmonieux pour un espace intime élégant.</p>
      </div>
      <img src="Image/IMG_9297.JPG" style="width:100%; aspect-ratio: 4/3; object-fit: cover; order: 1;">
    </div>
    <div class="grid-2 fade-up" style="margin-bottom: 6rem;">
      <img src="Image/IMG_9257.JPG" style="width:100%; aspect-ratio: 4/3; object-fit: cover;">
      <div>
        <div class="t-overline">03</div>
        <h2 class="t-xl" style="margin: 1rem 0;">Dressings & Rangements</h2>
        <p style="margin-bottom: 2rem;">De l'armoire intégrée au dressing room complet, chaque vêtement trouve sa place dans un écrin de bois sur mesure.</p>
      </div>
    </div>
    <div class="grid-2 fade-up" style="margin-bottom: 6rem;">
      <div style="order: 2;">
        <div class="t-overline">04</div>
        <h2 class="t-xl" style="margin: 1rem 0;">Salons & Meubles TV</h2>
        <p style="margin-bottom: 2rem;">Aménagement du salon, meubles TV suspendus, panneaux muraux en tasseaux et niches décoratives.</p>
      </div>
      <img src="Image/IMG_9227.JPG" style="width:100%; aspect-ratio: 4/3; object-fit: cover; order: 1;">
    </div>
    <div class="grid-2 fade-up">
      <img src="Image/IMG_9285.JPG" style="width:100%; aspect-ratio: 4/3; object-fit: cover;">
      <div>
        <div class="t-overline">05</div>
        <h2 class="t-xl" style="margin: 1rem 0;">Décoration Intérieure</h2>
        <p style="margin-bottom: 2rem;">Conseil, orientation et conception globale de vos espaces pour une esthétique cohérente et luxueuse.</p>
      </div>
    </div>
  </section>
""", dark_header=True)

pages["savoir-faire.html"] = layout("Savoir-Faire", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">SAVOIR-FAIRE</h1>
      <p style="font-size: 1.2rem; max-width: 600px; margin-top: 1rem;">Conception. Personnalisation. Fabrication. Finition. Installation.</p>
    </div>
  </section>
  <section class="container">
    <div class="grid-2 fade-up" style="margin-bottom: 4rem;">
      <div>
        <h2 class="t-xl" style="margin-bottom: 2rem;">CONCEPTION & PERSONNALISATION</h2>
        <p style="margin-bottom: 1rem;">Tout part d'une feuille blanche et de votre espace. Nous concevons nos meubles comme de véritables pièces d'architecture d'intérieur.</p>
      </div>
      <img src="Image/IMG_9266.JPG" style="width:100%; aspect-ratio: 4/3; object-fit: cover;">
    </div>
    <div class="grid-2 fade-up" style="margin-bottom: 4rem;">
      <img src="Image/IMG_9256.JPG" style="width:100%; aspect-ratio: 4/3; object-fit: cover;">
      <div>
        <h2 class="t-xl" style="margin-bottom: 2rem;">FABRICATION & FINITION</h2>
        <p style="margin-bottom: 1rem;">La matière est reine. Nous travaillons dans nos ateliers pour garantir des finitions lisses, des assemblages invisibles et une robustesse à toute épreuve.</p>
      </div>
    </div>
  </section>
""", dark_header=True)

pages["processus.html"] = layout("Processus", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">PROCESSUS</h1>
      <p style="font-size: 1.2rem; max-width: 600px; margin-top: 1rem;">Une méthodologie stricte pour un résultat sans surprise.</p>
    </div>
  </section>
  <section class="container">
    <div class="timeline fade-up">
      <div class="timeline-step"><div class="t-num">01</div><div class="t-content"><h3>Prise de contact</h3><p>Échangeons autour de votre projet.</p></div></div>
      <div class="timeline-step"><div class="t-num">02</div><div class="t-content"><h3>Inspection</h3><p>Une inspection permet de mieux comprendre l’espace, ses dimensions et ses contraintes. <br><strong>INSPECTION PAYANTE</strong></p></div></div>
      <div class="timeline-step"><div class="t-num">03</div><div class="t-content"><h3>Étude du projet</h3><p>Analyse de l’espace, des besoins, du modèle et des possibilités de personnalisation.</p></div></div>
      <div class="timeline-step"><div class="t-num">04</div><div class="t-content"><h3>Validation & Devis</h3><p>Validation du projet avant lancement en production. <br><strong>DEVIS GRATUIT</strong></p></div></div>
      <div class="timeline-step"><div class="t-num">05</div><div class="t-content"><h3>Fabrication</h3><p>Votre projet entre en phase de réalisation.</p></div></div>
      <div class="timeline-step"><div class="t-num">06</div><div class="t-content"><h3>Installation</h3><p>Nous procédons à l’installation finale de votre réalisation dans votre espace.</p></div></div>
    </div>
  </section>
""", dark_header=True)

pages["a-propos.html"] = layout("À Propos", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">MEILLEURE MENUISERIE DU BÉNIN</h1>
      <p class="t-overline" style="margin-top: 1rem; color: var(--c-ivory);">Créée en 2020</p>
    </div>
  </section>
  <section class="container">
    <div class="grid-2 fade-up">
      <img src="Image/IMG_9297.JPG" style="width:100%; aspect-ratio: 4/5; object-fit: cover;">
      <div>
        <h2 class="t-xl" style="margin-bottom: 2rem;">REPENSER L'INTÉRIEUR BÉNINOIS.</h2>
        <p style="margin-bottom: 1rem;">Créée en 2020, Meilleure Menuiserie du Bénin refuse la standardisation. Nous sommes guidés par une passion pour le bois, l'aménagement de l'espace, et l'exigence des finitions internationales.</p>
        <p style="margin-bottom: 1rem;">Nous accompagnons nos clients — particuliers et professionnels — dans la transformation de leurs espaces, en offrant un mobilier entièrement personnalisé qui allie l'esthétique contemporaine à la durabilité nécessaire sous notre climat.</p>
        <div style="margin-top: 2rem; border-top: 1px solid var(--c-gold); padding-top: 1rem;">
          <h4 style="color: var(--c-gold); margin-bottom: 0.5rem;">Cotonou, Bénin</h4>
          <p>Nous concevons et fabriquons localement.</p>
        </div>
      </div>
    </div>
  </section>
""", dark_header=True)

pages["faq.html"] = layout("FAQ", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">FAQ</h1>
      <p style="font-size: 1.2rem; max-width: 600px; margin-top: 1rem;">Tout ce que vous devez savoir.</p>
    </div>
  </section>
  <section class="container" style="max-width: 800px;">
    <div class="faq-item fade-up"><div class="faq-q">Quels types de projets réalisez-vous ? <span>+</span></div><div class="faq-a">Cuisines, chambres, lits, dressings, salons, meubles TV, bibliothèques, bureaux et décoration intérieure globale.</div></div>
    <div class="faq-item fade-up"><div class="faq-q">Travaillez-vous sur mesure ? <span>+</span></div><div class="faq-a">Oui, 100% de nos réalisations sont sur mesure.</div></div>
    <div class="faq-item fade-up"><div class="faq-q">Peut-on personnaliser les couleurs et les matériaux ? <span>+</span></div><div class="faq-a">Absolument, chaque projet est adapté à votre style.</div></div>
    <div class="faq-item fade-up"><div class="faq-q">Proposez-vous une conception 3D ? <span>+</span></div><div class="faq-a">La conception 3D peut être proposée selon la nature du projet.</div></div>
    <div class="faq-item fade-up"><div class="faq-q">Le devis est-il gratuit ? <span>+</span></div><div class="faq-a">Oui, le devis est gratuit.</div></div>
    <div class="faq-item fade-up"><div class="faq-q">L'inspection du site est-elle gratuite ? <span>+</span></div><div class="faq-a">Non. L'inspection du site est payante.</div></div>
    <div class="faq-item fade-up"><div class="faq-q">Intervenez-vous en dehors de Cotonou ? <span>+</span></div><div class="faq-a">Oui, selon le projet.</div></div>
    <div class="faq-item fade-up"><div class="faq-q">Comment est calculé le prix ? <span>+</span></div><div class="faq-a">Le prix dépend notamment de l'espace, du modèle, des dimensions et du niveau de personnalisation.</div></div>
  </section>
""", dark_header=True)

pages["contact.html"] = layout("Contact", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">PARLONS DE VOTRE PROJET.</h1>
    </div>
  </section>
  <section class="container">
    <div class="grid-2 fade-up">
      <div style="background: var(--c-white); padding: 3rem; border: 1px solid var(--c-cream);">
        <h2 class="t-xl" style="margin-bottom: 2rem;">ENVOYER UNE DEMANDE</h2>
        <form style="display:flex; flex-direction:column; gap:1rem;">
          <input type="text" placeholder="Nom" style="padding: 1rem; border: 1px solid var(--c-taupe-light); background: var(--c-ivory); font-family: var(--f-body);">
          <input type="tel" placeholder="Téléphone" style="padding: 1rem; border: 1px solid var(--c-taupe-light); background: var(--c-ivory); font-family: var(--f-body);">
          <input type="email" placeholder="Email" style="padding: 1rem; border: 1px solid var(--c-taupe-light); background: var(--c-ivory); font-family: var(--f-body);">
          <input type="text" placeholder="Ville" style="padding: 1rem; border: 1px solid var(--c-taupe-light); background: var(--c-ivory); font-family: var(--f-body);">
          <input type="text" placeholder="Type de projet (Cuisine, Dressing...)" style="padding: 1rem; border: 1px solid var(--c-taupe-light); background: var(--c-ivory); font-family: var(--f-body);">
          <textarea placeholder="Message (Dimensions approximatives, informations...)" rows="4" style="padding: 1rem; border: 1px solid var(--c-taupe-light); background: var(--c-ivory); font-family: var(--f-body); resize: vertical;"></textarea>
          <button type="button" class="btn btn-primary" style="align-self: flex-start; margin-top: 1rem;">Envoyer ma demande</button>
        </form>
      </div>
      <div style="padding: 3rem;">
        <h2 class="t-xl" style="margin-bottom: 2rem;">COORDONNÉES</h2>
        <div style="margin-bottom: 2rem;">
          <div class="t-overline">Téléphone & WhatsApp</div>
          <p>01 67 58 56 50<br>01 97 47 49 58</p>
        </div>
        <div style="margin-bottom: 2rem;">
          <div class="t-overline">Email</div>
          <p>madamemelinapro@gmail.com</p>
        </div>
        <div style="margin-bottom: 2rem;">
          <div class="t-overline">Réseaux Sociaux</div>
          <p>TikTok: @madame_melinaa</p>
        </div>
        <div style="margin-bottom: 2rem;">
          <div class="t-overline">Localisation</div>
          <p>Cotonou, Bénin<br>Sur rendez-vous uniquement.<br><em>Possibilité d'intervenir hors Cotonou.</em></p>
        </div>
      </div>
    </div>
  </section>
""", dark_header=True)

pages["realisations.html"] = layout("Réalisations", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">NOS RÉALISATIONS</h1>
      <p style="font-size: 1.2rem; max-width: 600px; margin-top: 1rem;">Une sélection de nos plus beaux projets.</p>
    </div>
  </section>
  <section class="container">
    <div class="filters fade-up">
      <button class="filter-btn active" data-filter="tout">TOUT</button>
      <button class="filter-btn" data-filter="cuisines">CUISINES</button>
      <button class="filter-btn" data-filter="salons">SALONS & TV</button>
      <button class="filter-btn" data-filter="rangements">RANGEMENTS</button>
    </div>
    <div id="portfolio-root" class="grid-2"></div>
  </section>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const root = document.getElementById('portfolio-root');
      if(typeof portfolioData !== 'undefined') {
        let html = '';
        portfolioData.forEach(p => {
          html += `<div class="portfolio-card fade-up" data-category="${p.category}" style="margin-bottom: 3rem;">
            <img src="Image/${p.cover}" style="width:100%; aspect-ratio:4/3; object-fit:cover; margin-bottom: 1rem;">
            <div class="t-overline">${p.category}</div>
            <h3 class="t-xl" style="margin-top: 0.5rem;">${p.title}</h3>
            <a href="/contact.html" style="color: var(--c-taupe); text-decoration: none; margin-top: 1rem; display: inline-block; border-bottom: 1px solid var(--c-taupe);">Parler de ce projet →</a>
          </div>`;
        });
        root.innerHTML = html;
      }
    });
  </script>
""", dark_header=True)

for name, content in pages.items():
    with open(name, 'w') as f:
        f.write(content)

with open('css/style.css', 'w') as f: f.write(css_content)
with open('js/main.js', 'w') as f: f.write(js_content)

print("Generated Perfect Match for Master Brief V3.")
