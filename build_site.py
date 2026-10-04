import os

# --- CSS ---
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
  font-family: var(--f-body);
  background-color: var(--c-ivory);
  color: var(--c-taupe);
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
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

/* Header */
.site-header {
  position: fixed; top: 0; left: 0; width: 100%; padding: 1.5rem 5vw; z-index: 1000;
  display: flex; justify-content: space-between; align-items: center;
  transition: all 0.4s ease;
}
.site-header.scrolled {
  background-color: rgba(70, 61, 54, 0.95);
  backdrop-filter: blur(10px);
  padding: 1rem 5vw;
  border-bottom: 1px solid rgba(201, 166, 107, 0.2);
  color: var(--c-ivory);
}
.site-header a { color: inherit; text-decoration: none; }
.logo img { height: 40px; transition: filter 0.3s; }
.nav-links { display: flex; gap: 2rem; }
.nav-links a { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; }
.nav-links a:hover { color: var(--c-gold); }
.mobile-toggle { display: none; }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 1rem 2rem; border-radius: 2px;
  font-family: var(--f-body); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em;
  text-decoration: none; transition: all 0.3s ease; border: 1px solid transparent;
}
.btn-primary { background-color: var(--c-gold); color: var(--c-white); }
.btn-primary:hover { background-color: var(--c-gold-warm); }
.btn-outline { border-color: var(--c-gold); color: var(--c-gold); }
.btn-outline:hover { background-color: var(--c-gold); color: var(--c-white); }

/* Hero */
.hero { position: relative; height: 100vh; display: flex; align-items: center; overflow: hidden; background: var(--c-taupe); color: var(--c-ivory); }
.hero-img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.6; }
.hero-content { position: relative; z-index: 2; max-width: 800px; }

/* Animations */
.fade-up { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease, transform 0.8s ease; }
.fade-up.is-visible { opacity: 1; transform: translateY(0); }

/* Layouts */
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-md); align-items: center; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-md); }

/* Portfolio */
.portfolio-masonry { display: grid; grid-template-columns: repeat(12, 1fr); gap: var(--space-sm); }
.portfolio-item { position: relative; display: block; overflow: hidden; }
.portfolio-item img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }
.portfolio-item:hover img { transform: scale(1.05); }
.portfolio-overlay {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(70, 61, 54, 0.6); opacity: 0; transition: opacity 0.3s;
  display: flex; flex-direction: column; justify-content: center; align-items: center; color: var(--c-ivory);
}
.portfolio-item:hover .portfolio-overlay { opacity: 1; }
.pi-1 { grid-column: 1 / 8; aspect-ratio: 16/9; }
.pi-2 { grid-column: 8 / 13; aspect-ratio: 4/5; }
.pi-3 { grid-column: 1 / 6; aspect-ratio: 4/5; }
.pi-4 { grid-column: 6 / 13; aspect-ratio: 16/9; }

/* Timeline */
.timeline { position: relative; max-width: 800px; margin: 0 auto; }
.timeline::before { content: ''; position: absolute; left: 50%; top: 0; width: 1px; height: 100%; background: var(--c-gold); transform: translateX(-50%); }
.timeline-step { display: flex; justify-content: space-between; margin-bottom: var(--space-lg); position: relative; }
.timeline-step:nth-child(even) { flex-direction: row-reverse; }
.t-content { width: 45%; text-align: right; }
.timeline-step:nth-child(even) .t-content { text-align: left; }
.t-num { position: absolute; left: 50%; top: 0; transform: translateX(-50%); width: 40px; height: 40px; background: var(--c-ivory); border: 1px solid var(--c-gold); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: var(--c-gold); font-weight: bold; }

/* FAQ */
.faq-item { border-bottom: 1px solid rgba(70, 61, 54, 0.2); padding: 1.5rem 0; cursor: pointer; }
.faq-q { display: flex; justify-content: space-between; align-items: center; font-family: var(--f-heading); font-size: 1.5rem; }
.faq-a { max-height: 0; overflow: hidden; transition: max-height 0.4s ease; margin-top: 0; color: var(--c-taupe-light); }
.faq-item.active .faq-a { max-height: 200px; margin-top: 1rem; }

