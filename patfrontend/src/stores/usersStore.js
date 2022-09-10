import { defineStore } from 'pinia'

export const authStore = defineStore({
  id: 'userauth',
  
  state: () => ({
    isAuthenticated: false,
    token: JSON.parse(localStorage.getItem('token')),

    
  }),
  getters: {
    // getAuthToken : (state) =
    doubleCount: (state) => state.counter * 2
  },
  actions: {
    // increment() {
    //   this.counter++
    // }
  }
})
