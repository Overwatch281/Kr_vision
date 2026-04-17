// Menu mobile
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

if (navToggle) {
    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
}

// Fermer le menu en cliquant ailleurs
document.addEventListener('click', (e) => {
    if (!e.target.closest('.navbar')) {
        navLinks?.classList.remove('active');
    }
});