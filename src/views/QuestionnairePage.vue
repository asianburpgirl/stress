<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Preferences</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" ion-padding>
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">App Preferences</ion-title>
        </ion-toolbar>
      </ion-header>
      <!-- can make use of ion-grid to contain your stuff -->
      <ion-grid class="ion-padding">
        <p>Before bringing you to the home page, let's get you set up 🙂</p>
        <ion-card color="tertiary" v-for="question in questionList" :key="question.id">
          <ion-card-header>
            <ion-card-title>Question {{ question.id }}</ion-card-title>
          </ion-card-header>
          <ion-card-content>
            {{question.question}}
          </ion-card-content>
          <ion-list>
            <ion-radio-group>
              <ion-item v-for="option in question.options" :key="option.label">
                <ion-label>{{ option.label }}</ion-label>
                <ion-radio slot="end" :value="option.label"></ion-radio>
              </ion-item>
            </ion-radio-group>
          </ion-list>
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
  IonGrid,
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardTitle,
  IonRadio,
  IonRadioGroup,
  IonList,
  IonItem,
  IonLabel,
} from "@ionic/vue";

import { defineComponent } from "vue";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonGrid,
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardTitle,
    IonRadio,
    IonRadioGroup,
    IonList,
    IonItem,
    IonLabel,
  },
  data() {
    return {
      questionList: [
        {
            id: 1,
            question: "What brings you to this mental health application?",
            options: [
                {
                    label: "To destress myself"
                },
                {
                    label: "To explore the application"
                }
            ]
        },
        {
            id: 2,
            question: "Have you ever received mental health treatment before?",
            options: [
                {
                    label: "Yes"
                },
                {
                    label: "No"
                }
            ]
        },
        {
            id: 3,
            question: "Have you ever been diagnosed with a mental health condition?",
            options: [
                {
                    label: "Yes"
                },
                {
                    label: "No"
                }
            ]
        },
        {
            id: 4,
            question: "Are you currently taking any medications for your mental health?",
            options: [
                {
                    label: "Yes"
                },
                {
                    label: "No"
                }
            ]
        },
        {
            id: 5,
            question: "How would you rate your current level of distress related to your mental health?",
            options: [
                {
                    label: "1"
                },
                {
                    label: "2"
                },
                {
                    label: "3"
                },
                {
                    label: "4"
                },
                {
                    label: "5"
                },
                {
                    label: "6"
                },
                {
                    label: "7"
                },
                {
                    label: "8"
                },
                {
                    label: "9"
                },
                {
                    label: "10"
                }
            ]
        },
        {
          id: 6,
          question: "How would you like to seek help?",
          options: [
            { label: "Self-help Methods" },
            { label: "Need Social Support" },
            { label: "Both" },
            { label: "None" },
          ],
        },
      ],
    };
  },
});
</script>

<style scoped>
ion-radio {
  --border-radius: 4px;
  --inner-border-radius: 4px;

  --color: #ddd;
  --color-checked: #6815ec;
}

ion-radio.ios {
  width: 20px;
  height: 20px;

  border: 2px solid #ddd;
  border-radius: 4px;
}

.radio-checked.ios {
  border-color: #6815ec;
}
</style>