/* Footer */
.site-footer { background: var(--c-taupe); color: var(--c-ivory); padding: var(--space-lg) 0 2rem 0; }
.site-footer a { color: inherit; text-decoration: none; opacity: 0.7; transition: opacity 0.3s; }
.site-footer a:hover { opacity: 1; color: var(--c-gold); }

/* Floating WA */
.wa-float { position: fixed; bottom: 30px; right: 30px; width: 60px; height: 60px; background: #25D366; border-radius: 50%; display: flex; align-items: center; justify-content: center; z-index: 1000; box-shadow: 0 10px 20px rgba(37,211,102,0.3); transition: transform 0.3s; }
.wa-float:hover { transform: scale(1.1); }
.wa-float svg { width: 30px; fill: white; }

/* Responsive */
@media(max-width: 768px) {
  .nav-links { display: none; }
  .mobile-toggle { display: block; font-size: 1.5rem; }
  .grid-2, .grid-3 { grid-template-columns: 1fr; }
  .pi-1, .pi-2, .pi-3, .pi-4 { grid-column: 1 / 13; aspect-ratio: 4/3; }
  .timeline::before { left: 20px; }
  .timeline-step, .timeline-step:nth-child(even) { flex-direction: row; padding-left: 60px; }
  .t-content { width: 100%; text-align: left; }
  .timeline-step:nth-child(even) .t-content { text-align: left; }
  .t-num { left: 20px; }
}
"""

# --- JS ---
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
});
"""

# --- HTML TEMPLATES ---
def layout(title, content, dark_header=False):
    header_class = "site-header" + (" scrolled" if dark_header else "")
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Meilleure Menuiserie du Bénin</title>
  <meta name="description" content="Conception et réalisation d'intérieurs et de mobilier sur mesure au Bénin.">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <a href="https://wa.me/22967585650" class="wa-float" target="_blank"><svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg></a>
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
  {content}
  <section class="bg-cream fade-up" style="text-align: center; border-top: 1px solid var(--c-gold);">
    <div class="container">
      <div class="t-overline">Votre projet commence ici</div>
      <h2 class="t-xxl" style="margin: 1rem 0 2rem 0;">IMAGINONS ENSEMBLE<br>VOTRE INTÉRIEUR.</h2>
      <a href="/contact.html" class="btn btn-primary">Demander un devis gratuit</a>
    </div>
  </section>
  <footer class="site-footer">
    <div class="container grid-3">
      <div>
        <img src="Image/LOGO.jpg" alt="MMB" style="height: 40px; filter: brightness(0) invert(1); margin-bottom: 1rem;">
        <p class="t-overline">L'Excellence Sur Mesure</p>
      </div>
      <div>
        <h4 style="color: var(--c-gold); margin-bottom: 1rem;">Navigation</h4>
        <div style="display:flex; flex-direction:column; gap:0.5rem;">
          <a href="/services.html">Services</a>
          <a href="/realisations.html">Réalisations</a>
          <a href="/a-propos.html">À Propos</a>
          <a href="/contact.html">Contact</a>
        </div>
      </div>
      <div>
        <h4 style="color: var(--c-gold); margin-bottom: 1rem;">Contact</h4>
        <p>01 67 58 56 50</p>
        <p>madamemelinapro@gmail.com</p>
        <p>Cotonou, Bénin</p>
      </div>
    </div>
  </footer>
  <script src="js/data.js"></script>
  <script src="js/main.js"></script>
</body>
</html>"""

pages = {}

pages["index.html"] = layout("Accueil", """
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
    </div>
  </section>
  <section class="container fade-up" style="text-align: center; max-width: 900px;">
    <h2 class="t-xxl" style="margin-bottom: 2rem;">VOTRE ESPACE.<br>NOTRE SAVOIR-FAIRE.<br>UNE RÉALISATION QUI VOUS RESSEMBLE.</h2>
    <div style="width: 1px; height: 60px; background: var(--c-gold); margin: 0 auto 2rem auto;"></div>
    <p style="font-size: 1.1rem;">Nous ne faisons pas simplement de la menuiserie. Nous transformons les espaces intérieurs grâce au sur-mesure, avec une exigence de qualité sans compromis adaptée au climat béninois.</p>
  </section>
  <section class="bg-cream">
    <div class="container">
      <div class="t-overline fade-up" style="text-align: center;">Nos Savoir-Faire</div>
      <h2 class="t-xl fade-up" style="text-align: center; margin-bottom: 3rem;">DES SOLUTIONS PENSÉES<br>POUR VOTRE ESPACE.</h2>
      <div class="grid-3">
        <div class="fade-up" style="background: white; padding: 2rem;">
          <h3 style="color: var(--c-gold); margin-bottom: 1rem;">01. Cuisines</h3>
          <p>Cuisines contemporaines sur mesure, fonctionnelles et élégantes.</p>
        </div>
        <div class="fade-up" style="background: white; padding: 2rem;">
          <h3 style="color: var(--c-gold); margin-bottom: 1rem;">02. Dressings</h3>
          <p>Aménagement d'espaces de rangement optimisés et luxueux.</p>
        </div>
        <div class="fade-up" style="background: white; padding: 2rem;">
          <h3 style="color: var(--c-gold); margin-bottom: 1rem;">03. Salons</h3>
          <p>Meubles TV et bibliothèques pensés comme des œuvres d'artisanat.</p>
        </div>
      </div>
      <div style="text-align: center; margin-top: 3rem;" class="fade-up"><a href="/services.html" class="btn btn-outline">Tous nos services</a></div>
    </div>
  </section>
  <section class="container">
    <div class="t-overline fade-up">Nos Réalisations</div>
    <h2 class="t-xl fade-up" style="margin-bottom: 3rem;">DES ESPACES PENSÉS DANS LES MOINDRES DÉTAILS.</h2>
    <div class="portfolio-masonry">
      <a href="/realisations.html" class="portfolio-item pi-1 fade-up"><img src="Image/IMG_9245.JPG"><div class="portfolio-overlay"><span class="t-xl">Cuisine Élégante</span></div></a>
      <a href="/realisations.html" class="portfolio-item pi-2 fade-up"><img src="Image/IMG_9227.JPG"><div class="portfolio-overlay"><span class="t-xl">Salon Sur Mesure</span></div></a>
      <a href="/realisations.html" class="portfolio-item pi-3 fade-up"><img src="Image/IMG_9257.JPG"><div class="portfolio-overlay"><span class="t-xl">Aménagement</span></div></a>
      <a href="/realisations.html" class="portfolio-item pi-4 fade-up"><img src="Image/IMG_9233.JPG"><div class="portfolio-overlay"><span class="t-xl">Cuisine Aquarium</span></div></a>
    </div>
    <div style="text-align: center; margin-top: 3rem;" class="fade-up"><a href="/realisations.html" class="btn btn-outline">Voir tout le portfolio</a></div>
  </section>
""")

pages["services.html"] = layout("Services", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">NOS SERVICES</h1>
      <p style="font-size: 1.2rem; max-width: 600px; margin-top: 1rem;">L'art de l'aménagement décliné dans toutes les pièces de votre vie.</p>
    </div>
  </section>
  <section class="container">
    <div class="grid-2 fade-up" style="margin-bottom: 4rem;">
      <img src="Image/IMG_9233.JPG" style="width:100%; aspect-ratio: 4/3; object-fit: cover;">
      <div>
        <div class="t-overline">01</div>
        <h2 class="t-xl" style="margin: 1rem 0;">Cuisines Sur Mesure</h2>
        <p style="margin-bottom: 2rem;">Le cœur de la maison mérite une attention particulière. Nous concevons des cuisines ergonomiques, dotées d'îlots centraux majestueux et de finitions impeccables.</p>
        <a href="/realisations.html" class="btn btn-outline">Voir les cuisines</a>
      </div>
    </div>
    <div class="grid-2 fade-up" style="margin-bottom: 4rem;">
      <div style="order: 2;">
        <div class="t-overline">02</div>
        <h2 class="t-xl" style="margin: 1rem 0;">Dressings & Rangements</h2>
        <p style="margin-bottom: 2rem;">L'optimisation de l'espace poussée à son paroxysme. Des dressings ouverts ou fermés qui mettent en valeur votre garde-robe.</p>
      </div>
      <img src="Image/IMG_9240.JPG" style="width:100%; aspect-ratio: 4/3; object-fit: cover; order: 1;">
    </div>
    <div class="grid-2 fade-up">
      <img src="Image/IMG_9227.JPG" style="width:100%; aspect-ratio: 4/3; object-fit: cover;">
      <div>
        <div class="t-overline">03</div>
        <h2 class="t-xl" style="margin: 1rem 0;">Salons & Bibliothèques</h2>
        <p style="margin-bottom: 2rem;">Des meubles TV suspendus, des habillages muraux en tasseaux de bois et des bibliothèques monumentales pour habiller vos espaces de vie.</p>
      </div>
    </div>
  </section>
""", dark_header=True)

