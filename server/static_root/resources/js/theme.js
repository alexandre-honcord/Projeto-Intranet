document.addEventListener("DOMContentLoaded", () => {
    const themeMode = document.querySelector('.theme');

    // Verifica o tema armazenado e aplica
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-theme');
        themeMode.classList.remove('fa-moon');
        themeMode.classList.add('fa-sun');
    }

    // Evento de clique para alternar o tema
    themeMode.addEventListener('click', () => {
        // Verifica se o ícone atual é o de lua
        if (themeMode.classList.contains('fa-moon')) {
            // Muda para o ícone de sol
            themeMode.classList.remove('fa-moon');
            themeMode.classList.add('fa-sun');
            document.body.classList.add('dark-theme');
            localStorage.setItem('theme', 'dark'); // Armazena a preferência
        } else {
            // Muda para o ícone de lua
            themeMode.classList.remove('fa-sun');
            themeMode.classList.add('fa-moon');
            document.body.classList.remove('dark-theme'); // Remove o tema escuro
            localStorage.setItem('theme', 'light'); // Armazena a preferência
        }
    });
}); 
