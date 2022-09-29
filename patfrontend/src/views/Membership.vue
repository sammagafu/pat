<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <AuthSideBar />
                </div>
                <div class="col-md-8">
                    <!-- <div class="form-group">
                        <label for="filter">Search</label>
                        <input type="text" name="filter" id="filter" placeholder="Enter users name, email, or mct number" v-model="keyword">
                    </div> -->
                    
                    <div class="card" v-for="me in member" :key="member.id">
                        <div class="row">
                            <!-- <div class="col-md-2" v-if="me.avatar == 'http://localhost:8000/default.jpg'">
                                <div class="img">
                                    <img src="../assets/images/avatar.jpg">
                                </div>
                            </div> -->
                            <div class="col-md-2">
                                <div class="img">
                                    <img :src="me.get_avatar">
                                </div>
                            </div>
                            <div class="col-md-8">
                                <div class="infos">
                            <div class="name">
                                <h2 class="userlink"><router-link :to="{name:'userdetails',params:{membershipid:me.memberId}}">{{ me.first_name }} {{ me.middlename }} {{ me.last_name }}</router-link></h2>
                                <h4>{{me.memberId}}</h4>
                            </div>
                            <p class="text">{{me.organization}}</p>
                            <ul class="stats">
                                <li>
                                    <h3>Gender</h3>
                                    <h4>{{me.gender}}</h4>
                                </li>
                                <li>
                                    <h3>Location</h3>
                                    <h4>{{me.region}}</h4>
                                </li>
                                <li>
                                    <h3>Industry</h3>
                                    <h4>{{me.areaofwork}}</h4>
                                </li>
                            </ul>
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
import axios from 'axios';
import AuthSideBar from '../components/AuthSideBar.vue';
export default {
    data() {
        return {
            member: [],
            filteredmembers: [],
            keyword: '',
        };
    },
    mounted() {
        this.getmebers();
    },
    computed : {
        filteredmembers(){
            let tempmambers = this.member
            tempmambers = tempmambers.filter((item) =>{
                return console.log(item);
            })
        }
    },
    methods: {
        

        async getmebers() {


            await axios.get("http://api.pediatrics.or.tz/api/v1/user/").then(response => {
                this.member = response.data;
                console.log(response.data);
            }).catch(error => {
                console.log(error);
            });
        }
    },
    components: { AuthSideBar }
}
</script>

<style scoped>
img {
    max-width: 100%;
    display: block;
}

ul {
    list-style: none;
}

/* Utilities */
.card::after,
.card img {
    border-radius: 50%;
}

body,
.card,
.stats {
    display: flex;
}

.card {
    padding: 2.5rem 2rem;
    border-radius: 10px;
    margin: 1.2rem 0;
    background-color: rgba(255, 255, 255, .5);
    box-shadow: 0 0 30px rgba(0, 0, 0, .15);
    position: relative;
    transform-style: preserve-3d;
    overflow: hidden;
}

.card::before,
.card::after {
    content: '';
    position: absolute;
    z-index: -1;
}

.card::before {
    width: 100%;
    height: 100%;
    border: 1px solid #FFF;
    border-radius: 10px;
    top: -.7rem;
    left: -.7rem;
}

.card::after {
    height: 15rem;
    width: 15rem;
    background-color: #4172f5aa;
    top: -8rem;
    right: -8rem;
    box-shadow: 2rem 6rem 0 -3rem #FFF
}

.card img {
    width: 8rem;
    min-width: 80px;
    box-shadow: 0 0 0 5px #FFF;
}

.infos {
    margin-left: 1.5rem;
}

.name {
    margin-bottom: 1rem;
}

.name h2 {
    font-size: 1.3rem;
}

.name h4 {
    font-size: .8rem;
    color: #333
}

.text {
    font-size: .9rem;
    margin-bottom: 1rem;
}

.stats {
    margin-bottom: 1rem;
}

.stats li {
    min-width: 5rem;
}

.stats li h3 {
    font-size: .99rem;
}

.stats li h4 {
    font-size: .75rem;
}
h2,a{
    color: #222;
    padding-bottom: .5rem;
    font-weight: 400;
}
.links button {
    font-family: 'Poppins', sans-serif;
    min-width: 120px;
    padding: .5rem;
    border: 1px solid #222;
    border-radius: 5px;
    font-weight: bold;
    cursor: pointer;
    transition: all .25s linear;
}

.links .follow,
.links .view:hover {
    background-color: #222;
    color: #FFF;
}

.links .view,
.links .follow:hover {
    background-color: transparent;
    color: #222;
}

@media screen and (max-width: 450px) {
    .card {
        display: block;
    }

    .infos {
        margin-left: 0;
        margin-top: 1.5rem;
    }

    .links button {
        min-width: 100px;
    }
}
</style>