<template>
  <div class="container">
    <Sidebar />
    <ChatArea />
  </div>
</template>

<script>
import Sidebar from '@/views/Sidebar.vue';
import ChatArea from '@/views/ChatArea.vue';

export default {
  components: {
    Sidebar,
    ChatArea,
  }
};
</script>

<style>
.container {
  display: flex;
  height: 100%; 
  width: 100%;  
}

@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
}
</style>
