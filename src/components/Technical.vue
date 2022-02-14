<template>
  <div class="skills-container">
    <div v-for="item in section" :key="item.id">
      <h1>{{ item.title }}</h1>
      <h3 v-if="item.location">{{ item.location }}</h3>
      <ul class="skill" v-for="skill in item.skills" :key="skill.id">
        <li>{{ skill }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Technical",
  props: {
    section: Array
  }
};
</script>

<style lang="scss">
@import "@/styles/experience.scss";
@import "@/styles/technical.scss";
</style>
