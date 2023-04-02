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
          <ion-card class="ion-padding">
            <ion-card-content class="ion-text-center">
              <ion-row>
                <ion-col size="3"> </ion-col>
                <ion-col size="3"> </ion-col>
                <ion-col size="6">
                  <ion-row>
                    <ion-col size="2"></ion-col>
                    <ion-col size="4">
                      <ion-img src="../assets/black-timer.png"></ion-img>
                    </ion-col>
                    <ion-col size="4">
                      <ion-input placeholder="10"></ion-input>
                    </ion-col>
                    <ion-col size="2">
                      <p>mins</p>
                    </ion-col>
                  </ion-row>
                </ion-col>
              </ion-row>
  
              <ion-row class="ion-padding-bottom">
                <ion-col size="3">
                  <ion-img class="left-arrow" src="../assets/black-arrow.png">
                  </ion-img>
                </ion-col>
                <ion-col size="6" class="grid ion-justify-content-center">
                  <ion-img
                    class="activity"
                    src="../assets/doctor.png"
                  ></ion-img>
                </ion-col>
                <ion-col size="3">
                  <ion-img class="right-arrow" src="../assets/black-arrow-left.png">
                  </ion-img>
                </ion-col>
              </ion-row>
              <div class="ion-padding-top">
                <p>Uncover the root of your struggles</p>
                <p>Reclaim control over your thoughts and emotions with evidence-based therapies.</p>
                <ion-button
                  expand="block"
                  shape="round"
                  color="primary"
                  @click="presentAlert"
                >
                  Start Therapy</ion-button
                >
              </div>
            </ion-card-content>
          </ion-card>
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
    IonInput,
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
      IonInput,
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
    /* margin-left:30px;  */
    margin-top: 50px;
  }
  
  ion-card {
    background-color: #d2e8ff;
  }
  
  ion-col {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
  }
  
  ion-img{
    width: 70%;
    height: 70%;
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
  