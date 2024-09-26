<template>
  <div class="bubble" :class="{'sent': sent, 'received': !sent}">
    <p>{{ text }}</p>
    <span class="timeMessage">{{ time }}</span>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true,
    },
    time: {
      type: String,
      required: true,
    },
    sent: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style>
.bubble {
  background-color: #dcf8c6; 
  border-radius: 10px;
  padding: 10px; 
  position: relative;
  max-width: 100%;
  min-width: 50px;
  margin: 5px;
  word-wrap: break-word;
  overflow-wrap: anywhere; 
  display: inline-block; 
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); 
  white-space: nowrap;
}

.bubble p {
  margin: 0; 
  font-size: 13px; 
  color: #333; 
  white-space: nowrap; 
}


.timeMessage {
  font-size: 10px; 
  color: #999; 
  position: absolute; 
  bottom: 1px;
  right: 10px; 
}

</style>
