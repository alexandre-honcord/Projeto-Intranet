document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.querySelector('.move-sidebar');
    const sidebar = document.querySelector('.sidebar');

    toggle.addEventListener("click", () => {
        sidebar.classList.toggle('active'); // Alterna a classe 'active' na sidebar
        const isActive = sidebar.classList.contains('active');

        // Atualiza o ícone
        toggle.classList.toggle('fa-caret-right', !isActive);
        toggle.classList.toggle('fa-caret-left', isActive);
        toggle.setAttribute('aria-expanded', isActive);
    });
});
