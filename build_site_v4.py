import os

css_content = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap');

:root {
  /* Colors */
  --c-ivory: #F4F0E8;
  --c-beige: #D8C8B3;
  --c-bois: #B8946B;
  --c-noyer: #4A3024;
  --c-brun: #2B1C16;
  --c-charbon: #181513;
  --c-bronze: #A98B63;

  /* Typography */
  --f-heading: 'Playfair Display', serif;
  --f-body: 'Inter', sans-serif;

  /* Spacing */
  --space-xs: clamp(0.5rem, 1vw, 1rem);
  --space-sm: clamp(1rem, 2vw, 2rem);
  --space-md: clamp(2rem, 4vw, 4rem);
  --space-lg: clamp(4rem, 8vw, 8rem);
  --space-xl: clamp(6rem, 12vw, 12rem);
  
  /* Transitions */
  --t-slow: 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  --t-med: 0.4s ease;
}

/* Reset & Global */
* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; font-size: 16px; }
body {
  font-family: var(--f-body);
  background-color: var(--c-ivory);
  color: var(--c-charbon);
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
  line-height: 1.6;
  cursor: default; /* We will add custom cursor via JS */
}

/* Custom Cursor */
.cursor-dot {
  width: 8px; height: 8px; background-color: var(--c-noyer);
  border-radius: 50%; position: fixed; pointer-events: none;
  transform: translate(-50%, -50%); z-index: 9999;
  transition: transform 0.2s ease, opacity 0.2s ease;
}
.cursor-outline {
  width: 40px; height: 40px; border: 1px solid rgba(74, 48, 36, 0.3);
  border-radius: 50%; position: fixed; pointer-events: none;
  transform: translate(-50%, -50%); z-index: 9998;
  transition: width 0.3s, height 0.3s, background-color 0.3s;
}
.cursor-hover .cursor-dot { transform: translate(-50%, -50%) scale(0); opacity: 0; }
.cursor-hover .cursor-outline { width: 60px; height: 60px; background-color: rgba(169, 139, 99, 0.1); border-color: var(--c-bronze); }

/* Typography Classes */
h1, h2, h3, h4, h5, h6 { font-family: var(--f-heading); font-weight: 400; line-height: 1.1; }
.t-huge { font-size: clamp(3rem, 8vw, 6.5rem); letter-spacing: -0.02em; }
.t-xxl { font-size: clamp(2.5rem, 5vw, 4.5rem); letter-spacing: -0.01em; }
.t-xl { font-size: clamp(1.8rem, 3.5vw, 3rem); }
.t-lg { font-size: clamp(1.2rem, 2vw, 1.8rem); }
.t-body { font-size: 1.1rem; color: var(--c-noyer); max-width: 600px; }
.t-label { font-family: var(--f-body); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 500; color: var(--c-bronze); }

/* Layouts */
.container { width: 100%; max-width: 1440px; margin: 0 auto; padding: 0 5vw; }
section { padding: var(--space-xl) 0; position: relative; }
.section-sm { padding: var(--space-lg) 0; }

.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-lg); align-items: center; }
.grid-2-asym { display: grid; grid-template-columns: 4fr 5fr; gap: var(--space-lg); align-items: center; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-md); }

/* Backgrounds */
.bg-dark { background-color: var(--c-charbon); color: var(--c-ivory); }
.bg-dark .t-body { color: var(--c-beige); }
.bg-dark .t-label { color: var(--c-bronze); }
.bg-brun { background-color: var(--c-brun); color: var(--c-ivory); }

/* Buttons & Links */
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 1rem 2.5rem; font-family: var(--f-body); font-size: 0.8rem;
  text-transform: uppercase; letter-spacing: 0.1em; text-decoration: none;
  transition: all var(--t-med); cursor: pointer; border: 1px solid transparent;
}
.btn-primary { background-color: var(--c-noyer); color: var(--c-ivory); }
.btn-primary:hover { background-color: var(--c-charbon); }
.btn-outline { border-color: var(--c-noyer); color: var(--c-noyer); }
.btn-outline:hover { background-color: var(--c-noyer); color: var(--c-ivory); }
.bg-dark .btn-primary { background-color: var(--c-ivory); color: var(--c-charbon); }
.bg-dark .btn-primary:hover { background-color: var(--c-beige); }
.bg-dark .btn-outline { border-color: var(--c-ivory); color: var(--c-ivory); }
.bg-dark .btn-outline:hover { background-color: var(--c-ivory); color: var(--c-charbon); }

.link-underline { position: relative; text-decoration: none; color: inherit; padding-bottom: 2px; }
.link-underline::after {
  content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 1px;
  background-color: currentColor; transform: scaleX(0); transform-origin: right; transition: transform var(--t-med);
}
.link-underline:hover::after { transform: scaleX(1); transform-origin: left; }

