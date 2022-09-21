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
      path: '/resource',
      name: 'resources',
      meta: {
        requireLogin: true
      },
      component: () => import('../views/Resources.vue'),
      children : [

      ]
    },
    {
      path: '/update/',
      
      children : [
        {
          path:"",
          name: 'updates',
          component: () => import('@/views/Update.vue'),
        },
        {
          path:':slug',
          name:'udatedetail',
          component: ()=> import('@/views/UpdateDetail.vue')
        },
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
      meta: {
        requireLogin: true
      },
      children : [
        {
          path: '',
          name: 'membership',
          component: () => import('../views/Membership.vue'),

        },
        {
          path:':membershipid',
          name:'userdetails',
          component : () => import ('../views/Userdetail.vue')
        }
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
        {
          path:'profile',
          name:'profile',
          component : () => import('@/views/MyProfile.vue')
        },
      ]
    }

  ]
})

router.beforeEach((to, from, next) => {
  const store = authStore()
  if (to.matched.some(record => record.meta.requireLogin) && !store.token) {
    next('/account/login')
  } else {
    next()
  }
})


export default router
