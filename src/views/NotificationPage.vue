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
                        <ion-label>Pokémon Yellow</ion-label>
                        <ion-button>Start Challenge</ion-button>
                    </ion-item>
                    <ion-item>
                        <ion-label>Mega Man X</ion-label>
                        <ion-button>Start Challenge</ion-button>
                    </ion-item>
                    <ion-item>
                        <ion-label>The Legend of Zelda</ion-label>
                        <ion-button>Start Challenge</ion-button>
                    </ion-item>
                    <ion-item>
                        <ion-label>Pac-Man</ion-label>
                        <ion-button>Start Challenge</ion-button>
                    </ion-item>
                    <ion-item>
                        <ion-label>Super Mario World</ion-label>
                        <ion-button>Start Challenge</ion-button>
                    </ion-item>
                </ion-list>
            </ion-grid>
        </ion-content>
    </ion-page>
</template>

<script setup lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonGrid } from '@ionic/vue';
</script>
