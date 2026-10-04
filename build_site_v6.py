import os

css_content = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Inter:wght@300;400;500;600&display=swap');

:root {
  /* Colors */
  --c-espresso: #191817;
  --c-brun-fonce: #3A2B22;
  --c-walnut: #634B3B;
  --c-bois-chaud: #876A50;
  --c-beige: #CDB99F;
  --c-ivoire: #F3EEE7;
  --c-blanc: #FAF8F4;
  --c-olive: #68705A;
  
  --bg-dark: var(--c-espresso);
  --text-light: var(--c-blanc);
  --text-dark: var(--c-espresso);
  --accent: var(--c-bois-chaud);

  /* Typography */
  --f-heading: 'Cormorant Garamond', serif;
  --f-body: 'Inter', sans-serif;

  /* Layout */
  --px: 5vw;
  --section-py: 10vw;
  --ease: cubic-bezier(0.19, 1, 0.22, 1);
  --ease-out: cubic-bezier(0.215, 0.610, 0.355, 1.000);
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  padding: 0;
  background-color: var(--bg-dark);
  color: var(--text-light);
  font-family: var(--f-body);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}

::selection {
  background: var(--c-bois-chaud);
  color: var(--c-blanc);
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

a {
  text-decoration: none;
  color: inherit;
}

/* Typography Utility */
.t-display {
  font-family: var(--f-heading);
  font-size: clamp(3rem, 8vw, 8rem);
  line-height: 0.9;
  font-weight: 300;
  letter-spacing: -0.02em;
  margin: 0;
}

.t-h2 {
  font-family: var(--f-heading);
  font-size: clamp(2.5rem, 5vw, 5rem);
  line-height: 1;
  font-weight: 400;
  margin: 0;
}

.t-h3 {
  font-family: var(--f-heading);
  font-size: clamp(1.5rem, 3vw, 2.5rem);
  line-height: 1.2;
  font-weight: 400;
}

.t-body {
  font-size: clamp(1rem, 1.2vw, 1.2rem);
  line-height: 1.6;
  font-weight: 300;
  color: rgba(250, 248, 244, 0.8);
}

.t-body-large {
  font-size: clamp(1.2rem, 2vw, 2rem);
  line-height: 1.4;
  font-weight: 300;
  font-family: var(--f-body);
}

.t-label {
  font-family: var(--f-body);
  font-size: 0.75rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  font-weight: 500;
}

.t-italic {
  font-style: italic;
  font-weight: 300;
}

/* Spacing */
.container {
  padding-left: var(--px);
  padding-right: var(--px);
}

.section {
  padding-top: var(--section-py);
  padding-bottom: var(--section-py);
}

.light-theme {
  background-color: var(--c-ivoire);
  color: var(--c-espresso);
}
.light-theme .t-body {
  color: rgba(25, 24, 23, 0.8);
}

/* Navbar */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 1.5rem var(--px);
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 100;
  transition: background 0.5s var(--ease), padding 0.5s var(--ease), border 0.5s var(--ease);
  box-sizing: border-box;
}

.navbar.scrolled {
  background: rgba(25, 24, 23, 0.75);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  padding: 1rem var(--px);
  border-bottom: 1px solid rgba(250, 248, 244, 0.1);
}

.logo-wrap {
  position: relative;
  width: 120px;
}
.logo-wrap img {
  width: 100%;
  height: auto;
  filter: brightness(0) invert(1);
}
.navbar.scrolled.light-nav .logo-wrap img {
  filter: brightness(0);
}

.nav-links {
  display: flex;
  gap: 2.5rem;
  align-items: center;
}

.nav-link {
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  position: relative;
  overflow: hidden;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 1px;
  background: currentColor;
  transform: scaleX(0);
  transform-origin: right;
  transition: transform 0.4s var(--ease-out);
}
.nav-link:hover::after {
  transform: scaleX(1);
  transform-origin: left;
}

.nav-cta {
  border: 1px solid rgba(250, 248, 244, 0.3);
  padding: 0.75rem 1.5rem;
  border-radius: 100px;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  transition: all 0.4s var(--ease);
}
.nav-cta:hover {
  background: var(--c-blanc);
  color: var(--c-espresso);
}

.menu-toggle {
  display: none;
  background: none;
  border: none;
  color: inherit;
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
}

/* Mobile Menu */
.mobile-menu {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background: var(--c-espresso);
  z-index: 99;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  transform: translateY(-100%);
  transition: transform 0.8s var(--ease);
}
.mobile-menu.open {
  transform: translateY(0);
}
.mobile-menu .nav-link {
  font-size: 2rem;
  font-family: var(--f-heading);
  text-transform: none;
}

/* Buttons */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: var(--c-blanc);
  color: var(--c-espresso);
  padding: 1rem 2rem;
  border-radius: 100px;
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-weight: 500;
  transition: all 0.4s var(--ease);
  position: relative;
  overflow: hidden;
}
.btn-primary:hover {
  background: var(--c-bois-chaud);
  color: var(--c-blanc);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(250, 248, 244, 0.3);
  color: var(--c-blanc);
  padding: 1rem 2rem;
  border-radius: 100px;
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  transition: all 0.4s var(--ease);
}
.btn-secondary:hover {
  border-color: var(--c-blanc);
  background: rgba(250, 248, 244, 0.1);
}

