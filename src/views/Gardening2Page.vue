<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <!-- can make use of ion-grid to contain your stuff -->
      <ion-img class="activity" src="../assets/garden1.jpeg"></ion-img>
      <ion-grid>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Start small: If you're new to gardening, start with a small project
            like a windowsill herb garden or a few potted plants. This can help
            you build confidence and get a feel for the process.
          </ion-card-content>
        </ion-card>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Choose the right plants: Choose plants that are easy to care for and
            that you enjoy. This can help make the experience more enjoyable and
            less stressful.
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
            Take breaks: Gardening can be physically demanding, so make sure to
            take breaks and stay hydrated. Take the time to enjoy your garden
            and appreciate the beauty around you.
          </ion-card-content>
        </ion-card>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Connect with nature: Gardening allows you to connect with nature and
            the natural world. Take the time to observe the plants, insects, and
            animals in your garden and appreciate their role in the ecosystem.
          </ion-card-content>
        </ion-card>
        <ion-card>
          <ion-card-content class="ion-text-center">
            Experiment: Gardening can be a creative and experimental process.
            Try new plants, colours, and designs to keep things interesting and
            find what works best for you.
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
                <p>You have earned 50 points!</p>
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
