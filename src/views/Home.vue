<template>
  <v-container fluid class="home" @wheel.prevent="handleWheel">
    <v-row class="mainbody">
      <v-col xl="5" lg="5" md="5" sm="5" xs="6">
        <img class="face" alt="Muh face" src="../assets/profile.png" />
      </v-col>
      <v-col xl="2" lg="2" md="2" sm="2" xs="1">
        <div class="split" />
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
              <v-hover v-slot="{ hover }">
                <v-icon
                  id="gmail"
                  large
                  dark
                  :color="hover ? '#CE493B' : '#edf5e1'"
                  >{{ mdiGmail }}</v-icon
                >
              </v-hover>
              <v-tooltip activator="#gmail" bottom color="#05385B">
                <span>htjmario@gmail.com</span>
              </v-tooltip>
            </a>
            <v-icon small dark>{{ mdiPowerOn }}</v-icon>
            <a
              target="_blank"
              rel="noopener noreferrer"
              href="https://github.com/HTJin"
            >
              <v-hover v-slot:default="{ hover }">
                <v-icon
                  id="github"
                  large
                  dark
                  :color="hover ? '#A66CFF' : '#edf5e1'"
                  >{{ mdiGithub }}</v-icon
                >
              </v-hover>
              <v-tooltip activator="#github" bottom color="#05385B">
                <span>github.com/htjin</span>
              </v-tooltip>
            </a>
            <v-icon small dark>{{ mdiPowerOn }}</v-icon>
            <a
              target="_blank"
              rel="noopener noreferrer"
              href="https://linkedin.com/in/HTJin"
            >
              <v-hover v-slot:default="{ hover }">
                <v-icon
                  id="linkedin"
                  large
                  dark
                  :color="hover ? '#0077B5' : '#edf5e1'"
                  >{{ mdiLinkedin }}</v-icon
                >
              </v-hover>
              <v-tooltip activator="#linkedin" bottom color="#05385B">
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
          <div class="down" @click="determineVisible" v-on="on">
            <router-link to="/timeline">
              <v-hover v-slot:default="{ hover }">
                <v-icon large dark :color="hover ? '#5cdb95' : '#edf5e1'">{{
                  hover ? mdiChevronTripleDown : mdiChevronDown
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
  computed: {
    visible() {
      return this.$store.state.visible;
    }
  },
  methods: {
    determineVisible() {
      this.$store.commit("determineVisible");
    },
    handleWheel() {
      let store = this.$store;
      let router = this.$router;
      window.addEventListener("wheel", function(event) {
        if (event.deltaY > 0) {
          store.commit("determineVisible");
          if (router.path !== "timeline") {
            router.push("timeline").catch(() => {});
          }
        }
      });
    }
  },
  data: () => ({
    mdiGithub: mdiGithub,
    mdiGmail: mdiGmail,
    mdiLinkedin: mdiLinkedin,
    mdiPowerOn: mdiPowerOn,
    mdiChevronDown: mdiChevronDown,
    mdiChevronTripleDown: mdiChevronTripleDown
  })
};
</script>

<style lang="scss">
@import "@/styles/home.scss";
</style>
