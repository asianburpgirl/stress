import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import TabsPage from '../views/TabsPage.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/tabs/home'
  },
  {
    path: '/tabs/',
    component: TabsPage,
    children: [
      // {
      //   path: '',
      //   redirect: '/tabs/home'
      // },
      {
        path: 'activity',
        component: () => import('@/views/ActivityPage.vue')
      },
      {
        path: 'leaderboard',
        component: () => import('@/views/LeaderboardPage.vue')
      },
      {
        path: 'home',
        component: () => import('@/views/HomePage.vue')
      },
      {
        path: 'notification',
        component: () => import('@/views/NotificationPage.vue')
      },
      {
        path: 'leaderboard',
        component: () => import('@/views/LeaderboardPage.vue')
      },
      {
        path: 'profile',
        component: () => import('@/views/ProfilePage.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
