<template>
  <div class="chat-area">
    <div class="chat-header">
      <h3>{{ selectedName || 'Selecione um contato' }}</h3> <!-- Mostra nome do contato ou texto padrão -->
    </div>
    <div class="messages-container">
      <!-- Exibindo mensagens -->
      <div 
        v-for="message in messages" 
        :key="message.id" 
        :class="['message', message.sent ? 'sent' : 'received']">
        <!-- Passando texto e horário para o componente MessageBubble -->
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
import { EventBus } from '../eventBus';

export default {
  components: { MessageBubble },
  data() {
    return {
      messages: [],
      newMessage: "",
      number: null, 
      isChatSelected: false,
      errorMsg: "" 
    };
  },
  async created() {
    await this.fetchMessages();
    this.connectToWebSocket();
    EventBus.on('chatSelected', (data) => { 
    this.number = String(data.number);
    this.selectedName = data.name;
    this.fetchMessages();

    });
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
    },

    connectToWebSocket() {
      const ws = new WebSocket("ws://localhost:8002/ws");
      ws.onopen = () => {
        console.log("Conectado ao WebSocket");
      };

      ws.onmessage = (event) => {
        if (this.isChatSelected) {
          const message = JSON.parse(event.data);
          this.messages.push({
            id: this.messages.length + 1,
            text: message,
            time: new Date().toLocaleTimeString().slice(0, 5),
            sent: false
          });
        }
      };

      ws.onerror = (error) => {
        console.error("Erro no WebSocket:", error);
      };

      ws.onclose = () => {
        console.log("WebSocket desconectado");
      };
    },

    setChatNumber(id) {
      this.number = id;
      this.isChatSelected = true;
      this.fetchMessages();
    },
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
  margin: 0;
  padding: 0;
}

.chat-header {
  width: 100%;  
  padding: 15px;
  background-color: rgba(255, 255, 255, 0.6);
  justify-content: flex-start;
  align-items: center;
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