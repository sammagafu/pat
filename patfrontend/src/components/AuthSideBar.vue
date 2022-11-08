<template>
    <div class="sidebar-department mr-20">
        <!-- <div class="widget">
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
        </div> -->

        <div class="widget">
            <div class="widget-body">
                <div class="widget-title">
                    <h3>Updates & Resources</h3>
            </div>
                <ul class="single-department-list">
                    <li><router-link :to="{name:'resources'}" class="link-level-1">Resources <i class="fas fa-angle-right"></i> </router-link></li>
                    <li><router-link :to="{name:'updates'}" class="link-level-1">Updates <i class="fas fa-angle-right"></i> </router-link></li>
                    <!-- <li><a href="#">Updates <i class="fas fa-angle-right"></i></a></li> -->
                </ul>
            </div>
        </div>

        <div class="widget">
            <div class="widget-title">
                <h3>Members</h3>
            </div>
            <div class="widget-body">
                <ul class="single-department-list">
                    <li><router-link :to="{name:'membership'}" class="link-level-1">Members List <i class="fas fa-angle-right"></i> </router-link></li>
                </ul>
            </div>
        </div>

        <div class="widget" v-if="is_staff">
            <div class="widget-title">
                <h3>Staff</h3>
            </div>
            <div class="widget-body">
                <ul class="single-department-list">
                    <li><router-link :to="{name:'profile'}" class="link-level-1">Create Activity Request <i class="fas fa-angle-right"></i> </router-link></li>
                    <li><router-link :to="{name:'updateaccount'}" class="link-level-1">Pending Activity Request <i class="fas fa-angle-right"></i> </router-link></li>
                    <li><router-link :to="{name:'updateaccount'}" class="link-level-1">Approved  Activity Request <i class="fas fa-angle-right"></i> </router-link></li>
                </ul>
            </div>
        </div>

        <div class="widget">
            <div class="widget-title">
                <h3>My Profile</h3>
            </div>
            <div class="widget-body">
                <ul class="single-department-list">
                    <li><router-link :to="{name:'profile'}" class="link-level-1">Profile <i class="fas fa-angle-right"></i> </router-link></li>
                    <li><router-link :to="{name:'updateaccount'}" class="link-level-1">Update My Profile <i class="fas fa-angle-right"></i> </router-link></li>
                    <li><a href="#">Download PAT ID <i class="fas fa-angle-right"></i></a></li>
                    <!-- <li><a href="#">Update My Profile <i class="fas fa-angle-right"></i></a></li> -->
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import { authStore } from '../stores/usersStore';
import { ref } from 'vue';
export default{
    setup(){
        const authdata = authStore()
        const is_staff = ref(authdata.user.is_staff)
        return {
            authdata,
            is_staff

        }
    }
}
</script>