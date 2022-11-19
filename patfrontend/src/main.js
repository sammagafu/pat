import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

import axios from 'axios'
import VueAxios from 'vue-axios'

import './assets/css/bootstrap.min.css'
import './assets/css/responsive.css'
import './assets/css/animate.css'
import './assets/css/lity.min.css'
import './assets/css/style.css'


// axios.defaults.baseURL = 'http://localhost:8000/api/v1/'
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(VueAxios, axios)

axios.defaults.baseURL = 'http://localhost:8000/api/v1/'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

app.mount('#app')
