// Essam Software - Main JS

document.addEventListener('DOMContentLoaded', function () {

    // Initialize AOS
    AOS.init({
        duration: 700,
        easing: 'ease-out-cubic',
        once: true,
        offset: 60,
    });

    // Navbar scroll effect
    const navbar = document.getElementById('mainNavbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Animated counters
    const counters = document.querySelectorAll('.counter-num');
    if (counters.length) {
        const observerOptions = { threshold: 0.5 };
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
        }, observerOptions);
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
                const src = this.querySelector('img').src;
                mainImg.src = src;
            });
        });
        if (thumbs[0]) thumbs[0].classList.add('active');
    }

    // Product type badge colors
    const typeBadges = document.querySelectorAll('[data-type]');
    typeBadges.forEach(badge => {
        const t = badge.getAttribute('data-type');
        if (t === 'desktop') badge.classList.add('badge-desktop');
        else if (t === 'web') badge.classList.add('badge-web');
        else if (t === 'mobile') badge.classList.add('badge-mobile');
    });

    // Auto-dismiss messages
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
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

});
