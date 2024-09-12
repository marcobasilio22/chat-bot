<template>
  <div class="sidebar">
    <input type="text" placeholder="Procurar ou começar uma nova conversa" class="search-bar" />
    <div v-for="chat in chats" :key="chat.id" class="chat-preview">
      <img :src="getAvatarSrc(chat.avatar)" alt="avatar" class="avatar" />
      <div class="chat-info">
        <h4>{{ chat.name }}</h4>
        <p>{{ chat.lastMessage }}</p>
      </div>
      <span class="time">{{ chat.lastTime }}</span>
    </div>
  </div>
</template>

<script>

import defaultAvatar from '@/assets/avatar.jpg';

export default {
  data() {
    return {
      chats: [
        { id: 1, name: "Maria", lastMessage: "Oi!", lastTime: "09:21", avatar: "avatar.jpg" }
      ],
    };
  },
  methods: {
    getAvatarSrc(avatar) {
      return avatar
        ? require(`@/assets/${avatar}`)
        : defaultAvatar; 
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
}

.search-bar {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: none;
  border-radius: 20px;
  background-color: #fff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.chat-preview {
  display: flex;
  align-items: flex-start;
  padding: 15px 10px;
  cursor: pointer;
  border-bottom: 1px solid #e0e0e0;
  transition: background-color 0.3s;
  position: relative;
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
  position: absolute;
  top: 15px;
  right: 10px;
}


</style>
