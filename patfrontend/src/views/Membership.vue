<template>
    <section class="py-100">
        <div class="container">
            <h2 class="title">Members</h2>
        </div>
        <div class="container">
            <div class="row">
                <div class="col-md-8" v-for="member in member" :key="member.id">
                    <div class="col-md-12">
                        <div class="row">
                            <div class="col-md-3">&nbsp;</div>
                            <div class="col-md-8">
                                <h2>{{member.first_name}} {{member.middlename}} {{member.last_name}}</h2>
                                <p>{{member.organization}}</p><p>{{member.region}}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
import axios from 'axios';
export default {
    data() {
        return {
            member: [],
        }
    },
    mounted() {
        this.getmebers()
    },
    methods: {
        async getmebers() {
            await axios.get("http://localhost:8000/api/v1/user/").then(response => {
                this.member = response.data
                console.log(response.data)
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>