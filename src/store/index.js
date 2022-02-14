import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    visible: true,
    show: true
  },
  mutations: {
    determineShow(state) {
      state.show = !state.show;
      if (state.show === true) {
        state.visible = false;
      } else {
        state.visible = true;
      }
    },
    determineVisible(state) {
      state.visible = !state.visible;
      if (state.visible === true) {
        state.show = false;
      } else {
        state.show = true;
      }
    }
  },
  actions: {},
  modules: {}
});