/* Header */
.header {
  position: fixed; top: 0; left: 0; width: 100%; padding: 2rem 5vw; z-index: 1000;
  display: flex; justify-content: space-between; align-items: center; transition: all var(--t-med);
}
.header.scrolled {
  padding: 1.2rem 5vw; background-color: rgba(244, 240, 232, 0.95); backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(74, 48, 36, 0.1);
}
.header.scrolled-dark {
  background-color: rgba(24, 21, 19, 0.95); border-bottom: 1px solid rgba(244, 240, 232, 0.1); color: var(--c-ivory);
}
.logo { font-family: var(--f-heading); font-size: 1.5rem; letter-spacing: 0.1em; text-decoration: none; color: inherit; }
.nav-links { display: flex; gap: 2.5rem; }
.nav-links a { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; text-decoration: none; color: inherit; opacity: 0.7; transition: opacity var(--t-med); }
.nav-links a:hover, .nav-links a.active { opacity: 1; }
.mobile-btn { display: none; font-size: 1.5rem; cursor: pointer; }

/* Mobile Nav */
.mobile-nav {
  position: fixed; top: 0; left: 0; width: 100%; height: 100vh;
  background-color: var(--c-charbon); color: var(--c-ivory);
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  gap: 2rem; z-index: 999; transform: translateY(-100%); transition: transform var(--t-slow);
}
.mobile-nav.active { transform: translateY(0); }
.mobile-nav a { font-family: var(--f-heading); font-size: 2.5rem; text-decoration: none; color: inherit; }
.mobile-nav .btn { margin-top: 2rem; border-color: var(--c-ivory); color: var(--c-ivory); }

/* Hero Section */
.hero { height: 100vh; min-height: 800px; position: relative; display: flex; align-items: center; overflow: hidden; background-color: var(--c-charbon); }
.hero-bg {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;
  opacity: 0.6; transform: scale(1.05); transition: transform 10s ease-out;
}
.hero.loaded .hero-bg { transform: scale(1); }
.hero-content { position: relative; z-index: 2; width: 100%; color: var(--c-ivory); text-align: center; }
.hero-content .t-huge { margin: 1rem 0 2rem 0; }
.hero-footer {
  position: absolute; bottom: 3rem; left: 5vw; right: 5vw; z-index: 2;
  display: flex; justify-content: space-between; align-items: flex-end; color: var(--c-ivory);
}

/* Animations */
.reveal { opacity: 0; transform: translateY(40px); transition: opacity var(--t-slow), transform var(--t-slow); }
.reveal.active { opacity: 1; transform: translateY(0); }
.reveal-delay-1 { transition-delay: 0.1s; }
.reveal-delay-2 { transition-delay: 0.2s; }

/* Asymmetric Image Grids */
.img-reveal { position: relative; overflow: hidden; }
.img-reveal img { width: 100%; height: 100%; object-fit: cover; transform: scale(1.1); transition: transform 1.5s cubic-bezier(0.16, 1, 0.3, 1); }
.img-reveal.active img { transform: scale(1); }
.img-reveal::after { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: var(--c-ivory); transform-origin: top; transition: transform 1s cubic-bezier(0.16, 1, 0.3, 1); }
.bg-dark .img-reveal::after { background: var(--c-charbon); }
.img-reveal.active::after { transform: scaleY(0); }

/* Immersive Services List */
.service-list { display: flex; flex-direction: column; margin-top: 4rem; border-top: 1px solid rgba(74, 48, 36, 0.2); }
.bg-dark .service-list { border-color: rgba(244, 240, 232, 0.2); }
.service-row {
  display: flex; justify-content: space-between; align-items: center; padding: 2rem 0;
  border-bottom: 1px solid rgba(74, 48, 36, 0.2); cursor: pointer; transition: padding var(--t-med);
  position: relative; overflow: hidden;
}
.bg-dark .service-row { border-color: rgba(244, 240, 232, 0.2); }
.service-row:hover { padding-left: 2rem; padding-right: 2rem; }
.service-row .t-xl { margin: 0; transition: color var(--t-med); }
.service-row:hover .t-xl { color: var(--c-bronze); }
.service-img-hover {
  position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%) scale(0.8);
  width: 400px; height: 500px; object-fit: cover; opacity: 0; pointer-events: none;
  transition: opacity var(--t-med), transform var(--t-med); z-index: 10;
}
.service-row:hover .service-img-hover { opacity: 1; transform: translate(-50%, -50%) scale(1); }

/* Timeline */
.process-timeline { max-width: 900px; margin: 4rem auto 0; position: relative; }
.process-timeline::before { content: ''; position: absolute; left: 50px; top: 0; bottom: 0; width: 1px; background: rgba(74, 48, 36, 0.2); }
.process-step { display: flex; gap: 4rem; margin-bottom: 4rem; position: relative; }
.step-num { width: 100px; font-family: var(--f-heading); font-size: 3rem; color: var(--c-beige); text-align: right; line-height: 1; }
.step-content { flex: 1; padding-top: 0.5rem; }
.step-content h3 { margin-bottom: 1rem; }

