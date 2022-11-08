import { defineStore } from 'pinia'


export const authStore = defineStore({
  id: 'userauth',
  
  state: () => ({
    isAuthenticated: false,
    isLoading: false,
    token: JSON.parse(localStorage.getItem('token')),
    user: {
      id: localStorage.getItem('userid'),
      email: localStorage.getItem('email'),
      is_staff: localStorage.getItem('is_staff'),
      memberId: localStorage.getItem('memberId')
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
      this.user = null;
      this.isAuthenticated = false
      localStorage.removeItem("token");
      localStorage.removeItem("userid");
      localStorage.removeItem("email");
      this.$router.push('/account/login')
    }
  }
})
