<template>
  <div class="chat-area">
    <div class="messages-container">
      <div v-for="message in messages" :key="message.id" :class="['message', message.sent ? 'sent' : 'received']">
        <MessageBubble :text="message.text" :time="message.time" />
      </div>
    </div>
    <div class="input-area">
      <input
        type="text"
        v-model="newMessage"
        placeholder="Digite uma mensagem"
        @keyup.enter="sendMessage"
      />
    </div>
  </div>
</template>

<script>
import MessageBubble from "./MessageBubble.vue";
import axios from '../axios/axios';

export default {
  components: { MessageBubble },
  data() {
    return {
      messages: [], 
      newMessage: "",
      number: "5511937590095", 
      errorMsg: "",
      socket: null,
    };
  },
  async created() {
    await this.fetchMessages();
    this.setupWebSocket();
  },
  beforeUnmount() { // Atualizado para beforeUnmount
    if (this.socket) {
      this.socket.close();
    }
  },
  methods: {
    async fetchMessages() {
      try {
        const response = await axios.get(`/messages/${this.number}`);
        this.messages = response.data.messages;
      } catch (error) {
        console.error('Erro ao buscar mensagens:', error);
        this.errorMsg = 'Erro ao buscar mensagens. Tente novamente.';
      }
    },
    
    setupWebSocket() {
      this.socket = new WebSocket("ws://localhost:8000/ws/chat");

      this.socket.onmessage = (event) => {
        const message = event.data;
        this.messages.push({
          id: this.messages.length + 1,
          text: message,
          time: new Date().toLocaleTimeString().slice(0, 5),
          sent: false
        });
      };

      this.socket.onopen = () => {
        console.log("Conexão WebSocket estabelecida.");
      };

      this.socket.onerror = (error) => {
        console.error("Erro na conexão WebSocket:", error);
      };

      this.socket.onclose = () => {
        console.log("Conexão WebSocket fechada.");
      };
    },
    
    async endPoint() {
      try {
        const response = await axios.post('/chat', {
          number: this.number,
          textMessage: { text: this.newMessage }
        });
        if (response.status === 200) {
          this.messages.push({
            id: this.messages.length + 1,
            text: this.newMessage,
            time: new Date().toLocaleTimeString().slice(0, 5),
            sent: true
          });
          this.newMessage = "";
        }
      } catch (error) {
        if (error.response && error.response.status === 500) {
          this.errorMsg = 'Erro ao enviar a mensagem. Tente novamente.';
        } else {
          this.errorMsg = 'Erro interno do servidor. Tente novamente mais tarde.';
        }
        console.error('Erro durante o envio:', error);
      }
    },
    
    sendMessage() {
      if (this.newMessage.trim() !== "") {
        this.endPoint();
      }
    }
  },
};
</script>

<style>
.chat-area {
  height: 100vh;
  width: 70%;
  padding: 10px;
  background-color: #e5ddd5;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.messages-container {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  overflow-y: auto;
}

.message {
  margin: 3px 0;
}

.sent {
  align-self: flex-end;
}

.received {
  align-self: flex-start;
}

.input-area {
  padding: 10px;
  background-color: #fff;
}

input {
  width: 100%;
  padding: 10px;
}
</style>