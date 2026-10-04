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
  --section-py: 3vw;
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
  font-size: clamp(2rem, 5vw, 4.5rem);
  line-height: 0.95;
  font-weight: 300;
  letter-spacing: -0.02em;
  margin: 0;
}

.t-h2 {
  font-family: var(--f-heading);
  font-size: clamp(1.75rem, 3.5vw, 3rem);
  line-height: 1.05;
  font-weight: 400;
  margin: 0;
}

.t-h3 {
  font-family: var(--f-heading);
  font-size: clamp(1.1rem, 2vw, 1.75rem);
  line-height: 1.2;
  font-weight: 400;
}

.t-body {
  font-size: clamp(0.95rem, 1.1vw, 1.1rem);
  line-height: 1.6;
  font-weight: 300;
  color: rgba(250, 248, 244, 0.8);
}

.t-body-large {
  font-size: clamp(1.1rem, 1.8vw, 1.8rem);
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
  width: 90px;
}
.logo-wrap img {
  width: 100%;
  height: auto;
}
.navbar.scrolled.light-nav .logo-wrap img {
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
  margin-top: 2rem;
  margin-bottom: 6rem;
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
  margin-bottom: 2.5rem;
  border-bottom: 1px solid rgba(25, 24, 23, 0.1);
  padding-bottom: 2rem;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
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
  margin-top: 2rem;
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
  margin-bottom: 2rem;
  flex-wrap: wrap;
}
.filter-btn {
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.6);
  font-family: var(--f-body);
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
  transition: color 0.3s ease;
  padding: 0;
}
.filter-btn.active, .filter-btn:hover {
  color: var(--c-blanc);
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
  margin-bottom: 2rem;
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
  background: #000000;
  padding: 5rem var(--px) 2rem;
  border-top: 2px solid #c79e61;
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
  color: #c79e61;
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
  .t-display {
    font-size: clamp(1.75rem, 7vw, 2.5rem);
  }
  .t-h2 {
    font-size: clamp(1.5rem, 6vw, 2rem);
  }
  .t-h3 {
    font-size: clamp(1.1rem, 4.5vw, 1.4rem);
  }
  .t-body-large {
    font-size: 1rem;
  }
  .nav-links, .nav-cta { display: none; }
  .menu-toggle { display: block; }
  .chiffres-grid { grid-template-columns: 1fr 1fr; }
  .f-grid { grid-template-columns: 1fr; }
  .hero-ctas { flex-direction: column; }
  .btn-primary, .btn-secondary { width: 100%; }
}

/* Custom Cursor */
@media (hover: hover) and (pointer: fine) {
  body {
    cursor: none;
  }
  .cursor-dot {
    position: fixed;
    top: 0;
    left: 0;
    width: 8px;
    height: 8px;
    background-color: var(--c-bois-chaud);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    pointer-events: none;
    z-index: 9999;
    transition: width 0.2s, height 0.2s, background-color 0.2s;
  }
  .cursor-ring {
    position: fixed;
    top: 0;
    left: 0;
    width: 40px;
    height: 40px;
    border: 1px solid rgba(135, 106, 80, 0.4);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    pointer-events: none;
    z-index: 9998;
    transition: transform 0.15s ease-out, width 0.2s, height 0.2s, background-color 0.2s;
  }
  a:hover ~ .cursor-dot, button:hover ~ .cursor-dot, .hover-target:hover ~ .cursor-dot {
    background-color: var(--c-blanc);
  }
  a:hover ~ .cursor-ring, button:hover ~ .cursor-ring, .hover-target:hover ~ .cursor-ring {
    width: 60px;
    height: 60px;
    background-color: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 255, 255, 0.2);
  }
}


/* Slideshow */
.hero-slideshow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 120%;
  z-index: -2;
}
.hero-bg.slide {
  opacity: 0;
  transition: opacity 1.5s ease-in-out, transform 4s ease-out;
  transform: scale(1.05);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.hero-bg.slide.active {
  opacity: 1;
  transform: scale(1);
}

/* Portfolio Masonry */
.portfolio-masonry {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  grid-auto-rows: 10px;
  gap: 20px;
}
.port-card {
  position: relative;
  border-radius: 0.5rem;
  overflow: hidden;
  display: block;
  background: var(--c-espresso);
  grid-row-end: span 30; /* default height */
}
.port-card:nth-child(2n) {
  grid-row-end: span 40;
}
.port-card:nth-child(3n) {
  grid-row-end: span 25;
}
.port-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 1s var(--ease), opacity 0.5s ease;
}

