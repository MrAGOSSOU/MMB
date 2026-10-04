import os

css_content = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Manrope:wght@200;300;400;500&display=swap');

:root {
  /* Colors */
  --c-ivory: #F4F0E8;
  --c-beige: #D8C8B3;
  --c-bois: #B8946B;
  --c-noyer: #4A3024;
  --c-brun: #2B1C16;
  --c-charbon: #181513;
  --c-charbon-dark: #110e0c;
  --c-bronze: #A98B63;

  /* Typography */
  --f-heading: 'Cormorant Garamond', serif;
  --f-body: 'Manrope', sans-serif;

  /* Spacing */
  --space-xs: clamp(1rem, 2vw, 1.5rem);
  --space-sm: clamp(2rem, 4vw, 3rem);
  --space-md: clamp(4rem, 8vw, 6rem);
  --space-lg: clamp(8rem, 12vw, 12rem);
  --space-xl: clamp(12rem, 18vw, 18rem);
  
  /* Transitions */
  --t-slow: 1.2s cubic-bezier(0.2, 0.9, 0.3, 1);
  --t-med: 0.6s cubic-bezier(0.2, 0.9, 0.3, 1);
}

/* Reset & Global */
* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; font-size: 16px; background-color: var(--c-charbon); }
body {
  font-family: var(--f-body);
  background-color: var(--c-charbon);
  color: var(--c-ivory);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  line-height: 1.5;
  cursor: default;
}

/* Selection */
::selection { background-color: var(--c-bronze); color: var(--c-charbon); }

/* Custom Cursor */
.cursor-dot {
  width: 6px; height: 6px; background-color: var(--c-ivory);
  border-radius: 50%; position: fixed; pointer-events: none;
  transform: translate(-50%, -50%); z-index: 9999;
  transition: opacity 0.3s ease; mix-blend-mode: difference;
}
.cursor-ring {
  width: 44px; height: 44px; border: 1px solid rgba(244, 240, 232, 0.3);
  border-radius: 50%; position: fixed; pointer-events: none;
  transform: translate(-50%, -50%); z-index: 9998;
  transition: width 0.4s ease, height 0.4s ease, border-color 0.4s ease;
}
.cursor-hover .cursor-dot { opacity: 0; }
.cursor-hover .cursor-ring { width: 80px; height: 80px; border-color: var(--c-bronze); background-color: rgba(169, 139, 99, 0.05); backdrop-filter: blur(2px); }

/* Typography */
h1, h2, h3, h4, h5, h6 { font-family: var(--f-heading); font-weight: 300; line-height: 1.1; }
.t-display { font-size: clamp(4rem, 12vw, 12rem); letter-spacing: -0.02em; text-transform: uppercase; line-height: 0.9; }
.t-huge { font-size: clamp(3rem, 8vw, 8rem); letter-spacing: -0.01em; }
.t-xxl { font-size: clamp(2.5rem, 5vw, 5rem); }
.t-xl { font-size: clamp(1.8rem, 3.5vw, 3.5rem); }
.t-italic { font-style: italic; font-weight: 300; }
.t-body { font-size: clamp(1rem, 1.2vw, 1.3rem); font-weight: 300; color: rgba(244, 240, 232, 0.7); max-width: 500px; }
.t-body-lg { font-size: clamp(1.2rem, 2vw, 2rem); font-family: var(--f-heading); color: var(--c-ivory); max-width: 800px; line-height: 1.4; }
.t-label { font-family: var(--f-body); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.25em; font-weight: 400; color: rgba(244, 240, 232, 0.5); }

/* Layouts */
.container { width: 100%; max-width: 1600px; margin: 0 auto; padding: 0 5vw; }
section { padding: var(--space-lg) 0; position: relative; }
.section-xl { padding: var(--space-xl) 0; }
.section-sm { padding: var(--space-md) 0; }

.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-md); }
.grid-2-asym { display: grid; grid-template-columns: 3fr 5fr; gap: var(--space-lg); align-items: center; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-sm); }

/* Separators */
.line-v { width: 1px; height: 100px; background-color: rgba(244, 240, 232, 0.1); margin: 0 auto; }
.line-h { width: 100%; height: 1px; background-color: rgba(244, 240, 232, 0.1); }

