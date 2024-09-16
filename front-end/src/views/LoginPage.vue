<template>
  <div class="login-container">
    <div class="login-box">
      <img src="@/assets/logo.png" alt="Logo" class="logo" />
      <h2>Bem Vindo(a) de Volta :D</h2>
      <p>Entre com a sua conta</p>
      <button class="google-login-btn">
        <img src="@/assets/google-logo.png" alt="Google Logo" />
        Fazer login com o Google
      </button>
      <div class="divider">
        <span>OU</span>
      </div>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="email">E-mail</label>
          <input type="email" id="email" v-model="email" placeholder="cliente@albsolution.com.br" required />
        </div>
        <div class="form-group">
          <label for="password">Senha</label>
          <input type="password" id="password" v-model="password" placeholder="Digite sua senha" required />
          <a href="#" class="forgot-password">Esqueceu sua senha?</a>
        </div>
        <div v-if="errorMsg" class="error-message">
          {{ errorMsg }}
        </div>
        <button type="submit" class="login-btn">Entrar</button>
      </form>
    </div>
  </div>
</template>
// src/views/LoginPage.vue
<script>
  import axios from '../axios/axios';
  import router from '../router';

  export default {
    data() {
      return {
        errorMsg: '',
        email: '',
        password: ''
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.get('/login', {
            params: {
              email: this.email,
              password: this.password
            },
          });
          if (response.status === 200) {
            router.push('/home');
          }
        } catch (error) {
          if (error.response && error.response.status === 500) {
            this.errorMsg = 'Usuário ou senha inválidos. Tente novamente.';
          } else {
            this.errorMsg = 'Erro interno do servidor. Tente novamente mais tarde.';
          }
          console.error('Erro durante o login:', error);
        }
      }
    }
  }
</script>


<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f9f9f9;
}

.login-box {
  width: 360px;
  padding: 20px;
  background: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.logo {
  width: 100px;
  margin-bottom: 20px;
}

h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

p {
  font-size: 16px;
  color: #666;
}

.google-login-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  background: #fff;
  border: 1px solid #ddd;
  cursor: pointer;
}

.google-login-btn img {
  width: 20px;
  margin-right: 10px;
}

.divider {
  position: relative;
  margin: 20px 0;
  text-align: center;
  color: #666;
}

.divider span {
  background: #fff;
  padding: 0 10px;
  position: relative;
  z-index: 1;
}

.divider::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: 1px;
  background: #ddd;
  z-index: 0;
}

.form-group {
  margin-bottom: 20px;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #666;
}

input {
  width: 95%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.forgot-password {
  display: block;
  margin-top: 10px;
  font-size: 14px;
  color: #007bff;
  text-align: right;
  text-decoration: none;
}

.forgot-password:hover {
  text-decoration: underline;
}

.login-btn {
  width: 100%;
  padding: 10px;
  background: #007bff;
  border: none;
  color: #fff;
  border-radius: 4px;
  cursor: pointer;
}

.login-btn:disabled {
  background: #ddd;
  cursor: not-allowed;
}

.error-message {
  width: 80%;
  height: 60px;
  padding: 30px;
  color: red;
}
</style>