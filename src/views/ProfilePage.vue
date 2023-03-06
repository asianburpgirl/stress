<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-title>Profile</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content :fullscreen="true" ion-padding style="margin:0">
            <ion-header collapse="condense">
                <ion-toolbar>
                    <ion-title size="large">Profile</ion-title>
                </ion-toolbar>
            </ion-header>
            <!-- can make use of ion-grid to contain your stuff -->
            <ion-grid style="margin: 0;display:flex">
              <ion-grid>
                <ion-img style="size:100%" src="../assets/profile.png"
                  ></ion-img>
            </ion-grid>
            </ion-grid>
        </ion-content>
    </ion-page>
</template>

<script setup lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonGrid } from '@ionic/vue';
</script>
