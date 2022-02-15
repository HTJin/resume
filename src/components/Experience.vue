<template>
  <v-slide-x-transition>
    <div class="resume-container">
      <v-hover v-slot:default="{ hover }">
        <span id="prof" class="toggle" @click="profOpen = !profOpen">
          <v-icon
            class="drawer-up"
            :large="windowWidth > 600"
            :small="windowWidth < 600"
            dark
            :color="!profOpen ? '#20688a' : hover ? '#5cdb95' : '#edf5e1'"
            >{{ mdiMenuUp }}</v-icon
          >
          <v-icon
            class="drawer-down"
            :large="windowWidth > 600"
            :small="windowWidth < 600"
            dark
            :color="profOpen ? '#20688a' : hover ? '#5cdb95' : '#edf5e1'"
            >{{ mdiMenuDown }}</v-icon
          >
        </span>
      </v-hover>
      <v-tooltip
        activator="#prof"
        :left="windowWidth > 600"
        :bottom="windowWidth < 600"
        color="#042D4A"
      >
        {{ profOpen ? "Close" : "Open" }}
      </v-tooltip>
      <h1>Professional Experience</h1>
      <div v-for="exp in sectionProfExp" :key="exp.id">
        <h2>
          {{ exp.job }}

          <span class="year">{{ exp.year }}</span>
        </h2>
        <h3>
          {{ exp.location }}
        </h3>
        <ul class="descProf" v-for="desc in exp.description" :key="desc.id">
          <v-expand-transition>
            <li v-show="profOpen">{{ desc }}</li>
          </v-expand-transition>
        </ul>
      </div>
      <v-hover v-slot:default="{ hover }">
        <span id="comm" class="toggle" @click="commOpen = !commOpen">
          <v-icon
            class="drawer-up"
            :large="windowWidth > 600"
            :small="windowWidth < 600"
            dark
            :color="!commOpen ? '#20688a' : hover ? '#5cdb95' : '#edf5e1'"
            >{{ mdiMenuUp }}</v-icon
          >
          <v-icon
            class="drawer-down"
            :large="windowWidth > 600"
            :small="windowWidth < 600"
            dark
            :color="commOpen ? '#20688a' : hover ? '#5cdb95' : '#edf5e1'"
            >{{ mdiMenuDown }}</v-icon
          >
        </span>
      </v-hover>
      <v-tooltip
        activator="#comm"
        :left="windowWidth > 600"
        :bottom="windowWidth < 600"
        color="#042D4A"
      >
        {{ commOpen ? "Close" : "Open" }}
      </v-tooltip>
      <h1>Community Involvement</h1>
      <div v-for="exp in sectionCommInv" :key="exp.id">
        <h2>
          {{ exp.job }}

          <span class="year">{{ exp.year }}</span>
        </h2>
        <h3>
          {{ exp.location }}
        </h3>
        <ul class="descComm" v-for="desc in exp.description" :key="desc.id">
          <v-expand-transition>
            <li v-show="commOpen">{{ desc }}</li>
          </v-expand-transition>
        </ul>
      </div>
      <v-hover v-slot:default="{ hover }">
        <span id="pers" class="toggle" @click="persOpen = !persOpen">
          <v-icon
            class="drawer-up"
            :large="windowWidth > 600"
            :small="windowWidth < 600"
            dark
            :color="!persOpen ? '#20688a' : hover ? '#5cdb95' : '#edf5e1'"
            >{{ mdiMenuUp }}</v-icon
          >
          <v-icon
            class="drawer-down"
            :large="windowWidth > 600"
            :small="windowWidth < 600"
            dark
            :color="persOpen ? '#20688a' : hover ? '#5cdb95' : '#edf5e1'"
            >{{ mdiMenuDown }}</v-icon
          >
        </span>
      </v-hover>
      <v-tooltip
        activator="#pers"
        :left="windowWidth > 600"
        :bottom="windowWidth < 600"
        color="#042D4A"
      >
        {{ persOpen ? "Close" : "Open" }}
      </v-tooltip>
      <h1>Personal Projects</h1>
      <div v-for="exp in sectionPersPro" :key="exp.id">
        <h3 class="projects">{{ exp.job }}</h3>
        <ul class="descPers" v-for="desc in exp.description" :key="desc.id">
          <v-expand-transition>
            <li v-show="persOpen">{{ desc }}</li>
          </v-expand-transition>
        </ul>
      </div>
    </div>
  </v-slide-x-transition>
</template>

<script>
import { mdiMenuUp } from "@mdi/js";
import { mdiMenuDown } from "@mdi/js";

export default {
  name: "Experience",
  props: {
    section: Array,
    windowWidth: Number
  },
  data: () => ({
    mdiMenuUp: mdiMenuUp,
    mdiMenuDown: mdiMenuDown,
    profOpen: false,
    persOpen: false,
    commOpen: false
  }),
  computed: {
    sectionProfExp: function() {
      return this.section.filter(function(t) {
        return t.title === "Professional Experience";
      });
    },
    sectionPersPro: function() {
      return this.section.filter(function(t) {
        return t.title === "Personal Projects";
      });
    },
    sectionCommInv: function() {
      return this.section.filter(function(t) {
        return t.title === "Community Involvement";
      });
    }
  }
};
</script>

<style lang="scss">
@import "@/styles/experience.scss";
</style>
