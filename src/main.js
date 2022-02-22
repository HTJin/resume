import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import vuescroll from "vue-scroll";

Vue.config.productionTip = false;
Vue.use(vuescroll);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
