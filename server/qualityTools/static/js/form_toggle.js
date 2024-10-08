// form_toggle.js

document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');

    if (form) {
        var opportunityOption = form.querySelector('#opportunityOption');
        var notificationOption = form.querySelector('#notificationOption');
        var opportunityFields = form.querySelector('#opportunityFields');
        var notificationFields = form.querySelector('#notificationFields');
        var errorOptions = form.querySelector('#errorOptions');

        function toggleFields() {
            if (opportunityOption.checked) {
                opportunityFields.style.display = 'block';
                notificationFields.style.display = 'none';
            } else if (notificationOption.checked) {
                notificationFields.style.display = 'block';
                opportunityFields.style.display = 'none';
            }
        }

        // Verifica inicialmente e sempre que houver mudança no radio group
        toggleFields();
        form.addEventListener('change', function() {
            toggleFields();
        });

        // Validação antes do envio do formulário
        form.addEventListener('submit', function(event) {
            if (!opportunityOption.checked && !notificationOption.checked) {
                errorOptions.textContent = 'Por favor, escolha uma opção.';
                event.preventDefault();  // Impede o envio do formulário
            } else {
                errorOptions.textContent = '';
            }
        });
    }
});
