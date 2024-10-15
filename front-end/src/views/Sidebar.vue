<template>
  <div class="sidebar">
    <input type="text" placeholder="Procurar ou começar uma nova conversa" class="search-bar" />
    <div 
      @contextmenu.prevent="handleRightClick($event, chat.number, chat.name)" 
      v-on:click="onClick(chat.number)" 
      v-for="chat in chats" 
      :key="chat.number" 
      class="chat-preview"
    >
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

    <div v-if="showRenameModal" class="modal">
      <div class="modal-content">
        <h3>Renomear Contato</h3>
        <input type="text" v-model="newName" placeholder="Novo nome" />
        <button @click="renameContact(selectedNumber, newName)">Renomear</button>
        <button @click="showRenameModal = false">Cancelar</button>
      </div>
    </div>

    <div v-if="showContextMenu" :style="{ top: `${menuY}px`, left: `${menuX}px` }" class="context-menu">
      <ul>
        <li @click="deleteContact(selectedNumber)">Deletar Contato</li>
        <li @click="openRenameForm(selectedNumber, selectedName)">Renomear Contato</li>
        <li @click="deleteMessages(selectedNumber)">Deletar Mensagens</li>
      </ul>
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
      showModal: false,
      showContextMenu: false,
      showRenameModal: false, 
      menuX: 0,
      menuY: 0,
      selectedNumber: null,
      selectedName: '', 
      newName: ''  
    };
  },
  mounted() {
    this.getContacts();
    document.addEventListener('click', this.handleClickOutside);
  },
  beforeUnmount() {
    document.removeEventListener('click', this.handleClickOutside);
  },
  methods: {
    openRenameForm(number, name) {
      this.selectedNumber = number;
      this.selectedName = name;
      this.newName = name;
      this.showRenameModal = true; 
      this.showContextMenu = false;  
    },

    renameContact(number, newName) {
      if (newName.trim()) { 
        this.func_rename_contact(number, newName); 
        this.showRenameModal = false; 
      } else {
        alert("O nome não pode estar vazio."); 
      }
    },

    handleRightClick(event, number, name) {
      event.preventDefault();
      this.menuX = event.clientX;
      this.menuY = event.clientY;
      this.selectedNumber = number;
      this.selectedName = name;
      this.showContextMenu = true;
    },
    
    handleClickOutside(event) {
      const contextMenu = this.$el.querySelector('.context-menu');
      if (contextMenu && !contextMenu.contains(event.target)) {
        this.showContextMenu = false;
        this.showRenameModal = false; 
      }
    },
    
    deleteContact(number) {
      axios.delete(`/delete_contact/${number}`)
        .then(response => {
          console.log(response.data.message);
          this.getContacts(); 
        })
        .catch(error => {
          const errorMessage = error.response?.data?.detail || "Erro desconhecido ao apagar contato";
          console.error("Erro ao apagar contato:", errorMessage);
        });
    },

    deleteMessages(number) {
    axios.delete(`/delete_messages/${number}`)
        .then(response => {
            console.log(response.data.message);
            this.getContacts();
        })
        .catch(error => {
            const errorMessage = error.response?.data?.detail || "Erro desconhecido ao apagar mensagens";
            console.error("Erro ao apagar mensagens:", errorMessage);
        });
    },

    func_rename_contact(number, newName) {
      axios.post('/renamecontact', {
          number: number,
          new_name: newName
      })
      .then(response => {
          console.log("Contato renomeado com sucesso:", response.data);
          this.getContacts(); 
      })
      .catch(error => {
          const errorMessage = error.response?.data?.detail || "Erro desconhecido ao renomear contato";
          console.error("Erro ao renomear contato:", errorMessage);
      });
    },

    getAvatarSrc(avatar) {
      return avatar ? require(`@/assets/${avatar}`) : defaultAvatar;
    },
    
    onClick(number) {
      EventBus.emit('chatSelected', number);
    },
    
    onNewContactClick() {
      this.showModal = true; 
    },
    

    // CONTINUAR A CONFIGURAR O WEBSOCKET
    connectToWebSocket() {
      const ws = new WebSocket("ws://localhost:8765/ws");
      ws.onopen = () => {
        console.log("Conectado ao WebSocket");
      };

      ws.onmessage = (event) => {
        const message = event.data;
        this.messages.push({
          id: this.messages.length + 1,
          text: message,
          time: new Date().toLocaleTimeString().slice(0, 5),
          sent: false
        });
      };
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
          let formattedTime = '';
          if (lastTime) {
            const messageDate = new Date(lastTime);
            const today = new Date();

            if (messageDate.toDateString() === today.toDateString()) {
              formattedTime = messageDate.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            } else {
              formattedTime = messageDate.toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit' });
            }
          }
          return {
            number: contact.number,
            name: contact.name,
            lastMessage: lastMessage,
            lastTime: formattedTime, 
            avatar: contact.avatar || 'avatar.jpg'
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
  height: 100vh;
  width: 30%;
  background-color: #f0f0f0;
  padding: 10px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
  position: relative; 
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

.context-menu {
  position: absolute;
  background-color: white;
  border: 1px solid #ccc;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  padding: 10px;
}

.context-menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.context-menu li {
  padding: 8px 12px;
  cursor: pointer;
}

.context-menu li:hover {
  background-color: #f0f0f0;
}


.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 300px; /* Ajuste a largura conforme necessário */
}

.rename-contact-form {
  display: flex;
  flex-direction: column;
  margin-top: 10px;
}

.rename-contact-form input {
  margin-bottom: 5px;
}
</style>
