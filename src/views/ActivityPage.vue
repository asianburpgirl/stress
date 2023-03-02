<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Activity</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" ion-padding>
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Activity</ion-title>
        </ion-toolbar>
      </ion-header>
      <!-- can make use of ion-grid to contain your stuff -->
      <ion-grid>
        <ion-card style="width: 340px; height: 600px; background-color: #Abaad8;">
          <ion-img src="../assets/deepbreath.png" 
          style="width: 200px; height: 200px; margin-left:70px; margin-top:90px"></ion-img>
          <ion-card-header>
            <ion-card-subtitle style="margin-left:45px; margin-top:40px;font-weight: bold; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 0.9rem;">Petals flowing in the wind</ion-card-subtitle>
          </ion-card-header>
          <ion-card-content>
            <p style="color:#F7f7ec ; font-weight: bold;text-align: center;">
              Relax your mind, body, and soul with each breath.
            </p>
            <br>
            <ion-button color="pink" style="background-color: pink; border-radius: 5vi; justify-self: center; display:flex;
            color:#222222; font-weight:bold">
              Start Breathing</ion-button>
          </ion-card-content>
        </ion-card>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonGrid,
  IonImg,
} from "@ionic/vue";
</script>