/* Hero Section */
.hero {
  height: 100vh;
  width: 100%;
  position: relative;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 120%;
  object-fit: cover;
  z-index: -2;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, rgba(25,24,23,0.9) 0%, rgba(25,24,23,0.4) 50%, rgba(25,24,23,0.1) 100%);
  z-index: -1;
}

.hero-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100%;
  margin-top: 5rem;
}

.hero-left {
  max-width: 800px;
}

.hero-label {
  margin-bottom: 2rem;
  display: inline-block;
  opacity: 0.8;
}

.hero-desc {
  margin-top: 2rem;
  max-width: 450px;
  margin-bottom: 3rem;
}

.hero-ctas {
  display: flex;
  gap: 1rem;
}

.hero-right {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.glass-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 2.5rem;
  border-radius: 1rem;
  max-width: 300px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}
.glass-item {
  margin-bottom: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.glass-item:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}
.glass-item-title {
  font-family: var(--f-heading);
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}
.glass-item-desc {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.7);
}

.scroll-indicator {
  position: absolute;
  bottom: 3rem;
  left: var(--px);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  opacity: 0.6;
}
.scroll-line {
  width: 1px;
  height: 60px;
  background: rgba(255,255,255,0.3);
  position: relative;
  overflow: hidden;
}
.scroll-line::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: #fff;
  animation: scrollAnim 2s infinite ease-in-out;
}
@keyframes scrollAnim {
  0% { transform: translateY(-100%); }
  100% { transform: translateY(200%); }
}

/* Manifest / Vision */
.vision-section {
  text-align: center;
  max-width: 900px;
  margin: 0 auto;
}
.vision-text {
  margin-top: 3rem;
  margin-bottom: 3rem;
}
.vision-divider {
  width: 1px;
  height: 100px;
  background: rgba(25, 24, 23, 0.2);
  margin: 0 auto;
}

/* Services */
.services-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 5rem;
  border-bottom: 1px solid rgba(25, 24, 23, 0.1);
  padding-bottom: 2rem;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
}

.service-card {
  position: relative;
  display: block;
  padding-top: 100%;
  overflow: hidden;
  border-radius: 0.5rem;
  background: var(--c-espresso);
}
.service-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.6;
  transition: transform 0.8s var(--ease), opacity 0.8s var(--ease);
}
.service-content {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  z-index: 2;
  color: var(--c-blanc);
}
.service-num {
  font-family: var(--f-body);
  font-size: 0.8rem;
  opacity: 0.7;
}
.service-title {
  font-family: var(--f-heading);
  font-size: 2rem;
  margin: 0;
  transform: translateY(10px);
  transition: transform 0.6s var(--ease);
}
.service-arrow {
  width: 24px;
  height: 24px;
  border: 1px solid rgba(255,255,255,0.3);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  align-self: flex-end;
  opacity: 0;
  transform: translate(-10px, 10px);
  transition: all 0.6s var(--ease);
}
.service-card:hover .service-img {
  transform: scale(1.05);
  opacity: 0.4;
}
.service-card:hover .service-title {
  transform: translateY(0);
}
.service-card:hover .service-arrow {
  opacity: 1;
  transform: translate(0, 0);
}

/* Savoir-Faire */
.savoir-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5vw;
  align-items: center;
}
.savoir-img-wrap {
  position: relative;
  border-radius: 1rem;
  overflow: hidden;
}
.savoir-img {
  width: 100%;
  height: 130%;
  object-fit: cover;
  position: relative;
  top: -15%;
}
.savoir-list {
  display: flex;
  flex-direction: column;
  gap: 3rem;
  margin-top: 4rem;
}
.savoir-item {
  display: grid;
  grid-template-columns: 50px 1fr;
  gap: 2rem;
  border-top: 1px solid rgba(250, 248, 244, 0.1);
  padding-top: 2rem;
}
.savoir-num {
  font-family: var(--f-heading);
  font-size: 1.5rem;
  color: var(--c-bois-chaud);
}

/* Portfolio */
.portfolio-filters {
  display: flex;
  gap: 2rem;
  margin-bottom: 4rem;
  flex-wrap: wrap;
}
.filter-btn {
  background: none;
  border: none;
  color: rgba(25, 24, 23, 0.5);
  font-family: var(--f-body);
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
  transition: color 0.3s ease;
  padding: 0;
}
.filter-btn.active, .filter-btn:hover {
  color: var(--c-espresso);
}

.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 2rem;
}
.port-card {
  position: relative;
  border-radius: 0.5rem;
  overflow: hidden;
  display: block;
  background: var(--c-espresso);
}
.port-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 1s var(--ease), opacity 0.5s ease;
}
.port-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(25,24,23, 0.6);
  opacity: 0;
  transition: opacity 0.5s ease;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--c-blanc);
  text-align: center;
}
.port-card:hover img {
  transform: scale(1.03);
}
.port-card:hover .port-overlay {
  opacity: 1;
}