/* Buttons & Links */
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 1.2rem 3rem; font-family: var(--f-body); font-size: 0.75rem;
  text-transform: uppercase; letter-spacing: 0.2em; text-decoration: none;
  transition: all var(--t-med); cursor: pointer; border: 1px solid rgba(244, 240, 232, 0.2);
  color: var(--c-ivory); position: relative; overflow: hidden;
}
.btn::before {
  content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
  background-color: var(--c-ivory); transform: translateY(100%); transition: transform var(--t-med); z-index: -1;
}
.btn:hover { color: var(--c-charbon); border-color: var(--c-ivory); }
.btn:hover::before { transform: translateY(0); }

.link-line {
  position: relative; text-decoration: none; color: inherit; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em; display: inline-block; padding-bottom: 5px;
}
.link-line::after {
  content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 1px;
  background-color: currentColor; transform: scaleX(0); transform-origin: right; transition: transform 0.6s cubic-bezier(0.19, 1, 0.22, 1);
}
.link-line:hover::after { transform: scaleX(1); transform-origin: left; }

/* Header */
.header {
  position: fixed; top: 0; left: 0; width: 100%; padding: 2.5rem 5vw; z-index: 1000;
  display: flex; justify-content: space-between; align-items: center; transition: all var(--t-med);
  mix-blend-mode: difference;
}
.header.scrolled { padding: 1.5rem 5vw; mix-blend-mode: normal; background-color: rgba(24, 21, 19, 0.8); backdrop-filter: blur(20px); border-bottom: 1px solid rgba(244, 240, 232, 0.05); }
.logo { font-family: var(--f-heading); font-size: 1.5rem; letter-spacing: 0.2em; text-transform: uppercase; text-decoration: none; color: #fff; }
.menu-toggle { font-family: var(--f-body); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.2em; cursor: pointer; color: #fff; border: none; background: none; }

/* Fullscreen Menu */
.menu-overlay {
  position: fixed; top: 0; left: 0; width: 100%; height: 100vh;
  background-color: var(--c-charbon-dark); z-index: 999;
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  clip-path: circle(0% at 100% 0%); transition: clip-path 1s cubic-bezier(0.7, 0, 0.3, 1);
}
.menu-overlay.active { clip-path: circle(150% at 100% 0%); }
.menu-links { display: flex; flex-direction: column; gap: 2rem; text-align: center; }
.menu-links a {
  font-family: var(--f-heading); font-size: clamp(3rem, 6vw, 5rem); text-decoration: none; color: var(--c-ivory);
  opacity: 0; transform: translateY(30px); transition: all 0.6s ease;
}
.menu-links a:hover { color: var(--c-bronze); font-style: italic; }
.menu-overlay.active .menu-links a { opacity: 1; transform: translateY(0); }
.menu-overlay.active .menu-links a:nth-child(1) { transition-delay: 0.3s; }
.menu-overlay.active .menu-links a:nth-child(2) { transition-delay: 0.4s; }
.menu-overlay.active .menu-links a:nth-child(3) { transition-delay: 0.5s; }
.menu-overlay.active .menu-links a:nth-child(4) { transition-delay: 0.6s; }
.menu-overlay.active .menu-links a:nth-child(5) { transition-delay: 0.7s; }
.menu-overlay.active .menu-links a:nth-child(6) { transition-delay: 0.8s; }

/* Hero Section */
.hero { height: 100vh; position: relative; display: flex; flex-direction: column; justify-content: flex-end; padding-bottom: 5vw; }
.hero-img-wrap { position: absolute; top: 0; left: 0; width: 100%; height: 100%; overflow: hidden; z-index: -1; }
.hero-img-wrap img { width: 100%; height: 100%; object-fit: cover; opacity: 0.6; transform: scale(1.1); transition: transform 20s ease-out; }
.hero.loaded .hero-img-wrap img { transform: scale(1); }
.hero-img-wrap::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 50%; background: linear-gradient(to top, var(--c-charbon) 0%, transparent 100%); }
.hero-content { position: relative; z-index: 2; display: flex; justify-content: space-between; align-items: flex-end; }
.hero-title-box { flex: 1; }
.hero-title-box .t-label { margin-bottom: 2rem; display: block; }
.hero-desc { width: 30%; text-align: right; }
.hero-desc p { margin-bottom: 2rem; margin-left: auto; }

/* Animations */
.anim-up { opacity: 0; transform: translateY(50px); transition: opacity var(--t-slow), transform var(--t-slow); }
.anim-up.in-view { opacity: 1; transform: translateY(0); }
.anim-delay-1 { transition-delay: 0.2s; }
.anim-delay-2 { transition-delay: 0.4s; }

.img-parallax { overflow: hidden; position: relative; }
.img-parallax img { width: 100%; height: 130%; object-fit: cover; position: relative; top: -15%; }

/* Editorial Image Layouts */
.ed-img-group { display: grid; grid-template-columns: 6fr 4fr; gap: var(--space-md); align-items: end; }
.ed-img-tall { aspect-ratio: 3/4; }
.ed-img-wide { aspect-ratio: 16/9; margin-bottom: 10%; }

/* Minimalist Services Accordion/List */
.service-items { border-top: 1px solid rgba(244, 240, 232, 0.1); margin-top: 5rem; }
.s-item {
  display: flex; justify-content: space-between; align-items: center;
  padding: 3rem 0; border-bottom: 1px solid rgba(244, 240, 232, 0.1);
  position: relative; cursor: pointer; group;
}
.s-num { font-family: var(--f-body); font-size: 0.8rem; color: rgba(244, 240, 232, 0.3); transition: color var(--t-med); }
.s-title { font-family: var(--f-heading); font-size: clamp(2rem, 4vw, 4rem); font-weight: 300; transition: transform var(--t-med), color var(--t-med); }
.s-item:hover .s-num { color: var(--c-bronze); }
.s-item:hover .s-title { transform: translateX(20px); font-style: italic; color: var(--c-ivory); }
.s-img {
  position: absolute; right: 20%; top: 50%; transform: translateY(-50%) scale(0.9);
  width: 300px; height: 400px; object-fit: cover; opacity: 0; pointer-events: none;
  transition: all var(--t-med); z-index: 10;
}
.s-item:hover .s-img { opacity: 1; transform: translateY(-50%) scale(1); right: 15%; }

/* Stats/Manifesto */
.manifesto-text { text-align: center; max-width: 1200px; margin: 0 auto; }
.manifesto-text p { font-family: var(--f-heading); font-size: clamp(2rem, 4.5vw, 4.5rem); font-weight: 300; line-height: 1.2; color: var(--c-ivory); }
.manifesto-text span { font-style: italic; color: rgba(244, 240, 232, 0.5); }

/* Projects Gallery (Asymmetric) */
.proj-grid { display: grid; grid-template-columns: repeat(12, 1fr); gap: 2rem; margin-top: 5rem; }
.proj-card { display: block; text-decoration: none; color: inherit; group; position: relative; }
.proj-img { overflow: hidden; margin-bottom: 1.5rem; }
.proj-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 1.5s cubic-bezier(0.2, 0.9, 0.3, 1); filter: grayscale(20%); }
.proj-card:hover .proj-img img { transform: scale(1.05); filter: grayscale(0%); }
.proj-info { display: flex; justify-content: space-between; align-items: flex-end; }
.proj-title { font-family: var(--f-heading); font-size: 1.8rem; font-weight: 300; }
.p1 { grid-column: 1 / 8; aspect-ratio: 16/9; }
.p2 { grid-column: 9 / 13; aspect-ratio: 3/4; margin-top: 20%; }
.p3 { grid-column: 2 / 7; aspect-ratio: 4/5; margin-top: -10%; }
.p4 { grid-column: 8 / 13; aspect-ratio: 16/9; }

