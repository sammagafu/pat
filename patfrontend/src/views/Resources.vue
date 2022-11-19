<template>
    <section class="py-100 about-us about-us-3">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <auth-side-bar></auth-side-bar>
                </div>
                <div class="col-md-8" v-if="resources == null">
                    <template v-if="resources">
                        <div class="faq" v-for="(resources,index) in resources" :key="resources.index">
                        <div class="faq-box">
                            <h5 class="question-header">
                                <a :href="resources.file" class="text-primary">{{resources.title}}</a>
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
                <div class="col-md-8" v-else>
                    <div class="row">
                        <h4>No resources for now ! come back later</h4>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import AuthSideBar from '../components/AuthSideBar.vue';
export default {
    data() {
        return {
            resources: [],
        };
    },
    methods: {
        getResources() {
            axios.get("resource/")
                .then(response => {
                this.resources = response.data;
            })
                .catch(error => {
                console.log(error);
            });
        }
    },
    mounted() {
        this.getResources();
    },
    components: { AuthSideBar }
}
</script>