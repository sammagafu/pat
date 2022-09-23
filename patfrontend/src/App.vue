<template>
  <div class="loading" style="display:block" v-if="authdata.isLoading">
    <div class="loading-box">
      <img class="img-fluid" src="../src/assets/images/loading.gif" alt="Loading">
    </div>
  </div>
  <TopHeader />
  <RouterView />
  <Footer />
</template>

<style>
@import url('../src/assets/css/responsive.css');

.loading {
  display: flex;
}
</style>

<script>
import { RouterLink, RouterView } from 'vue-router'
import TopHeader from '@/components/TopHeader.vue';
import Footer from '@/components/Footer.vue';
import { authStore } from '@/stores/usersStore';
import { ref } from 'vue'

export default {
    setup() {
        const authdata = authStore();
        return {
            authdata
        };
    },
    components: { TopHeader, Footer }
}
</script>