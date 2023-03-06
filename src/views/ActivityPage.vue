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
          <ion-grid>
            <ion-row>
              <ion-col size="3">
                <ion-img src="../assets/timer.png"
                  style="width: 45px; height: 45px; margin-left:170px; margin-top:20px"></ion-img>
              </ion-col>
              <ion-col size="6">
                <ion-input style="border-radius:1rem;width:50px;background-color:white;
                          margin-left:140px; margin-top:25px; color: black; text-align: center;"></ion-input>
              </ion-col>
              <ion-col size="3">
                <p style="margin-top:39px; margin-left:32px; font-weight:bold; color:white;">mins</p>
              </ion-col>
            </ion-row>
          </ion-grid>
          <ion-grid>
            <ion-row>
              <ion-col size="3">
                <ion-img src="../assets/left-arrow.png"
                  style="width: 50px; height: 50px; margin-left:-10px; margin-top:150px">
                </ion-img>
              </ion-col>
              <ion-col size="6">
                <ion-img src="../assets/deepbreath.png"
                  style="width: 200px; height: 200px; margin-left:-20px; margin-top:50px">
                </ion-img>
              </ion-col>
              <ion-col size="3">
                <ion-img src="../assets/right-arrow.png"
                  style="width: 50px; height: 50px; margin-left:30px; margin-top:150px">
                </ion-img>
              </ion-col>
            </ion-row>
          </ion-grid>
          <ion-card-header>
            <ion-card-subtitle
              style="margin-left:45px; margin-top:40px;font-weight: bold; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 0.9rem;">
              Petals flowing in the wind</ion-card-subtitle>
          </ion-card-header>
          <ion-card-content>
            <p style="color:#F7f7ec ; font-weight: bold;text-align: center;">
              Relax your mind, body, and soul with each breath.
            </p>
            <br>
            <ion-button @click="presentAlert" color="#FFB6C1" style="background-color:#FFB6C1; border-radius: 5vi; justify-self: center; display:flex;
                    font-weight:bold; color:#1a1a1a">
              Start Breathing</ion-button>

          </ion-card-content>
        </ion-card>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { ref } from 'vue';
import { RouteRecordRaw } from 'vue-router';
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonGrid,
  IonImg, IonButton, alertController,
  IonCol,
  IonInput
} from '@ionic/vue';
import router from "@/router";
export default {
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonGrid,
    IonImg,
    IonButton,
    IonCol,
    IonInput
  },
  setup() {
    const presentAlert = async () => {
      const alert = await alertController.create({
        header: 'Mission Complete!',
        cssClass: 'custom-alert',
        message: `
      <div class="image-container">
        <img src="../assets/business.png" alt="My Image">
      </div>
      <p>You have earned 15 points!</p>
    `,
        buttons: [
          {
            text: 'Cancel',
            cssClass: 'alert-button-cancel',
          },
          {
            text: 'View Leaderboard',
            cssClass: 'alert-button-confirm',
            handler: () => {
              router.push('/tabs/leaderboard');
            },
          },
        ],
      });

      await alert.present();
    };

    return { presentAlert };
  },
};
</script>
<style>
ion-alert.custom-alert {
  --backdrop-opacity: 0.7;
}

.custom-alert .image-container .img {
  height: 10px;
  width: 10px;
}

button.alert-button.alert-button-confirm {
  width: 10px;
  background-color: var(--ion-color-success);
  color: var(--ion-color-success-contrast);
}

.md button.alert-button.alert-button-confirm {
  border-radius: 4px;
}

.ios .custom-alert button.alert-button {
  border: 0.55px solid rgba(var(--ion-text-color-rgb, 0, 0, 0), 0.2);
}

.ios button.alert-button.alert-button-cancel {
  border-right: 0;
  border-bottom-left-radius: 13px;
  border-top-left-radius: 13px;
}

.ios button.alert-button.alert-button-confirm {
  border-bottom-right-radius: 13px;
  border-top-right-radius: 13px;
}
</style>