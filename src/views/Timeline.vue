<template>
  <v-container fluid v-show="show" class="timeline">
    <div class="experience-container">
      <Experience :section="section" />
    </div>
    <div class="scroll">
      <v-tooltip top color="#5cdb95">
        <template v-slot:activator="{ on, attrs }">
          <div class="up" @click="determineShow" v-on="on" v-bind="attrs">
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
import Experience from "../components/Experience.vue";

export default {
  name: "Timeline",
  components: {
    Experience
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
    section: [
      {
        title: "Professional Experience",
        job: "Associate Applications Developer",
        location: "Highmark Health Solutions Inc., Pittsburgh, PA",
        year: "2019 - 2020",
        description: [
          "Successfully delivered a web portal application using Vue.js and Java that makes inquiries/referrals to the Highmark providers",
          "Was able to demonstrate the value and strength of Vue as a Javascript framework to the company and even had Github unblocked and moved to the company proxy whitelist",
          "Main front end developer/architect for a scrum team, led and determined story points for AGILE sprints",
          "Used PegaSystems Platform to maintain and develop Highmark's Utilization Management tool, which gets used by Highmark hospital's doctors and nurses"
        ]
      },
      {
        title: "Professional Experience",
        job: "Junior Web Developer",
        location: "Checkmate Digital, New Haven, CT",
        year: "2018 - 2019",
        description: [
          "Worked remotely from Pittsburgh on client to client projects",
          "Gained front end experience working with Javascript frameworks, exposing myself to a variety of projects depending on the client",
          "Learned the importance of proper Git version control and adapted to company’s Git flow",
          "Contributed to 4 unique projects"
        ]
      },
      {
        title: "Personal Projects",
        job:
          "Rift - Public Repository: https://github.com/OpenLeagueSeries/Rift/",
        description: [
          "Registration application for a popular video gaming club at University of Pittsburgh",
          "Created with React.js and was formerly deployed at https://pitt.lol",
          "Recruited and taught students on using React and Git. Made a tutorial video at https://www.twitch.tv/videos/273200884"
        ]
      },
      {
        title: "Personal Projects",
        job: "Password Evaluation and Cracker",
        description: [
          "Password cracking program created with Java",
          "Uses a given dictionary.txt file with words and evaluates the strength of passwords",
          "Implemented MD5 Hash for cracking passwords"
        ]
      },
      {
        title: "Personal Projects",
        job: "Restaurant Website",
        description: [
          "Website for a restaurant created with HTML, CSS, and JavaScript",
          "Users can make reservations, order from a menu and add to shopping cart, then make transactions online",
          "Implemented Google maps API to display location of the restaurant, and Paypal API for transactions"
        ]
      },
      {
        title: "Personal Projects",
        job: "Forum Website",
        description: [
          "Created an online forum with PHP and MySQL database where users can post a topic, comments, and replies to one another"
        ]
      },
      {
        title: "Personal Projects",
        job: "University of Pittsburgh Mobile App Proposal",
        description: [
          "Designed a University of Pittsburgh mobile application and presented a paper model demo to the school’s web administrator"
        ]
      },
      {
        title: "Community Involvement",
        job: "Coordinator & Co-Founder",
        location: "Pitt Smash Bros. Club - University of Pittsburgh",
        year: "2014 - 2015",
        description: [
          "Established a video gaming community on campus by creating events to play Super Smash Bros. on campus",
          "Co-coordinated national size tournaments that over 288 unique entrants participated in",
          "Set up live broadcasts for streaming online through popular website platform, www.twitch.tv"
        ]
      },
      {
        title: "Community Involvement",
        job: "Media Communications Chair",
        location: "Korean Culture Association - University of Pittsburgh",
        year: "2012 - 2013",
        description: [
          "A cultural organization on campus to promote Korean culture on campus; ~400+ body members at large and ~14 executive officers",
          "Managed organizational budget (~$22K) with Business Manager to host speakers, performers, and cultural events",
          "Collaborated in weekly executive board meetings; served as organizational representative to monthly cross-organizational meetings and networking events"
        ]
      },
      {
        title: "Community Involvement",
        job: "Founding Member",
        location: "iDEAS Conference - University of Pittsburgh",
        year: "2011 - 2012",
        description: [
          "Focused on creating a solid management and leadership structure for CMU and PITT",
          "Helped develop the mission statement and vision for the structure of the conference",
          "Created the conference description and conference structure",
          "Co-created the Marketing Plan which outlines the necessary steps for a successful conference"
        ]
      }
    ]
  })
};
</script>

<style lang="scss">
@import "@/styles/timeline.scss";
</style>
