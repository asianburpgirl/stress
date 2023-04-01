<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Analytics</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content ion-padding>
      <!-- <ion-grid> -->
      <ion-row>
        <ion-col>
          <div class="chart-container">
            <Bar :data="heartRateData"></Bar>
          </div>
        </ion-col>
        <ion-col>
          <div class="chart-container">
            <LineChart :data="hrvData"></LineChart>
          </div>
        </ion-col>
      </ion-row>
      <!-- </ion-grid> -->
      <ion-card>
        <ion-card-header>
          <ion-card-title>Heart Rate</ion-card-title>
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
          <ion-card-title>HRV</ion-card-title>
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
  IonCard,
  IonRow,
  IonNote,
  IonCardContent,
  IonCardHeader,
  IonCardTitle,
  IonItem,
  IonLabel,
  IonList,
  // IonGrid,
  IonCol,
} from "@ionic/vue";
import { Bar, Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Chart,
} from "chart.js";
ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
);

import axios from "axios";
import { defineComponent } from "vue";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonCard,
    IonRow,
    IonNote,
    IonCardContent,
    IonCardHeader,
    IonCardTitle,
    IonItem,
    IonLabel,
    IonList,
    // IonGrid,
    IonCol,
    Bar,
    LineChart: Line,
  },
  data() {
    return {
      heartRateData: {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        datasets: [
          {
            label: "Heart Rate",
            data: [78, 82, 79, 85, 90, 92, 88],
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgba(255, 99, 132, 1)",
            borderWidth: 1,
          },
        ],
      },
      hrvData: {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        datasets: [
          {
            label: "HRV",
            data: [60, 63, 65, 61, 59, 57, 61],
            fill: false,
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 1,
          },
        ],
      },
      revenueData: [
        { id: 1, label: "Monday", amount: "78" },
        { id: 2, label: "Tuesday", amount: "82" },
        { id: 3, label: "Wednesday", amount: "79" },
        { id: 4, label: "Thursday", amount: "85" },
        { id: 5, label: "Friday", amount: "90" },
        { id: 6, label: "Saturday", amount: "92" },
        { id: 7, label: "Sunday", amount: "88" },
      ],
      userData: [
        { id: 1, label: "Monday", amount: "60" },
        { id: 2, label: "Tuesday", amount: "63" },
        { id: 3, label: "Wednesday", amount: "65" },
        { id: 4, label: "Thursday", amount: "61" },
        { id: 5, label: "Friday", amount: "59" },
        { id: 6, label: "Saturday", amount: "57" },
        { id: 7, label: "Sunday", amount: "61" },
      ],
    };
  },
  mounted() {
    this.heartdata();
  },
  methods: {
    heartdata() {
      const url = "http://127.0.0.1:5000/alldata";
      const HRresult: string[] = [];
      axios
        .get(url)
        .then((response) => {
          const heartData = response.data;
          for (const heartRate of heartData) {
            // console.log(heartRate["Date"]);
            // this.heartDate = heartRate["HR"];
            HRresult.push(heartRate["HR"]);
          }
          console.log(HRresult);
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    // generateData() {
    //     const heartRateData = {
    //         labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    //         datasets: [
    //             {
    //                 label: 'Heart Rate',
    //                 data: [78, 82, 79, 85, 90, 92, 88],
    //                 backgroundColor: 'rgba(255, 99, 132, 0.2)',
    //                 borderColor: 'rgba(255, 99, 132, 1)',
    //                 borderWidth: 1,
    //             }
    //         ],
    //     }
    //     const hrvData = {
    //         labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    //         datasets: [
    //         {
    //             label: 'HRV',
    //             data: [60, 63, 65, 61, 59, 57, 61],
    //             fill: false,
    //             borderColor: 'rgba(54, 162, 235, 1)',
    //             borderWidth: 1,
    //         },
    //         ],
    //     };

    //     this.heartRateData = heartRateData;
    //     this.hrvData = hrvData;

    // }
  },
});
</script>

<style scoped>
.chart-container {
  position: relative;
  margin: auto;
  width: 80vw;
}
</style>
