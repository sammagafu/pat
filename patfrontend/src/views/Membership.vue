<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                        <div class="sidebar-department mr-20">
                            <div class="widget">
                                <div class="widget-title">
                                    <h3>Search For Members</h3>
                                </div>
                                <div class="widget-body">
                                    <div class="search">
                                        <input type="search" name="search" placeholder="Search Users...">
                                        <button class="click">
                                            <i class="fas fa-search"></i>
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <div class="widget">
                                <!-- <div class="widget-title">
                                    <h3>Members</h3>
                                </div> -->
                                <div class="widget-body">
                                    <ul class="single-department-list">
                                        <li class="active"><a href="#">Resources <i class="fas fa-angle-right"></i></a></li>
                                        <li><a href="#">Updates <i class="fas fa-angle-right"></i></a></li>
                                    </ul>
                                </div>
                            </div>

                            <div class="widget">
                                <div class="widget-title">
                                    <h3>My Profile</h3>
                                </div>
                                <div class="widget-body">
                                    <ul class="single-department-list">
                                        <li class="active"><a href="#">View My Profile <i class="fas fa-angle-right"></i></a></li>
                                        <li><a href="#">Settings <i class="fas fa-angle-right"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                <div class="col-md-8">
                    <div class="col-md-12"  v-for="member in member" :key="member.id">
                        <div class="row">
                            <div class="col-md-3">&nbsp;</div>
                            <div class="col-md-8">
                                <h2>{{member.first_name}} {{member.middlename}} {{member.last_name}}</h2>
                                <p>{{member.organization}}</p><p>{{member.region}}</p>
                            </div>
                        </div>
                        <hr>
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
            member: [],
        }
    },
    mounted() {
        this.getmebers()
    },
    methods: {
        async getmebers() {
            await axios.get("http://localhost:8000/api/v1/user/").then(response => {
                this.member = response.data
                console.log(response.data)
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>