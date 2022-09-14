<template>
    <section class="breadcrumb-header">
        <div class="overlay"></div>
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="banner">
                        <h1>{{project.projectname}}</h1>
                        <ul>
                            <li>
                                <router-link :to="{ name: 'home' }">Home</router-link>
                            </li>
                            <li><i class="fas fa-angle-right"></i></li>
                            <li>
                                <router-link :to="{ name: 'projects' }">Projects</router-link>
                            </li>
                            <li><i class="fas fa-angle-right"></i></li>
                            <li>{{project.projectname}}</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="single-bolg py-100-70">
        <div class="container">
            <div class="row">
                <div class="col-lg-8">
                    <div class="blog-item">
                        <div class="img-box">
                            <img class="img-fluid" :src="project.cover" alt="03 Blog">
                        </div>
                        <div class="text-box">
                            <span class="blog-date"> Starting date : {{project.startdate}}</span>
                            <h5>{{ project.projectname }}</h5>
                            <h6>Specific Objective</h6>
                            <p>{{ project.specificObjective }}</p>
                            <h6>Project Description</h6>
                            <p>{{ project.shortdescription }}</p>

                            <div class="row py-100">
                                <div class="col-sm-6 col-lg-3" v-for="goals in project.goals">
                                    <div class="statistic-item">
                                        <div class="statistic-counter">{{goals.results}}</div>
                                        <div class="counter-name">{{goals.goal}}</div>
                                    </div>
                                </div>
                            </div>

                            <div class="share-post">
                                <span>Share Post :</span>
                                <ul>
                                    <li><a href="#"><i class="fab fa-facebook-f"></i></a></li>
                                    <li><a href="#"><i class="fab fa-twitter"></i></a></li>
                                </ul>
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
            project: []
            // this.$route.params.slug 
        }
    },
    mounted() {
        this.getProductDetail()
    },
    methods: {
        getProductDetail() {
            axios.get(`http://localhost:8000/api/v1/project/${this.$route.params.slug}`)
                .then(response => {
                    this.project = response.data;
                    document.title = 'PAT: ' + response.data.projectname
                })
                .catch(error => {
                    console.log(error);
                });
        }

    },
}
</script>