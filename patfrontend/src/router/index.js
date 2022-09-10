import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { authStore } from "@/stores/usersStore"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('../views/Contactus.vue')
    },
    {
      path: '/resources',
      name: 'resources',
      meta: {
        requireLogin: true
      },
      component: () => import('../views/Resources.vue'),
      children : [

      ]
    },
    {
      path: '/projects/',
      
      children : [
        {
          path:"",
          name: 'projects',
          component: () => import('@/views/Project.vue'),
        },
        {
          path:':slug',
          name:'projectdetail',
          component: ()=> import('@/views/ProjectDetail.vue')
        },
      ]
    },
    {
      path: '/membership',
      name: 'membership',
      meta: {
        requireLogin: true
      },
      component: () => import('../views/Membership.vue'),
      children : [

      ]
    },
    {
      path: '/account',
      name: 'account',
      children : [
        {
          path:'login',
          name:'login',
          component : () => import('@/views/Login.vue')
        },
        {
          path:'register',
          name:'register',
          component : () => import('@/views/Register.vue')
        },
      ]
    }

  ]
})

router.beforeEach((to, from, next) => {
  const store = authStore()
  if (to.matched.some(record => record.meta.requireLogin) && !store.isAuthenticated) {
    next('account/login')
  } else {
    next()
  }
})


// router.beforeEach(async (to, from) => {
//   const store = authStore()
//   if (
//     // make sure the user is authenticated
//     !store.isAuthenticated &&
//     // ❗️ Avoid an infinite redirect
//     to.name !== 'Login'
//   ) {
//     // redirect the user to the login page
//     return { name: 'login' }
//   }
// })

export default router
