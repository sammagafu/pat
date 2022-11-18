import {
  defineStore
} from 'pinia'
import axios from 'axios'
import { useRoute } from 'vue-router'



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

    userLogin(email, password) {
      const loginData = {
        email,password
      }
      axios.post('auth/login/', loginData)
        .then(response => {
          const token = response.data.access
          this.token = token
          this.isAuthenticated = true
          console.log(loginData);
          localStorage.setItem('token', JSON.stringify(token));
          axios.defaults.headers.common["Authorization"] = "Bearer " + token
        }).catch(error => {
          console.log(error)
        })

      axios
        .get('auth/users/me/',{
          headers: {
            "Authorization": `Bearer ${this.token}`
        }
        })
        .then(response => {
            this.setUser({
                'userid':response.data.pk,
                'email':response.data.email,
                'is_staff':response.data.is_staff,
                'memberId':response.data.memberId,
            })
            localStorage.setItem('email', response.data.email)
            localStorage.setItem('userid', response.data.pk)
            localStorage.setItem('is_staff', response.data.is_staff)
            localStorage.setItem('memberId', response.data.memberId)
    
        })
        .catch(error => {
            console.log(error.response.data)
            this.message = error.response.data
        })

    },

    logoutUser() {
      this.user = null;
      this.isAuthenticated = false
      localStorage.removeItem("token");
      localStorage.removeItem("userid");
      localStorage.removeItem("email");
      localStorage.removeItem("memberId");
      localStorage.removeItem("is_staff");
    }
  }
})