/* Portfolio Masonry */
.gallery-grid { display: grid; grid-template-columns: repeat(12, 1fr); gap: 2rem; margin-top: 4rem; }
.gal-item { position: relative; overflow: hidden; display: block; cursor: pointer; }
.gal-item img { width: 100%; height: 100%; object-fit: cover; transition: transform var(--t-slow); }
.gal-item:hover img { transform: scale(1.05); }
.gal-overlay {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(24, 21, 19, 0.6); display: flex; flex-direction: column; justify-content: flex-end;
  padding: 2rem; opacity: 0; transition: opacity var(--t-med); color: var(--c-ivory);
}
.gal-item:hover .gal-overlay { opacity: 1; }
.gal-1 { grid-column: 1 / 8; aspect-ratio: 16/9; }
.gal-2 { grid-column: 8 / 13; aspect-ratio: 3/4; }
.gal-3 { grid-column: 1 / 5; aspect-ratio: 3/4; }
.gal-4 { grid-column: 5 / 13; aspect-ratio: 16/9; }
.gal-5 { grid-column: 1 / 13; aspect-ratio: 21/9; margin-top: 2rem; }

/* Lightbox */
.lightbox {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background: var(--c-charbon); z-index: 2000; display: flex; flex-direction: column;
  opacity: 0; pointer-events: none; transition: opacity var(--t-med);
}
.lightbox.active { opacity: 1; pointer-events: auto; }
.lb-close { position: absolute; top: 2rem; right: 2rem; color: var(--c-ivory); font-size: 2rem; cursor: pointer; z-index: 2001; }
.lb-content { flex: 1; display: flex; align-items: center; justify-content: center; padding: 4rem; }
.lb-content img { max-width: 100%; max-height: 80vh; object-fit: contain; }
.lb-info { text-align: center; color: var(--c-ivory); padding: 2rem; }

/* WhatsApp Float */
.wa-float {
  position: fixed; bottom: 2rem; right: 2rem; width: 60px; height: 60px;
  background: var(--c-charbon); border: 1px solid var(--c-bronze); border-radius: 50%;
  display: flex; align-items: center; justify-content: center; z-index: 1000;
  transition: transform var(--t-med), background var(--t-med);
}
.wa-float:hover { transform: scale(1.1); background: var(--c-bronze); }
.wa-float svg { width: 30px; fill: var(--c-ivory); }

/* Footer */
.footer { background: var(--c-charbon); color: var(--c-ivory); padding: var(--space-xl) 0 2rem; border-top: 1px solid rgba(244, 240, 232, 0.1); }
.footer a { color: inherit; text-decoration: none; opacity: 0.7; transition: opacity var(--t-med); }
.footer a:hover { opacity: 1; color: var(--c-bronze); }
.footer-divider { width: 100%; height: 1px; background: rgba(244, 240, 232, 0.1); margin: 4rem 0 2rem; }

