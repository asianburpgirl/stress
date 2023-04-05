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
            <ion-card-subtitle> Health Statistics: </ion-card-subtitle>
          </ion-card-header>
          <ion-card-content>
            <ion-grid>
              <ion-row class="ion-justify-content-center">
                <ion-col class="ion-justify-content-center">
                  <img
                    src="../../public/assets/heart.png"
                    @click="$router.push('/tabs/heartdata')"
                  />
                  <ion-card-subtitle>Heart rate</ion-card-subtitle>
                  <p>75 bpm</p>
                </ion-col>
                <ion-col>
                  <img src="../../public/assets/logo.png" />
                  <ion-card-subtitle> Respiratory rate </ion-card-subtitle>
                  <p>18 bpm</p>
                </ion-col>
              </ion-row>
              <ion-row>
                <ion-col>
                  <img src="../../public/assets/temperature.png" />
                  <ion-card-subtitle>Temperature</ion-card-subtitle>
                  <p>37˚C</p>
                </ion-col>
                <ion-col>
                  <img src="../../public/assets/brain.png" />
                  <ion-card-subtitle> Brain activity </ion-card-subtitle>
                  <p>1ms (fMRI)</p>
                </ion-col>
              </ion-row>
            </ion-grid>
          </ion-card-content>
        </ion-card>
      </ion-grid>
      <!-- <ion-grid class="ion-padding">
        <h4>Recommended Therapies</h4>
        <ion-row>
          <ion-col size="6 " size-md="6">
            <ion-card
              class="ion-padding ion-text-center"
              v-if="result1 === 'Self-help Methods' || result1 === 'Both'"
              href="/tabs/breathing"
            >
              <img src="../../public/assets/deep-breathing.png" />
              <ion-card-content>
                <ion-card-subtitle>Breathing</ion-card-subtitle>
                <p>10 mins</p>
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col size="6">
            <ion-card
              class="ion-padding ion-text-center"
              v-if="result1 === 'Self-help Methods' || result1 === 'Both'"
              href="/tabs/reading"
            >
              <img src="../../public/assets/open-book.png" />
              <ion-card-content>
                <ion-card-subtitle>Reading</ion-card-subtitle>
                <p>30 mins</p>
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
        <ion-row>
          <ion-col size="6">
            <ion-card
              class="ion-padding ion-text-center"
              v-if="result1 === 'Self-help Methods' || result1 === 'Both'"
              href="/tabs/gardening"
            >
              <img src="../../public/assets/farming.png" />
              <ion-card-content>
                <ion-card-subtitle>Planting</ion-card-subtitle>
                <p>1 hour</p>
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col size="6">
            <ion-card
              class="ion-padding ion-text-center"
              v-if="result1 === 'Self-help Methods' || result1 === 'Both'"
              href="/tabs/yoga"
            >
              <img src="../../public/assets/yoga.png" />
              <ion-card-content>
                <ion-card-subtitle>Yoga</ion-card-subtitle>
                <p>15 min</p>
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
        <ion-row>
          <ion-col size="6">
            <ion-card
              class="ion-padding ion-text-center"
              v-if="result1 === 'Need Social Support' || result1 === 'Both'"
              href="/tabs/support"
            >
              <img src="../../public/assets/social-support.png" />
              <ion-card-content>
                <ion-card-subtitle>Social Support</ion-card-subtitle>
                <p>1 hour</p>
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col size="6">
            <ion-card
              class="ion-padding ion-text-center"
              v-if="result1 === 'Need Social Support' || result1 === 'Both'"
              href="/tabs/professional"
            >
              <img src="../../public/assets/professional-help.png" />
              <ion-card-content>
                <ion-card-subtitle>Professional</ion-card-subtitle>
                <p>15 min</p>
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
      </ion-grid> -->
      <ion-grid class="ion-padding" v-if="result1 != 'None'">
        <h4>Recommended Therapies</h4>
        <ion-card color="tertiary" v-if="result1 === 'Self-help Methods' || result1 === 'Both'">
          <ion-card-header>
            <ion-card-title> Breathe </ion-card-title>
          </ion-card-header>
          <ion-card-content>
            <ion-row>
              <ion-col>
                <img src="../../public/assets/breathing.png" />
              </ion-col>
              <ion-col size="10">
                <p>Petals flowing in the wind</p>
                <p>Relax your mind, body, and soul with each breath.</p>
              </ion-col>
            </ion-row>

            <ion-button
              class="ion-padding"
              expand="block"
              shape="round"
              fill="outline"
              color="light"
              href="/tabs/breathing"
            >
              Start Breathing</ion-button
            >
          </ion-card-content>
        </ion-card>
        <ion-card color="primary"  v-if="result1 === 'Self-help Methods' || result1 === 'Both'">
          <ion-card-header>
            <ion-card-title> Yoga </ion-card-title>
          </ion-card-header>
          <ion-card-content>
            <ion-row>
              <ion-col>
                <img src="../../public/assets/yoga1.png" />
              </ion-col>
              <ion-col size="10">
                <p>Find balance in your practice and in your life</p>
              </ion-col>
            </ion-row>
            <ion-button
              class="ion-padding"
              expand="block"
              shape="round"
              fill="outline"
              color="light"
              href="/tabs/yoga"
            >
              Start Session</ion-button
            >
          </ion-card-content>
        </ion-card>
        <ion-card color="success" v-if="result1 === 'Self-help Methods' || result1 === 'Both'">
          <ion-card-header>
            <ion-card-title> Gardening </ion-card-title>
          </ion-card-header>
          <ion-card-content>
            <ion-row>
              <ion-col>
                <img src="../../public/assets/gardening1.png" />
              </ion-col>
              <ion-col size="10">
                <p>Start planting your seeds</p>
                <p>
                  Relax your mind, body, and soul as you embark on your
                  gardening journey.
                </p>
              </ion-col>
            </ion-row>
            <ion-button
              class="ion-padding"
              expand="block"
              shape="round"
              fill="outline"
              color="light"
              href="/tabs/gardening"
            >
              Start Gardening</ion-button
            >
          </ion-card-content>
        </ion-card>
        <ion-card color="secondary" v-if="result1 === 'Self-help Methods' || result1 === 'Both'">
          <ion-card-header>
            <ion-card-title> Reading </ion-card-title>
          </ion-card-header>
          <ion-card-content>
            <ion-row>
              <ion-col>
                <img src="../../public/assets/reading.png" />
              </ion-col>
              <ion-col size="10">
                <p>Breaking the Stigma: My Journey with Mental Health</p>
                <p>
                  Relax your mind, body, and soul with each turn of page of this
                  masterpiece.
                </p>
              </ion-col>
            </ion-row>
            <ion-button
              class="ion-padding"
              expand="block"
              shape="round"
              fill="outline"
              color="light"
              href="/tabs/reading"
            >
              Start Reading</ion-button
            >
          </ion-card-content>
        </ion-card>
        <ion-card color="light" v-if="result1 === 'Need Social Support' || result1 === 'Both'">
          <ion-card-header>
            <ion-card-title> Social Support </ion-card-title>
          </ion-card-header>
          <ion-card-content>
            <ion-row>
              <ion-col>
                <img src="../../public/assets/socialsupport.png" />
              </ion-col>
              <ion-col size="10">
                <p>You are loved and valued.</p>
                <p>
                  Surround yourself with people who lift you up and support your
                  growth.
                </p>
              </ion-col>
            </ion-row>

            <ion-button
              class="ion-padding"
              expand="block"
              shape="round"
              fill="outline"
              color="dark"
              href="/tabs/support"
            >
              Start Communicating</ion-button
            >
          </ion-card-content>
        </ion-card>

        <ion-card color="medium"  v-if="result1 === 'Need Social Support' || result1 === 'Both'">
          <ion-card-header>
            <ion-card-title> Professional Help </ion-card-title>
          </ion-card-header>
          <ion-card-content>
            <ion-row>
              <ion-col>
                <img src="../../public/assets/professional.png" />
              </ion-col>
              <ion-col size="10">
                <p>You are loved and valued.</p>
                <p>
                  Surround yourself with people who lift you up and support your
                  growth.
                </p>
              </ion-col>
            </ion-row>

            <ion-button
              class="ion-padding"
              expand="block"
              shape="round"
              fill="outline"
              color="light"
              href="/tabs/professional"
            >
              Start Communicating</ion-button
            >
          </ion-card-content>
        </ion-card>
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
  // IonInput,
  IonButton,
  IonCard,
  IonCardSubtitle,
  IonCardHeader,
  IonRow,
  IonCol,
  IonGrid,
  IonCardContent,
  alertController,
  IonCardTitle,
} from "@ionic/vue";

