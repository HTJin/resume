<template>
  <v-container fluid v-show="show" class="timeline" style="height: 88vh;">
    <div class="sections-container">
      <v-col xl="8" lg="8" md="8" sm="8" xs="6">
        <Experience :section="ExpSection" />
      </v-col>
      <v-col xl="1" lg="1" md="1" sm="1" xs="1">
        <div class="split" />
      </v-col>
      <v-col xl="4" lg="4" md="4" sm="4" xs="6">
        <Technical :section="TechSection" />
      </v-col>
    </div>
    <div class="scroll">
      <v-tooltip top color="#5cdb95">
        <template v-slot:activator="{ on }">
          <div class="up" @click="determineShow" v-on="on">
            <router-link to="/">
              <v-hover v-slot:default="{ hover }">
                <v-icon v-if="hover" large dark color="#5cdb95">{{
                  mdiChevronTripleUp
                }}</v-icon>
                <v-icon v-else large dark color="#edf5e1">{{
                  mdiChevronUp
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
    ExpSection: ExpSection,
    TechSection: TechSection
  })
};
</script>

<style lang="scss">
@import "@/styles/timeline.scss";
</style>