/* Responsive */
@media (max-width: 1024px) {
  .grid-2, .grid-2-asym, .grid-3 { grid-template-columns: 1fr; }
  .process-timeline::before { left: 20px; }
  .step-num { width: 60px; font-size: 2rem; text-align: left; }
  .process-step { gap: 1.5rem; }
  .gal-1, .gal-2, .gal-3, .gal-4 { grid-column: 1 / 13; aspect-ratio: 4/3; }
  .service-row { padding-left: 1rem; padding-right: 1rem; }
  .service-row:hover { padding-left: 1rem; padding-right: 1rem; }
  .service-img-hover { display: none; }
}
@media (max-width: 768px) {
  .nav-links, .header .btn { display: none; }
  .mobile-btn { display: block; }
  .cursor-dot, .cursor-outline { display: none; }
  body { cursor: auto; }
  .hero-footer { flex-direction: column; align-items: flex-start; gap: 1rem; }
}
"""

js_content = """
document.addEventListener('DOMContentLoaded', () => {
  // Custom Cursor
  const cursorDot = document.querySelector('.cursor-dot');
  const cursorOutline = document.querySelector('.cursor-outline');
  
  if (window.innerWidth > 768 && cursorDot) {
    window.addEventListener('mousemove', (e) => {
      cursorDot.style.left = `${e.clientX}px`; cursorDot.style.top = `${e.clientY}px`;
      cursorOutline.style.left = `${e.clientX}px`; cursorOutline.style.top = `${e.clientY}px`;
    });
    
    document.querySelectorAll('a, button, .gal-item, .service-row').forEach(el => {
      el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
      el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
    });
  }

  // Header & Mobile Nav
  const header = document.querySelector('.header');
  const mobileBtn = document.querySelector('.mobile-btn');
  const mobileNav = document.querySelector('.mobile-nav');
  const isDarkBg = document.querySelector('.bg-dark') && window.scrollY < 100;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      if (document.body.classList.contains('page-dark')) {
        header.classList.add('scrolled-dark');
      } else {
        header.classList.add('scrolled');
      }
    } else {
      header.classList.remove('scrolled', 'scrolled-dark');
    }
  });

  if(mobileBtn) {
    mobileBtn.addEventListener('click', () => {
      mobileNav.classList.toggle('active');
      mobileBtn.innerHTML = mobileNav.classList.contains('active') ? '✕' : '☰';
    });
  }

  // Scroll Reveal
  const revealElements = document.querySelectorAll('.reveal, .img-reveal');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  
  revealElements.forEach(el => revealObserver.observe(el));
  
  // Hero load animation
  const hero = document.querySelector('.hero');
  if (hero) setTimeout(() => hero.classList.add('loaded'), 100);

  // Lightbox Logic
  const lightbox = document.getElementById('lightbox');
  if (lightbox) {
    const lbImg = lightbox.querySelector('img');
    const lbTitle = lightbox.querySelector('.t-xl');
    const lbCat = lightbox.querySelector('.t-label');
    const closeBtn = lightbox.querySelector('.lb-close');
    
    document.querySelectorAll('.gal-item').forEach(item => {
      item.addEventListener('click', () => {
        lbImg.src = item.dataset.img;
        lbTitle.innerText = item.dataset.title;
        lbCat.innerText = item.dataset.cat;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
      });
    });
    
    closeBtn.addEventListener('click', () => {
      lightbox.classList.remove('active');
      document.body.style.overflow = 'auto';
    });
  }
});
"""

def layout(title, content, page_dark=False):
    body_class = "page-dark bg-dark" if page_dark else ""
    header_style = "color: var(--c-ivory);" if page_dark else ""
    logo_style = "filter: brightness(0) invert(1);" if page_dark else ""
    btn_class = "btn-outline"
    if page_dark:
        btn_class = "btn-outline"
        
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | MEILLEURE MENUISERIE DU BÉNIN | Menuiserie & Ameublement sur Mesure</title>
  <meta name="description" content="MEILLEURE MENUISERIE DU BÉNIN conçoit et réalise vos cuisines, dressings, mobiliers et aménagements intérieurs sur mesure. Qualité, personnalisation et savoir-faire au Bénin.">
  <link rel="stylesheet" href="css/style.css">
</head>
<body class="{body_class}">
  <div class="cursor-dot"></div>
  <div class="cursor-outline"></div>

  <!-- HEADER -->
  <header class="header" style="{header_style}">
    <a href="/" class="logo">MMB.</a>
    <nav class="nav-links">
      <a href="/realisations.html">Réalisations</a>
      <a href="/services.html">Services</a>
      <a href="/a-propos.html">À Propos</a>
      <a href="/processus.html">Processus</a>
      <a href="/faq.html">FAQ</a>
      <a href="/contact.html">Contact</a>
    </nav>
    <a href="/contact.html" class="btn {btn_class} nav-links">Demander un Devis</a>
    <div class="mobile-btn">☰</div>
  </header>

  <!-- MOBILE NAV -->
  <div class="mobile-nav">
    <a href="/">Accueil</a>
    <a href="/realisations.html">Réalisations</a>
    <a href="/services.html">Services</a>
    <a href="/a-propos.html">À Propos</a>
    <a href="/processus.html">Processus</a>
    <a href="/faq.html">FAQ</a>
    <a href="/contact.html">Contact</a>
    <a href="/contact.html" class="btn btn-outline" style="border-color:var(--c-ivory);color:var(--c-ivory);">Demander un Devis</a>
  </div>

  <main>
    {content}

    <!-- SECTION FIN DE PAGE -->
    <section class="section-sm bg-brun reveal">
      <div class="container" style="text-align: center;">
        <h2 class="t-xxl" style="margin-bottom: 2rem;">L'EXCELLENCE COMMENCE PAR UNE IDÉE.</h2>
        <p class="t-body" style="margin: 0 auto 3rem auto; color: var(--c-ivory);">Parlez-nous de votre projet. Nous nous chargeons de lui donner forme.</p>
        <a href="/contact.html" class="btn btn-primary" style="background:var(--c-ivory);color:var(--c-charbon);">Demander un Devis</a>
      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="container grid-3">
      <div>
        <div class="logo" style="font-size: 2rem; margin-bottom: 1rem;">MMB.</div>
        <p class="t-label">Meilleure Menuiserie du Bénin</p>
        <p style="opacity: 0.7; margin-bottom: 2rem;">L'EXCELLENCE SUR MESURE</p>
      </div>
      <div class="grid-2">
        <div>
          <h4 class="t-label" style="margin-bottom: 1.5rem;">Navigation</h4>
          <div style="display:flex; flex-direction:column; gap:0.5rem;">
            <a href="/realisations.html">Réalisations</a>
            <a href="/services.html">Services</a>
            <a href="/a-propos.html">À Propos</a>
            <a href="/processus.html">Processus</a>
            <a href="/faq.html">FAQ</a>
            <a href="/contact.html">Contact</a>
          </div>
        </div>
        <div>
          <h4 class="t-label" style="margin-bottom: 1.5rem;">Contact</h4>
          <div style="display:flex; flex-direction:column; gap:0.5rem;">
            <a href="tel:0167585650">01 67 58 56 50</a>
            <a href="tel:0197474958">01 97 47 49 58</a>
            <a href="mailto:madamemelinapro@gmail.com">madamemelinapro@gmail.com</a>
            <a href="https://wa.me/22967585650" target="_blank">WhatsApp</a>
            <a href="https://www.tiktok.com/@madame_melinaa" target="_blank">TikTok</a>
          </div>
        </div>
      </div>
      <div style="text-align: right;">
        <h4 class="t-label" style="margin-bottom: 1.5rem;">Adresse</h4>
        <p style="opacity: 0.7;">Sur rendez-vous<br>Bénin</p>
      </div>
    </div>
    <div class="container">
      <div class="footer-divider"></div>
      <div style="display:flex; justify-content: space-between; align-items: center; opacity: 0.5; font-size: 0.8rem;">
        <p>© 2026 Meilleure Menuiserie du Bénin.</p>
        <p>Design Premium</p>
      </div>
    </div>
  </footer>

  <!-- WHATSAPP FLOAT -->
  <a href="https://wa.me/22967585650?text=Bonjour,%20je%20souhaite%20obtenir%20un%20devis%20pour%20un%20projet%20d'aménagement%20sur%20mesure." class="wa-float" target="_blank">
    <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
  </a>

  <!-- LIGHTBOX -->
  <div id="lightbox" class="lightbox">
    <div class="lb-close">✕</div>
    <div class="lb-content"><img src="" alt="Realisation"></div>
    <div class="lb-info">
      <div class="t-label"></div>
      <h3 class="t-xl" style="margin-top:0.5rem;"></h3>
    </div>
  </div>

  <script src="js/main.js"></script>
</body>
</html>"""

