<template>
  <div>
    <h2>タスク一覧</h2>
    <h3>{{ message }}</h3>
    <ul>
      <li v-for="task in tasks" v-bind:key="task.id">
        <input type="checkbox" v-bind:checked="task.done">
        {{ task.name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  computed: {
    message() {
      return this.$store.getters.message
    },
    tasks() {
      return this.$store.getters.tasks
    }
  },
}
</script>
