import { defineStore } from 'pinia'

export const authStore = defineStore({
  id: 'userauth',
  
  state: () => ({
    isAuthenticated: false,
    token: JSON.parse(localStorage.getItem('token')),
    user: {
      id: localStorage.getItem('userid'),
      email: localStorage.getItem('email')
    },

    
  }),
  getters: {
    // getAuthToken : (state) =
    doubleCount: (state) => state.counter * 2
  },
  actions: {
    setUser(user) {
      this.user = user
    },
    logoutUser (){
      localStorage.removeItem("token");
      localStorage.removeItem("userid");
      localStorage.removeItem("email");
      this.$router.to({name:'login'})
    }
  }
})
