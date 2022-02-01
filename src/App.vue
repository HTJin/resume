<template>
  <v-app>
    <v-content>
      <v-expand-transition mode="out-in">
        <router-view></router-view>
      </v-expand-transition>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  })
};
</script>
