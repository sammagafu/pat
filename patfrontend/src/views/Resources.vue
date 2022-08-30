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

    <section class="about-us about-us-3 py-100">
        <div class="container">
            <div class="row">
                <div class="col-md-8">
                    <div class="faq">
                        <div class="faq-box">
                            <h5 class="question-header">
                                <button class="btn btn-primary click" type="button" data-bs-toggle="collapse"
                                    data-bs-target="#faqs-1" aria-expanded="false" aria-controls="faqs-1">How can i find
                                    a job ?<i class="fas fa-angle-right"></i>
                                </button>
                            </h5>
                            <div class="collapse show" id="faqs-1">
                                <div class="card card-body about-text">
                                    <b>Petrol Are A Professional Industry and Manufacturing Services Provider
                                        Institutions. Suitable For Factory, Manufacturing, Industry and any Industrial
                                        related business field.</b> Lorem ipsum dolor sit amet, consectetur adipisicing
                                    elit, sed do eiusm tmpor incididunt ut labore et dolore magna aliqua. Ut enim ad
                                    minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
                                    commodo consequat adipisicing elit, sed do eiusm tempor incididunt ut labore.
                                </div>
                            </div>
                        </div>
                    </div>
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
            axios.get("http://localhost:8000/api/v1/resources/")
        }
    }
}
</script>