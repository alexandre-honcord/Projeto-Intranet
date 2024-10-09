document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.querySelector('.move-sidebar');
    const sidebar = document.querySelector('.sidebar');

    // Set aria-expanded attribute for accessibility
    toggle.setAttribute('aria-expanded', localStorage.getItem('bar') !== 'off');

    // Initial state check
    if (localStorage.getItem('bar') === 'off') {
        sidebar.classList.remove('active');
    } else {
        sidebar.classList.add('active');
    }

    toggle.addEventListener("click", () => {
        sidebar.classList.toggle('active');
        const isActive = sidebar.classList.contains('active');

        // Update icon and localStorage
        toggle.classList.toggle('fa-caret-left', !isActive);
        toggle.classList.toggle('fa-caret-right', isActive);
        localStorage.setItem('bar', isActive ? 'on' : 'off');
        toggle.setAttribute('aria-expanded', isActive);
    });
});