/* Timeline Process */
.timeline { position: relative; margin-top: 5rem; padding-left: 20vw; }
.t-item { position: relative; padding: 4rem 0; border-bottom: 1px solid rgba(244, 240, 232, 0.1); display: grid; grid-template-columns: 1fr 2fr; gap: 4rem; }
.t-item::before {
  content: ''; position: absolute; left: -10vw; top: 0; width: 1px; height: 100%;
  background: rgba(244, 240, 232, 0.1);
}
.t-num-large { font-family: var(--f-heading); font-size: 4rem; color: rgba(244, 240, 232, 0.1); line-height: 1; transition: color var(--t-med); }
.t-item:hover .t-num-large { color: var(--c-bronze); font-style: italic; }

/* Big Footer CTA */
.footer-cta { text-align: center; padding: 10vw 0; border-bottom: 1px solid rgba(244, 240, 232, 0.1); }
.footer-cta .t-display { margin-bottom: 3rem; }

/* Footer */
.footer { padding: var(--space-md) 0 2rem; }
.f-grid { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 4rem; }
.f-col h4 { font-family: var(--f-body); font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.2em; color: rgba(244, 240, 232, 0.3); margin-bottom: 2rem; }
.f-links { display: flex; flex-direction: column; gap: 1rem; }
.f-links a { font-family: var(--f-body); font-size: 0.85rem; color: var(--c-ivory); text-decoration: none; opacity: 0.7; transition: opacity 0.3s; }
.f-links a:hover { opacity: 1; }
.f-bottom { display: flex; justify-content: space-between; align-items: center; margin-top: 5rem; padding-top: 2rem; border-top: 1px solid rgba(244, 240, 232, 0.1); font-size: 0.7rem; color: rgba(244, 240, 232, 0.3); text-transform: uppercase; letter-spacing: 0.1em; }

