with open("css/style.css", "r") as f:
    css = f.read()

new_css = """
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
"""

with open("css/style.css", "a") as f:
    f.write("\n" + new_css)
