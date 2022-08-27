<template>
<div class="top-navbar">
                <div class="container">
                    <div class="content-box d-flex align-items-center justify-content-between">
                        <ul class="website-info">
                            <li class="text-lowercase">
                                <i class="far fa-envelope"></i>
                                <a href="mailto:info@pediatrics.or.tz">info@pediatrics.or.tz</a>
                            </li>
                            <li class="text-capitalize">
                                <i class="fas fa-map-marker-alt"></i>
                                 United Nations Rd, Dar Es Salaam
                            </li>
                            <li>
                                <i class="far fa-clock"></i>
                                mon - fri : 8:00 AM - 5:30 PM
                            </li>
                        </ul>
                        <ul class="website-icon-social">
                            <li><a href="#"><i class="fab fa-facebook-f"></i></a></li>
                            <li><a href="#"><i class="fab fa-twitter"></i></a></li>
                            <li><a href="#"><i class="fab fa-linkedin-in"></i></a></li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- :: Navbar -->
            <nav class="nav-bar">
                <div class="container">
                    <div class="content-box d-flex align-items-center justify-content-between">
                        <div class="logo">
                            <router-link :to="{name:'home'}" class="logo-nav">
                                <img class="img-fluid one" src="../assets/logo.png" alt="01 Logo">
                            </router-link>
                            <a href="#open-nav-bar-menu" class="open-nav-bar">
                                <span></span>
                                <span></span>
                                <span></span>
                            </a>
                        </div>
                        <div class="nav-bar-links" id="open-nav-bar-menu">
                            <ul class="level-1">
                                <li class="item-level-1">
                                    <router-link :to="{name:'home'}" class="link-level-1">Home</router-link>
                                </li>

                                <li class="item-level-1">
                                    <router-link :to="{name:'about'}" class="link-level-1">About Us</router-link>
                                </li>

                                <li class="item-level-1" data-v-577b7a29="">
                                    <a href="https://pat.co.tz/" class="link-level-1">Conferences</a>
                                </li>

                                 <li class="item-level-1">
                                    <router-link :to="{name:'contact'}" class="link-level-1">Contact Us</router-link>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </nav>
</template>

<style scoped>
.logo-nav > img{
    width: 40% !important;
}
</style>