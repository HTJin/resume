<template>
  <v-container fluid v-show="show" class="timeline" style="height: 88vh;">
    <div v-if="!toggleSkills" class="sections-container">
      <v-col xl="8" lg="8" md="8" sm="8" xs="6">
        <Experience :section="ExpSection" :windowWidth="windowWidth" />
      </v-col>
      <v-col xl="1" lg="1" md="1" sm="1" xs="1">
        <div v-if="windowWidth > 600" class="split" />
        <div v-else class="toggle-over" @click="toggleSkills = !toggleSkills">
          <v-icon v-for="n in 5" :key="n.id" dark color="#5cdb95">
            {{ mdiTransferRight }}
          </v-icon>
        </div>
      </v-col>
      <v-col v-if="windowWidth > 600" xl="8" lg="8" md="8" sm="8" xs="6">
        <Technical :section="TechSection" :windowWidth="windowWidth" />
      </v-col>
    </div>
    <div v-if="toggleSkills" class="sections-container">
      <v-col xl="1" lg="1" md="1" sm="1" xs="1">
        <div class="toggle-over" @click="toggleSkills = !toggleSkills">
          <v-icon v-for="n in 5" :key="n.id" dark color="#5cdb95">
            {{ mdiTransferLeft }}
          </v-icon>
        </div>
      </v-col>
      <v-col xl="11" lg="11" md="11" sm="11" xs="11">
        <Technical :section="TechSection" :windowWidth="windowWidth" />
      </v-col>
    </div>
    <div class="scroll">
      <v-tooltip top color="#5cdb95">
        <template v-slot:activator="{ on }">
          <div class="up" @click="determineShow" v-on="on">
            <router-link to="/">
              <v-hover v-slot:default="{ hover }">
                <v-icon large dark :color="hover ? '#5cdb95' : '#edf5e1'">{{
                  hover ? mdiChevronTripleUp : mdiChevronUp
                }}</v-icon>
              </v-hover>
            </router-link>
          </div>
        </template>
        <span>Back Up</span>
      </v-tooltip>
    </div>
  </v-container>
</template>

<script>
import { mdiChevronUp } from "@mdi/js";
import { mdiChevronTripleUp } from "@mdi/js";
import { mdiTransferLeft } from "@mdi/js";
import { mdiTransferRight } from "@mdi/js";
import Experience from "@/components/Experience.vue";
import ExpSection from "@/contents/ExpSection.json";
import Technical from "@/components/Technical.vue";
import TechSection from "@/contents/TechSection.json";

export default {
  name: "Timeline",
  components: {
    Experience,
    Technical
  },
  computed: {
    show() {
      return this.$store.state.show;
    }
  },
  methods: {
    determineShow() {
      this.$store.commit("determineShow");
    }
  },
  data: () => ({
    mdiChevronUp: mdiChevronUp,
    mdiChevronTripleUp: mdiChevronTripleUp,
    mdiTransferLeft: mdiTransferLeft,
    mdiTransferRight: mdiTransferRight,
    ExpSection: ExpSection,
    TechSection: TechSection,
    windowWidth: window.innerWidth,
    toggleSkills: false
  }),
  mounted() {
    window.onresize = () => {
      this.windowWidth = window.innerWidth;
    };
  }
};
</script>

<style lang="scss">
@import "@/styles/timeline.scss";
</style>
