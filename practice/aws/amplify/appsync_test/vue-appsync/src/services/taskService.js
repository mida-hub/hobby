import { API, graphqlOperation } from 'aws-amplify'
export default {
  async getTasks () {
    const listTasks = `query listTasks {
      listTasks {
        items {
          id
          title
          completed
        }
      }
    }`
const tasks = await API.graphql(graphqlOperation(listTasks))
    return tasks.data.listTasks.items
  },
  async createTask(taskTitle) {
    const createTask = `
    mutation createTask($title: String!, $completed: Boolean!) {
      createTask(
        input: {
          title: $title, completed: $completed
        }
      ) {
        id
      }
    }
    `
const taskDetails = {
      title: taskTitle,
      completed: false
    }
const newTask = await API.graphql(graphqlOperation(createTask, taskDetails))
    return newTask
  },
  async updateTask(taskDetails) {
    const updateTask = `
    mutation updateTask($id: ID!, $completed: Boolean!) {
      updateTask(
        input: {
          id: $id
          completed: $completed
        }
      ) {
        completed
      }
    }
    `
const updatedTask = await API.graphql(graphqlOperation(updateTask, taskDetails))
    return updatedTask
  },
  async deleteTask(taskId) {
    const deleteTask = `
    mutation deleteTask($id: ID!) {
      deleteTask(
        input: {
          id: $id
        }
      ) {
        id
      }
    }
    `
const taskDetails = {
      id: taskId
    }
return API.graphql(graphqlOperation(deleteTask, taskDetails))
  }
}
