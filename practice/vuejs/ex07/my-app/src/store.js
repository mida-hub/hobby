import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// ストアの定義
const store = new Vuex.Store({
  state: {
    message: '初期メッセージ',
    tasks: [
      {
        id: 1,
        name: '牛乳を買う',
        labelIds: [1, 2],
        done: false
      },
      {
        id: 2,
        name: 'Vue の本を買う',
        labelIds: [1, 3],
        done: true
      }
    ],
  },
  getters: {
    // messageを使用するゲッター
    message(state) {
      return state.message
    },
    tasks(state){
      return state.tasks
    },
  },
})

// ストアをエクスポート
export default store