/* Responsive */
@media(max-width: 1024px) {
  .hero-desc { width: 50%; }
  .grid-2-asym { grid-template-columns: 1fr; }
  .timeline { padding-left: 0; }
  .t-item::before { display: none; }
  .p1, .p2, .p3, .p4 { grid-column: 1 / 13; aspect-ratio: 4/3; margin-top: 0; margin-bottom: 2rem; }
  .s-img { display: none; }
}
@media(max-width: 768px) {
  .cursor-dot, .cursor-ring { display: none; }
  body { cursor: auto; }
  .hero-content { flex-direction: column; align-items: flex-start; gap: 3rem; }
  .hero-desc { width: 100%; text-align: left; }
  .hero-desc p { margin-left: 0; }
  .f-grid { grid-template-columns: 1fr; }
  .t-item { grid-template-columns: 1fr; gap: 1rem; padding: 2rem 0; }
  .manifesto-text p { font-size: 2rem; }
}
"""

js_content = """
document.addEventListener('DOMContentLoaded', () => {
  // Custom Cursor
  const cursorDot = document.querySelector('.cursor-dot');
  const cursorRing = document.querySelector('.cursor-ring');
  
  if (window.innerWidth > 768 && cursorDot) {
    window.addEventListener('mousemove', (e) => {
      cursorDot.style.left = `${e.clientX}px`; cursorDot.style.top = `${e.clientY}px`;
      // Add slight delay for the ring to create a dragging effect
      setTimeout(() => {
        cursorRing.style.left = `${e.clientX}px`; cursorRing.style.top = `${e.clientY}px`;
      }, 50);
    });
    
    document.querySelectorAll('a, button, .s-item, .proj-card').forEach(el => {
      el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
      el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
    });
  }

  // Header Scroll
  const header = document.querySelector('.header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 100) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
  });

  // Fullscreen Menu
  const menuToggle = document.querySelector('.menu-toggle');
  const menuOverlay = document.querySelector('.menu-overlay');
  if(menuToggle) {
    menuToggle.addEventListener('click', () => {
      menuOverlay.classList.toggle('active');
      menuToggle.innerText = menuOverlay.classList.contains('active') ? 'FERMER' : 'MENU';
    });
  }

  // Scroll Animations
  const animElements = document.querySelectorAll('.anim-up');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  animElements.forEach(el => observer.observe(el));

  // Initial Load Animation
  setTimeout(() => {
    document.querySelector('.hero').classList.add('loaded');
  }, 100);

  // Simple Parallax Effect for Images
  const parallaxImages = document.querySelectorAll('.img-parallax img');
  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    parallaxImages.forEach(img => {
      const speed = 0.15;
      const yPos = -(scrolled * speed);
      img.style.transform = `translateY(${yPos}px)`;
    });
  });
});
"""

def layout(title, content):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | MMB — L'Excellence Sur Mesure</title>
  <meta name="description" content="Architecture d'intérieur et menuiserie premium au Bénin.">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div class="cursor-dot"></div>
  <div class="cursor-ring"></div>

  <header class="header">
    <a href="/" class="logo">MMB.</a>
    <button class="menu-toggle">MENU</button>
  </header>

  <div class="menu-overlay">
    <div class="menu-links">
      <a href="/">Accueil</a>
      <a href="/realisations.html">Réalisations</a>
      <a href="/services.html">Services</a>
      <a href="/processus.html">Processus</a>
      <a href="/a-propos.html">À Propos</a>
      <a href="/contact.html">Contact</a>
    </div>
  </div>

  <main>
    {content}
    
    <section class="footer-cta">
      <div class="container anim-up">
        <h2 class="t-display">VOUS AVEZ<br><span class="t-italic">un projet ?</span></h2>
        <a href="/contact.html" class="btn">Démarrer une conversation</a>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container f-grid">
      <div class="f-col">
        <a href="/" class="logo" style="font-size: 2rem;">MMB.</a>
        <p class="t-body" style="margin-top: 2rem; font-size: 0.9rem;">L'Excellence Sur Mesure.<br>Menuiserie haut de gamme et architecture d'intérieur.</p>
      </div>
      <div class="f-col">
        <h4>Navigation</h4>
        <div class="f-links">
          <a href="/realisations.html">Portfolio</a>
          <a href="/services.html">Expertise</a>
          <a href="/processus.html">Processus</a>
          <a href="/a-propos.html">L'Atelier</a>
          <a href="/contact.html">Contact</a>
        </div>
      </div>
      <div class="f-col">
        <h4>Contact</h4>
        <div class="f-links">
          <a href="tel:0167585650">01 67 58 56 50</a>
          <a href="tel:0197474958">01 97 47 49 58</a>
          <a href="mailto:madamemelinapro@gmail.com">madamemelinapro@gmail.com</a>
          <a href="https://wa.me/22967585650" target="_blank">WhatsApp</a>
          <a href="https://www.tiktok.com/@madame_melinaa" target="_blank">TikTok</a>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="f-bottom">
        <span>© 2026 MMB.</span>
        <span>Studio Design Premium</span>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>"""

