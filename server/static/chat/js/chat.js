const $chatMessages = Qs(".messages");

const setRoomActive = (room_id) => {
  QsAll(".list-rooms li").forEach((el) => el.classList.remove("active"));
  Qs(`#room-${room_id}`).classList.add("active");
  Qs("#selected-room").value = room_id;
};

const getMessages = async (room_id) => {
  const response = await fetch(`/chat/${room_id}`);  // Adicione o prefixo /chat/
  const html = await response.text();
  $chatMessages.innerHTML = html;
  setRoomActive(room_id);
};

const sendMessage = async (data) => {
  console.log(data);

  const response = await fetch(`/chat/${data.room_id}/send/`, {  // Adicione o prefixo /chat/
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": data.csrfmiddlewaretoken,
    },
    body: JSON.stringify(data),
  });
  const html = await response.text();
  const $uniqueMessageContainer = Qs(".unique-message-container");
  $uniqueMessageContainer.insertAdjacentHTML("beforeend", html);
  Qs(".send-message").reset();
};

let isCreatingRoom = false; // Flag para evitar múltiplas criações de sala

const createRoom = async (data) => {
  try {
    const response = await fetch('/chat/create-room/', {  // Certifique-se de que isso também está correto
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": data.csrfmiddlewaretoken,
      },
      body: JSON.stringify(data),
    });

    console.log("Resposta do servidor:", response);

    if (!response.ok) {
      throw new Error(`Erro: ${response.statusText}`);
    }

    const html = await response.text();
    const $listRooms = Qs(".list-rooms");
    $listRooms.insertAdjacentHTML("afterbegin", html);
    const modal = bootstrap.Modal.getInstance(Qs("#staticBackdrop"));
    modal.hide();
    Qs(".create-room").reset();
    getLastRoom();
  } catch (error) {
    console.error("Erro ao criar a sala:", error);
  }
};

// Interceptando o envio do formulário de criar sala
Qs(".create-room").addEventListener("submit", (e) => {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(e.target).entries());
  createRoom(data);
});

// Função para selecionar a última sala
const getLastRoom = () => {
  Qs(".list-rooms li").click();
};

// Interceptando o envio do formulário de enviar mensagem
Qs(".send-message").addEventListener("submit", (e) => {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(e.target).entries());
  sendMessage(data);
});

// Inicialização
getLastRoom();
