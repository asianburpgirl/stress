<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Profile</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" ion-padding style="margin: 0">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Profile</ion-title>
        </ion-toolbar>
      </ion-header>
      <!-- can make use of ion-grid to contain your stuff -->
      <ion-grid class="ion-text-center ion-padding">
        
        <img src="../../public/assets/woman.png" />
       
        <ion-card class="ion-padding">
           <h4 class="ion-text-start">Badges Earned</h4>
          <ion-row>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../../public/assets/king.png" />
              </ion-avatar>
            </ion-col>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../../public/assets/diamond.png" />
              </ion-avatar>
            </ion-col>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../../public/assets/sword.png" />
              </ion-avatar>
            </ion-col>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../../public/assets/trophy.png" />
              </ion-avatar>
            </ion-col>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../../public/assets/stars.png" />
              </ion-avatar>
            </ion-col>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../../public/assets/medal.png" />
              </ion-avatar>
            </ion-col>
          </ion-row>
         
        </ion-card>
        
      </ion-grid>
      <ion-grid class="ion-padding">
        <h4>Account Settings</h4>
        <ion-list class="ion-padding-bottom">
          <ion-item>
            <ion-label>Edit Profile</ion-label>
          </ion-item>
          <ion-item>
            <ion-label>Settings</ion-label>
          </ion-item>
        </ion-list>
        <ion-button href="/" fill="outline" expand="block">Log Out</ion-button>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonGrid,
  IonRow,
  IonCol,
  IonAvatar,
  IonCard,
} from "@ionic/vue";

import { defineComponent } from "vue";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonGrid,
    IonRow,
    IonCol,
    IonAvatar,
    IonCard,
  },
});
</script>

<style>
/* ion-avatar{
    background-color:skyblue;
} */
</style>
