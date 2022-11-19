<template>
    <section class="breadcrumb-header">
        <div class="overlay"></div>
        <div class="container">
            <div class="row">
                <div class="col-lg-6">
                    <div class="banner">
                        <h1>Conferences</h1>
                        <ul>
                            <li>
                                <router-link :to="{ name: 'home' }">Home</router-link>
                            </li>
                            <li><i class="fas fa-angle-right"></i></li>
                            <li>Conferences</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-md-6 col-lg-4" v-for="conf in confrences" :key="conf.index">
                    <div class="gallery-item">
                        <span style="top: -133.484px; left: 261px;"></span>
                        <div class="img-box">
                            <img class="img-fluid gallery-item-img" :src="conf.cover"
                                alt="01 Gallery">
                        </div>
                        <div class="hover-box">
                            <div class="text-box">
                                

                                <div class="tags"><a href="#">{{conf.venue}}</a></div>
                                <h4><router-link :to="{name:'conferenceDetails',params:{slug:conf.slug}}"><h5>{{conf.name}}</h5></router-link></h4>
                            </div>
                            <ul class="gallery-icon">
                                <li><router-link :to="{name:'conferenceDetails',params:{slug:conf.slug}}"><i
                                            class="far fa-eye"></i></router-link></li>
                                <!-- <li><a class="popup" href="assets/images/gallery/01_gallery.jpg"></a></li> -->
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </section>

</template>

<style scoped>
.breadcrumb-header {
    background-image: url(../assets/images/header/01_header.jpg)
}
</style>

<script>
    import axios from 'axios';
    export default{
        data(){
            return {
                confrences:[]
            }
        },
        methods:{
        getResources(){
            axios.get("conference/")
            .then(response => {
                        this.confrences = response.data;
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

<style scoped>
    .breadcrumb-header{
      background-image: url(../assets/images/header/01_header.jpg)
    }
  </style>