<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <!-- can make use of ion-grid to contain your stuff -->
      <ion-img class="activity" src="../assets/reading.webp"></ion-img>
      <ion-grid>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Make time for reading: carve out time in your schedule for reading.
            Whether it's a few minutes in the morning or an hour before bed, set
            aside a regular time to read each day
          </ion-card-content>
        </ion-card>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Find a comfortable spot: Settle into a comfortable spot, whether
            it's on the couch, in bed or in a favourite chair, where you can
            fully relax and enjoy your reading.
          </ion-card-content>
        </ion-card>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Turn off distractions: Turn off any distractions such as your phone,
            computer or TV, and focus solely on your reading.
          </ion-card-content>
        </ion-card>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Take breaks: Take breaks every 30 minutes to an hour to stretch,
            breathe, and move around. This will help you to relax, refocus and
            avoid feeling fatigued.
          </ion-card-content>
        </ion-card>

        <ion-grid>
          <ion-button expand="block" color="tertiary" @click="presentAlert">
            Done Challenge</ion-button
          >
        </ion-grid>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { ref, defineComponent } from "vue";
import {
  IonPage,
  // IonHeader,
  // IonToolbar,
  // IonTitle,
  IonContent,
  IonGrid,
  IonImg,
  IonButton,
  alertController,
  // IonRow,
  // IonCol,
  IonCard,
  // IonItem
} from "@ionic/vue";

import router from "../router/index";

export default defineComponent({
  components: {
    IonPage,
    // IonHeader,
    // IonToolbar,
    // IonTitle,
    IonContent,
    IonGrid,
    IonImg,
    IonButton,
    // IonRow,
    // IonCol,
    IonCard,
    // IonItem
  },
  setup() {
    const presentAlert = async () => {
      const alert = await alertController.create({
        header: "Mission Complete!",
        cssClass: "custom-alert",
        message: `
                <div class="image-container ion-text-center ion-padding-top">
                  <img src="../assets/business.png" alt="My Image">
                  <p>You have earned 100 points!</p>
                </div>
                
              `,
        buttons: [
          {
            text: "Cancel",
            cssClass: "alert-button-cancel",
          },
          {
            text: "View Leaderboard",
            cssClass: "alert-button-confirm",
            handler: () => {
              router.push("/tabs/leaderboard");
            },
          },
        ],
      });

      await alert.present();
    };

    return { presentAlert };
  },
});
</script>

<style scoped>
.center {
  padding-top: 20px;
  padding-bottom: 15px;
  text-align: center;
}

ion-alert.custom-alert {
  --backdrop-opacity: 0.8;
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

p {
  color: black;
}

/* .activity {
    width: 130px;
    height: 150px;
  } */

ion-col {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
</style>
