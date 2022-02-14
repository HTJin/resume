<template>
  <v-app>
    <v-content>
      <transition :name="transitionName" mode="out-in">
        <router-view></router-view>
      </transition>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
  watch: {
    $route(to, from) {
      const toDepth = to.path.split("/timeline").length;
      const fromDepth = from.path.split("/").length;
      this.transitionName =
        toDepth < fromDepth ? "slide-home" : "slide-timeline";
    }
  }
};
</script>

<style lang="scss">
.slide-home-enter-active {
  animation: slideTimeline 0.5s;
}
.slide-home-leave-active {
  animation: slideHome 0.5s reverse;
}
.slide-timeline-enter-active {
  animation: slideHome 0.5s;
}
.slide-timeline-leave-active {
  animation: slideTimeline 0.5s reverse;
}
@keyframes slideHome {
  0% {
    transform: translateY(100vh);
  }
  100% {
    transform: translateY(0);
  }
}
@keyframes slideTimeline {
  0% {
    transform: translateY(-100vh);
  }
  100% {
    transform: translateY(0);
  }
}
</style>
