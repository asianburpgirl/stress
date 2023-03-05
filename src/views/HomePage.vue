<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Home</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" ion-padding>
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Home</ion-title>
        </ion-toolbar>
      </ion-header>
      <!-- can make use of ion-grid to contain your stuff -->
      <ion-grid>
        <ion-card style="width: 340px; height: 600px; background-color: #ffffff;">
          <ion-grid>
            <ion-row>
              <ion-img src="../assets/logo and bubbles.png"
                style="width: 100%; height: 100%">
              </ion-img>
            </ion-row>
          </ion-grid>
          <ion-card-header>
            <ion-card-subtitle
              style="text-align: center; margin-top: -15px; font-weight: bold; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 1.2rem">
              <span style="color:#5678AB">Stress</span><span style="color:#D36FA5">Less</span></ion-card-subtitle>
          </ion-card-header>
          <ion-grid>
            <ion-row>
              <ion-img src="../assets/singpass.png"
                style="width: 75%; height: auto; margin-top: -10px; display: block; margin-left: auto; margin-right: auto">
              </ion-img>
            </ion-row>
          </ion-grid>
        </ion-card>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import ExploreContainer from '@/components/ExploreContainer.vue';
</script>
