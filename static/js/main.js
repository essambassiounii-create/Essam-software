// Nova Soft - Main JS

document.addEventListener('DOMContentLoaded', function () {

    // Initialize AOS
    AOS.init({
        duration: 800,
        easing: 'ease-out-cubic',
        once: true,
        offset: 60,
    });

    // Navbar scroll effect
    const navbar = document.getElementById('mainNavbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            navbar.classList.toggle('scrolled', window.scrollY > 50);
        });
    }

    // Hero Particles
    const particlesContainer = document.getElementById('heroParticles');
    if (particlesContainer) {
        for (let i = 0; i < 18; i++) {
            const p = document.createElement('div');
            p.classList.add('particle');
            const size = Math.random() * 20 + 8;
            p.style.cssText = `
                width:${size}px; height:${size}px;
                left:${Math.random() * 100}%;
                animation-duration:${Math.random() * 15 + 10}s;
                animation-delay:${Math.random() * 10}s;
                opacity:${Math.random() * 0.3 + 0.05};
            `;
            particlesContainer.appendChild(p);
        }
    }

    // Animated counters
    const counters = document.querySelectorAll('.counter-num');
    if (counters.length) {
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    const target = parseInt(el.getAttribute('data-target'));
                    const duration = 2000;
                    const increment = target / (duration / 16);
                    let current = 0;
                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= target) {
                            el.textContent = target;
                            clearInterval(timer);
                        } else {
                            el.textContent = Math.floor(current);
                        }
                    }, 16);
                    observer.unobserve(el);
                }
            });
        }, { threshold: 0.5 });
        counters.forEach(c => observer.observe(c));
    }

    // Skill bars animation
    const skillFills = document.querySelectorAll('.skill-fill');
    if (skillFills.length) {
        const skillObserver = new IntersectionObserver(function (entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.width = entry.target.getAttribute('data-width') + '%';
                    skillObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        skillFills.forEach(bar => {
            const width = bar.style.width;
            bar.setAttribute('data-width', parseInt(width));
            bar.style.width = '0%';
            skillObserver.observe(bar);
        });
    }

    // Screenshot gallery
    const mainImg = document.getElementById('mainScreenshot');
    const thumbs = document.querySelectorAll('.screenshot-thumb');
    if (mainImg && thumbs.length) {
        thumbs.forEach(thumb => {
            thumb.addEventListener('click', function () {
                thumbs.forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                mainImg.style.opacity = '0';
                setTimeout(() => {
                    mainImg.src = this.querySelector('img').src;
                    mainImg.style.opacity = '1';
                }, 200);
            });
        });
        if (thumbs[0]) thumbs[0].classList.add('active');
    }

    // Auto-dismiss messages
    document.querySelectorAll('.alert').forEach(alert => {
        setTimeout(() => {
            try { new bootstrap.Alert(alert).close(); } catch(e) {}
        }, 5000);
    });

    // Smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Tech items hover glow
    document.querySelectorAll('.tech-item').forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.background = 'linear-gradient(135deg, rgba(108,99,255,0.05), rgba(108,99,255,0.02))';
        });
        item.addEventListener('mouseleave', function() {
            this.style.background = 'white';
        });
    });

});
