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
                    <ion-title size="large">Home</ion-title>
                </ion-toolbar>
            </ion-header>
            <!-- can make use of ion-grid to contain your stuff -->
            <ion-grid>
                <ion-card style="width: 340px; height: 600px; background-color: white;">
                    <ion-grid>
                        <ion-row>
                            <ion-card-header
                                style="color: #5678AB; text-align: center; font-weight: bold; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 1.2rem; margin-left: 25px; margin-top:50px">
                                Hello, Anna!
                            </ion-card-header>
                            <ion-card style="display: block; margin: auto; width: 275px; border-radius: 10px">
                                <ion-card-header>
                                    <ion-card-title
                                        style="font-weight: bold; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 1rem">
                                        How are you feeling today?
                                    </ion-card-title>
                                    <ion-card-subtitle style="font-size: 0.6rem">
                                        Here's a summary of your health statistics:
                                    </ion-card-subtitle>
                                </ion-card-header>
                                <ion-card-content>
                                    <ion-grid>
                                        <ion-row style="margin-left: -10px; margin-right: -10px">
                                            <ion-col>
                                                <ion-img src="../assets/heartrate.png"
                                                    style="width: 25%; float: left; margin-right: 5px">
                                                </ion-img>
                                                <ion-card-subtitle style="font-size: 0.3rem">
                                                    Heart rate:<br>75 bpm
                                                </ion-card-subtitle>
                                                <ion-img src="../assets/respiratoryrate.png"
                                                    style="width: 25%; float: left; margin-right: 5px; margin-top: 20px">
                                                </ion-img>
                                                <ion-card-subtitle style="font-size: 0.3rem; margin-top: 20px">
                                                    Respiratory rate: 18 bpm
                                                </ion-card-subtitle>
                                            </ion-col>
                                            <ion-col>
                                                <ion-img src="../assets/temperature.png"
                                                    style="width: 25%; float: left; margin-right: 5px">
                                                </ion-img>
                                                <ion-card-subtitle style="font-size: 0.3rem">
                                                    Temperature:<br>37˚C
                                                </ion-card-subtitle>
                                                <ion-img src="../assets/brainactivity.png"
                                                    style="width: 25%; float: left; margin-right: 5px; margin-top: 20px">
                                                </ion-img>
                                                <ion-card-subtitle style="font-size: 0.3rem; margin-top: 20px">
                                                    Brain activity:<br>1ms (fMRI)
                                                </ion-card-subtitle>
                                            </ion-col>
                                        </ion-row>
                                    </ion-grid>
                                </ion-card-content>
                            </ion-card>
                        </ion-row>
                        <ion-row>
                            <ion-card-subtitle
                                style="font-size: 0.6rem; font-weight: bold; text-align: center; margin: 30px auto">
                                Here are some recommended therapies for you:
                            </ion-card-subtitle>
                        </ion-row>
                        <ion-row style="margin: -30px auto; width: 95%">
                            <ion-col>
                                <ion-card style="height: 90px; border-radius: 10px; background-color: #F2F7FF">
                                    <ion-img src="../assets/deepbreathing.png"
                                        style="width: 30%; display: block; margin: 15px auto">
                                    </ion-img>
                                    <ion-card-subtitle style="text-align: center; font-size: 0.6rem; margin-top: 10px">
                                        Deep breathing
                                    </ion-card-subtitle>
                                </ion-card>
                                <ion-card
                                    style="height: 90px; margin-top: 20px; border-radius: 10px; background-color: #F2F7FF">
                                    <ion-img src="../assets/reading.png"
                                        style="width: 30%; display: block; margin: 15px auto">
                                    </ion-img>
                                    <ion-card-subtitle style="text-align: center; font-size: 0.6rem; margin-top: 10px">
                                        Reading (30 min)
                                    </ion-card-subtitle>
                                </ion-card>
                            </ion-col>
                            <ion-col>
                                <ion-card style="height: 90px; border-radius: 10px; background-color: #F2F7FF">
                                    <ion-img src="../assets/gardening.png"
                                        style="width: 30%; display: block; margin: 15px auto">
                                    </ion-img>
                                    <ion-card-subtitle style="text-align: center; font-size: 0.6rem; margin-top: 10px">
                                        Gardening
                                    </ion-card-subtitle>
                                </ion-card>
                                <ion-card
                                    style="height: 90px; margin-top: 20px; border-radius: 10px; background-color: #F2F7FF">
                                    <ion-img src="../assets/yoga.png" style="width: 30%; display: block; margin: 15px auto">
                                    </ion-img>
                                    <ion-card-subtitle style="text-align: center; font-size: 0.6rem; margin-top: 10px">
                                        Doing yoga (15 min)
                                    </ion-card-subtitle>
                                </ion-card>
                            </ion-col>
                        </ion-row>
                    </ion-grid>
                </ion-card>
            </ion-grid>
        </ion-content>
    </ion-page>
</template>

<script setup lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import ExploreContainer from '@/components/ExploreContainer.vue';
</script>

<style scoped>
/* iOS places the subtitle above the title */
ion-card-header.ios {
    display: flex;
    flex-flow: column-reverse;
}

ion-card-title {
    --color: gray
}
</style>