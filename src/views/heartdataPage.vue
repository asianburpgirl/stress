<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Analytics</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
      <ion-card>
        <ion-card-header>
          <ion-card-title>Revenue</ion-card-title>
        </ion-card-header>
        <ion-card-content>
          <ion-list>
            <ion-item v-for="item in revenueData" :key="item.id">
              <ion-label>{{ item.label }}</ion-label>
              <ion-note slot="end">{{ item.amount }}</ion-note>
            </ion-item>
          </ion-list>
        </ion-card-content>
      </ion-card>

      <ion-card>
        <ion-card-header>
          <ion-card-title>Users</ion-card-title>
        </ion-card-header>
        <ion-card-content>
          <ion-list>
            <ion-item v-for="item in userData" :key="item.id">
              <ion-label>{{ item.label }}</ion-label>
              <ion-note slot="end">{{ item.amount }}</ion-note>
            </ion-item>
          </ion-list>
        </ion-card-content>
      </ion-card>
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
  data() {
    return {
      revenueData: [
        { id: 1, label: "Today", amount: "$1,000" },
        { id: 2, label: "This Week", amount: "$5,000" },
        { id: 3, label: "This Month", amount: "$20,000" },
        { id: 4, label: "This Year", amount: "$100,000" },
      ],
      userData: [
        { id: 1, label: "Active Users", amount: "100" },
        { id: 2, label: "New Users", amount: "20" },
        { id: 3, label: "Total Users", amount: "1,000" },
      ],
    };
  },
});

// const revenueData = [
//   { id: 1, label: "Today", amount: "$1,000" },
//   { id: 2, label: "This Week", amount: "$5,000" },
//   { id: 3, label: "This Month", amount: "$20,000" },
//   { id: 4, label: "This Year", amount: "$100,000" },
// ];

// const userData = [
//   { id: 1, label: "Active Users", amount: "100" },
//   { id: 2, label: "New Users", amount: "20" },
//   { id: 3, label: "Total Users", amount: "1,000" },
// ];
</script>
