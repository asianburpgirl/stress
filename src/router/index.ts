import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import QuestionnairePage from '../views/QuestionnairePage.vue';
import TabsPage from '../views/TabsPage.vue';
import LoginPage from '../views/LoginPage.vue';
import BreathingPage from '../views/BreathingPage.vue';
import GardeningPage from '../views/GardeningPage.vue';
import YogaPage from '../views/YogaPage.vue';
import ReadingPage from '../views/ReadingPage.vue';
import SupportPage from '../views/SocialSupport.vue';
import ProfessionalPage from '../views/ProfessionalPage.vue';
import Breathing2Page from '../views/Breathing2Page.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: LoginPage,
    // redirect: '/tabs/home'
  },
  {
    path: '/questionnaire',
    component: QuestionnairePage
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
        path: 'breathing',
        component: BreathingPage,
      },
      {
        path: 'reading',
        component: ReadingPage,
      },
      {
        path: 'yoga',
        component: YogaPage,
        
      },
      {
        path: 'gardening',
        component: GardeningPage,
      },
      {
        path: 'support',
        component: SupportPage,
      },
      {
        path: 'professional',
        component: ProfessionalPage,
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
      },
      {
        path: 'heartdata',
        component: () => import('@/views/heartdataPage.vue')
      },
      {
        path: 'breathe',
        component: () => import('@/views/Breathing2Page.vue')
      },
      {
        path: 'yoga1',
        component: () => import('@/views/Yoga2Page.vue')
      },
      {
        path: 'garden1',
        component: () => import('@/views/Gardening2Page.vue')
      },
      {
        path: 'read',
        component: () => import('@/views/Reading2Page.vue')
      },
      {
        path: 'help',
        component: () => import('@/views/Professional2Page.vue')
      },
      {
        path: 'support1',
        component: () => import('@/views/SocialSupportPage.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
