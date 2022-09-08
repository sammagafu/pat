import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { axios } from 'axios'
import App from './App.vue'
import router from './router'

import './assets/css/bootstrap.min.css'
import './assets/css/responsive.css'
import './assets/css/animate.css'
import './assets/css/lity.min.css'
import './assets/css/style.css'


// axios.defaults.baseURL = 'http://localhost:8000/api/v1/'
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(axios)
// axios.defaults.baseURL = 'http://localhost:8000/api/v1/'
app.mount('#app')
