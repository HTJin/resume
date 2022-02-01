<template>
  <div class="resume-container">
    <h1>Professional Experience</h1>
    <div v-for="exp in sectionProfExp" :key="exp.id">
      <h2>{{ exp.job }}</h2>
      <h3>
        {{ exp.location }}
        <span class="year">{{ exp.year }}</span>
      </h3>
      <ul v-for="desc in exp.description" :key="desc.id">
        <li>{{ desc }}</li>
      </ul>
    </div>

    <h1>Personal Projects</h1>
    <div v-for="exp in sectionPersPro" :key="exp.id">
      <h3>{{ exp.job }}</h3>
      <ul v-for="desc in exp.description" :key="desc.id">
        <li>{{ desc }}</li>
      </ul>
    </div>

    <h1>Community Involvement</h1>
    <div v-for="exp in sectionCommInv" :key="exp.id">
      <h2>{{ exp.job }}</h2>
      <h3>
        {{ exp.location }}
        <span class="year">{{ exp.year }}</span>
      </h3>
      <ul v-for="desc in exp.description" :key="desc.id">
        <li>{{ desc }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Experience",
  props: {
    section: Array
  },
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
