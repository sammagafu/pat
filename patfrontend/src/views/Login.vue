<template>
    <section class="py-100-70 login">
        <div class="text-center mb-4">
            <h2>Welcome Please Login</h2>
        </div>
        <div class="container">
            <div class="col-md-4 offset-md-4">
                <div class="tab-pane fade show active" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
                        <form @submit.prevent="login">
                            <!-- Email input -->
                            <div class="alert alert-danger" role="alert" v-if="message">
                                {{message.detail}}
                            </div>
                            
                            <div class="form-group mb-4">
                                <label class="form-label" for="loginName">Email Address</label>
                                <input type="text" id="loginName" class="form-control" v-model="email"/>
                                
                            </div>

                            <!-- Password input -->
                            <div class="form-group mb-4">
                                <label class="form-label" for="loginPassword">Password</label>
                                <input type="password" id="loginPassword" class="form-control" v-model="password"/>
                            </div>

                            <!-- 2 column grid layout -->
                            <div class="row mb-4">
                                <div class="col-md-6 d-flex justify-content-center">
                                    <!-- Checkbox -->
                                    <div class="form-check mb-3 mb-md-0">
                                        <label class="form-check-label" for="loginCheck"> Remember me </label>
                                        <input class="form-check-input" type="checkbox" v-model="rememberme" id="loginCheck" />
                                        
                                    </div>
                                </div>

                                <div class="col-md-6 d-flex justify-content-center">
                                    <!-- Simple link -->
                                    <a href="#!">Forgot password?</a>
                                </div>
                            </div>

                            <!-- Submit button -->
                            <button type="submit" class="btn btn-primary btn-block mb-4">Sign in</button>

                            <!-- Register buttons -->
                            <div class="text-center">
                               <p>Not a member? <router-link :to="{name:'register'}"> Register</router-link></p>
                            </div>
                        </form>
                    </div>
            </div>
        </div>
    </section>
</template>

<script>
    import axios from 'axios';
    import { authStore } from "@/stores/usersStore";

    const userStore = authStore()

    export default{
        data(){
            return {
                email : '',
                password : '',
                rememberme : false,
                message : ''
            }
        },
        computed(){
        },
        methods : {
            async login (){
                localStorage.removeItem("token")

                const loginData = {
                    email: this.email,
                    password: this.password
                }

                await axios.post('http://localhost:8000/api/v1/auth/token/login/', loginData)
                    .then(response => {
                        const token = response.data.auth_token
                        userStore.token = token
                        userStore.isAuthenticated =true
                        localStorage.setItem('token', JSON.stringify(token));
                        axios.defaults.headers.common["Authorization"] = "Token " + token
                    }).catch(error => {
                        console.log(error)
                    })

                await axios
                    .get('http://localhost:8000/api/v1/auth/users/me/')
                    .then(response => {
                        // this.$store.commit('setUser', {
                        //     'id': response.data.id,
                        //     'email': response.data.email
                        // })
                        userStore.setUser({
                            'id':response.data.id,
                            'email':response.data.email,
                        })
                        localStorage.setItem('email', response.data.email)
                        localStorage.setItem('userid', response.data.id)
                    })
                    .catch(error => {
                        console.log(error.response.data)
                        this.message = error.response.data
                    })

                    const toPath = this.$route.query.to || '/resource'
                    this.$router.push(toPath)
            }
        }
    }
</script>

<style scoped>
    a{
        color: #1A3D7D;
        font-size: 14px;
        font-weight: 700;
    }
    a:hover{
        color: darkblue;
    }
</style>