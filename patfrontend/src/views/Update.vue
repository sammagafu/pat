<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <AuthSideBar />
                </div>
                <div class="col-md-8" v-if="update == null">
                    <div class="row">
                        <div class="col-md-6 col-lg-4" v-for="up in update">
                            <div class="blog-item">
                                <div class="img-box">
                                    <!-- <a href="01_single-blog.html" class="open-post">
                                        <img class="img-fluid" :src="up.cover" alt="01 Blog">
                                    </a> -->
                                    <router-link :to="{name:'udatedetail',params:{slug:up.slug}}" class="open-post"><img class="img-fluid" :src="up.cover" alt="01 Blog"></router-link>
                                </div>
                                <div class="text-box">
                                    <span class="blog-date">{{up.created}}</span>
                                    <a href="01_single-blog.html" class="title-blog">
                                        <h5>{{up.title}}</h5>
                                    </a>
                                    <a href="01_single-blog.html" class="link">Discover More</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-8" v-else>
                    <div class="row">
                        <h4>No Updates for now ! come back later</h4>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';
import AuthSideBar from '../components/AuthSideBar.vue';

export default {
    data() {
        return {
            update: []
        }
    },
    methods: {
        getResources() {
            axios.get("http://localhost:8000/api/v1/update/")
                .then(response => {
                    this.update = response.data;
                    console.log(this.update)
                })
                .catch(error => {
                    console.log(error);
                });
        }
    },
    mounted() {
        this.getResources()
    },
    components: { AuthSideBar }
}
</script>