<template>
  <div class="home">
    <div class="profile">
      <img class="face" alt="Muh face" src="../assets/profile.jpeg" />
    </div>
    <div class="split"></div>
    <div class="link-buttons">
      <h1>Hyun-Tae Jin</h1>
      <div class="mdiIcons">
        <v-icon large dark>{{ mdiAt }}</v-icon>
        <v-icon large dark>{{ mdiGithub }}</v-icon>
        <v-icon large dark>{{ mdiLinkedin }}</v-icon>
      </div>
    </div>
  </div>
</template>

<script>
import { mdiAt } from "@mdi/js";
import { mdiGithub } from "@mdi/js";
import { mdiLinkedin } from "@mdi/js";

export default {
  name: "Home",
  data: () => ({
    mdiGithub: mdiGithub,
    mdiAt: mdiAt,
    mdiLinkedin: mdiLinkedin
  })
};
</script>

<style lang="scss">
@import "@/styles/home.scss";
</style>
