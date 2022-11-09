<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <AuthSideBar />
                </div>
                <div class="col-md-8">
                    <h2>Electronic Activity Request</h2>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import AuthSideBar from '@/components/AuthSideBar.vue';
export default{
    components :{
        AuthSideBar
    }
}
</script>