pages = {}

pages["index.html"] = layout("Accueil", """
  <!-- 1. HERO -->
  <section class="hero bg-dark">
    <img src="Image/IMG_9233.JPG" alt="Intérieur premium" class="hero-bg">
    <div class="hero-content">
      <div class="t-label reveal">MEILLEURE MENUISERIE DU BÉNIN</div>
      <h1 class="t-huge reveal reveal-delay-1">L'EXCELLENCE<br>SUR MESURE</h1>
    </div>
    <div class="hero-footer reveal reveal-delay-2">
      <p style="max-width: 400px; font-size: 1.1rem;">Nous concevons des espaces et mobiliers pensés autour de vos dimensions, de votre style et de votre vision.</p>
      <div style="display: flex; gap: 1rem;">
        <a href="/contact.html" class="btn btn-primary">Demander un Devis</a>
        <a href="/realisations.html" class="btn btn-outline" style="border-color:var(--c-ivory);color:var(--c-ivory);">Explorer Nos Réalisations</a>
      </div>
    </div>
  </section>

  <!-- 2. MANIFESTE -->
  <section class="container" style="padding-top: 10rem; padding-bottom: 10rem;">
    <h2 class="t-xxl reveal" style="max-width: 900px;">VOTRE ESPACE N'EST PAS STANDARD.<br><span style="color:var(--c-bronze);">Votre mobilier ne devrait pas l'être non plus.</span></h2>
    <div class="grid-2" style="margin-top: 5rem;">
      <div></div>
      <p class="t-body reveal">Depuis 2020, MEILLEURE MENUISERIE DU BÉNIN imagine et réalise des aménagements intérieurs adaptés à chaque espace, chaque dimension et chaque style.</p>
    </div>
  </section>

  <!-- 3. L'ART DU SUR-MESURE -->
  <section class="bg-brun">
    <div class="container grid-2-asym">
      <div class="reveal">
        <div class="t-label">L'ART DU SUR-MESURE</div>
        <h2 class="t-xl" style="margin: 2rem 0;">DIMENSIONS. MATIÈRES. FINITIONS.</h2>
        <p class="t-body" style="color:var(--c-ivory); margin-bottom: 2rem;">Nous ne fabriquons pas simplement des meubles. Nous traitons le mobilier comme de l'architecture intérieure. Les lignes, les proportions, les textures : chaque détail est pensé pour créer une harmonie parfaite dans votre espace.</p>
        <a href="/processus.html" class="link-underline">Découvrir notre processus</a>
      </div>
      <div class="img-reveal"><img src="Image/IMG_9256.JPG" alt="Atelier" style="aspect-ratio: 4/5;"></div>
    </div>
  </section>

  <!-- 4. SERVICES IMMERSIVE -->
  <section class="container">
    <div class="t-label reveal">NOS SAVOIR-FAIRE</div>
    <div class="service-list reveal">
      <a href="/services.html" class="service-row">
        <h3 class="t-xl">CUISINES SUR MESURE</h3><span class="t-label">01</span>
        <img src="Image/IMG_9233.JPG" class="service-img-hover">
      </a>
      <a href="/services.html" class="service-row">
        <h3 class="t-xl">DRESSINGS & PLACARDS</h3><span class="t-label">02</span>
        <img src="Image/IMG_9257.JPG" class="service-img-hover">
      </a>
      <a href="/services.html" class="service-row">
        <h3 class="t-xl">AMÉNAGEMENT DE SALON</h3><span class="t-label">03</span>
        <img src="Image/IMG_9227.JPG" class="service-img-hover">
      </a>
      <a href="/services.html" class="service-row">
        <h3 class="t-xl">DÉCORATION INTÉRIEURE</h3><span class="t-label">04</span>
        <img src="Image/IMG_9297.JPG" class="service-img-hover">
      </a>
    </div>
    <div style="margin-top: 4rem; text-align: right;"><a href="/services.html" class="btn btn-outline">Voir tous nos services</a></div>
  </section>

  <!-- 5. PORTFOLIO APERÇU -->
  <section class="bg-dark">
    <div class="container">
      <div class="grid-2 reveal">
        <h2 class="t-xxl">DES ESPACES PENSÉS<br>POUR VOUS.</h2>
        <p class="t-body" style="align-self: flex-end; padding-bottom: 1rem;">Découvrez quelques-unes de nos réalisations qui illustrent notre passion pour le détail et la perfection.</p>
      </div>
      <div class="gallery-grid">
        <div class="gal-item gal-1 reveal" data-img="Image/IMG_9245.JPG" data-title="Cuisine Contemporaine" data-cat="Cuisine">
          <img src="Image/IMG_9245.JPG"><div class="gal-overlay"><div class="t-label">Cuisine</div><h3 class="t-xl">Résidence Cotonou</h3></div>
        </div>
        <div class="gal-item gal-2 reveal reveal-delay-1" data-img="Image/IMG_9273.JPG" data-title="Meuble TV" data-cat="Salon">
          <img src="Image/IMG_9273.JPG"><div class="gal-overlay"><div class="t-label">Salon</div><h3 class="t-xl">Aménagement Mural</h3></div>
        </div>
      </div>
      <div style="margin-top: 4rem; text-align: center;"><a href="/realisations.html" class="btn btn-primary">Explorer le portfolio</a></div>
    </div>
  </section>
""", page_dark=False)