import { defineComponent } from "vue";
import axios from "axios";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    // IonInput,
    IonButton,
    IonCard,
    IonCardSubtitle,
    IonCardHeader,
    IonRow,
    IonCol,
    IonGrid,
    IonCardContent,
    IonCardTitle,
  },
  data() {
    return {
      result1: "",
      result: 0,
      alertButtons: ["OK"],
    };
  },
  methods: {
    getStressValue() {
      axios
        .get("http://127.0.0.1:5000/newData")
        .then((response) => {
          const responseData = response.data;
          this.result = responseData["Stress"];
          console.log("Stress level is " + this.result);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getQuestionnaireValue() {
      axios
        .get("http://127.0.0.1:5000/response")
        .then((response) => {
          const responseData = response.data;
          this.result1 = responseData["options"][3];
          console.log("Questionnaire value is " + this.result1);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    presentAlert() {
      return alertController
        .create({
          header: "STRESS ALERT",
          subHeader: "Take a chill pill please",
          message: "Please exercise your therapies",
          buttons: this.alertButtons,
        })
        .then((a) => a.present());
    },
  },
  mounted() {
    this.getStressValue();
    this.getQuestionnaireValue();
  },
  watch: {
    result() {
      if (this.result > 1) {
        this.presentAlert();
      }
    },
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

/* ion-card {
  background-color: #f2f7ff;
} */
</style>
