document.addEventListener("DOMContentLoaded", () => {
    const clickedButtonTV = document.querySelector('.fa-clapperboard');
    const clickedButtonJournal = document.querySelector('.fa-newspaper');
    const tvHoncord = document.querySelector('.tvHoncord');
    const journalHoncord = document.querySelector('.journalHoncord');
    const loginForm = document.querySelector('.main-content');

    clickedButtonTV.addEventListener("click", () => {
        if (!clickedButtonTV.classList.contains('toggledButton')) {
            clickedButtonTV.classList.add('toggledButton'); 
            clickedButtonJournal.classList.remove('toggledButton');
            tvHoncord.style.display = 'flex'; 
            journalHoncord.style.display = 'none'; 
            loginForm.style.display = 'none';
        } else {
            clickedButtonTV.classList.remove('toggledButton'); 
            tvHoncord.style.display = 'none'; 
            loginForm.style.display = 'flex';
        }
    });

    clickedButtonJournal.addEventListener("click", () => {
        if (!clickedButtonJournal.classList.contains('toggledButton')) {
            clickedButtonJournal.classList.add('toggledButton'); 
            clickedButtonTV.classList.remove('toggledButton'); 
            journalHoncord.style.display = 'flex'; 
            tvHoncord.style.display = 'none'; 
            loginForm.style.display = 'none';
        } else {
            clickedButtonJournal.classList.remove('toggledButton'); 
            journalHoncord.style.display = 'none'; 
            loginForm.style.display = 'flex';
        }
    });

    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
});

function togglePassword(inputId, iconId) {
    var inputElement = document.querySelector('input[name="' + inputId + '"]');
    var iconElement = document.getElementById(iconId);

    inputElement.type = inputElement.type === "password" ? "text" : "password";
    iconElement.classList.toggle('fa-eye-slash');
    iconElement.classList.toggle('fa-eye');
}
