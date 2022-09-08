import { defineStore } from 'pinia'

export const userStore = defineStore({
  id: 'userauth',
  
  state: () => ({
    counter: 0,
    isAuthenticated: false,
    token:'',
  }),
  getters: {
    doubleCount: (state) => state.counter * 2
  },
  actions: {
    increment() {
      this.counter++
    }
  }
})
