import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

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
      component: () => import('../views/Resources.vue'),
      children : [

      ]
    },
    {
      path: '/projects/',
      name: 'projects',
      component: () => import('../views/Project.vue'),
      children : [
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
        }
      ]
    }

  ]
})

export default router
