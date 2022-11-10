<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <AuthSideBar />
                </div>
                <div class="col-md-8" id="element-to-convert">
                    <div class="id-header">
                        <h2 class="text-left">Membership Identification Card</h2>
                    </div>
                    <div class="row">
                        <div class="col-md-2 avatar">
                            <div v-if="user.avatar == 'http://localhost:8000/media/default.jpg'">
                                <img :src="user.avatar" :alt="user.first_name + user.last_name" class="avatar">
                            </div>
                            <div v-else>
                                <img src="../assets/images/avatar.jpg" alt="">
                            </div>
                        </div>

                        <div class="col-md-8">
                            <h2>{{ user.first_name }} {{ user.last_name }}</h2>
                    <p>Membership ID: {{ user.memberId }}</p>
                    <p>Member type: {{ user.typeofmember }}</p>
                        </div>
                    </div>
                </div>
                <button @click="generateIdCard">Download ID </button>
            </div>
        </div>
    </section>
</template>

<script>
import AuthSideBar from '../components/AuthSideBar.vue';
import { authStore } from '../stores/usersStore';
import axios from 'axios';
import { ref, onMounted } from 'vue'


import html2pdf from "html2pdf.js";


export default {
    components: {
        AuthSideBar
    },
    methods: {
        generateIdCard() {
            html2pdf(document.getElementById("element-to-convert"), {
                margin: 1,
                filename: "IdCard.pdf",
                image: { type: 'jpeg', quality: 0.98 },
                jsPDF: { format: 'credit-card', orientation: 'l', compress: false, }
            });
        },
    },
    setup() {
        const authdata = authStore()
        const token = authdata.token
        let user = ref([])
        console.log(token)

        onMounted(() => {
            axios.get('http://localhost:8000/api/v1/auth/users/me/', {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            })
                .then(response => {
                    user.value = response.data;
                    console.log(response.data)
                })
                .catch(error => {
                    console.log(error);
                });
        })


        return {
            user
        }
    }
}
</script>

<style scoped>
.id-header {
    padding: 12px 0;
}
h2{
    font-size: medium;
    font-weight: bolder;
}
.avatar img{
    width: 75px;
}
</style>