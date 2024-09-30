<template>
  <div class="sidebar">
    <input type="text" placeholder="Procurar ou começar uma nova conversa" class="search-bar" />
    <div v-on:click="onClick(chat.number)" v-for="chat in chats" :key="chat.number" class="chat-preview">
      <img :src="getAvatarSrc(chat.avatar)" alt="avatar" class="avatar" />
      <div class="chat-info">
        <h4>{{ chat.name }}</h4>
        <p>{{ chat.lastMessage || 'Nenhuma mensagem ainda' }}</p>
      </div>
      <span class="time">{{ chat.lastTime || 'Agora' }}</span>
    </div>
    <div class="newcontact" @click="onNewContactClick">
      <img src="@/assets/bottonnew.png" alt="botton of new" width="55" height="auto" />
    </div>
    
    <NewContact v-if="showModal" :isVisible="showModal" @close="showModal = false" />
  </div>
</template>

<script>
import { EventBus } from '../eventBus';
import defaultAvatar from '@/assets/avatar.jpg';
import NewContact from './NewContact.vue'; 
import axios from '../axios/axios';

export default {
  components: {
    NewContact
  },
  data() {
    return {
      chats: [],
      lastMessages: {},
      showModal: false 
    };
  },
  mounted() {
    this.getContacts();
  },
  methods: {
    getAvatarSrc(avatar) {
      return avatar ? require(`@/assets/${avatar}`) : defaultAvatar;
    },
    onClick(number) {
      EventBus.emit('chatSelected', number);
    },
    onNewContactClick() {
      this.showModal = true; 
    },
    async getContacts() {
      try {
        const responseContacts = await axios.get('/listcontact');
        const contacts = responseContacts.data.data;

        const responseMessages = await axios.get('/lastmessage');
        const messages = responseMessages.data.data;

        const messageMap = {};
        const timeMap = {};
        messages.forEach(msg => {
          messageMap[msg.customer_id] = msg.message;
          timeMap[msg.customer_id] = msg.date;
        });

        this.chats = contacts.map(contact => {
          const lastMessage = messageMap[contact.id] || '';
          const lastTime = timeMap[contact.id] || ''; 
          
          const formattedTime = lastTime ? new Date(lastTime).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : '';
          
          return {
            number: contact.number,
            name: contact.name,
            lastMessage: lastMessage,
            lastTime: formattedTime, 
            avatar: 'avatar.jpg'
          };
        });

      } catch (error) {
        console.error("Erro ao obter contatos:", error);
      }
    }
  }
};
</script>


<style>

.sidebar {
  height: 100%;
  width: 30%; 
  background-color: #f0f0f0;
  padding: 10px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
  position: relative;
}

.chat-preview {
  display: flex;
  align-items: flex-start;
  padding: 15px 10px;
  cursor: pointer;
  border-bottom: 1px solid #e0e0e0;
  transition: background-color 0.3s;
}

.chat-preview:hover {
  background-color: #e6e6e6;
}

.avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 15px;
}

.chat-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  flex-grow: 1;
}

.chat-info h4 {
  margin: 0;
  font-size: 16px;
  font-weight: 500;
}

.chat-info p {
  margin: 0;
  margin-top: 5px;
  color: #666;
  font-size: 14px;
}

.time {
  font-size: 12px;
  color: #999;
  position: relative;
  margin-left: 10px;
  white-space: nowrap;
  align-self: flex-start; 
}

.newcontact {
  position: fixed; 
  bottom: 20px; 
  right: 85rem; 
  z-index: 100; 
  display: flex;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.2s ease;
}
</style>