/* Chiffres */
.chiffres-section {
  background: var(--c-brun-fonce);
  color: var(--c-blanc);
  text-align: center;
}
.chiffres-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
}
.chiffre-item h4 {
  font-family: var(--f-heading);
  font-size: clamp(3rem, 6vw, 6rem);
  font-weight: 300;
  margin: 0 0 1rem 0;
  color: var(--c-beige);
}

/* Pourquoi Nous */
.pourquoi-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5vw;
}
.pourquoi-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 3rem;
}
.pourquoi-item {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  font-size: 1.2rem;
  padding: 1.5rem 0;
  border-bottom: 1px solid rgba(250,248,244,0.1);
}
.pourquoi-item span {
  font-family: var(--f-body);
  font-size: 0.8rem;
  color: var(--c-bois-chaud);
}

/* Processus */
.timeline {
  max-width: 800px;
  margin: 4rem auto 0;
  position: relative;
}
.timeline-line {
  position: absolute;
  top: 0;
  left: 20px;
  width: 1px;
  height: 100%;
  background: rgba(25,24,23,0.1);
}
.timeline-progress {
  position: absolute;
  top: 0;
  left: 20px;
  width: 1px;
  height: 0%;
  background: var(--c-espresso);
  transition: height 0.5s ease;
}
.timeline-item {
  position: relative;
  padding-left: 60px;
  margin-bottom: 4rem;
}
.timeline-dot {
  position: absolute;
  top: 5px;
  left: 16px;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--c-bois-chaud);
}
.timeline-item h4 {
  font-family: var(--f-heading);
  font-size: 1.8rem;
  margin: 0 0 0.5rem 0;
}

/* Immersion CTA */
.cta-immersive {
  position: relative;
  padding: 15vw 5vw;
  text-align: center;
  color: var(--c-blanc);
  overflow: hidden;
}
.cta-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 120%;
  object-fit: cover;
  z-index: -2;
}
.cta-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(25,24,23, 0.7);
  z-index: -1;
}

/* FAQ */
.faq-wrap {
  max-width: 800px;
  margin: 4rem auto 0;
}
.faq-item {
  border-bottom: 1px solid rgba(25,24,23,0.1);
}
.faq-q {
  padding: 2rem 0;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--f-heading);
  font-size: 1.5rem;
}
.faq-a {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.5s var(--ease);
}
.faq-a p {
  padding-bottom: 2rem;
  margin: 0;
  color: rgba(25,24,23,0.8);
}
.faq-icon {
  width: 20px;
  height: 20px;
  position: relative;
}
.faq-icon::before, .faq-icon::after {
  content: '';
  position: absolute;
  background: var(--c-espresso);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: transform 0.3s ease;
}
.faq-icon::before { width: 100%; height: 1px; }
.faq-icon::after { height: 100%; width: 1px; }
.faq-item.active .faq-icon::after { transform: translate(-50%, -50%) rotate(90deg); }
.faq-item.active .faq-a { max-height: 500px; }

/* Contact */
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5vw;
}
.contact-info {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
.contact-form {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(250,248,244,0.1);
  padding: 3rem;
  border-radius: 1rem;
}
.input-group {
  margin-bottom: 2rem;
}
.input-group input, .input-group textarea {
  width: 100%;
  background: transparent;
  border: none;
  border-bottom: 1px solid rgba(250,248,244,0.3);
  padding: 1rem 0;
  color: var(--c-blanc);
  font-family: var(--f-body);
  font-size: 1rem;
  outline: none;
  transition: border-color 0.3s ease;
}
.input-group input:focus, .input-group textarea:focus {
  border-color: var(--c-bois-chaud);
}

/* Footer */
.footer {
  background: var(--c-charbon-dark);
  padding: 5rem var(--px) 2rem;
}
.f-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 4rem;
  padding-bottom: 4rem;
  border-bottom: 1px solid rgba(250,248,244,0.1);
}
.f-links {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.f-links a {
  opacity: 0.7;
  transition: opacity 0.3s ease;
  font-size: 0.9rem;
}
.f-links a:hover {
  opacity: 1;
}
.f-bottom {
  display: flex;
  justify-content: space-between;
  padding-top: 2rem;
  font-size: 0.8rem;
  opacity: 0.5;
}

/* Animations Reveal */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: all 1s var(--ease-out);
}
.reveal.active {
  opacity: 1;
  transform: translateY(0);
}

