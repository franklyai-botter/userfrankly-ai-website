/* Neural Nautic — nn.js */

/* Mobile nav toggle */
(function () {
  const toggle = document.querySelector('.nn-nav__toggle');
  const menu   = document.querySelector('.nn-nav__menu');
  if (!toggle || !menu) return;

  toggle.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
  });

  document.addEventListener('click', (e) => {
    if (!toggle.contains(e.target) && !menu.contains(e.target)) {
      menu.classList.remove('open');
      toggle.setAttribute('aria-expanded', false);
    }
  });
})();

/* Active nav link */
(function () {
  const current = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nn-nav__menu a').forEach(link => {
    if (link.getAttribute('href') === current) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });
})();

/* SVG animation trigger on scroll */
(function () {
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const svgs = document.querySelectorAll('.nn-workflow-svg');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.querySelectorAll('.nn-node').forEach(node => {
        node.style.animationPlayState = 'running';
      });
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.15 });

  svgs.forEach(svg => {
    svg.querySelectorAll('.nn-node').forEach(node => {
      node.style.animationPlayState = 'paused';
    });
    observer.observe(svg);
  });
})();
