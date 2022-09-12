<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <AuthSideBar/>
                </div>
                <div class="col-md-8">
                    <h2>My Profile</h2>
                    <p></p>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import AuthSideBar from '../components/AuthSideBar.vue';
    export default{
    components: { AuthSideBar }
}
</script>