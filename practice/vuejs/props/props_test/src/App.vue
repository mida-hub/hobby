<template>
  <div id="app">
    <buttonmark name="John"></buttonmark>
    <p>
      <input v-model = "nameParent">
    </p>
    <buttonmark :name="nameParent"></buttonmark>
  </div>
</template>

<script>
import buttonmark from './buttonmark.vue'

export default {
  name: 'App',
  components: {
    buttonmark
  },
  data: function () {
    return {
      nameParent: ''
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
