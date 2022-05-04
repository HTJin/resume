<template>
  <div class="quiz">
    <div class="display-container">
      <Display />
    </div>
    <div class="keyboard-container">
      <Keyboard :board="Board" />
    </div>
  </div>
</template>

<script>
import Display from "@/components/Display.vue";
import Keyboard from "@/components/Keyboard.vue";
import Board from "@/contents/Board.json";
import Questions from "@/contents/Quiz.json";

export default {
  name: "Quiz",
  components: {
    Display,
    Keyboard
  },
  data: () => ({
    Board: Board,
    Questions: Questions
  })
};
</script>

<style lang="scss">
@import "@/styles/quiz.scss";
</style>
