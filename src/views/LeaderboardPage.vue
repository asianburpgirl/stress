<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-title>Leaderboard</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content :fullscreen="true" ion-padding>
            <ion-header collapse="condense">
                <ion-toolbar>
                    <ion-title size="large">Leaderboard</ion-title>
                </ion-toolbar>
            </ion-header>
            <!-- can make use of ion-grid to contain your stuff -->
            <ion-grid>
                <ion-img src="../assets/leaderboard.png"></ion-img>
            </ion-grid>
        </ion-content>
    </ion-page>
</template>

<script setup lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonGrid } from '@ionic/vue';
</script>
