<template>
  <v-container fluid v-if="visible" class="home">
    <v-row class="mainbody">
      <v-col xl="5" lg="5" md="5" sm="5" xs="6">
        <img class="face" alt="Muh face" src="../assets/profile.jpeg" />
      </v-col>
      <v-col xl="2" lg="2" md="2" sm="2" xs="1">
        <div class="split"></div>
      </v-col>
      <v-col xl="5" lg="5" md="5" sm="5" xs="6">
        <div class="link-buttons">
          <h1>Hyun-Tae Jin</h1>
          <div class="mdiIcons">
            <a
              target="_blank"
              rel="noopener noreferrer"
              href="mailto:htjmario@gmail.com"
            >
              <v-tooltip bottom color="#05385B">
                <template v-slot:activator="{ on }">
                  <v-hover v-slot:default="{ hover }">
                    <v-icon
                      large
                      dark
                      v-on="on"
                      :color="hover ? '#CE493B' : '#edf5e1'"
                      >{{ mdiGmail }}</v-icon
                    >
                  </v-hover>
                </template>
                <span>htjmario@gmail.com</span>
              </v-tooltip>
            </a>
            <v-icon small dark>{{ mdiPowerOn }}</v-icon>
            <a
              target="_blank"
              rel="noopener noreferrer"
              href="https://github.com/HTJin"
            >
              <v-tooltip bottom color="#05385B">
                <template v-slot:activator="{ on }">
                  <v-hover v-slot:default="{ hover }">
                    <v-icon
                      large
                      dark
                      v-on="on"
                      :color="hover ? '#A66CFF' : '#edf5e1'"
                      >{{ mdiGithub }}</v-icon
                    >
                  </v-hover>
                </template>
                <span>github.com/htjin</span>
              </v-tooltip>
            </a>
            <v-icon small dark>{{ mdiPowerOn }}</v-icon>
            <a
              target="_blank"
              rel="noopener noreferrer"
              href="https://linkedin.com/in/HTJin"
            >
              <v-tooltip bottom color="#05385B">
                <template v-slot:activator="{ on }">
                  <v-hover v-slot:default="{ hover }">
                    <v-icon
                      large
                      dark
                      v-on="on"
                      :color="hover ? '#0077B5' : '#edf5e1'"
                      >{{ mdiLinkedin }}</v-icon
                    >
                  </v-hover>
                </template>
                <span>linkedin/in/HTJin</span>
              </v-tooltip>
            </a>
          </div>
        </div>
      </v-col>
    </v-row>
    <div class="scroll">
      <v-tooltip top color="#5cdb95">
        <template v-slot:activator="{ on }">
          <div class="down" @click="visible = !visible" v-on="on">
            <router-link to="/timeline">
              <v-hover v-slot:default="{ hover }">
                <v-icon
                  v-if="hover"
                  large
                  dark
                  color="#5cdb95"
                  @click="visible = !visible"
                  >{{ mdiChevronTripleDown }}</v-icon
                >
                <v-icon v-else large dark color="#edf5e1">{{
                  mdiChevronDown
                }}</v-icon>
              </v-hover>
            </router-link>
          </div>
        </template>
        <span>Timeline</span>
      </v-tooltip>
    </div>
  </v-container>
</template>

<script>
import { mdiGmail } from "@mdi/js";
import { mdiGithub } from "@mdi/js";
import { mdiLinkedin } from "@mdi/js";
import { mdiPowerOn } from "@mdi/js";
import { mdiChevronDown } from "@mdi/js";
import { mdiChevronTripleDown } from "@mdi/js";

export default {
  name: "Home",
  data: () => ({
    mdiGithub: mdiGithub,
    mdiGmail: mdiGmail,
    mdiLinkedin: mdiLinkedin,
    mdiPowerOn: mdiPowerOn,
    mdiChevronDown: mdiChevronDown,
    mdiChevronTripleDown: mdiChevronTripleDown,
    visible: true
  })
};
</script>

<style lang="scss">
@import "@/styles/home.scss";
</style>