pages = {}

pages["index.html"] = layout("Accueil", """
  <!-- HERO -->
  <section class="hero">
    <div class="hero-img-wrap"><img src="Image/IMG_9233.JPG" alt="Intérieur"></div>
    <div class="container hero-content">
      <div class="hero-title-box anim-up">
        <span class="t-label">Meilleure Menuiserie du Bénin</span>
        <h1 class="t-display">L'EXCELLENCE<br><span class="t-italic">sur mesure.</span></h1>
      </div>
      <div class="hero-desc anim-up anim-delay-1">
        <p class="t-body">Nous concevons des espaces et mobiliers pensés autour de vos dimensions, de votre style et de votre vision.</p>
        <a href="/contact.html" class="link-line">Demander un Devis</a>
      </div>
    </div>
  </section>

  <!-- MANIFESTO -->
  <section class="section-xl container">
    <div class="manifesto-text anim-up">
      <p>VOTRE ESPACE N'EST PAS STANDARD.<br><span>Votre mobilier ne devrait pas l'être non plus.</span></p>
      <div class="line-v" style="margin: 4rem auto;"></div>
      <p class="t-body" style="margin: 0 auto; text-align: center;">Depuis 2020, MMB imagine et réalise des aménagements intérieurs adaptés à chaque espace, chaque dimension et chaque style au Bénin.</p>
    </div>
  </section>

  <!-- L'ART DU SUR-MESURE -->
  <section class="section-xl container">
    <div class="grid-2-asym">
      <div class="anim-up">
        <span class="t-label">L'art du sur-mesure</span>
        <h2 class="t-xxl" style="margin: 2rem 0;">DIMENSIONS.<br><span class="t-italic">Matières.</span><br>FINITIONS.</h2>
        <p class="t-body" style="margin-bottom: 3rem;">Nous traitons le mobilier comme de l'architecture intérieure. Les lignes, les proportions, les textures : chaque détail est pensé pour créer une harmonie parfaite.</p>
        <a href="/a-propos.html" class="link-line">Découvrir l'atelier</a>
      </div>
      <div class="ed-img-group anim-up anim-delay-1">
        <div class="img-parallax ed-img-tall"><img src="Image/IMG_9256.JPG"></div>
        <div class="img-parallax ed-img-wide"><img src="Image/IMG_9285.JPG"></div>
      </div>
    </div>
  </section>

  <!-- SERVICES IMMERSIVE ACCORDION -->
  <section class="section-xl container">
    <div style="display:flex; justify-content: space-between; align-items: flex-end;" class="anim-up">
      <h2 class="t-xxl">NOS<br><span class="t-italic">Savoir-Faire.</span></h2>
      <a href="/services.html" class="link-line">Toutes nos expertises</a>
    </div>
    
    <div class="service-items anim-up anim-delay-1">
      <a href="/services.html" class="s-item">
        <span class="s-num">01</span>
        <h3 class="s-title">CUISINES</h3>
        <span class="t-label" style="opacity: 0.5;">Sur Mesure</span>
        <img src="Image/IMG_9233.JPG" class="s-img">
      </a>
      <a href="/services.html" class="s-item">
        <span class="s-num">02</span>
        <h3 class="s-title">DRESSINGS</h3>
        <span class="t-label" style="opacity: 0.5;">Rangements</span>
        <img src="Image/IMG_9257.JPG" class="s-img">
      </a>
      <a href="/services.html" class="s-item">
        <span class="s-num">03</span>
        <h3 class="s-title">MOBILIER</h3>
        <span class="t-label" style="opacity: 0.5;">Salons & TV</span>
        <img src="Image/IMG_9227.JPG" class="s-img">
      </a>
      <a href="/services.html" class="s-item">
        <span class="s-num">04</span>
        <h3 class="s-title">DÉCORATION</h3>
        <span class="t-label" style="opacity: 0.5;">Intérieurs</span>
        <img src="Image/IMG_9297.JPG" class="s-img">
      </a>
    </div>
  </section>

  <!-- PORTFOLIO PREVIEW -->
  <section class="section-xl container">
    <div class="anim-up" style="text-align: center; margin-bottom: 5rem;">
      <h2 class="t-xxl">DES ESPACES<br><span class="t-italic">Pensés pour vous.</span></h2>
    </div>
    
    <div class="proj-grid">
      <a href="/realisations.html" class="proj-card p1 anim-up">
        <div class="proj-img img-parallax"><img src="Image/IMG_9245.JPG"></div>
        <div class="proj-info">
          <span class="t-label">Cuisine</span>
          <h3 class="proj-title">L'Îlot Central</h3>
        </div>
      </a>
      <a href="/realisations.html" class="proj-card p2 anim-up anim-delay-1">
        <div class="proj-img img-parallax"><img src="Image/IMG_9273.JPG"></div>
        <div class="proj-info">
          <span class="t-label">Salon</span>
          <h3 class="proj-title">Mur Design</h3>
        </div>
      </a>
      <a href="/realisations.html" class="proj-card p3 anim-up">
        <div class="proj-img img-parallax"><img src="Image/IMG_9257.JPG"></div>
        <div class="proj-info">
          <span class="t-label">Chambre</span>
          <h3 class="proj-title">Dressing Suite</h3>
        </div>
      </a>
      <a href="/realisations.html" class="proj-card p4 anim-up anim-delay-1">
        <div class="proj-img img-parallax"><img src="Image/IMG_9227.JPG"></div>
        <div class="proj-info">
          <span class="t-label">Intérieur</span>
          <h3 class="proj-title">Espace à vivre</h3>
        </div>
      </a>
    </div>
    <div style="text-align: center; margin-top: 6rem;" class="anim-up">
      <a href="/realisations.html" class="btn">Voir toutes les réalisations</a>
    </div>
  </section>
""")

