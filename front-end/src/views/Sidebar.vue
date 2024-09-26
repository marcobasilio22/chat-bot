<template>
  <div class="sidebar">
    <input type="text" placeholder="Procurar ou começar uma nova conversa" class="search-bar" />
    <div v-on:click="onClick(chat.id)" v-for="chat in chats" :key="chat.id" class="chat-preview">
      <img :src="getAvatarSrc(chat.avatar)" alt="avatar" class="avatar" />
      <div class="chat-info">
        <h4>{{ chat.name }}</h4>
        <p>{{ chat.lastMessage }}</p>
      </div>
      <span class="time">{{ chat.lastTime }}</span>
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

export default {
  components: {
    NewContact
  },
  data() {
    return {
      chats: [
        { id: 5511937590095, name: "Pessoal", lastMessage: " ", lastTime: "09:21", avatar: "avatar.jpg" },
        { id: 5511912246642, name: "Bot ", lastMessage: " ", lastTime: "09:21", avatar: "avatar.jpg" },
        { id: 5519999768346, name: "Lopes ", lastMessage: " ", lastTime: "09:21", avatar: "avatar.jpg" },
      ],
      showModal: false 
    };
  },
  methods: {
    getAvatarSrc(avatar) {
      return avatar ? require(`@/assets/${avatar}`) : defaultAvatar;
    },
    onClick(id) {
      EventBus.emit('chatSelected', id);
    },
    onNewContactClick() {
      this.showModal = true; 
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

.sidebar {
  height: 100vh;
  width: 30%;
  background-color: #f0f0f0;
  padding: 10px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
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
