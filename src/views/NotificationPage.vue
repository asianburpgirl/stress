<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-title>Notification</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content :fullscreen="true" ion-padding>
            <ion-header collapse="condense">
                <ion-toolbar>
                    <ion-title size="large">Notification</ion-title>
                </ion-toolbar>
            </ion-header>
            <!-- can make use of ion-grid to contain your stuff -->
            <ion-grid>
                <ion-list>
                    <ion-item>
                        <ion-label>Your Stress Level is {{ result }} today.</ion-label>            
                    </ion-item>
                </ion-list>
            </ion-grid>
        </ion-content>
    </ion-page>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonGrid, IonList, IonItem, IonLabel } from '@ionic/vue';
import { defineComponent } from "vue";
import axios from "axios";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonGrid,
    IonList,
    IonItem,
    IonLabel
  },
  data() {
    return {
      result: 0,
    };
  },
  methods:{
    getStressValue(){
        axios.get("http://127.0.0.1:5000/newData")
      .then(response => {
        const responseData = response.data;
        this.result = responseData["Stress"];
        console.log(this.result)
      })
      .catch(error => {
        console.log(error)
      })
    },
    // presentAlert() {
    //   return alertController
    //     .create({
    //       header: 'STRESS ALERT',
    //       subHeader: 'Keep Calm and Relax',
    //       message: 'You are feeling stressed. Please check your notifications for the challenges.',
    //       buttons: this.alertButtons
    //     })
    //     .then(a => a.present())
    // },
  },
  mounted() {
    this.getStressValue();
  },
  // watch: {
  //   result() {
  //     if (this.result > 2) {
  //       this.presentAlert();
  //     }
  //   },
  // },
});

</script>