pages["savoir-faire.html"] = layout("Savoir-faire", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">SAVOIR-FAIRE</h1>
      <p style="font-size: 1.2rem; max-width: 600px; margin-top: 1rem;">La matière, le geste, la précision.</p>
    </div>
  </section>
  <section class="container">
    <div class="grid-2 fade-up">
      <div>
        <h2 class="t-xl" style="margin-bottom: 2rem;">VOTRE ESPACE.<br>VOS DIMENSIONS.<br>VOTRE STYLE.</h2>
        <p style="margin-bottom: 1rem;">Dans nos ateliers au Bénin, nous allions les techniques traditionnelles de la menuiserie aux exigences du design contemporain.</p>
        <p>Le choix des matériaux est primordial : nous sélectionnons des bois et finitions capables de résister au climat local tout en offrant un rendu "importé" ultra-premium.</p>
      </div>
      <img src="Image/IMG_9256.JPG" style="width:100%; aspect-ratio: 1/1; object-fit: cover;">
    </div>
  </section>
""", dark_header=True)

pages["processus.html"] = layout("Processus", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">PROCESSUS</h1>
      <p style="font-size: 1.2rem; max-width: 600px; margin-top: 1rem;">De l'idée à la matière, un accompagnement sans faille.</p>
    </div>
  </section>
  <section class="container">
    <div class="timeline fade-up">
      <div class="timeline-step"><div class="t-num">01</div><div class="t-content"><h3>Prise de Contact</h3><p>Échange initial sur votre projet.</p></div></div>
      <div class="timeline-step"><div class="t-num">02</div><div class="t-content"><h3>Inspection du Site</h3><p>Prise de cotes précise. <em>(Inspection payante)</em></p></div></div>
      <div class="timeline-step"><div class="t-num">03</div><div class="t-content"><h3>Étude & Conception</h3><p>Analyse et conception 3D selon le projet.</p></div></div>
      <div class="timeline-step"><div class="t-num">04</div><div class="t-content"><h3>Validation & Devis</h3><p>Validation finale. <em>(Devis gratuit)</em></p></div></div>
      <div class="timeline-step"><div class="t-num">05</div><div class="t-content"><h3>Fabrication</h3><p>Réalisation dans nos ateliers.</p></div></div>
      <div class="timeline-step"><div class="t-num">06</div><div class="t-content"><h3>Installation</h3><p>Pose minutieuse par nos équipes.</p></div></div>
    </div>
  </section>
""", dark_header=True)

