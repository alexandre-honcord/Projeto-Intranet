document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.querySelector('.move-sidebar');
    const sidebar = document.querySelector('.sidebar');
    
    // Verifica o estado inicial da barra lateral ao carregar a página
    if (localStorage.getItem('bar') === 'off') {
        sidebar.classList.remove('active'); // Se 'off', garante que a barra lateral esteja oculta
    } else {
        sidebar.classList.add('active'); // Se não, garante que a barra lateral esteja visível
    }

    toggle.addEventListener("click", () => {
        // Alterna a visibilidade da barra lateral
        sidebar.classList.toggle('active');
        
        // Altera a classe do ícone e atualiza o localStorage
        if (sidebar.classList.contains('active')) {
            toggle.classList.remove('fa-caret-left'); 
            toggle.classList.add('fa-caret-right'); 
            localStorage.setItem('bar', 'on'); // Salva o estado como 'on'
        } else {
            toggle.classList.remove('fa-caret-right'); 
            toggle.classList.add('fa-caret-left'); 
            localStorage.setItem('bar', 'off'); // Salva o estado como 'off'
        }
    });
});