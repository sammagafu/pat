<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <AuthSideBar/>
                </div>
                <div class="col-md-8">
                    <h2>My Profile {{authdata.user.email}}</h2>
                    <p></p>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import AuthSideBar from '../components/AuthSideBar.vue';
import { authStore } from '../stores/usersStore';
import axios from 'axios'; 
import { ref } from 'vue'

const authdata = authStore()
const email = ref(authdata.user)

</script>