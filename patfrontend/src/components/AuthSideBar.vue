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

        <div class="widget">
            <div class="widget-title">
                <h3>My Profile</h3>
            </div>
            <div class="widget-body">
                <ul class="single-department-list">
                    <li><router-link :to="{name:'profile'}" class="link-level-1">Profile <i class="fas fa-angle-right"></i> </router-link></li>
                    <li><a href="#">Settings <i class="fas fa-angle-right"></i></a></li>
                </ul>
            </div>
        </div>

    </div>
</template>