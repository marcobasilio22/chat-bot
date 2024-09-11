<template>
  <div class="chat-area">
    <div class="messages-container">
      <div v-for="message in messages" :key="message.id" :class="['message', message.sent ? 'sent' : 'received']">
        <MessageBubble :text="message.text" :time="message.time" />
      </div>
    </div>
    <div class="input-area">
      <input type="text" v-model="newMessage" placeholder="Digite uma mensagem" @keyup.enter="sendMessage" />
    </div>
  </div>
</template>

<script>
import MessageBubble from "./MessageBubble.vue";

export default {
  components: { MessageBubble },
  data() {
    return {
      messages: [
        { id: 1, text: "Oi!", time: "09:21", sent: true },
        { id: 2, text: "Oi! Tudo bem?", time: "09:22", sent: false },
      ],
      newMessage: "",
    };
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim() !== "") {
        this.messages.push({
          id: this.messages.length + 1,
          text: this.newMessage,
          time: new Date().toLocaleTimeString().slice(0, 5),
          sent: true,
        });
        this.newMessage = "";
      }
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