pages["a-propos.html"] = layout("À Propos", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">À PROPOS</h1>
      <p class="t-overline" style="margin-top: 1rem; color: var(--c-ivory);">Créée en 2020</p>
    </div>
  </section>
  <section class="container">
    <div class="grid-2 fade-up">
      <img src="Image/IMG_9297.JPG" style="width:100%; aspect-ratio: 4/5; object-fit: cover;">
      <div>
        <h2 class="t-xl" style="margin-bottom: 2rem;">UNE VISION DE<br>L'AMÉNAGEMENT.</h2>
        <p style="margin-bottom: 1rem;">Meilleure Menuiserie du Bénin est née d'une conviction : il est possible d'obtenir un mobilier de qualité internationale, fabriqué localement et sur mesure.</p>
        <p style="margin-bottom: 1rem;">Nous ne sommes pas de simples exécutants. Nous conseillons, nous orientons, et nous créons des espaces de vie qui subliment le quotidien de nos clients.</p>
        <ul style="list-style: none; margin-top: 2rem; color: var(--c-taupe-light);">
          <li style="margin-bottom: 0.5rem;">✦ Qualité premium garantie</li>
          <li style="margin-bottom: 0.5rem;">✦ Matériaux durables</li>
          <li style="margin-bottom: 0.5rem;">✦ Accompagnement total</li>
        </ul>
      </div>
    </div>
  </section>
""", dark_header=True)

pages["faq.html"] = layout("FAQ", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">FAQ</h1>
      <p style="font-size: 1.2rem; max-width: 600px; margin-top: 1rem;">Les réponses à vos questions.</p>
    </div>
  </section>
  <section class="container" style="max-width: 800px;">
    <div class="faq-item fade-up"><div class="faq-q">Le devis est-il gratuit ? <span>+</span></div><div class="faq-a">Oui, le devis est entièrement gratuit.</div></div>
    <div class="faq-item fade-up"><div class="faq-q">L'inspection du site est-elle gratuite ? <span>+</span></div><div class="faq-a">Non, l'inspection sur site pour prendre les cotes est payante.</div></div>
    <div class="faq-item fade-up"><div class="faq-q">Proposez-vous une conception 3D ? <span>+</span></div><div class="faq-a">Oui, la conception 3D peut être proposée selon la nature du projet.</div></div>
    <div class="faq-item fade-up"><div class="faq-q">Intervenez-vous hors de Cotonou ? <span>+</span></div><div class="faq-a">Oui, selon le projet nous pouvons intervenir en dehors de Cotonou.</div></div>
    <div class="faq-item fade-up"><div class="faq-q">Comment est calculé le prix ? <span>+</span></div><div class="faq-a">Le prix dépend notamment de l'espace, du modèle, des dimensions et du niveau de personnalisation.</div></div>
  </section>
""", dark_header=True)

