<template>
    <div v-if="isVisible" class="modal-overlay">
        <div class="modal">
            <div class="modal-header">
                <h3>Criar Novo Contato</h3>
                <button @click="closeModal">X</button>
            </div>
            <div class="modal-body">
                <form @submit.prevent="submitForm">
                    <label for="name">Nome:</label>
                    <input type="text" id="name" v-model="name" required />
                    <label for="number">Número:</label>
                    <input type="text" id="number" v-model="number" required />
                    <button type="submit">Criar</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '../axios/axios';

export default {
    props: ['isVisible'],
    data() {
        return {
            name: '',
            number: '' 
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
                    this.closeModal();
                }
            } catch (error) {
                console.error('Erro ao criar o contato:', error);
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
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal {
    background: white;
    padding: 20px;
    border-radius: 8px;
    width: 300px;
    max-width: 80%;
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.modal-body {
    margin-top: 20px;
}
</style>
