<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Login</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" ion-padding>
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Login</ion-title>
        </ion-toolbar>
      </ion-header>
      <!-- can make use of ion-grid to contain your stuff -->

      <ion-grid class="padding">
        <div class="ion-text-center">
          <img src="../../public/assets/logo.png" />
        </div>
        <ion-card-header class="ion-text-center ion-padding-top">
          <ion-card-title>
            <span style="color: #5678ab">Stress</span
            ><span style="color: #d36fa5">Less</span>
          </ion-card-title>
        </ion-card-header>
        <ion-row class="ion-justify-content-center">
          <ion-col size="10">
            <p>Scan with Singpass app to login</p>
          </ion-col>
          <ion-col size="10">
            <a href="/questionnaire">
              <img src="../../public/assets/singpass.png" class="singpass" style="width: 50%; height: 90%;"/> 
            </a>
          </ion-col>
          <ion-col size="10">
            <ion-button href="/questionnaire" size="small" style="">
              <ion-icon :icon="lockClosed"></ion-icon>
              Use password login instead
            </ion-button>
          </ion-col>
          <ion-col size="10">
            <p>Don't have the Singpass app?</p>
            <p>
              <a href="/questionnaire">Download now</a>
            </p>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonCardHeader,
  IonIcon,
  IonRow,
  IonCol,
  IonGrid,
  IonCardTitle,
  IonButton,
} from "@ionic/vue";

import { defineComponent } from "vue";
import { lockClosed } from "ionicons/icons";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonCardHeader,
    IonIcon,
    IonRow,
    IonCol,
    IonGrid,
    IonCardTitle,
    IonButton,
  },
  setup() {
    return { lockClosed };
  },
});
</script>

<style scoped>
ion-button {
  --background: white;
  --color: gray;
  --color-hover: black;
  --box-shadow: none;
  --text-transform: none;
  --padding-top: 10px;
  --padding-bottom: 10px;
  display: block;
  margin-top: 10px;
  margin-left: auto;
  margin-right: auto;
  text-transform: none;
}

ion-card-subtitle {
  font-weight: bold;
  font-size: 1.2rem;
}

p {
  color: black;
  text-align: center;
  width: 100%;

  font-size: 0.9rem;
}

.singpass {
  width: 55%;
  height: auto;
  display: block;
  margin-top: 5%;
  margin-left: auto;
  margin-right: auto;
}

a {
  color: red;
  text-decoration: none;
}

.padding{
  padding-top: 50px;
}
</style>
