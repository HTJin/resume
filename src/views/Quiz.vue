<template>
  <div class="quiz">
    <div class="keyboard-container">
      <Keyboard :board="Board" />
    </div>
  </div>
</template>

<script>
import Keyboard from "@/components/Keyboard.vue";
import Board from "@/contents/Board.json";
import Questions from "@/contents/Quiz.json";

export default {
  name: "Quiz",
  components: { Keyboard },
  data: () => ({
    Board: Board,
    Questions: Questions
  })
};
</script>

<style lang="scss">
@import "@/styles/quiz.scss";
</style>
