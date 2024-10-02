<template>
    <div v-if="isVisible" class="modal-overlay">
      <div class="modal-content">
        <h2>Criar Novo Contato</h2>
        <input type="text" v-model="name" placeholder="Nome" class="input-field" required />
        <input
          type="text"
          v-model="number"
          placeholder="Número"
          class="input-field"
          @focus="setDefaultNumber"
          required
        />
        <div class="button-group">
            <button @click="submitForm" class="button create" :disabled="number.length < 13">Criar</button>
            <button @click="closeModal" class="button cancel">Fechar</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from '../axios/axios';
  
  export default {
    props: {
      isVisible: {
        type: Boolean,
        default: false
      }
    },
    data() {
      return {
        name: '',
        number: '55'
      };
    },
    methods: {
      closeModal() {
        this.$emit('close');
      },
      async submitForm() {
        const newContact = {
          name: this.name,
          number: this.number
        };
        
        try {
          const response = await axios.post('/createcontact', newContact);
  
          if (response.status === 200) {
            console.log('Novo contato criado:', response.data);
            this.$emit('contactCreated', newContact); 
            this.closeModal();
          }
        } catch (error) {
          console.error('Erro ao criar o contato:', error);
        }
      },
      setDefaultNumber() {
        if (this.number === '') {
          this.number = '55';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .modal-overlay {
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
    background-color: #ffffff;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    width: 400px;  
    text-align: center;  
  }
  
  h2 {
    margin-bottom: 20px;
    color: #333;
  }
  
  .input-field {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    transition: border-color 0.3s;
  }
  
  .input-field:focus {
    border-color: #007bff; 
    outline: none;
  }
  
  .button-group {
    display: flex;
    justify-content: space-between; 
  }
  
  .button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s; 
  }
  
  .create {
    background-color: #007bff; 
    color: white;
  }
  
  .create:hover {
    background-color: #0056b3; 
  }
  
  .cancel {
    background-color: #f44336; 
    color: white;
  }
  
  .cancel:hover {
    background-color: #d32f2f;
  }
  </style>
  