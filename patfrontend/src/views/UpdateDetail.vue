<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-3">
                    <AuthSideBar/>
                </div>
                <div class="col-md-8">
                    <div class="blog-item">
                            <div class="img-box">
                                <img class="img-fluid" :src="up.cover" alt="03 Blog">
                            </div>
                            <div class="text-box">
                                <span class="blog-date"> Published at : {{up.created}}</span>
                                <h5>{{ up.title }}</h5>
                                <p>{{ up.content }}</p>

                                
                                <div class="share-post">
                                    <span>Share Post :</span>
                                    <ul>
                                        <li><a href="#"><i class="fab fa-facebook-f"></i></a></li>
                                        <li><a href="#"><i class="fab fa-twitter"></i></a></li>
                                        <li><a href="#"><i class="fab fa-instagram"></i></a></li>
                                        <li><a href="#"><i class="fab fa-dribbble"></i></a></li>
                                        <li><a href="#"><i class="fab fa-behance"></i></a></li>
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
import AuthSideBar from '../components/AuthSideBar.vue';
import axios from 'axios';
    export default{
        data(){
            return {
                up : []
            }
        },
        mounted (){
            this.getProductDetail()
        },
        methods:{
        getProductDetail(){
            axios.get(`http://api.pediatrics.or.tz/api/v1/update/${this.$route.params.slug}`)
            .then(response => {
                        this.up = response.data;
                        document.title = 'PAT: ' + response.data.projectname
            })
            .catch(error => {
                console.log(error);
            });
        }

    },
    components: { AuthSideBar },
    
}
</script>