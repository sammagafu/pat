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
                            <div class="form-group mb-4">
                                <label class="form-label" for="loginName">Email or username</label>
                                <input type="email" id="loginName" class="form-control" :model="email"/>
                                
                            </div>

                            <!-- Password input -->
                            <div class="form-group mb-4">
                                <label class="form-label" for="loginPassword">Password</label>
                                <input type="password" id="loginPassword" class="form-control" :model="password"/>
                            </div>

                            <!-- 2 column grid layout -->
                            <div class="row mb-4">
                                <div class="col-md-6 d-flex justify-content-center">
                                    <!-- Checkbox -->
                                    <div class="form-check mb-3 mb-md-0">
                                        <label class="form-check-label" for="loginCheck"> Remember me </label>
                                        <input class="form-check-input" type="checkbox" value="" id="loginCheck"
                                            checked />
                                        
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
    export default{
        data(){
            return {
                email : '',
                password : '',
                rememberme : true
            }
        },
        computed(){
        },
        methods : {
            login (){
                
            }
        }
    }
</script>

<style>
    a{
        color: #1A3D7D;
        font-size: 14px;
        font-weight: 700;
    }
    a:hover{
        color: darkblue;
    }
</style>