<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Activity</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" class="ion-padding">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Yoga</ion-title>
        </ion-toolbar>
      </ion-header>
      <!-- can make use of ion-grid to contain your stuff -->
      <ion-grid>
        <ion-card>
          <ion-card-content class="ion-text-center">
            <ion-row>
              <ion-col size="3"></ion-col>
              <ion-col size="6">
                <ion-img
                  class="activity"
                  src="../assets/yoga-activity.png"
                ></ion-img>
              </ion-col>
              <ion-col size="3"> </ion-col>
            </ion-row>
          </ion-card-content>
        </ion-card>
        <ion-grid class="ion-text-center">
          <ion-row>
            <ion-col>
              <b><i>Do 1 hour</i></b>
            </ion-col>
            <ion-col> | </ion-col>
            <ion-col>
              <b><i>100 points</i></b>
            </ion-col>
          </ion-row>
        </ion-grid>

        <ion-grid>
          <div>
            <h1><b>Relax your mind</b></h1>
            <p>
              Yoga can relieve stress by combining physical movement, controlled
              breathing, and mindfulness to promote relaxation and reduce
              tension in the body. The practice of yoga can help release
              endorphins, reduce cortisol levels, and increase feelings of
              well-being and calmness.
            </p>
          </div>
          <ion-button
            expand="block"
            shape="round"
            color="tertiary"
            href="/tabs/yoga1"
          >
            Accept Challenge</ion-button
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
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonGrid,
  IonImg,
  IonButton,
  alertController,
  IonRow,
  IonCol,
  IonCard,
  // IonItem
} from "@ionic/vue";

import router from "../router/index";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonGrid,
    IonImg,
    IonButton,
    IonRow,
    IonCol,
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
            <p>You have earned 15 points!</p>
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

.left-arrow {
  width: 50px;
  height: 50px;
  /* margin-left: -10px; */
  margin-top: 100px;
}

.right-arrow {
  width: 50px;
  height: 50px;
  /* margin-left: 20px; */
  margin-top: 100px;
}

.activity {
  width: 130px;
  height: 150px;
}

ion-card {
  background-color: #ccd7fb;
}

ion-col {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

ion-img {
  width: 70%;
  height: 70%;
}

ion-item {
  background: none;
}
</style>