/* Chiffres Redesign */
.chiffres-flex {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 3rem;
  padding: 4rem 0;
}
.chiffre-card {
  text-align: center;
  color: var(--c-blanc);
}
.chiffre-card h4 {
  margin: 0;
  color: var(--c-beige);
}
.c-line {
  width: 40px;
  height: 2px;
  background: var(--c-bois-chaud);
  margin: 1.5rem auto;
}

/* Pourquoi Nous Redesign */
.pq-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}
.pq-card {
  background: var(--c-blanc);
  padding: 3rem 2rem;
  border-radius: 1rem;
  border: 1px solid rgba(25,24,23,0.05);
  transition: transform 0.4s var(--ease), box-shadow 0.4s var(--ease);
}
.pq-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.05);
}
.pq-icon {
  font-family: var(--f-heading);
  font-size: 3rem;
  color: var(--c-bois-chaud);
  opacity: 0.5;
  margin-bottom: 1.5rem;
}
.pq-card h3 {
  margin-top: 0;
  margin-bottom: 1rem;
}

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

@media (max-width: 768px) {
  .hero-content {
    padding-bottom: 8rem;
  }
}


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

html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meilleure Menuiserie du Bénin | Ameublement & Design Intérieur Sur Mesure</title>
  <meta name="description" content="Meilleure Menuiserie du Bénin conçoit et réalise vos meubles, cuisines, dressings et aménagements intérieurs sur mesure avec des matériaux de qualité.">
  <link rel="stylesheet" href="css/style.css">

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
</head>
<body>
  <div class="cursor-dot"></div>
  <div class="cursor-ring"></div>

  <nav class="navbar">
    <a href="#" class="logo-wrap">
      <img src="Image/LOGO.jpg" alt="MMB Logo">
    </a>
    <div class="nav-links">
      <a href="#services" class="nav-link">Services</a>
      <a href="#realisations" class="nav-link">Réalisations</a>
      <a href="#processus" class="nav-link">Notre Processus</a>
      <a href="#a-propos" class="nav-link">À Propos</a>
      <a href="#faq" class="nav-link">FAQ</a>
    </div>
    <a href="#" onclick="document.getElementById('devis-modal').classList.add('active'); return false;" class="nav-cta">Demander un devis</a>
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
      <div class="hero-slideshow">
        <img src="Image/image1-salon.JPG" class="hero-bg slide active">
        <img src="Image/image2-cuisine.JPG" class="hero-bg slide">
        <img src="Image/image3-decoration.JPG" class="hero-bg slide">
        <img src="Image/image4-dressing.jpg" class="hero-bg slide">
      </div>
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
        <span class="t-label">Scrollez et explorez</span>
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
      
      <style>
        .services-bento {
          display: grid;
          grid-template-columns: repeat(4, 1fr);
          grid-auto-rows: 250px;
          gap: 1.5rem;
        }
        .bento-card {
          position: relative;
          border-radius: 1.5rem;
          overflow: hidden;
          display: block;
          background: var(--c-espresso);
        }
        .bento-card img {
          width: 100%;
          height: 100%;
          object-fit: cover;
          transition: transform 0.8s var(--ease);
        }
        .bento-card:hover img {
          transform: scale(1.05);
        }
        .bento-overlay {
          position: absolute;
          inset: 0;
          background: linear-gradient(to top, rgba(25,24,23,0.9) 0%, rgba(25,24,23,0.2) 50%, rgba(25,24,23,0) 100%);
          display: flex;
          flex-direction: column;
          justify-content: flex-end;
          padding: 1.5rem;
          pointer-events: none;
        }
        
        .bento-card:nth-child(1) { grid-column: span 2; grid-row: span 2; }
        .bento-card:nth-child(2) { grid-column: span 1; grid-row: span 1; }
        .bento-card:nth-child(3) { grid-column: span 1; grid-row: span 1; }
        .bento-card:nth-child(4) { grid-column: span 2; grid-row: span 1; }
        .bento-card:nth-child(5) { grid-column: span 1; grid-row: span 2; }
        .bento-card:nth-child(6) { grid-column: span 1; grid-row: span 1; }
        .bento-card:nth-child(7) { grid-column: span 2; grid-row: span 1; }
        .bento-card:nth-child(8) { grid-column: span 1; grid-row: span 1; }
        .bento-card:nth-child(9) { grid-column: span 2; grid-row: span 1; }

        @media (max-width: 900px) {
          .services-bento {
            grid-template-columns: repeat(2, 1fr);
            grid-auto-rows: 200px;
          }
          .bento-card:nth-child(1) { grid-column: span 2; grid-row: span 2; }
          .bento-card:nth-child(n+2) { grid-column: span 1; grid-row: span 1; }
          .bento-card:nth-child(4) { grid-column: span 2; grid-row: span 1; }
          .bento-card:nth-child(7) { grid-column: span 2; grid-row: span 1; }
          .bento-card:nth-child(9) { grid-column: span 2; grid-row: span 1; }
        }
        @media (max-width: 600px) {
          .services-bento {
            grid-template-columns: 1fr;
          }
          .bento-card:nth-child(n) { grid-column: span 1; grid-row: span 1; }
          .bento-card:nth-child(1) { grid-row: span 2; }
        }
      </style>

      <div class="services-bento">
        <a href="#" data-cat="cuisines" class="bento-card reveal open-lightbox-btn">
          <img src="Image/image2-cuisine.JPG">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">01 — CUISINES SUR MESURE</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Cuisines</h3>
          </div>
        </a>
        <a href="#" data-cat="dressings" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.1s;">
          <img src="Image/image4-dressing.jpg">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">02 — DRESSINGS</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Dressings</h3>
          </div>
        </a>
        <a href="#" data-cat="salons" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.2s;">
          <img src="Image/Salon_new.jpg">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">03 — SALONS</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Salons</h3>
          </div>
        </a>
        <a href="#" data-cat="chambres" class="bento-card reveal open-lightbox-btn">
          <img src="Image/chambre_new_v2.jpg">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">04 — CHAMBRES</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Chambres</h3>
          </div>
        </a>
        <a href="#" data-cat="bureaux" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.1s;">
          <img src="Image/Bureau_new.jpg">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">05 — BUREAUX</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Bureaux</h3>
          </div>
        </a>
        <a href="#" data-cat="dressings" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.2s;">
          <img src="Image/IMG_9230.JPG">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">06 — RANGEMENTS</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Rangements</h3>
          </div>
        </a>
        <a href="#" data-cat="salons" class="bento-card reveal open-lightbox-btn">
          <img src="Image/IMG_9227.JPG">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">07 — MEUBLES TV</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Meubles TV</h3>
          </div>
        </a>
        <a href="#" data-cat="salons" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.1s;">
          <img src="Image/IMG_9285.JPG">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">08 — DÉCORATION</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Intérieurs</h3>
          </div>
        </a>
        <a href="#" data-cat="salles-de-bain" class="bento-card reveal open-lightbox-btn" style="transition-delay: 0.2s;">
          <img src="Image/salle_de_bain_new.jpg">
          <div class="bento-overlay">
            <span class="service-num" style="margin-bottom: 0.5rem; font-size: 0.8rem;">09 — SALLES DE BAIN</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Salles de bain</h3>
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
                <div class="savoir-img-wrap reveal" id="savoir-fader" style="position: relative; height: 800px; border-radius: 1rem; overflow: hidden;">
          <img src="Image/Autres../30af9e8b28b889719b75a378cf36a958.jpg" class="savoir-img parallax-img fade-img active" data-speed="0.1" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity: 1; transition: opacity 0.8s ease;">
          <img src="Image/Autres../415aa88df9f7460bd2f377ea8b50adc5.jpg" class="savoir-img parallax-img fade-img " data-speed="0.1" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity: 0; transition: opacity 0.8s ease;">
          <img src="Image/Autres../50f0d86238313db7515d854b8b6307b7.jpg" class="savoir-img parallax-img fade-img " data-speed="0.1" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity: 0; transition: opacity 0.8s ease;">
          <img src="Image/Autres../6314c1a8f4a29acfe488645eb605eba5.jpg" class="savoir-img parallax-img fade-img " data-speed="0.1" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity: 0; transition: opacity 0.8s ease;">
          <img src="Image/Autres../67644d0c557ce1fe318e5a42877c40cd.jpg" class="savoir-img parallax-img fade-img " data-speed="0.1" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity: 0; transition: opacity 0.8s ease;">
          <img src="Image/Autres../ab8f039197ad7b740125543be97870d4.jpg" class="savoir-img parallax-img fade-img " data-speed="0.1" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity: 0; transition: opacity 0.8s ease;">
        </div>
      </div>
    </section>

    
    <!-- REALISATIONS WRAPPER -->
    <div style="position: relative; background: url('Image/photo8-coiffeuse.JPG') center/cover fixed; overflow: hidden;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to right, rgba(25,24,23,0.95), rgba(25,24,23,0.7)); backdrop-filter: blur(8px);"></div>
      <div style="position: relative; z-index: 2;">
        <section id="realisations" class="section container">
      <div class="reveal">
        <h2 class="t-display">Nos réalisations</h2>
        <p class="t-body-large" style="margin-bottom: 3rem; color: var(--c-bois-chaud);">Des projets uniques. Des espaces qui ont leur propre identité.</p>
      </div>

      <div class="portfolio-filters reveal">
        <a href="#" data-cat="tout" class="filter-btn active">TOUT</a>
        <a href="#" data-cat="cuisines" class="filter-btn">CUISINES</a>
        <a href="#" data-cat="dressings" class="filter-btn">DRESSINGS</a>
        <a href="#" data-cat="salons" class="filter-btn">SALONS</a>
        <a href="#" data-cat="chambres" class="filter-btn">CHAMBRES</a>
        <a href="#" data-cat="bureaux" class="filter-btn">BUREAUX</a>
      </div>

            <style>
        .portfolio-trio {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 2rem;
          margin-top: 4rem;
        }
        .trio-item {
          position: relative;
          border-radius: 1rem;
          overflow: hidden;
          aspect-ratio: 4 / 5;
          display: block;
        }
        .trio-item img {
          width: 100%;
          height: 100%;
          object-fit: cover;
          transition: transform 0.8s ease;
        }
        .trio-item:hover img {
          transform: scale(1.05);
        }
        @media (max-width: 768px) {
          .portfolio-trio {
            grid-template-columns: 1fr;
          }
          .trio-item {
            aspect-ratio: 16 / 9;
          }
        }
      </style>
      
      <div class="portfolio-trio">
        <a href="#contact" class="trio-item reveal">
          <img src="Image/photo1-decoration.JPG">
          <div class="port-overlay">
            <span style="color: #FADDAA; font-weight: bold; font-size: 0.85rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem;">Intérieur</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Décoration</h3>
          </div>
        </a>
        <a href="#contact" class="trio-item reveal" style="transition-delay: 0.1s;">
          <img src="Image/photo2-coiffeuse.JPG">
          <div class="port-overlay">
            <span style="color: #FADDAA; font-weight: bold; font-size: 0.85rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem;">Meuble</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Coiffeuse</h3>
          </div>
        </a>
        <a href="#contact" class="trio-item reveal" style="transition-delay: 0.2s;">
          <img src="Image/photo23-cuisine.jpg">
          <div class="port-overlay">
            <span style="color: #FADDAA; font-weight: bold; font-size: 0.85rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem;">Sur mesure</span>
            <h3 class="t-h3" style="color: white; margin: 0;">Cuisine</h3>
          </div>
        </a>
      </div>
      </section>
    </div>

        <!-- POURQUOI NOUS CHOISIR -->
    <section id="pourquoi-nous" class="section container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 4rem; align-items: center;">
        <div class="reveal">
          <h2 class="t-display" style="margin-bottom: 2rem;">Pourquoi<br><span class="t-italic">nous choisir ?</span></h2>
          <p class="t-body-large" style="margin-bottom: 2rem; color: var(--c-bois-chaud);">L'excellence et la confiance, notre priorité.</p>
          <p class="t-body" style="margin-bottom: 1.5rem;">Faire appel à la Meilleure Menuiserie du Bénin, c'est choisir un artisanat d'exception. Nous mettons un point d'honneur à respecter vos délais tout en garantissant des finitions parfaites.</p>
          <ul style="list-style: none; padding: 0; margin-bottom: 2rem; color: var(--c-blanc);">
            <li style="margin-bottom: 1rem;">✓ <span style="margin-left: 1rem;">Matériaux nobles et durables</span></li>
            <li style="margin-bottom: 1rem;">✓ <span style="margin-left: 1rem;">Accompagnement 100% personnalisé</span></li>
            <li style="margin-bottom: 1rem;">✓ <span style="margin-left: 1rem;">Respect strict des délais d'installation</span></li>
          </ul>
        </div>
        <div class="reveal" style="position: relative; border-radius: 1rem; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.5); aspect-ratio: 4/5; max-width: 400px; margin: 0 auto;">
          <img src="Image/image-pdg.JPG" alt="PDG Meilleure Menuiserie du Bénin" style="width: 100%; height: 100%; object-fit: cover; object-position: center top;">
        </div>
      </div>
    </section>

