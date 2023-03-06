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
      <ion-grid class="ion-text-center">
        <h1>Badges</h1>
        <img src="../asset/woman.png" />
        <ion-card class="ion-padding ion-text-center">
          <ion-row>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../asset/king.png" />
              </ion-avatar>
            </ion-col>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../asset/diamond.png" />
              </ion-avatar>
            </ion-col>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../asset/sword.png" />
              </ion-avatar>
            </ion-col>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../asset/trophy.png" />
              </ion-avatar>
            </ion-col>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../asset/stars.png" />
              </ion-avatar>
            </ion-col>
            <ion-col size-md="4">
              <ion-avatar>
                <img src="../asset/medal.png" />
              </ion-avatar>
            </ion-col>
          </ion-row>
        </ion-card>
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
