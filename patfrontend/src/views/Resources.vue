<template>
    <section class="breadcrumb-header">
        <div class="overlay"></div>
        <div class="container">
            <div class="row">
                <div class="col-lg-6">
                    <div class="banner">
                        <h1>Resources</h1>
                        <ul>

                            <li>
                                <router-link :to="{ name: 'home' }">Home</router-link>
                            </li>
                            <li><i class="fas fa-angle-right"></i></li>
                            <li>Resources</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="about-us about-us-3">
        <div class="container">
            <div class="row">
                <div class="col-md-8">
                    <template v-if="resources">
                        <div class="faq" v-for="(resources,index) in resources" :key="resources.index">
                        <div class="faq-box">
                            <h5 class="question-header">
                                {{resources.title}}
                                <!-- <button class="btn btn-primary click" type="button" data-bs-toggle="collapse"
                                    data-bs-target="#faqs-1" aria-expanded="false" aria-controls="faqs-1">How can i find
                                    a job ?<i class="fas fa-angle-right"></i>
                                </button> -->
                            </h5>
                            <div class="collapse show" id="faqs-1">
                                <div class="card card-body about-text">
                                    {{resources.description}}
                                </div>
                            </div>
                        </div>
                    </div>
                    </template>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            resources: [],
        }
    },
    methods:{
        getResources(){
            axios.get("http://localhost:8000/api/v1/resource/")
            .then(response => {
                        this.resources = response.data;
            })
            .catch(error => {
                console.log(error);
            });
        }
    },
    mounted (){
        this.getResources()
    }

}
</script>