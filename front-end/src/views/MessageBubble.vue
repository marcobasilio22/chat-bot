<template>
  <div class="bubble">
    <p>{{ text }}</p>
    <span class="timeMessage">{{ time }}</span>
  </div>
</template>

<script>
export default {
  props: ['text', 'time'],
};
</script>

<style>
.bubble {
  background-color: #dcf8c6;
  border-radius: 10px;
  padding: 10px;
  position: relative;
  max-width: 60%;
  margin: 5px;
  word-wrap: break-word;
}

.bubble p {
  margin: 0;
  font-size: 14px;
  color: #333;
}

.timeMessage {
  font-size: 10px;
  color: #999;
  position: absolute;
  bottom: 5px;
  right: 10px;
}
</style>