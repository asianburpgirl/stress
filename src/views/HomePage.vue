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
          <ion-title size="large">Hello, Anna</ion-title>
        </ion-toolbar>
      </ion-header>
      <!-- can make use of ion-grid to contain your stuff -->
      <ion-grid>
        <ion-card class="ion-padding">
          <ion-card-header>
            <p>How are you feeling today?</p>
            <ion-card-subtitle>
              Health Statistics:
            </ion-card-subtitle>
          </ion-card-header>
          <ion-card-content>
            <ion-grid>
              <ion-row class="ion-justify-content-center">
                <ion-col class="ion-justify-content-center">
                  <img src="../asset/heart.png" />
                  <ion-card-subtitle>Heart rate</ion-card-subtitle>
                  <p>75 bpm </p>
                </ion-col>
                <ion-col>
                  <img src="../asset/logo.png" />
                  <ion-card-subtitle>
                    Respiratory rate
                  </ion-card-subtitle>
                  <p>18 bpm</p>
                </ion-col>
              </ion-row>
              <ion-row>
                <ion-col>
                  <img src="../asset/temperature.png" />
                  <ion-card-subtitle>Temperature</ion-card-subtitle>
                  <p>37˚C</p>
                </ion-col>
                <ion-col>
                  <img src="../asset/brain.png" />
                  <ion-card-subtitle>
                    Brain activity
                  </ion-card-subtitle>
                  <p>
                    1ms (fMRI)
                  </p>
                </ion-col>
              </ion-row>
            </ion-grid>
          </ion-card-content>
        </ion-card>
      </ion-grid>
      <ion-grid class="ion-padding">
        <h4>Recommended Therapies</h4>
        <ion-row>
          <ion-col size="6 " size-md="6">
            <ion-card class="ion-padding ion-text-center">
              <img src="../asset/deep-breathing.png" />
              <ion-card-content>
                <ion-card-subtitle>Breathing</ion-card-subtitle>
                <p>10 mins</p>
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col size="6">
            <ion-card class="ion-padding ion-text-center">
              <img src="../asset/open-book.png" />
              <ion-card-content>
                <ion-card-subtitle>Reading</ion-card-subtitle>
                <p>30 mins</p>
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
        <ion-row>
          <ion-col size="6">
            <ion-card class="ion-padding ion-text-center">
              <img src="../asset/farming.png" />
              <ion-card-content>
                <ion-card-subtitle>Planting</ion-card-subtitle>
                <p>1 hour</p>
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col size="6">
            <ion-card class="ion-padding ion-text-center">
              <img src="../asset/yoga.png" />
              <ion-card-content>
                <ion-card-subtitle>Yoga</ion-card-subtitle>
                <p>15 min</p>
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
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
} from "@ionic/vue";

import { defineComponent } from "vue";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
  },
});
</script>

<style scoped>
/* iOS places the subtitle above the title */

/* ion-card-header.ios {
  display: flex;
  flex-flow: column-reverse;
} */

/* ion-card-title {
  --color: gray;
} */

ion-img {
  width: 20%;
  height: 20%;
  justify-content: center;
}

ion-card {
  background-color: #f2f7ff;
}
</style>