<!-- NOUVEAU PROCESSUS -->
    <section id="processus" class="section light-theme">
      <div class="container">
        <div class="reveal" style="text-align: center; margin-bottom: 4rem;">
          <h2 class="t-display">Comment nous travaillons.</h2>
          <p class="t-body-large" style="color: var(--c-bois-chaud);">Un processus clair, sans surprise.</p>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
          <div class="reveal" style="padding: 2rem; border: 1px solid rgba(25,24,23,0.1); border-radius: 1rem; background: var(--c-blanc);">
            <div style="font-family: var(--f-heading); font-size: 3rem; color: var(--c-bois-chaud); margin-bottom: 1rem;">01</div>
            <h3 class="t-h3" style="margin-bottom: 1rem;">L'Écoute</h3>
            <p class="t-body" style="color: var(--c-espresso);">Nous analysons vos besoins, votre espace et vos goûts lors d'une première consultation détaillée.</p>
          </div>
          
          <div class="reveal" style="padding: 2rem; border: 1px solid rgba(25,24,23,0.1); border-radius: 1rem; background: var(--c-blanc); transition-delay: 0.1s;">
            <div style="font-family: var(--f-heading); font-size: 3rem; color: var(--c-bois-chaud); margin-bottom: 1rem;">02</div>
            <h3 class="t-h3" style="margin-bottom: 1rem;">La Conception</h3>
            <p class="t-body" style="color: var(--c-espresso);">Réalisation des plans, choix des matériaux nobles et validation du devis sur-mesure.</p>
          </div>
          
          <div class="reveal" style="padding: 2rem; border: 1px solid rgba(25,24,23,0.1); border-radius: 1rem; background: var(--c-blanc); transition-delay: 0.2s;">
            <div style="font-family: var(--f-heading); font-size: 3rem; color: var(--c-bois-chaud); margin-bottom: 1rem;">03</div>
            <h3 class="t-h3" style="margin-bottom: 1rem;">La Fabrication</h3>
            <p class="t-body" style="color: var(--c-espresso);">Vos meubles prennent vie dans notre atelier, avec une finition artisanale irréprochable.</p>
          </div>
          
          <div class="reveal" style="padding: 2rem; border: 1px solid rgba(25,24,23,0.1); border-radius: 1rem; background: var(--c-bois-chaud); color: var(--c-blanc); transition-delay: 0.3s;">
            <div style="font-family: var(--f-heading); font-size: 3rem; color: var(--c-beige); margin-bottom: 1rem;">04</div>
            <h3 class="t-h3" style="margin-bottom: 1rem;">L'Installation</h3>
            <p class="t-body" style="color: rgba(255,255,255,0.9);">Livraison et pose experte chez vous, pour un résultat clé en main exceptionnel.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- NOUVEAU CONTACT / CTA MINIMALISTE -->
    <section id="contact" class="section container" style="padding-top: 8rem; padding-bottom: 8rem;">
      <div class="reveal" style="background: var(--c-espresso); border-radius: 2rem; padding: 4rem 2rem; text-align: center; position: relative; overflow: hidden; border: 1px solid rgba(255,255,255,0.1);">
        <div style="position: relative; z-index: 2;">
          <h2 class="t-display" style="color: var(--c-blanc); margin-bottom: 1rem;">Prêt à transformer<br><span class="t-italic" style="color: var(--c-beige);">votre intérieur ?</span></h2>
          <p class="t-body-large" style="color: rgba(255,255,255,0.7); max-width: 600px; margin: 0 auto 3rem;">Discutons ensemble de vos idées. Nous sommes à votre écoute pour concevoir l'espace qui vous ressemble parfaitement.</p>
          
          <div style="display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
            <a href="https://wa.me/22967585650" target="_blank" class="btn-primary" style="background: var(--c-bois-chaud); color: white; border: none; padding: 1.2rem 2.5rem; font-size: 0.9rem;">PARLER SUR WHATSAPP</a>
            <a href="tel:0167585650" class="btn-secondary" style="padding: 1.2rem 2.5rem; font-size: 0.9rem;">APPELER DIRECTEMENT</a>
          </div>
        </div>
      </div>
    </section>
    
  
  </main>

  <footer class="footer">
    <div class="container f-grid">
      <div class="f-col">
        <a href="/" class="logo" style="display:inline-block; max-width:250px;"><img src="Image/logo_mmb_footer.jpg" alt="MMB Logo" style="width: 100%; height: auto; object-fit: contain;"></a>
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
          <a href="https://wa.me/22967585650?text=Salut%2C%20je%20suis%20interss%C3%A9e%20par%20vos%20realisation%2C%20j%27aimerais%20en%20savoir%20plus%20." target="_blank">WhatsApp</a>
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

    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/+22900000000?text=Salut,%20je%20suis%20interessé%20par%20ce%20que%20vous%20faites,%20puis%20en%20savoir%20plus%20?" target="_blank" class="whatsapp-btn">
      <svg viewBox="0 0 24 24" fill="white" width="30" height="30">
        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a5.22 5.22 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>
      </svg>
    </a>


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

