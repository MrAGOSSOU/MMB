
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
