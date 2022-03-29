import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Timeline from "../views/Timeline.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/timeline",
    name: "Timeline",
    component: Timeline
  }
];

const router = new VueRouter({
  routes
});

export default router;