</body>
</html>"""

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

  // Custom Cursor
  const cursorDot = document.querySelector('.cursor-dot');
  const cursorRing = document.querySelector('.cursor-ring');
  
  if(cursorDot && cursorRing && matchMedia('(pointer:fine)').matches) {
    let mouseX = 0;
    let mouseY = 0;
    let ringX = 0;
    let ringY = 0;
    
    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      
      cursorDot.style.left = mouseX + 'px';
      cursorDot.style.top = mouseY + 'px';
    });
    
    const renderCursor = () => {
      ringX += (mouseX - ringX) * 0.15;
      ringY += (mouseY - ringY) * 0.15;
      
      cursorRing.style.left = ringX + 'px';
      cursorRing.style.top = ringY + 'px';
      
      requestAnimationFrame(renderCursor);
    };
    
    requestAnimationFrame(renderCursor);
  }

  // Hero Slideshow
  const slides = document.querySelectorAll('.hero-bg.slide');
  let currentSlide = 0;
  if (slides.length > 0) {
    setInterval(() => {
      slides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('active');
    }, 4000);
  }
});


const galleryData = {
  "cuisines": [
    "Image/cuisines/57a4fc203dcb2d454a1e8f4522ed4c80.jpg",
    "Image/cuisines/799229c0dfaed0822dcb96760c54322b.jpg",
    "Image/cuisines/d07730b8847c1bb994d16fda21deac6d.jpg",
    "Image/cuisines/IMG_9245.JPG",
    "Image/cuisines/648a8f300ce304a9df2d887bab481ceb.jpg",
    "Image/cuisines/4294719e7e2fde77211abc6fe1c50a08.jpg",
    "Image/cuisines/82a193c6ceb8881f71bc47edac92a840.jpg",
    "Image/cuisines/b315081c3219bc1245f1ffe83111613d.jpg",
    "Image/cuisines/2032868a75e30c2d866672f83c5bdc05.jpg",
    "Image/cuisines/d3824e98ea33632f17b5151c43506e78.jpg",
    "Image/cuisines/8a161e6da546b9da0a122a51aca7323f.jpg",
    "Image/cuisines/photo4-cuisine.JPG"
  ],
  "dressings": [
    "Image/dressings/bd040f77902ff7d6a4db488f3a3d1911.jpg",
    "Image/dressings/099211b3ba76d0a8ceddf42092ef47ea.jpg",
    "Image/dressings/36a439065c3ed385a9e6414e7cb7638a.jpg",
    "Image/dressings/acf583f2cd5ae81a5167ca8fdf1ab179.jpg",
    "Image/dressings/02de764d6a52aaa24c4050a298967ead.jpg",
    "Image/dressings/911d67db50bcfc24389ac3af9f0e9bc5.jpg",
    "Image/dressings/c28a4f20dd3d6430d244a8d275076b1c.jpg",
    "Image/dressings/0eb2dd96ad2b897d16983500f0b69ccc.jpg",
    "Image/dressings/7c0fb3301e851dfd196c678b37ab995b.jpg",
    "Image/dressings/1e29b03451c3cab885e0216801319c55.jpg",
    "Image/dressings/5dd25528ca083d60eb3a497a74b3aa0b.jpg"
  ],
  "salons": [
    "Image/saloon/f8c76b55c40475e20afec396b7be8bab.jpg",
    "Image/saloon/9f413bd936b1b0ddb2ecda414da353e8.jpg",
    "Image/saloon/e72dd6797a23a38ed1e337fa0563a7aa.jpg",
    "Image/saloon/1b48110e0a958a540d225062a2cbd450.jpg",
    "Image/saloon/d3d3112a7c2646e014563ded5d35a44a.jpg",
    "Image/saloon/192e85f55e0dc646d39599966ffcc602.jpg",
    "Image/saloon/39ba8176590f61b5e0bdf72a3ba67b66.jpg",
    "Image/saloon/9d552e5e1294dfb4216aa8b4596a0df6.jpg",
    "Image/saloon/75d08cb4c05caf343698bac71db7e56b.jpg",
    "Image/saloon/14194bf12dd9a2505c2b01d4f6a3f9de.jpg",
    "Image/saloon/487184374813b70c57c383794cf58091.jpg",
    "Image/saloon/cacd0668015da266106de7103cb78df8.jpg"
  ],
  "chambres": [
    "Image/chambre/abc00e149bfcf3a9b45c37557920db31.jpg",
    "Image/chambre/ef6f95bcd123a45124a61f8b8360516d.jpg",
    "Image/chambre/aa28583344a9f91b3168b15ccd38b8ab.jpg",
    "Image/chambre/6eef9c3177f17f493cbc78a1b63709d9.jpg",
    "Image/chambre/252dca03e694004797ac2ceb193dd414.jpg",
    "Image/chambre/2ad9f249745149100f8a2daf0b24eaf6.jpg",
    "Image/chambre/398075ef1bdc5896601c799a58475126.jpg",
    "Image/chambre/520d757300c0258c9b43193a6e964232.jpg"
  ],
  "bureaux": [
    "Image/bureaux/dfd2db8878588a14a353d0715d7b1be2.jpg",
    "Image/bureaux/88b305991b4e68bf55f3f1adef6618f2.jpg",
    "Image/bureaux/f87ad8e6419c21f2d9ff7f6384b329be.jpg",
    "Image/bureaux/5d66a7b8d12863782a8e3d819118d8e5.jpg",
    "Image/bureaux/6ac029360a9cdd9a01819a0cdffeeee9.jpg",
    "Image/bureaux/19c91eb1dc7fad7a5a266179455dda1a.jpg",
    "Image/bureaux/34a3077e5f53b0606b6d0e99ea71c7dc.jpg",
    "Image/bureaux/615d68b101619ab99d9fb4abb7a6872a.jpg",
    "Image/bureaux/0dfb300be51dbbbb3cd6c8d730e12322.jpg",
    "Image/bureaux/205cbbc747dee24be28639f9b77977a0.jpg",
    "Image/bureaux/41b788d313c66cd2703d1e0878d80e11.jpg"
  ],
  "salles-de-bain": [
    "Image/salle de bain/6314c1a8f4a29acfe488645eb605eba5.jpg",
    "Image/salle de bain/795c13de31b01c659d9dc5c70139647d.jpg",
    "Image/salle de bain/ece1c8540d8eab2b9b01ec12a5bbab79.jpg",
    "Image/salle de bain/848ce957d7d762260ea99567c1e50601.jpg",
    "Image/salle de bain/dc75d5cd9cd20eb64ef8ad10233ed431.jpg",
    "Image/salle de bain/71e3aa6adb398eb8b27d8560704214fd.jpg",
    "Image/salle de bain/ab8f039197ad7b740125543be97870d4.jpg"
  ]
};

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
      window.location.href = 'realisations.html';
    } else {
      openLightbox(cat);
    }
  });
});

document.querySelectorAll('.open-lightbox-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    const cat = btn.getAttribute('data-cat');
    openLightbox(cat);
  });
});


// Devis Form Submission
window.submitDevis = function(e) {
  e.preventDefault();
  const nom = document.getElementById('devis-nom').value;
  const projet = document.getElementById('devis-projet').value;
  const message = document.getElementById('devis-message').value;
  
  const text = `Bonjour, je suis ${nom}.\nJe souhaite demander un devis pour un projet de type : ${projet}.\nDétails : ${message}`;
  const whatsappUrl = `https://wa.me/22967585650?text=${encodeURIComponent(text)}`;
  
  window.open(whatsappUrl, '_blank');
  document.getElementById('devis-modal').classList.remove('active');
  document.getElementById('devis-form').reset();
};
"""

os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
os.makedirs("Image", exist_ok=True)

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("js/main.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Site généré avec succès !")
