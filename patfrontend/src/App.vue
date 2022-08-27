<script setup>
import { RouterLink, RouterView } from 'vue-router'
import TopHeader from './components/TopHeader.vue';
import Footer from './components/Footer.vue';
</script>

<template>
<TopHeader />
  <RouterView />
<Footer />
</template>

<style>
</style>
