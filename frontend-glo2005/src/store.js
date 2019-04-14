import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      username: ""
    }
  },
  mutations: {
    saveUsername(state, payload) {
      state.user.username = payload
    }
  },
  actions: {
  }
})