pages["realisations.html"] = layout("Réalisations", """
  <section class="section-xl container" style="padding-top: 15rem;">
    <h1 class="t-display anim-up">NOTRE<br><span class="t-italic">Portfolio.</span></h1>
    <div class="line-h" style="margin: 4rem 0;"></div>
    
    <div class="proj-grid">
      <div class="proj-card p1 anim-up">
        <div class="proj-img img-parallax"><img src="Image/IMG_9245.JPG"></div>
        <div class="proj-info"><span class="t-label">Cuisine</span><h3 class="proj-title">Cuisine Contemporaine</h3></div>
      </div>
      <div class="proj-card p2 anim-up anim-delay-1">
        <div class="proj-img img-parallax"><img src="Image/IMG_9273.JPG"></div>
        <div class="proj-info"><span class="t-label">Salon</span><h3 class="proj-title">Aménagement Mural</h3></div>
      </div>
      <div class="proj-card p3 anim-up">
        <div class="proj-img img-parallax"><img src="Image/IMG_9257.JPG"></div>
        <div class="proj-info"><span class="t-label">Dressing</span><h3 class="proj-title">Espace Rangement</h3></div>
      </div>
      <div class="proj-card p4 anim-up anim-delay-1">
        <div class="proj-img img-parallax"><img src="Image/IMG_9233.JPG"></div>
        <div class="proj-info"><span class="t-label">Cuisine</span><h3 class="proj-title">Design Sombre</h3></div>
      </div>
    </div>
  </section>
""")

