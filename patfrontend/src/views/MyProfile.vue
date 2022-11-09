<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <AuthSideBar />
                </div>
                <div class="col-md-8" id="divToPrint">
                    <div v-if="user.avatar == 'http://localhost:8000/media/default.jpg'">
                        <img :src="user.avatar" :alt="user.first_name + user.last_name" class="avatar">
                    </div>
                    <div v-else>
                        <img src="../assets/images/avatar.jpg" alt="">
                    </div>
                    
                    <h2>{{ user.first_name }} {{ user.last_name }}</h2>
                    <p>Membership ID: {{ user.memberId }}</p>
                    <p>Member type: {{ user.typeofmember }}</p>

                    <!-- <div class="row">
                        <img :src="user.avatar" :alt="user.first_name + user.last_name" class="avatar">
                    </div>
                    <h2>My Profile for {{ user.first_name }} {{ user.last_name }}</h2>
                    <p>Membership ID: {{ user.memberId }}</p>
                    <p>Member type: {{ user.typeofmember }}</p>
                    <hr>
                    <p>First name : {{ user.first_name }}</p>
                    <p>Middle name : {{ user.middle_name }}</p>
                    <p>Last Name : {{ user.last_name }}</p>
                    <p>Gender : {{ user.gender }}</p>
                    <p>email : {{ user.email }}</p>
                    <p>Phone Number : {{ user.phone }}</p>

                    <hr>
                    <p>MCT Number : {{ user.mctnumber }}</p>
                    <p>Your Occupation: {{ user.profession }}</p>
                    <p>Working at: {{ user.organization }}</p>
                    <p>Region : {{ user.region }}</p>
                    <p>Field: {{ user.areaofwork }}</p> -->

                    
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


import pdfMake from 'pdfmake';
import pdfFonts from 'pdfmake/build/vfs_fonts';
import htmlToPdfmake from 'html-to-pdfmake';

export default {
    components: {
        AuthSideBar
    },
    methods :{
        generateIdCard () {
            // this.$refs.html2Pdf.generatePdf()
        const pdfTable = document.getElementById('divToPrint');
          //html to pdf format
          var html = htmlToPdfmake(pdfTable.innerHTML);
        
          const documentDefinition = { content: html };
          pdfMake.vfs = pdfFonts.pdfMake.vfs;
          pdfMake.createPdf(documentDefinition).open();
        }
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
.avatar {
    margin-bottom: 18px;
}

img {
    width: 200px !important;
}
</style>