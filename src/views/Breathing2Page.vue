<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <!-- can make use of ion-grid to contain your stuff -->
      <ion-img class="activity" src="../assets/breathing1.png"></ion-img>
      <ion-grid>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Find a comfortable seated or lying position, with your back straight
            and your hands resting comfortably in your lap.
          </ion-card-content>
        </ion-card>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Close your eyes and bring your attention to your breath. Notice the
            sensation of the air moving in and out of your body.
          </ion-card-content>
        </ion-card>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Begin to take slow, deep breaths, focusing on filling your lungs
            fully and exhaling completely.
          </ion-card-content>
        </ion-card>
        <ion-card>
          <ion-card-content class="ion-text-center">
            If your mind begins to wander, gently bring your focus back to your
            breath. Don't judge yourself for losing focus; simply acknowledge
            the distraction and redirect your attention.
          </ion-card-content>
        </ion-card>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Try to maintain this focus for several minutes, or for as long as
            feels comfortable.
          </ion-card-content>
        </ion-card>
        <ion-card>
          <ion-card-content class="ion-text-center">
            When you're ready to end your practice, take a few final deep
            breaths and slowly open your eyes.
          </ion-card-content>
        </ion-card>
        

        <ion-grid>
          <ion-button
            expand="block"
            color="tertiary"
            @click="presentAlert"
          >
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
              <p>You have earned 20 points!</p>
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

ion-input.custom {
    --background: none
    --placeholder-opacity: .8;
    --padding-bottom: 10px;
    --padding-end: 10px;
    --padding-start: 10px;
    --padding-top: 10px;
  }

ion-item{
  background: none;
}
</style>