pages["realisations.html"] = layout("Réalisations", """
  <section class="container" style="padding-top: 10rem;">
    <div class="t-label reveal">NOS RÉALISATIONS</div>
    <h1 class="t-huge reveal reveal-delay-1" style="max-width: 900px; margin-top: 2rem;">Le sur-mesure prend forme.</h1>
    
    <div class="gallery-grid" style="margin-top: 8rem;">
      <div class="gal-item gal-1 reveal" data-img="Image/IMG_9245.JPG" data-title="Cuisine Contemporaine" data-cat="Cuisines">
        <img src="Image/IMG_9245.JPG"><div class="gal-overlay"><div class="t-label">Cuisines</div><h3 class="t-xl">Cuisine Contemporaine</h3></div>
      </div>
      <div class="gal-item gal-2 reveal reveal-delay-1" data-img="Image/IMG_9273.JPG" data-title="Aménagement Mural" data-cat="Salons">
        <img src="Image/IMG_9273.JPG"><div class="gal-overlay"><div class="t-label">Salons</div><h3 class="t-xl">Aménagement Mural</h3></div>
      </div>
      <div class="gal-item gal-3 reveal" data-img="Image/IMG_9257.JPG" data-title="Dressing Intégré" data-cat="Dressings">
        <img src="Image/IMG_9257.JPG"><div class="gal-overlay"><div class="t-label">Dressings</div><h3 class="t-xl">Dressing Intégré</h3></div>
      </div>
      <div class="gal-item gal-4 reveal reveal-delay-1" data-img="Image/IMG_9233.JPG" data-title="Îlot Central" data-cat="Cuisines">
        <img src="Image/IMG_9233.JPG"><div class="gal-overlay"><div class="t-label">Cuisines</div><h3 class="t-xl">Îlot Central</h3></div>
      </div>
      <div class="gal-item gal-5 reveal" data-img="Image/IMG_9227.JPG" data-title="Salon Élégant" data-cat="Salons">
        <img src="Image/IMG_9227.JPG"><div class="gal-overlay"><div class="t-label">Salons</div><h3 class="t-xl">Salon Élégant</h3></div>
      </div>
    </div>
  </section>
""")

pages["services.html"] = layout("Services", """
  <section class="container" style="padding-top: 10rem;">
    <h1 class="t-huge reveal">NOS SAVOIR-FAIRE.</h1>
    
    <div style="margin-top: 8rem;" class="grid-2-asym reveal">
      <div>
        <div class="t-label">01</div>
        <h2 class="t-xxl" style="margin: 1rem 0 2rem;">CUISINES<br>SUR MESURE</h2>
        <p class="t-body">L'alliance de l'ergonomie et de l'esthétisme. Chaque cuisine est pensée autour de vos habitudes de vie, avec des matériaux nobles et des finitions impeccables pour résister au temps.</p>
      </div>
      <div class="img-reveal"><img src="Image/IMG_9233.JPG" style="aspect-ratio: 4/3;"></div>
    </div>

    <div style="margin-top: 8rem;" class="grid-2-asym reveal">
      <div class="img-reveal"><img src="Image/IMG_9257.JPG" style="aspect-ratio: 4/3;"></div>
      <div style="padding-left: 2rem;">
        <div class="t-label">02</div>
        <h2 class="t-xxl" style="margin: 1rem 0 2rem;">DRESSINGS &<br>PLACARDS</h2>
        <p class="t-body">L'optimisation de l'espace élevée au rang d'art. Des rangements intelligents, des penderies éclairées et des tiroirs sur mesure pour une organisation parfaite.</p>
      </div>
    </div>

    <div style="margin-top: 8rem;" class="grid-2-asym reveal">
      <div>
        <div class="t-label">03</div>
        <h2 class="t-xxl" style="margin: 1rem 0 2rem;">SALONS &<br>MEUBLES TV</h2>
        <p class="t-body">De la bibliothèque architecturale au meuble TV suspendu, nous concevons des éléments centraux qui structurent votre espace de vie avec élégance.</p>
      </div>
      <div class="img-reveal"><img src="Image/IMG_9227.JPG" style="aspect-ratio: 4/3;"></div>
    </div>
  </section>
""")

