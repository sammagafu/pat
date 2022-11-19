<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-3">
                    <AuthSideBar />
                </div>

                <div class="col-md-6" id="element-to-convert">
                    <div class="id-header text-center pb-4">
                        <img src="@/assets/logo.png" alt="" style="height:130px;width:130px;">
                        <h2 class="text-left"> PAT Membership Identity Card</h2>
                    </div>
                    <div class="row">
                        <div class="col-md-4 avatar">
                            <div v-if="user.avatar == 'http://localhost:8000/media/default.jpg'">
                                <img :src="user.avatar" :alt="user.first_name + user.last_name" class="avatar">
                            </div>
                            <div v-else>
                                <img src="../assets/images/avatar.jpg" alt="">
                            </div>
                        </div>

                        <div class="col-md-8">
                            <h2>{{ user.first_name }} {{ user.middle_name }} {{ user.last_name }}</h2>
                            <p>Membership ID: {{ user.memberId }}</p>
                            <p>Member type: {{ user.typeofmember }}</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="btn-group" role="group" aria-label="Basic mixed styles example">
                        <button type="button" class="btn btn-primary"><i class="fa fa-pencil" aria-hidden="true"></i>
                            Profile</button>
                        <button type="button" class="btn btn-secondary"><i class="fa fa-download"
                                aria-hidden="true" @click="generateIdCard"></i> ID Card</button>
                    </div>
                </div>
                <!-- <button @click="generateIdCard"> ID Card</button> -->
            </div>
        </div>
    </section>
</template>

<script>
import AuthSideBar from '../components/AuthSideBar.vue';
import { authStore } from '../stores/usersStore';
import axios from 'axios';
import { ref, onMounted } from 'vue'
import jsPDF from 'jsPDF'




export default {
    components: {
        AuthSideBar,
    },
    methods: {
        generateIdCard() {
            let pdfName = 'test';
            var doc = new jsPDF();
            doc.text(this.name, 10, 10);
            doc.save(pdfName + '.pdf');
        },
    },
    setup() {
        const authdata = authStore()
        const token = authdata.token
        let user = ref([])

        onMounted(() => {
            axios.get('auth/users/me/', {
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
    margin: auto;
}

h2 {
    font-size: medium;
    font-weight: bolder;
    font-size: 2rem;
}

.avatar img {
    width: 100% !important;
}
</style>