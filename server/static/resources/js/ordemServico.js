// Armazenar valores selecionados
const selectedValues = {
    ordem: null,
    tipoOrdem: null,
    classificacao: null,
    descricao: null,
    anexo: null,
    dano: null,
};

// Função para mostrar a seção de classificação da Ordem de Serviço
function showClassificacao() {
    const classificacaoAccordion = document.getElementById('flush-collapseTwo');
    classificacaoAccordion.classList.add('show'); // Mostra a seção de classificação
    console.log("Classificação da Ordem de Serviço aberta.");
}
// Função para mostrar a seção de classificação da Ordem de Serviço
function showOrdemTipo() {
    const classificacaoAccordion = document.getElementById('flush-collapseThree');
    classificacaoAccordion.classList.add('show'); // Mostra a seção de classificação
    console.log("Tipo de Ordem de Serviço aberta.");
}
// Função para mostrar a seção de tipo de ordem
function showTipoOrdem() {
    const tipoOrdemItem = document.getElementById('tipoOrdemItem');
    tipoOrdemItem.style.display = 'block'; // Mostra "Tipo de Ordem de Serviço"
}

// Adiciona listeners aos botões de Ordem de Serviço
document.querySelectorAll('#accordionFlushExample .nav-link').forEach(item => {
    item.addEventListener('click', function() {
        selectedValues.ordem = item.getAttribute('data-value'); // Armazena a ordem
        console.log("Ordem de Serviço selecionada:", selectedValues.ordem); // Log para verificar o valor

        // Mostra a seção de classificação
        showClassificacao();

        // Reseta a seleção anterior
        selectedValues.classificacao = null;
        const tipoOrdemItem = document.getElementById('tipoOrdemItem');
        tipoOrdemItem.style.display = 'none'; // Esconde tipo de ordem ao selecionar nova ordem

        // Se "Tecnologia da Informação" for selecionada, mostra a seção de tipo de ordem
        if (selectedValues.ordem === 'ti') {
            showTipoOrdem(); // Chama a função para mostrar o tipo de ordem
        }
    });
});

// Adiciona listeners aos botões de classificação
document.querySelectorAll('#accordionFlushExample2 .nav-link').forEach(item => {
    item.addEventListener('click', function() {
        selectedValues.classificacao = item.getAttribute('data-value'); // Armazena a classificação
        console.log("Classificação selecionada:", selectedValues.classificacao); // Log para verificar o valor

        showOrdemTipo(); // Chama a função para mostrar o tipo de ordem

    });
});

// Adiciona listeners aos botões de tipo de ordem
document.querySelectorAll('#accordionFlushExample3 .nav-link').forEach(item => {
    item.addEventListener('click', function() {
        selectedValues.tipoOrdem = item.getAttribute('data-value'); // Armazena o tipo de ordem
        console.log("Tipo de Ordem selecionado:", selectedValues.tipoOrdem); // Log para verificar o valor
    });
});

// Captura o evento de envio do formulário
document.getElementById('ordemServicoForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    // Captura os dados do formulário
    selectedValues.descricao = document.getElementById('exampleFormControlInput1').value; // Captura descrição
    selectedValues.dano = document.getElementById('exampleFormControlTextarea1').value; // Captura dano

    console.log("Dados a serem enviados:", selectedValues); // Log para verificar todos os dados

    // Envia os dados para o Django usando fetch
    const formData = new FormData(this);
    formData.append('tipo_ordem', selectedValues.tipoOrdem);
    formData.append('classificacao_ordem', selectedValues.classificacao);
    formData.append('descricao_ordem', selectedValues.descricao);
    formData.append('dano_ordem', selectedValues.dano);

    fetch('/processar-ordem/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}', // Adicione o token CSRF
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log("Resposta do Django:", data); // Log para verificar a resposta
    })
    .catch(error => console.error('Erro:', error));
});

// Inicializa o acordeão de Ordem de Serviço
document.addEventListener('DOMContentLoaded', function() {
    const ordemServicoButton = document.querySelector('#home-tab2');
    if (ordemServicoButton) {
        ordemServicoButton.click(); // Simula um clique inicial para abrir a Ordem de Serviço
    }
});
function checkForm() {
    const descricao = document.getElementById('exampleFormControlInput1').value;
    const dano = document.getElementById('exampleFormControlTextarea1').value;
    const submitBtn = document.getElementById('submitBtn');
    
    // Verifica se todos os campos obrigatórios estão preenchidos
    if (descricao && dano) {
        submitBtn.disabled = false; // Habilita o botão se todos os campos estão preenchidos
    } else {
        submitBtn.disabled = true; // Desabilita o botão se algum campo estiver vazio
    }
};
// Função para limpar variáveis e redirecionar
function limparERedirecionar() {
    // Limpa as variáveis
    for (const key in selectedValues) {
        selectedValues[key] = null;
    }

    // Redireciona para /painelOrdemServico
    window.location.href = '/painel/OrdemServico';
};

// Adiciona listener ao botão "Cancelar"
document.getElementById('cancelarBtn').addEventListener('click', limparERedirecionar);
