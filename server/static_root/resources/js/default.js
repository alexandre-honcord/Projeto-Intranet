document.addEventListener("DOMContentLoaded", () => {
    const clickedButtonTV = document.querySelector('.fa-clapperboard');
    const clickedButtonJournal = document.querySelector('.fa-newspaper');
    const clickedButtonFunctions = document.querySelector('.fa-compass');
    const tvHoncord = document.querySelector('.tvHoncord');
    const journalHoncord = document.querySelector('.journalHoncord');
    const appsWindow = document.querySelector('.apps');
    const loginBlock = document.querySelector('.main-content [data-block="login"]');
    const homeBlock = document.querySelector('.main-content [data-block="home"]');

    const offcanvasElementList = document.querySelectorAll('.offcanvas');
    const offcanvasList = [...offcanvasElementList].map(offcanvasEl => new bootstrap.Offcanvas(offcanvasEl));

    function toggleVisibility(activeButton, inactiveButton, activeContent, inactiveContent) {
        const isActive = activeButton.classList.contains('toggledButton');

        activeButton.classList.toggle('toggledButton', !isActive);

        if (!isActive) {
            if (activeContent) {
                activeContent.style.display = 'block';
                if (loginBlock) loginBlock.style.display = 'none';
                if (homeBlock && activeButton !== clickedButtonFunctions) homeBlock.style.display = 'none';
            }
        } else {
            if (activeContent) {
                activeContent.style.display = 'none';
                if (!clickedButtonTV.classList.contains('toggledButton') && !clickedButtonJournal.classList.contains('toggledButton')) {
                    if (loginBlock) loginBlock.style.display = 'flex';  
                    if (homeBlock) homeBlock.style.display = 'block';    
                }
            }
        }

        const buttons = [clickedButtonTV, clickedButtonJournal];
        buttons.forEach(button => {
            if (button !== activeButton && button.classList.contains('toggledButton')) {
                button.classList.remove('toggledButton');
                const correspondingContent = button === clickedButtonTV ? tvHoncord : journalHoncord;
                if (correspondingContent) correspondingContent.style.display = 'none';
            }
        });
    }

    // Event listeners for buttons
    if (clickedButtonFunctions) {
        clickedButtonFunctions.addEventListener("click", () => {
            toggleVisibility(clickedButtonFunctions, null, appsWindow);
        });
    }

    if (clickedButtonTV) {
        clickedButtonTV.addEventListener("click", () => {
            toggleVisibility(clickedButtonTV, clickedButtonJournal, tvHoncord, journalHoncord);
        });
    }

    if (clickedButtonJournal) {
        clickedButtonJournal.addEventListener("click", () => {
            toggleVisibility(clickedButtonJournal, clickedButtonTV, journalHoncord, tvHoncord);
        });
    }

    // Tooltips com delay de 5 segundos no hover
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltipTriggerList.forEach(tooltipTriggerEl => {
        let tooltipInstance;
        let tooltipTimeout;

        const showTooltip = () => {
            tooltipTimeout = setTimeout(() => {
                tooltipInstance = new bootstrap.Tooltip(tooltipTriggerEl);
                tooltipInstance.show();
            }, 500);
        };

        const hideTooltip = () => {
            clearTimeout(tooltipTimeout);
            if (tooltipInstance) {
                tooltipInstance.hide();
                tooltipInstance.dispose();
                tooltipInstance = null;
            }
        };

        tooltipTriggerEl.addEventListener('mouseover', showTooltip);
        tooltipTriggerEl.addEventListener('mouseout', hideTooltip);
    });
});

// Function to toggle password visibility
function togglePassword(inputId, iconId) {
    const inputElement = document.querySelector(`input[name="${inputId}"]`);
    const iconElement = document.getElementById(iconId);

    if (inputElement && iconElement) {
        inputElement.type = inputElement.type === "password" ? "text" : "password";
        iconElement.classList.toggle('fa-eye-slash');
        iconElement.classList.toggle('fa-eye');
    }
}
