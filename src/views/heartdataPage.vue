<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Analytics</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content ion-padding>
    <canvas id="mychart"></canvas>
    <canvas id="mychart2"></canvas>
        <div v-for="i in HRresult" :key="i">
          <p>{{ i["HR"] }}</p>
        </div>
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
              <ion-note :style="{color: 'red'}" v-if="Number(item.amount) < 65" slot="end">{{ item.amount }}</ion-note>
              <ion-note :style="{color: 'green'}" v-else  slot="end">{{ item.amount }}</ion-note>
            </ion-item>
          </ion-list>
        </ion-card-content>
      </ion-card>
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
} from "chart.js/auto";
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
import { isProxy, toRaw } from 'vue';
import {Bar, Line} from 'vue-chartjs'
const responseData = "http://127.0.0.1:5000/alldata";

export default defineComponent({

  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonCard,
    IonNote,
    IonCardContent,
    IonCardHeader,
    IonCardTitle,
    IonItem,
    IonLabel,
    IonList,
    // IonGrid,
    //Bar,
    //Line
  
  },
  data(){
    return {
        dataList: [],
        HRresult: [],
      
      heartRateData: {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        datasets: [
          {
            label: "Heart Rate",
            data: [],
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
            data: [59.24640691,46.89195955,64.40598994,76.24500979,66.0516333,70.89614346277754,67.28650447311502],
            fill: false,
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 1,
          },
        ],
      },
      revenueData: [
        { id: 1, label: "Monday", amount: "78" },
        { id: 2, label: "Tuesday", amount: "76" },
        { id: 3, label: "Wednesday", amount: "71" },
        { id: 4, label: "Thursday", amount: "78" },
        { id: 5, label: "Friday", amount: "78" },
        { id: 6, label: "Saturday", amount: "82" },
        { id: 7, label: "Sunday", amount: "84" },
      ],
      userData: [
        { id: 1, label: "Monday", amount: "59" },
        { id: 2, label: "Tuesday", amount: "46" },
        { id: 3, label: "Wednesday", amount: "64" },
        { id: 4, label: "Thursday", amount: "76" },
        { id: 5, label: "Friday", amount: "66" },
        { id: 6, label: "Saturday", amount: "70" },
        { id: 7, label: "Sunday", amount: "67" },
      ],
    };
  },
  mounted() {
     this.heartdata()
     const ctx = document.getElementById('mychart').getContext('2d')
     axios.get(responseData).then(response =>{
      const d =  response.data.map(item => item.HR)
      const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
              labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
              datasets: [{
                label: 'Heart Rate',
                data: d,
                backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)',
                  'rgba(0, 255, 0, 0.2)'
                  
                          ],
                borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)',
                  'rgba(0, 255, 0, 0.2)'
                ],
                borderWidth:1
              }]
            },
            options: {
              responsive: true,
              scales: {
                y: {  
                  beginAtZero: false
                }
              }
            }
          });
     });
     const ctx2 = document.getElementById('mychart2').getContext('2d')
     axios.get(responseData).then(response =>{
      const d =  response.data.map(item => item.SDNN)
      const myChart = new Chart(ctx2, {
            type: 'line',
            data: {
              labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
              datasets: [{
                label: 'HRV',
                data: d,
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1

              }]
            },
            options: {
              responsive: true,
              scales: {
                y: {
                  beginAtZero: false
                }
              }
            }
          });
     })
  },
  methods: {
    heartdata(){
      try {
        axios.get(responseData).then(response =>
          {
            const data = response.data
            const HRValue =data.map(item => item.HR);
            const SDNNValue =data.map(item => item.SDNN)
            this.revenueData = []
            this.userData = []
            
            const labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            for (let i = 0 ; i < 7 ; i ++){
              this.revenueData.push({
                id : i,
                label : labels[i],
                amount : HRValue[i]
              })
              this.userData.push({
                id : i,
                label : labels[i],
                amount : SDNNValue[i].toFixed(0)
              })
            }
          }
        )
        
      } catch (error) {
        console.error(error);
      }
      
    }
    },
  },
  );

</script>

<style scoped>
.chart-container {
  position: relative;
  margin: auto;
  width: 80vw;
}
</style>
