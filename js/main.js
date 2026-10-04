
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
});
