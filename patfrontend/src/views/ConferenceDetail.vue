<template>
    <section class="breadcrumb-header">
        <div class="overlay"></div>
        <div class="container">
            <div class="row">
                <div class="col-lg-10">
                    <div class="banner">
                        <h1>{{confernce.name}}</h1>
                        <ul>
                            <li>
                                {{confernce.venue}}
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="single-department single-gallery py-100-70">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4">
                        <div class="sidebar-department mr-20">
                            <div class="widget">
                                <div class="widget-title">
                                    <h3>Resources</h3>
                                </div>
                                <div class="widget-body">
                                    <ul class="single-department-list">
                                        <li><a :href="confernce.resolution">Resolution <i class="fas fa-angle-right"></i></a></li>
                                        <li><a :href="confernce.abstract">Abstract Book <i class="fas fa-angle-right"></i></a></li>
                                        <li><a :href="confernce.images">Images <i class="fas fa-angle-right"></i></a></li>
                                        <li><a :href="confernce.presentation">Presentations <i class="fas fa-angle-right"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-8">
                        <div class="single-department-box">
                            <h2>Theme:{{confernce.theme}}</h2>
                            <p>{{confernce.shortdescription}}</p>
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
            confernce: []
            // this.$route.params.slug 
        }
    },
    mounted() {
        this.getProductDetail()
    },
    methods: {
        getProductDetail() {
            axios.get(`conference/${this.$route.params.slug}`)
                .then(response => {
                    this.confernce = response.data;
                    document.title = 'Conference : ' + response.data.name
                })
                .catch(error => {
                    console.log(error);
                });
        }

    },
}
</script>