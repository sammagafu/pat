<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <AuthSideBar />
                </div>
                <div class="col-md-8">

                </div>
            </div>
        </div>
    </section>
</template>

<script>
import AuthSideBar from '../components/AuthSideBar.vue';
import { authStore } from '../stores/usersStore';
import axios from 'axios';
import { ref, onMounted } from 'vue'
export default {
    components : {
        AuthSideBar 
    },
    setup() {
        // const 
        const authdata = authStore()
        const user = ref({})
        // const middlename = ref('')
        // const lastname = ref('')
        // const username = ref('')
        // const email = ref('')
        // const mct = ref('')
        // const gender = ref('')
        // const region = ref('')
        // const phonenumber = ref('')
        // const profession = ref('')
        // const organization = ref('')
        // const industry = ref('')
        // const typeofmember = ref('')
        // const graduation = ref('')
        // const masters = ref('')
        // const year = ref('')
        // const msg = ref([])
        
        // function onUnmounted(callback: () => void): void
        onMounted(() => {
            axios.put(`http://api.pediatrics.or.tz/${authdata.user.id}`)
                .then(response => {
                    console.log(response.data)
                    user.value = response.data

                })
                .catch(error => {
                    console.log(error);
                });
        })


        return {
            // firstname,middlename,lastname,username,email,mct,gender,region,phonenumber,profession,organization,industry,typeofmember,graduation,masters,year
            user,authdata
        }
    }
}
</script>

<style scoped>
.avatar{
    margin-bottom: 18px;
}
img{
    width: 200px !important;
}
</style>