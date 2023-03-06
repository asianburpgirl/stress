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
        <ion-card style="width: 340px; height: 600px; background-color: white;">
          <ion-grid>
            <ion-row>
              <ion-img src="../assets/logo and bubbles.png" style="width: 100%; height: 100%">
              </ion-img>
            </ion-row>
          </ion-grid>
          <ion-card-header>
            <ion-card-subtitle
              style="text-align: center; margin-top: -15px; font-weight: bold; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 1.2rem">
              <span style="color: #5678AB">Stress</span><span style="color:#D36FA5">Less</span>
            </ion-card-subtitle>
          </ion-card-header>
          <ion-grid>
            <ion-row>
              <ion-card-subtitle
                style="color: black; text-align: center; width: 100%; font-weight: bold; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 0.9rem">
                Scan with Singpass app
              </ion-card-subtitle>
              <ion-card-subtitle
                style="color: black; text-align: center; width: 100%; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 0.9rem">
                to log in
              </ion-card-subtitle>
            </ion-row>
            <ion-row>
              <a href="/">
                <ion-img src="../assets/singpass.png" 
                style="width: 55%; height: auto; display: block; margin-top: 5%; margin-left: auto; margin-right: auto">
                </ion-img>
              </a>
            </ion-row>
            <ion-row>
              <ion-button href="/" size="small" style="display: block; margin-top: 10px; margin-left: auto; margin-right: auto; text-transform: none">
                <ion-icon slot="start" :icon="lockClosed"></ion-icon>
                Use password login instead
              </ion-button>
            </ion-row>
            <ion-row>
                <ion-card-subtitle
                  style="color: gray; text-align: center; width: 100%; margin-top: 5px; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 0.2rem">
                  Don't have the Singpass app?
                </ion-card-subtitle>
                <ion-card-subtitle
                  style="text-align: center; width: 100%; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 0.2rem">
                  <a href="/" style="color: red; text-decoration: none">Download now</a>
                </ion-card-subtitle>
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

import { IonButton, IonIcon } from '@ionic/vue';
import { defineComponent } from 'vue';
import { lockClosed } from 'ionicons/icons';
</script>

<style scoped>
ion-button {
  --background: white;
  --color: gray;
  --color-hover: black;
  --border-color: gray;
  --border-style: solid;
  --border-width: 1px;
  --bow-shadow: none;
  --text-transform: none;
  --padding-top: 10px;
  --padding-bottom: 10px;
}
</style>