/* Responsive */
@media (max-width: 1024px) {
  .hero-content {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 4rem;
  }
  .hero-left { margin: 0 auto; }
  .hero-right { justify-content: center; }
  .services-grid { grid-template-columns: repeat(2, 1fr); }
  .savoir-grid, .pourquoi-grid, .contact-grid { grid-template-columns: 1fr; }
  .f-grid { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 768px) {
  :root {
    --section-py: 15vw;
  }
  .nav-links, .nav-cta { display: none; }
  .menu-toggle { display: block; }
  .chiffres-grid { grid-template-columns: 1fr 1fr; }
  .f-grid { grid-template-columns: 1fr; }
  .hero-ctas { flex-direction: column; }
  .btn-primary, .btn-secondary { width: 100%; }
}
"""

js_content = """
// Smooth Scroll & Lenis Setup
// For the sake of simplicity without external dependencies, we implement basic smooth scroll and observers.
// In a real env, import Lenis.

document.addEventListener("DOMContentLoaded", () => {
  // Mobile Menu
  const menuToggle = document.querySelector('.menu-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');
  
  if(menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
      menuToggle.textContent = mobileMenu.classList.contains('open') ? 'FERMER' : 'MENU';
    });
  }

  // Navbar background on scroll
  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', () => {
    if(window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  // Reveal Animations
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        obs.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.reveal').forEach(el => {
    observer.observe(el);
  });

  // Parallax Images
  const pImages = document.querySelectorAll('.parallax-img');
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    pImages.forEach(img => {
      const speed = img.getAttribute('data-speed') || 0.1;
      img.style.transform = `translateY(${y * speed}px)`;
    });
  });

  // Timeline Progress
  const timeline = document.querySelector('.timeline');
  const progress = document.querySelector('.timeline-progress');
  if(timeline && progress) {
    window.addEventListener('scroll', () => {
      const rect = timeline.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      if(rect.top < windowHeight && rect.bottom > 0) {
        let percentage = (windowHeight - rect.top) / (rect.height + windowHeight) * 100;
        percentage = Math.max(0, Math.min(100, percentage));
        progress.style.height = `${percentage}%`;
      }
    });
  }

  // FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const q = item.querySelector('.faq-q');
    q.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      faqItems.forEach(i => i.classList.remove('active'));
      if(!isActive) item.classList.add('active');
    });
  });
});
"""

html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meilleure Menuiserie du Bénin | Ameublement & Design Intérieur Sur Mesure</title>
  <meta name="description" content="Meilleure Menuiserie du Bénin conçoit et réalise vos meubles, cuisines, dressings et aménagements intérieurs sur mesure avec des matériaux de qualité.">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <nav class="navbar">
    <a href="#" class="logo-wrap">
      <img src="Image/logo.png" alt="MMB Logo">
    </a>
    <div class="nav-links">
      <a href="#services" class="nav-link">Services</a>
      <a href="#realisations" class="nav-link">Réalisations</a>
      <a href="#processus" class="nav-link">Notre Processus</a>
      <a href="#a-propos" class="nav-link">À Propos</a>
      <a href="#faq" class="nav-link">FAQ</a>
    </div>
    <a href="#contact" class="nav-cta">Demander un devis</a>
    <button class="menu-toggle">MENU</button>
  </nav>

  <div class="mobile-menu">
    <a href="#services" class="nav-link">Services</a>
    <a href="#realisations" class="nav-link">Réalisations</a>
    <a href="#processus" class="nav-link">Processus</a>
    <a href="#a-propos" class="nav-link">À Propos</a>
    <a href="#faq" class="nav-link">FAQ</a>
    <a href="#contact" class="nav-link">Contact</a>
  </div>

  <main>
    <!-- HERO -->
    <section class="hero">
      <img src="Image/IMG_9233.JPG" alt="Intérieur contemporain" class="hero-bg parallax-img" data-speed="0.3">
      <div class="hero-overlay"></div>
      
      <div class="container hero-content">
        <div class="hero-left reveal">
          <span class="t-label hero-label">MENUISERIE & DESIGN INTÉRIEUR — BÉNIN</span>
          <h1 class="t-display">L'EXCELLENCE<br><span class="t-italic">sur mesure.</span></h1>
          <p class="t-body hero-desc">Nous concevons et réalisons des meubles et aménagements intérieurs sur mesure, pensés pour votre espace, votre style et les réalités du climat béninois.</p>
          <div class="hero-ctas">
            <a href="#contact" class="btn-primary">Parler de mon projet</a>
            <a href="#realisations" class="btn-secondary">Voir nos réalisations</a>
          </div>
        </div>
        
        <div class="hero-right reveal" style="transition-delay: 0.2s;">
          <div class="glass-card">
            <div class="glass-item">
              <div class="glass-item-title">Depuis 2020</div>
              <div class="glass-item-desc">Expertise reconnue</div>
            </div>
            <div class="glass-item">
              <div class="glass-item-title">Sur mesure</div>
              <div class="glass-item-desc">Conception personnalisée</div>
            </div>
            <div class="glass-item">
              <div class="glass-item-title">Haute qualité</div>
              <div class="glass-item-desc">Matériaux premium</div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="scroll-indicator">
        <span class="t-label">Scroll to explore</span>
        <div class="scroll-line"></div>
      </div>
    </section>

    <!-- INTRO -->
    <section class="section light-theme">
      <div class="container vision-section reveal">
        <span class="t-label">Notre Vision</span>
        <h2 class="t-h2 vision-text">Nous transformons les espaces en intérieurs qui vous ressemblent.</h2>
        <div class="vision-divider"></div>
        <p class="t-body-large" style="margin-top: 3rem;">Chez Meilleure Menuiserie du Bénin, chaque réalisation est pensée comme une pièce unique. Nous associons design contemporain, fabrication sur mesure et matériaux de qualité pour créer des espaces élégants, fonctionnels et durables.</p>
      </div>
    </section>

    <!-- SERVICES -->
    <section id="services" class="section container">
      <div class="services-header reveal">
        <h2 class="t-display">Des espaces pensés<br>dans les <span class="t-italic">moindres détails.</span></h2>
      </div>
      
      <div class="services-grid">
        <a href="#contact" class="service-card reveal">
          <img src="Image/IMG_9245.JPG" class="service-img">
          <div class="service-content">
            <span class="service-num">01 — CUISINES SUR MESURE</span>
            <div style="display:flex; justify-content:space-between; align-items:flex-end;">
              <h3 class="service-title">Cuisines</h3>
              <div class="service-arrow">→</div>
            </div>
          </div>
        </a>
        <a href="#contact" class="service-card reveal" style="transition-delay: 0.1s;">
          <img src="Image/IMG_9257.JPG" class="service-img">
          <div class="service-content">
            <span class="service-num">02 — DRESSINGS</span>
            <div style="display:flex; justify-content:space-between; align-items:flex-end;">
              <h3 class="service-title">Dressings</h3>
              <div class="service-arrow">→</div>
            </div>
          </div>
        </a>
        <a href="#contact" class="service-card reveal" style="transition-delay: 0.2s;">
          <img src="Image/IMG_9227.JPG" class="service-img">
          <div class="service-content">
            <span class="service-num">03 — PLACARDS & RANGEMENTS</span>
            <div style="display:flex; justify-content:space-between; align-items:flex-end;">
              <h3 class="service-title">Rangements</h3>
              <div class="service-arrow">→</div>
            </div>
          </div>
        </a>
        <a href="#contact" class="service-card reveal" style="transition-delay: 0.3s;">
          <img src="Image/IMG_9273.JPG" class="service-img">
          <div class="service-content">
            <span class="service-num">04 — MEUBLES TV</span>
            <div style="display:flex; justify-content:space-between; align-items:flex-end;">
              <h3 class="service-title">Salons</h3>
              <div class="service-arrow">→</div>
            </div>
          </div>
        </a>
        <a href="#contact" class="service-card reveal">
          <img src="Image/IMG_9285.JPG" class="service-img">
          <div class="service-content">
            <span class="service-num">05 — AMÉNAGEMENT DE SALON</span>
            <div style="display:flex; justify-content:space-between; align-items:flex-end;">
              <h3 class="service-title">Intérieurs</h3>
              <div class="service-arrow">→</div>
            </div>
          </div>
        </a>
        <a href="#contact" class="service-card reveal" style="transition-delay: 0.1s;">
          <img src="Image/IMG_9297.JPG" class="service-img">
          <div class="service-content">
            <span class="service-num">06 — AMÉNAGEMENT DE CHAMBRES</span>
            <div style="display:flex; justify-content:space-between; align-items:flex-end;">
              <h3 class="service-title">Chambres</h3>
              <div class="service-arrow">→</div>
            </div>
          </div>
        </a>
        <a href="#contact" class="service-card reveal" style="transition-delay: 0.2s;">
          <img src="Image/IMG_9256.JPG" class="service-img">
          <div class="service-content">
            <span class="service-num">07 — MOBILIER DE BUREAU</span>
            <div style="display:flex; justify-content:space-between; align-items:flex-end;">
              <h3 class="service-title">Bureaux</h3>
              <div class="service-arrow">→</div>
            </div>
          </div>
        </a>
        <a href="#contact" class="service-card reveal" style="transition-delay: 0.3s;">
          <img src="Image/IMG_9233.JPG" class="service-img">
          <div class="service-content">
            <span class="service-num">08 — DÉCORATION INTÉRIEURE</span>
            <div style="display:flex; justify-content:space-between; align-items:flex-end;">
              <h3 class="service-title">Décoration</h3>
              <div class="service-arrow">→</div>
            </div>
          </div>
        </a>
      </div>
    </section>

    <!-- SAVOIR-FAIRE -->
    <section id="a-propos" class="section light-theme container">
      <div class="savoir-grid">
        <div class="savoir-content reveal">
          <h2 class="t-display" style="margin-bottom: 2rem;">Le sur-mesure n'est pas une option.<br><span class="t-italic">C'est notre standard.</span></h2>
          
          <div class="savoir-list">
            <div class="savoir-item">
              <div class="savoir-num">01</div>
              <div>
                <h4 class="t-h3" style="margin: 0 0 1rem;">Conception Personnalisée</h4>
                <p class="t-body">Chaque projet est pensé selon les dimensions, les contraintes et le style du client.</p>
              </div>
            </div>
            <div class="savoir-item">
              <div class="savoir-num">02</div>
              <div>
                <h4 class="t-h3" style="margin: 0 0 1rem;">Matériaux de Qualité</h4>
                <p class="t-body">Utilisation de matériaux modernes et de qualité, adaptés aux réalités du climat béninois.</p>
              </div>
            </div>
            <div class="savoir-item">
              <div class="savoir-num">03</div>
              <div>
                <h4 class="t-h3" style="margin: 0 0 1rem;">Finitions & Précision</h4>
                <p class="t-body">Une attention particulière portée aux dimensions, aux assemblages et aux finitions.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="savoir-img-wrap reveal" style="transition-delay: 0.2s; height: 800px;">
          <img src="Image/IMG_9233.JPG" class="savoir-img parallax-img" data-speed="0.1">
        </div>
      </div>
    </section>

    <!-- REALISATIONS -->
    <section id="realisations" class="section container">
      <div class="reveal">
        <h2 class="t-display">Nos réalisations</h2>
        <p class="t-body-large" style="margin-bottom: 3rem; color: var(--c-bois-chaud);">Des projets uniques. Des espaces qui ont leur propre identité.</p>
      </div>

      <div class="portfolio-filters reveal">
        <button class="filter-btn active">TOUT</button>
        <button class="filter-btn">CUISINES</button>
        <button class="filter-btn">DRESSINGS</button>
        <button class="filter-btn">SALONS</button>
        <button class="filter-btn">CHAMBRES</button>
        <button class="filter-btn">BUREAUX</button>
      </div>

      <div class="portfolio-grid">
        <a href="#contact" class="port-card reveal" style="grid-column: span 8; height: 600px;">
          <img src="Image/IMG_9245.JPG">
          <div class="port-overlay">
            <span class="t-label">Cuisine</span>
            <h3 class="t-h3" style="margin: 0.5rem 0 1rem;">Cuisine contemporaine</h3>
            <div class="service-arrow" style="opacity:1; transform:none; border-color:white;">→</div>
          </div>
        </a>
        <a href="#contact" class="port-card reveal" style="transition-delay: 0.1s; grid-column: span 4; height: 600px;">
          <img src="Image/IMG_9257.JPG">
          <div class="port-overlay">
            <span class="t-label">Dressing</span>
            <h3 class="t-h3" style="margin: 0.5rem 0 1rem;">Dressing sur mesure</h3>
            <div class="service-arrow" style="opacity:1; transform:none; border-color:white;">→</div>
          </div>
        </a>
        <a href="#contact" class="port-card reveal" style="grid-column: span 5; height: 500px;">
          <img src="Image/IMG_9273.JPG">
          <div class="port-overlay">
            <span class="t-label">Salon</span>
            <h3 class="t-h3" style="margin: 0.5rem 0 1rem;">Salon moderne</h3>
            <div class="service-arrow" style="opacity:1; transform:none; border-color:white;">→</div>
          </div>
        </a>
        <a href="#contact" class="port-card reveal" style="transition-delay: 0.1s; grid-column: span 7; height: 500px;">
          <img src="Image/IMG_9285.JPG">
          <div class="port-overlay">
            <span class="t-label">Intérieur</span>
            <h3 class="t-h3" style="margin: 0.5rem 0 1rem;">Aménagement intérieur</h3>
            <div class="service-arrow" style="opacity:1; transform:none; border-color:white;">→</div>
          </div>
        </a>
      </div>
    </section>

    <!-- CHIFFRES -->
    <section class="section chiffres-section">
      <div class="container chiffres-grid reveal">
        <div class="chiffre-item">
          <h4>2020</h4>
          <span class="t-label">ANNÉE DE CRÉATION</span>
        </div>
        <div class="chiffre-item">
          <h4>100%</h4>
          <span class="t-label">SUR MESURE</span>
        </div>
        <div class="chiffre-item">
          <h4>360°</h4>
          <span class="t-label">ACCOMPAGNEMENT</span>
        </div>
        <div class="chiffre-item">
          <h4>∞</h4>
          <span class="t-label">GARANTIE</span>
        </div>
      </div>
    </section>

    <!-- POURQUOI NOUS -->
    <section class="section container">
      <div class="pourquoi-grid">
        <div class="reveal">
          <h2 class="t-h2">Pourquoi Meilleure Menuiserie du Bénin ?</h2>
          <div class="pourquoi-list">
            <div class="pourquoi-item">
              <span>01</span>
              <div>FABRICATION SUR MESURE</div>
            </div>
            <div class="pourquoi-item">
              <span>02</span>
              <div>MATÉRIAUX DE QUALITÉ</div>
            </div>
            <div class="pourquoi-item">
              <span>03</span>
              <div>ACCOMPAGNEMENT PERSONNALISÉ</div>
            </div>
            <div class="pourquoi-item">
              <span>04</span>
              <div>INSTALLATION PROFESSIONNELLE</div>
            </div>
            <div class="pourquoi-item">
              <span>05</span>
              <div>GARANTIE ILLIMITÉE</div>
            </div>
          </div>
        </div>
        <div class="reveal" style="transition-delay: 0.2s;">
          <img src="Image/IMG_9297.JPG" style="border-radius: 0.5rem; height: 100%; object-fit:cover;">
        </div>
      </div>
    </section>

    <!-- PROCESSUS -->
    <section id="processus" class="section light-theme container">
      <div class="text-center reveal" style="text-align: center;">
        <h2 class="t-display">De l'idée à la réalisation.</h2>
      </div>
      
      <div class="timeline reveal">
        <div class="timeline-line"></div>
        <div class="timeline-progress"></div>
        
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <span class="t-label" style="color: var(--c-bois-chaud);">01 — PRISE DE CONTACT</span>
          <h4>Vous nous présentez votre projet et vos besoins.</h4>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <span class="t-label" style="color: var(--c-bois-chaud);">02 — INSPECTION DU SITE</span>
          <h4>Une inspection est réalisée afin d'étudier précisément l'espace.</h4>
          <span class="t-label" style="opacity: 0.5;">(Inspection payante)</span>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <span class="t-label" style="color: var(--c-bois-chaud);">03 — ÉTUDE DU PROJET</span>
          <h4>Analyse des dimensions, du style, des matériaux et des contraintes.</h4>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <span class="t-label" style="color: var(--c-bois-chaud);">04 — VALIDATION DU PROJET & DU DEVIS</span>
          <h4>Validation du concept et du devis personnalisé.</h4>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <span class="t-label" style="color: var(--c-bois-chaud);">05 — FABRICATION</span>
          <h4>Réalisation de votre mobilier avec précision.</h4>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <span class="t-label" style="color: var(--c-bois-chaud);">06 — INSTALLATION</span>
          <h4>Installation et mise en place finale.</h4>
        </div>
      </div>
    </section>

    <!-- CTA IMMERSIF -->
    <section class="cta-immersive">
      <img src="Image/IMG_9227.JPG" class="cta-img parallax-img" data-speed="0.2">
      <div class="cta-overlay"></div>
      <div class="container reveal">
        <h2 class="t-display" style="margin-bottom: 2rem;">Votre espace mérite<br><span class="t-italic">mieux que du standard.</span></h2>
        <p class="t-body-large" style="max-width: 600px; margin: 0 auto 3rem;">Parlons de votre projet et imaginons ensemble un intérieur conçu spécialement pour vous.</p>
        <div style="display:flex; justify-content:center; gap: 1rem; flex-wrap: wrap;">
          <a href="#contact" class="btn-primary">Demander mon devis</a>
          <a href="https://wa.me/22967585650" target="_blank" class="btn-secondary">Contacter sur WhatsApp</a>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section id="faq" class="section container">
      <div class="text-center reveal" style="text-align: center;">
        <h2 class="t-h2">Questions Fréquentes</h2>
      </div>
      
      <div class="faq-wrap reveal">
        <div class="faq-item">
          <div class="faq-q">
            <span>Combien coûte une cuisine sur mesure ?</span>
            <div class="faq-icon"></div>
          </div>
          <div class="faq-a">
            <p>Chaque projet est personnalisé. Le prix dépend notamment de l'espace, du modèle choisi, des dimensions et des finitions. Contactez-nous pour obtenir un devis personnalisé.</p>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-q">
            <span>Quels matériaux utilisez-vous ?</span>
            <div class="faq-icon"></div>
          </div>
          <div class="faq-a">
            <p>Nous travaillons avec des matériaux modernes de grande qualité, sélectionnés pour leur esthétique, leur résistance et leur adaptation aux réalités du climat béninois.</p>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-q">
            <span>Faites-vous la conception 3D ?</span>
            <div class="faq-icon"></div>
          </div>
          <div class="faq-a">
            <p>La conception 3D dépend de la nature et des exigences du projet. Contactez-nous afin d'en discuter.</p>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-q">
            <span>Combien de temps prend la fabrication ?</span>
            <div class="faq-icon"></div>
          </div>
          <div class="faq-a">
            <p>Le délai dépend de la complexité, des dimensions et des spécificités du projet. Un délai vous sera communiqué lors de la validation du projet.</p>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-q">
            <span>Faites-vous l'installation ?</span>
            <div class="faq-icon"></div>
          </div>
          <div class="faq-a">
            <p>Oui. Nous assurons l'installation de nos réalisations.</p>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-q">
            <span>Intervenez-vous en dehors de Cotonou ?</span>
            <div class="faq-icon"></div>
          </div>
          <div class="faq-a">
            <p>Oui, nous pouvons intervenir en dehors de Cotonou selon le projet.</p>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-q">
            <span>Peut-on choisir les couleurs et les matériaux ?</span>
            <div class="faq-icon"></div>
          </div>
          <div class="faq-a">
            <p>Oui. Chaque réalisation est personnalisée selon vos préférences, votre espace et votre projet.</p>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-q">
            <span>Quelle garantie proposez-vous ?</span>
            <div class="faq-icon"></div>
          </div>
          <div class="faq-a">
            <p>Meilleure Menuiserie du Bénin annonce une garantie illimitée sur ses réalisations.</p>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-q">
            <span>Comment demander un devis ?</span>
            <div class="faq-icon"></div>
          </div>
          <div class="faq-a">
            <p>Contactez-nous par téléphone, WhatsApp ou via le formulaire de contact.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CONTACT -->
    <section id="contact" class="section container light-theme">
      <div class="contact-grid">
        <div class="contact-info reveal">
          <h2 class="t-display" style="margin-bottom: 2rem;">Parlons de votre projet.</h2>
          
          <div>
            <span class="t-label">TÉLÉPHONE</span>
            <h4 class="t-h3" style="margin: 0.5rem 0;"><a href="tel:0167585650">01 67 58 56 50</a></h4>
            <h4 class="t-h3" style="margin: 0;"><a href="tel:0197474958">01 97 47 49 58</a></h4>
          </div>
          
          <div style="margin-top: 2rem;">
            <span class="t-label">WHATSAPP</span>
            <h4 class="t-h3" style="margin: 0.5rem 0;"><a href="https://wa.me/22967585650" target="_blank">01 67 58 56 50</a></h4>
            <h4 class="t-h3" style="margin: 0;"><a href="https://wa.me/22997474958" target="_blank">01 97 47 49 58</a></h4>
          </div>
          
          <div style="margin-top: 2rem;">
            <span class="t-label">EMAIL</span>
            <h4 class="t-h3" style="margin: 0.5rem 0;"><a href="mailto:madamemelinapro@gmail.com">madamemelinapro@gmail.com</a></h4>
          </div>
          
          <div style="margin-top: 2rem;">
            <span class="t-label">LOCALISATION</span>
            <h4 class="t-h3" style="margin: 0.5rem 0;">Sur rendez-vous</h4>
          </div>
        </div>
        
        <div class="contact-form reveal" style="transition-delay: 0.2s; background: var(--c-espresso); color: var(--c-blanc);">
          <form>
            <div class="input-group">
              <input type="text" placeholder="Nom complet" required>
            </div>
            <div class="input-group">
              <input type="tel" placeholder="Téléphone" required>
            </div>
            <div class="input-group">
              <input type="email" placeholder="Email" required>
            </div>
            <div class="input-group">
              <input type="text" placeholder="Type de projet (ex: Cuisine, Dressing...)" required>
            </div>
            <div class="input-group">
              <input type="text" placeholder="Budget indicatif">
            </div>
            <div class="input-group">
              <textarea placeholder="Description du projet" rows="4" required></textarea>
            </div>
            <button type="button" class="btn-primary" style="width: 100%; border: none; cursor: pointer;">ENVOYER MA DEMANDE</button>
            <a href="https://wa.me/22967585650" target="_blank" class="btn-secondary" style="width: 100%; margin-top: 1rem; text-align: center;">Prendre contact sur WhatsApp</a>
          </form>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container f-grid">
      <div>
        <img src="Image/logo.png" alt="MMB Logo" style="width: 150px; margin-bottom: 2rem; filter: brightness(0) invert(1);">
        <p class="t-body">L'EXCELLENCE SUR MESURE</p>
      </div>
      <div>
        <h4 class="t-label" style="color: var(--c-bois-chaud); margin-bottom: 1.5rem;">NAVIGATION</h4>
        <div class="f-links">
          <a href="#">Accueil</a>
          <a href="#services">Services</a>
          <a href="#realisations">Réalisations</a>
          <a href="#processus">Processus</a>
          <a href="#faq">FAQ</a>
          <a href="#contact">Contact</a>
        </div>
      </div>
      <div>
        <h4 class="t-label" style="color: var(--c-bois-chaud); margin-bottom: 1.5rem;">CONTACT</h4>
        <div class="f-links">
          <a href="tel:0167585650">01 67 58 56 50</a>
          <a href="tel:0197474958">01 97 47 49 58</a>
          <a href="mailto:madamemelinapro@gmail.com">Email</a>
        </div>
      </div>
      <div>
        <h4 class="t-label" style="color: var(--c-bois-chaud); margin-bottom: 1.5rem;">SOCIAL</h4>
        <div class="f-links">
          <a href="https://www.tiktok.com/@madame_melinaa" target="_blank">TikTok</a>
        </div>
        <a href="#contact" class="btn-secondary" style="margin-top: 2rem; padding: 0.75rem 1.5rem;">PARLER DE MON PROJET →</a>
      </div>
    </div>
    <div class="container f-bottom">
      <span>© 2026 Meilleure Menuiserie du Bénin. Tous droits réservés.</span>
      <a href="#top" style="color: var(--c-blanc);">Retour en haut ↑</a>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
"""

# Generating main index page
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# We will just write a small stub for the sub-pages if requested, but for a one-page architecture it's not strictly necessary. 
# The user asked for an extremely premium one-page feel with anchors. We'll stick to index.html and overwrite the CSS/JS.
os.makedirs('css', exist_ok=True)
os.makedirs('js', exist_ok=True)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Cinematic One-Page generated successfully.")
