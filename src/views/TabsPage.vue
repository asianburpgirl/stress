<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar slot="bottom">
        <ion-tab-button tab="home" href="/tabs/home">
          <ion-icon aria-hidden="true" :icon="home" />
          <ion-label>Home</ion-label>
        </ion-tab-button>

        <!-- <ion-tab-button tab="notification" href="/tabs/notification">
          <ion-icon aria-hidden="true" :icon="mail" />
          <ion-label>Notification</ion-label>
        </ion-tab-button> -->

        <ion-tab-button tab="leaderboard" href="/tabs/leaderboard">
          <ion-icon aria-hidden="true" :icon="trophy" />
          <ion-label>Leaderboard</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="profile" href="/tabs/profile">
          <ion-icon aria-hidden="true" :icon="person" />
          <ion-label>Profile</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script>
import { IonTabBar, IonTabButton, IonTabs, IonLabel, IonIcon, IonPage, IonRouterOutlet } from '@ionic/vue';
import { home, mail, person, trophy } from 'ionicons/icons';
import { defineComponent } from "vue";
export default defineComponent({
  components: {
    IonTabBar, IonTabButton, IonTabs, IonLabel, IonIcon, IonPage, IonRouterOutlet
  },
  setup(){
    return { home, mail, person, trophy }
  },
});
</script>