pages["services.html"] = layout("Services", """
  <section class="section-xl container" style="padding-top: 15rem;">
    <h1 class="t-display anim-up">L'ART DE<br><span class="t-italic">l'aménagement.</span></h1>
    
    <div class="service-items anim-up anim-delay-1" style="margin-top: 10rem;">
      <div class="s-item" style="cursor: default; padding: 5rem 0;">
        <span class="s-num t-xxl" style="color:var(--c-bronze);">01</span>
        <div style="flex: 1; padding-left: 10vw;">
          <h3 class="t-xxl" style="margin-bottom: 2rem;">CUISINES SUR MESURE</h3>
          <p class="t-body-lg">Le cœur de la maison. Cuisines contemporaines, îlots centraux, rangements intégrés et finitions haut de gamme.</p>
        </div>
      </div>
      <div class="s-item" style="cursor: default; padding: 5rem 0;">
        <span class="s-num t-xxl" style="color:var(--c-bronze);">02</span>
        <div style="flex: 1; padding-left: 10vw;">
          <h3 class="t-xxl" style="margin-bottom: 2rem;">DRESSINGS & PLACARDS</h3>
          <p class="t-body-lg">L'optimisation absolue pour vos effets personnels, avec des penderies éclairées et une organisation parfaite.</p>
        </div>
      </div>
      <div class="s-item" style="cursor: default; padding: 5rem 0;">
        <span class="s-num t-xxl" style="color:var(--c-bronze);">03</span>
        <div style="flex: 1; padding-left: 10vw;">
          <h3 class="t-xxl" style="margin-bottom: 2rem;">SALONS & MEUBLES TV</h3>
          <p class="t-body-lg">Aménagement du salon, meubles TV suspendus, panneaux muraux en tasseaux et niches décoratives.</p>
        </div>
      </div>
      <div class="s-item" style="cursor: default; padding: 5rem 0;">
        <span class="s-num t-xxl" style="color:var(--c-bronze);">04</span>
        <div style="flex: 1; padding-left: 10vw;">
          <h3 class="t-xxl" style="margin-bottom: 2rem;">DÉCORATION INTÉRIEURE</h3>
          <p class="t-body-lg">Conseil, conception 3D et réalisation globale pour une harmonie parfaite de votre espace de vie.</p>
        </div>
      </div>
    </div>
  </section>
""")

pages["processus.html"] = layout("Processus", """
  <section class="section-xl container" style="padding-top: 15rem;">
    <h1 class="t-display anim-up">NOTRE<br><span class="t-italic">Méthode.</span></h1>
    
    <div class="timeline anim-up anim-delay-1">
      <div class="t-item">
        <div class="t-num-large">01</div>
        <div><h3 class="t-xl" style="margin-bottom: 1rem;">Prise de Contact</h3><p class="t-body-lg">Échangeons sur votre vision.</p></div>
      </div>
      <div class="t-item">
        <div class="t-num-large">02</div>
        <div><h3 class="t-xl" style="margin-bottom: 1rem;">Inspection du Site</h3><p class="t-body-lg">Analyse, cotes et lumière. <br><span class="t-label" style="color:var(--c-bronze); margin-top:1rem; display:block;">Inspection Payante</span></p></div>
      </div>
      <div class="t-item">
        <div class="t-num-large">03</div>
        <div><h3 class="t-xl" style="margin-bottom: 1rem;">Étude du Projet</h3><p class="t-body-lg">Plans, matériaux et 3D.</p></div>
      </div>
      <div class="t-item">
        <div class="t-num-large">04</div>
        <div><h3 class="t-xl" style="margin-bottom: 1rem;">Validation & Devis</h3><p class="t-body-lg">Validation finale. <br><span class="t-label" style="color:var(--c-bronze); margin-top:1rem; display:block;">Devis Gratuit</span></p></div>
      </div>
      <div class="t-item">
        <div class="t-num-large">05</div>
        <div><h3 class="t-xl" style="margin-bottom: 1rem;">Fabrication</h3><p class="t-body-lg">Réalisation artisanale précise.</p></div>
      </div>
      <div class="t-item">
        <div class="t-num-large">06</div>
        <div><h3 class="t-xl" style="margin-bottom: 1rem;">Installation</h3><p class="t-body-lg">Pose experte et minutieuse.</p></div>
      </div>
    </div>
  </section>
""")