pages["contact.html"] = layout("Contact", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">CONTACT</h1>
      <p style="font-size: 1.2rem; max-width: 600px; margin-top: 1rem;">Discutons de votre espace.</p>
    </div>
  </section>
  <section class="container">
    <div class="grid-2 fade-up">
      <div>
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
          <div class="t-overline">Localisation</div>
          <p>Cotonou, Bénin<br>Sur rendez-vous uniquement.</p>
        </div>
      </div>
      <div style="background: var(--c-cream); padding: 3rem;">
        <h2 class="t-xl" style="margin-bottom: 2rem;">DEMANDER UN DEVIS</h2>
        <a href="https://wa.me/22967585650" class="btn btn-primary" style="width: 100%;">Contact direct via WhatsApp</a>
      </div>
    </div>
  </section>
""", dark_header=True)

pages["realisations.html"] = layout("Réalisations", """
  <section class="bg-taupe" style="padding-top: 150px;">
    <div class="container fade-up">
      <h1 class="t-huge">RÉALISATIONS</h1>
      <p style="font-size: 1.2rem; max-width: 600px; margin-top: 1rem;">Un aperçu de notre travail sur mesure.</p>
    </div>
  </section>
  <section class="container">
    <div id="portfolio-root" class="grid-2"></div>
  </section>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const root = document.getElementById('portfolio-root');
      if(typeof portfolioData !== 'undefined') {
        let html = '';
        portfolioData.forEach(p => {
          html += `<div class="fade-up" style="margin-bottom: 3rem;">
            <img src="Image/${p.cover}" style="width:100%; aspect-ratio:4/3; object-fit:cover; margin-bottom: 1rem;">
            <div class="t-overline">${p.category}</div>
            <h3 class="t-xl" style="margin-top: 0.5rem;">${p.title}</h3>
          </div>`;
        });
        root.innerHTML = html;
      }
    });
  </script>
""", dark_header=True)

# Create css and js dirs
os.makedirs('css', exist_ok=True)
os.makedirs('js', exist_ok=True)

with open('css/style.css', 'w') as f: f.write(css_content)
with open('js/main.js', 'w') as f: f.write(js_content)

for name, content in pages.items():
    with open(name, 'w') as f:
        f.write(content)

print("Generated full Master Brief Awwwards-level Multi-Page architecture.")
