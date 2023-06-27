document.querySelector(".menu-btn").addEventListener("click", () => {
    document.querySelector(".nav-menu").classList.toggle("show");
  });
  
  ScrollReveal().reveal('.showcase');
  ScrollReveal().reveal('.poemas', { delay: 1000});
  ScrollReveal().reveal('.card-banner-one', { delay: 900});
  ScrollReveal().reveal('.card-banner-two', { delay: 1000});