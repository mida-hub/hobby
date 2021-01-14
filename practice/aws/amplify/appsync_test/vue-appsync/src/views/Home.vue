<template>
  <v-container>
    <h3>AppSync Tasks</h3>
    <v-form>
      <v-text-field
      v-model="taskTitle"
      label="タスク名"
      ></v-text-field>
    </v-form>
    <v-btn @click="createTask()">タスク追加</v-btn>
    <v-flex xs4 v-for="(task, index) in tasks" :key="index">
      <div>
        <h4 class="headline mb-0">{{ task.title }}</h4>
        <h4 class="headline mb-0">{{ task.id }}</h4>
        <h4 class="headline mb-0">{{ task.completed }}</h4>
        <v-btn @click="toggleComplete(task)">更新</v-btn>
        <v-btn @click="deleteTask(task)">削除</v-btn>
      </div>
    </v-flex>
  </v-container>
</template>

<script>
import taskService from '../services/taskService'
export default {
  name: 'Home',
  data () {
    return {
      taskTitle: '',
      tasks: [],
      deleteDialog: false
    }
  },
  methods: {
    async createTask () {
      console.log(this.taskTitle);
      await taskService.createTask(this.taskTitle)
      this.tasks = await taskService.getTasks()
      this.taskTitle = ''
    },
    async toggleComplete (task) {
      const taskDetails = {
        id: task.id,
        completed: !task.completed
      }
      await taskService.updateTask(taskDetails)
      this.tasks = await taskService.getTasks()
    },
    async deleteTask (task) {
      await taskService.deleteTask(task.id)
      this.tasks = await taskService.getTasks()
    }
  },
  async mounted () {
    this.tasks = await taskService.getTasks()
  }
}
</script>