pages["processus.html"] = layout("Processus", """
  <section class="container" style="padding-top: 10rem;">
    <div class="t-label reveal">NOTRE MÉTHODE</div>
    <h1 class="t-huge reveal reveal-delay-1" style="max-width: 900px; margin-top: 2rem;">DE L'IDÉE À LA RÉALISATION.</h1>
    
    <div class="process-timeline reveal">
      <div class="process-step">
        <div class="step-num">01</div>
        <div class="step-content">
          <h3 class="t-xl">PRISE DE CONTACT</h3>
          <p class="t-body">Nous échangeons sur votre vision, vos envies et les spécificités de votre projet.</p>
        </div>
      </div>
      <div class="process-step">
        <div class="step-num">02</div>
        <div class="step-content">
          <h3 class="t-xl">INSPECTION DU SITE</h3>
          <p class="t-body">Notre équipe se déplace pour analyser l'espace, prendre les cotes exactes et comprendre la lumière. <br><span class="t-label">Inspection Payante</span></p>
        </div>
      </div>
      <div class="process-step">
        <div class="step-num">03</div>
        <div class="step-content">
          <h3 class="t-xl">ÉTUDE DU PROJET</h3>
          <p class="t-body">Nous concevons les plans, sélectionnons les matériaux et proposons (si nécessaire) une modélisation 3D.</p>
        </div>
      </div>
      <div class="process-step">
        <div class="step-num">04</div>
        <div class="step-content">
          <h3 class="t-xl">VALIDATION & DEVIS</h3>
          <p class="t-body">Présentation détaillée du projet finalisé et de son devis. <br><span class="t-label">Devis Gratuit</span></p>
        </div>
      </div>
      <div class="process-step">
        <div class="step-num">05</div>
        <div class="step-content">
          <h3 class="t-xl">FABRICATION</h3>
          <p class="t-body">Réalisation dans nos ateliers avec une précision millimétrique et un contrôle qualité rigoureux.</p>
        </div>
      </div>
      <div class="process-step">
        <div class="step-num">06</div>
        <div class="step-content">
          <h3 class="t-xl">INSTALLATION</h3>
          <p class="t-body">Nos experts assurent une pose soignée, dans le respect de votre intérieur, pour un résultat impeccable.</p>
        </div>
      </div>
    </div>
  </section>
""")

pages["a-propos.html"] = layout("À Propos", """
  <section class="container" style="padding-top: 10rem;">
    <div class="grid-2-asym">
      <div class="reveal">
        <div class="t-label">L'ENTREPRISE</div>
        <h1 class="t-huge" style="margin: 2rem 0;">DEPUIS 2020.</h1>
        <p class="t-body">MEILLEURE MENUISERIE DU BÉNIN accompagne ses clients dans la conception et la réalisation de mobiliers et d'aménagements intérieurs sur mesure.</p>
        <p class="t-body" style="margin-top: 2rem;">Nous avons fait le choix de l'excellence : des matériaux de premier choix adaptés à notre climat, un design contemporain inspiré des grandes tendances architecturales, et une fabrication locale de très haute précision.</p>
      </div>
      <div class="img-reveal"><img src="Image/IMG_9297.JPG" style="aspect-ratio: 3/4;"></div>
    </div>
    
    <div style="margin-top: 10rem;" class="grid-3 reveal">
      <div>
        <div class="t-label">01</div>
        <h3 class="t-lg" style="margin: 1rem 0;">SUR MESURE</h3>
        <p class="t-body" style="font-size: 0.95rem;">Chaque réalisation est unique, adaptée à l'espace et aux besoins spécifiques du client.</p>
      </div>
      <div>
        <div class="t-label">02</div>
        <h3 class="t-lg" style="margin: 1rem 0;">MATÉRIAUX</h3>
        <p class="t-body" style="font-size: 0.95rem;">Des matériaux modernes, durables et rigoureusement sélectionnés pour le climat béninois.</p>
      </div>
      <div>
        <div class="t-label">03</div>
        <h3 class="t-lg" style="margin: 1rem 0;">GARANTIE</h3>
        <p class="t-body" style="font-size: 0.95rem;">Nous offrons une garantie illimitée, preuve de la confiance absolue en notre travail.</p>
      </div>
    </div>
  </section>
""")

