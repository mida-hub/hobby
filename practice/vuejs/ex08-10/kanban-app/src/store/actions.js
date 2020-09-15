/* eslint-disalbe no-unused-vars */
import * as types from './mutation-type'
import { Auth, List, Task } from '../api'
/* eslint-enable no-unused-vars */

export default {
  login: ({ commit }) => {
    throw new Error('login action should be implemented')
  },

  fetchLists: ({ commit }) => {
    throw new Error('fetchLists action should be implemented')
  },

  addTask: ({ commit }) => {
    throw new Error('addTask action should be implemented')
  },

  updateTask: ({ commit }) => {
    throw new Error('updateTask action should be implemented')
  },

  removeTask: ({ commit }) => {
    throw new Error('removeTask action should be implemented')
  },

  logoutTask: ({ commit }) => {
    throw new Error('logoutTask action should be implemented')
  }
}
