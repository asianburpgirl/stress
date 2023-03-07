<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Leaderboard</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" ion-padding style="margin: 0">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Leaderboard</ion-title>
        </ion-toolbar>
      </ion-header>
      <!-- can make use of ion-grid to contain your stuff -->
      <ion-grid style="margin: 0; display: flex" class="ion-padding-top">
        <!-- <ion-img style="size: 100%" src="../assets/leaderboard.png"></ion-img> -->

        <ion-segment :value="$data.subView" @ionChange="segmentChanged($event)">
          <ion-segment-button value="today" id="today">
            <ion-label>Today</ion-label>
          </ion-segment-button>
          <ion-segment-button value="week" id="week">
            <ion-label>Week</ion-label>
          </ion-segment-button>
          <ion-segment-button value="month" id="month">
            <ion-label>Month</ion-label>
          </ion-segment-button>
        </ion-segment>
      </ion-grid>
      <ion-grid class="ion-padding ion-text-center" v-if="subView == 'today'">
        <ion-row>
          <ion-col> <h1>2</h1> </ion-col>
          <ion-col> <h1>1</h1> </ion-col>
          <ion-col> <h1>3</h1> </ion-col>
        </ion-row>
        <ion-row class="ion-padding-top">
          <ion-col>
            <img src="../../public/assets/grin.png" />
          </ion-col>
          <ion-col>
            <img src="../../public/assets/queen.png" />
          </ion-col>
          <ion-col>
            <img src="../../public/assets/man.png" />
          </ion-col>
        </ion-row>
        <ion-list class="ion-padding" lines="full">
          <ion-item>
            <h1>4</h1>
            <ion-label class="ion-padding">Antony</ion-label>
            <p slot="end">6574</p>
          </ion-item>
          <ion-item>
            <h1>5</h1>
            <ion-label class="ion-padding">Britney</ion-label>
            <p slot="end">5673</p>
          </ion-item>
          <ion-item>
            <h1>6</h1>
            <ion-label class="ion-padding">Dylan</ion-label>
            <p slot="end">5129</p>
          </ion-item>
        </ion-list>
      </ion-grid>
      <ion-grid class="ion-padding" v-if="subView == 'week'">
        <!-- select: week -->
      </ion-grid>
      <ion-grid class="ion-padding" v-if="subView == 'month'">
        <!-- select: month -->
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
  IonSegment,
  IonSegmentButton,
  IonList,
  IonItem,
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
    IonSegment,
    IonSegmentButton,
  },
  data() {
    return {
      subView: "today",
    };
  },
  methods: {
    segmentChanged(e: CustomEvent) {
      this.subView = e.detail.value;
    },
  },
});
</script>

<style scoped>
/* ion-segment-button::part(indicator-background) {
  background: #08a391;
}

ion-segment-button.ios::part(native) {
  color: #08a391;
}

.segment-button-checked.ios::part(native) {
  color: #fff;
}

ion-segment-button.ios::part(indicator-background) {
  border-radius: 20px;
} */
</style>
