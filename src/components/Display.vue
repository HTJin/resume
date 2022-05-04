<template>
  <div class="display">
    <v-row class="modifiers">
      <v-col class="input-info">
        <h1>Modifiers:</h1>
        <v-icon large dark>{{ mdiInformationOutline }}</v-icon>
      </v-col>
      <v-col class="input-mod"> </v-col>
    </v-row>
    <v-row class="keys">
      <v-col class="input-info">
        <h1>Keys:</h1>
      </v-col>
      <v-col class="input-key"> </v-col>
    </v-row>
  </div>
</template>

<script>
import { mdiInformationOutline } from "@mdi/js";

export default {
  name: "Display",
  data: () => ({
    mdiInformationOutline: mdiInformationOutline
  })
};
</script>

<style lang="scss">
@import "@/styles/display.scss";
</style>