pages["faq.html"] = layout("FAQ", """
  <section class="container" style="padding-top: 10rem; max-width: 900px;">
    <h1 class="t-huge reveal">FAQ</h1>
    <div style="margin-top: 4rem;" class="reveal">
      <div style="padding: 2rem 0; border-bottom: 1px solid rgba(74, 48, 36, 0.2);">
        <h3 class="t-lg" style="margin-bottom: 1rem;">Combien coûte une cuisine sur mesure ?</h3>
        <p class="t-body">Chaque projet est unique. Le prix dépend de l'espace, du modèle choisi, des matériaux et des finitions. Le devis personnalisé est gratuit.</p>
      </div>
      <div style="padding: 2rem 0; border-bottom: 1px solid rgba(74, 48, 36, 0.2);">
        <h3 class="t-lg" style="margin-bottom: 1rem;">Quels matériaux utilisez-vous ?</h3>
        <p class="t-body">Des matériaux modernes, de haute qualité, spécialement sélectionnés pour résister au climat du Bénin.</p>
      </div>
      <div style="padding: 2rem 0; border-bottom: 1px solid rgba(74, 48, 36, 0.2);">
        <h3 class="t-lg" style="margin-bottom: 1rem;">L'inspection du site est-elle gratuite ?</h3>
        <p class="t-body">Non. L'inspection du site est payante, elle nous permet de faire une étude technique approfondie et une prise de cotes exacte.</p>
      </div>
      <div style="padding: 2rem 0; border-bottom: 1px solid rgba(74, 48, 36, 0.2);">
        <h3 class="t-lg" style="margin-bottom: 1rem;">Faites-vous la conception 3D ?</h3>
        <p class="t-body">Oui, une conception 3D est réalisée selon la nature et l'envergure du projet.</p>
      </div>
      <div style="padding: 2rem 0; border-bottom: 1px solid rgba(74, 48, 36, 0.2);">
        <h3 class="t-lg" style="margin-bottom: 1rem;">Faites-vous l'installation ?</h3>
        <p class="t-body">Absolument. Nous prenons en charge la fabrication et l'installation complète.</p>
      </div>
      <div style="padding: 2rem 0; border-bottom: 1px solid rgba(74, 48, 36, 0.2);">
        <h3 class="t-lg" style="margin-bottom: 1rem;">Quelle garantie proposez-vous ?</h3>
        <p class="t-body">Nous offrons une garantie illimitée sur la qualité de nos réalisations.</p>
      </div>
    </div>
  </section>
""")

pages["contact.html"] = layout("Contact", """
  <section class="container" style="padding-top: 10rem;">
    <div class="grid-2-asym reveal">
      <div>
        <h1 class="t-huge" style="margin-bottom: 4rem;">CONTACT.</h1>
        <div style="margin-bottom: 3rem;">
          <div class="t-label" style="margin-bottom: 1rem;">TÉLÉPHONES & WHATSAPP</div>
          <p class="t-lg">01 67 58 56 50<br>01 97 47 49 58</p>
        </div>
        <div style="margin-bottom: 3rem;">
          <div class="t-label" style="margin-bottom: 1rem;">EMAIL</div>
          <p class="t-lg">madamemelinapro@gmail.com</p>
        </div>
        <div style="margin-bottom: 3rem;">
          <div class="t-label" style="margin-bottom: 1rem;">ADRESSE</div>
          <p class="t-lg">Sur rendez-vous</p>
        </div>
      </div>
      <div style="background-color: var(--c-beige); padding: 4rem;">
        <h3 class="t-xxl" style="margin-bottom: 2rem;">VOTRE PROJET</h3>
        <form style="display:flex; flex-direction:column; gap: 2rem;">
          <input type="text" placeholder="NOM" style="background:transparent; border:none; border-bottom: 1px solid var(--c-noyer); padding: 1rem 0; font-family: var(--f-body); color: var(--c-noyer); outline:none;">
          <input type="tel" placeholder="TÉLÉPHONE / WHATSAPP" style="background:transparent; border:none; border-bottom: 1px solid var(--c-noyer); padding: 1rem 0; font-family: var(--f-body); color: var(--c-noyer); outline:none;">
          <input type="email" placeholder="EMAIL" style="background:transparent; border:none; border-bottom: 1px solid var(--c-noyer); padding: 1rem 0; font-family: var(--f-body); color: var(--c-noyer); outline:none;">
          <input type="text" placeholder="TYPE DE PROJET (Cuisine, Dressing...)" style="background:transparent; border:none; border-bottom: 1px solid var(--c-noyer); padding: 1rem 0; font-family: var(--f-body); color: var(--c-noyer); outline:none;">
          <textarea placeholder="MESSAGE" rows="4" style="background:transparent; border:none; border-bottom: 1px solid var(--c-noyer); padding: 1rem 0; font-family: var(--f-body); color: var(--c-noyer); outline:none; resize:none;"></textarea>
          <button type="button" class="btn btn-primary" style="align-self: flex-start; margin-top: 1rem;">ENVOYER MA DEMANDE</button>
        </form>
      </div>
    </div>
  </section>
""")

for name, content in pages.items():
    with open(name, 'w') as f:
        f.write(content)

with open('css/style.css', 'w') as f:
    f.write(css_content)

with open('js/main.js', 'w') as f:
    f.write(js_content)

print("V4 generation complete.")