pages["a-propos.html"] = layout("À Propos", """
  <section class="section-xl container" style="padding-top: 15rem;">
    <div class="grid-2-asym">
      <div class="anim-up">
        <h1 class="t-display" style="margin-bottom: 3rem;">L'ATELIER<br><span class="t-italic">MMB.</span></h1>
        <p class="t-body-lg" style="margin-bottom: 2rem;">Créée en 2020, Meilleure Menuiserie du Bénin refuse la standardisation.</p>
        <p class="t-body" style="margin-bottom: 2rem;">Nous sommes guidés par une passion pour le bois, l'aménagement de l'espace, et l'exigence des finitions internationales. Nous accompagnons nos clients dans la transformation de leurs espaces, en offrant un mobilier entièrement personnalisé qui allie esthétique contemporaine et durabilité.</p>
      </div>
      <div class="img-parallax ed-img-tall anim-up anim-delay-1"><img src="Image/IMG_9297.JPG"></div>
    </div>
  </section>
""")

pages["contact.html"] = layout("Contact", """
  <section class="section-xl container" style="padding-top: 15rem;">
    <div class="grid-2-asym">
      <div class="anim-up">
        <h1 class="t-display" style="margin-bottom: 4rem;">CONTACT.</h1>
        <div style="margin-bottom: 3rem;">
          <h4 class="t-label" style="margin-bottom: 1rem;">APPEL & WHATSAPP</h4>
          <p class="t-xl t-italic">01 67 58 56 50<br>01 97 47 49 58</p>
        </div>
        <div style="margin-bottom: 3rem;">
          <h4 class="t-label" style="margin-bottom: 1rem;">EMAIL</h4>
          <p class="t-xl t-italic">madamemelinapro@gmail.com</p>
        </div>
      </div>
      <div class="anim-up anim-delay-1" style="border: 1px solid rgba(244, 240, 232, 0.1); padding: 5vw;">
        <h3 class="t-xxl" style="margin-bottom: 3rem;">VOTRE PROJET</h3>
        <form style="display:flex; flex-direction:column; gap: 3rem;">
          <input type="text" placeholder="NOM COMPLET" style="background:transparent; border:none; border-bottom: 1px solid rgba(244,240,232,0.3); padding: 1rem 0; font-family:var(--f-body); font-size:0.8rem; letter-spacing:0.1em; color:var(--c-ivory); outline:none;">
          <input type="tel" placeholder="TÉLÉPHONE / WHATSAPP" style="background:transparent; border:none; border-bottom: 1px solid rgba(244,240,232,0.3); padding: 1rem 0; font-family:var(--f-body); font-size:0.8rem; letter-spacing:0.1em; color:var(--c-ivory); outline:none;">
          <textarea placeholder="PARLEZ-NOUS DE VOTRE ESPACE..." rows="4" style="background:transparent; border:none; border-bottom: 1px solid rgba(244,240,232,0.3); padding: 1rem 0; font-family:var(--f-body); font-size:0.8rem; letter-spacing:0.1em; color:var(--c-ivory); outline:none; resize:none;"></textarea>
          <button type="button" class="btn" style="align-self: flex-start; margin-top: 1rem;">ENVOYER LA DEMANDE</button>
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

print("V5 Ultra-Premium generation complete.")
