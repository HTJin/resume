<template>
  <div class="keyboard">
    <div class="func-row">
      <span><button>{{ board[0][0] }}</button></span>
      <span v-for="func in board[1]" :key="func.id"><button>{{ func }}</button></span>
    </div>
    <div class="num-row">
      <span v-for="num in board[2]" :key="num.id"><button>{{ num }}</button></span>
      <span><button>{{ board[3][0] }}</button></span>
      <span v-for="navs in board[4]" :key="navs.id"><button>{{ navs }}</button></span>
    </div>
    <div class="qwer-row">
      <span><button>{{ board[5][0] }}</button></span>
      <span v-for="char in board[6]" :key="char.id"><button>{{ char }}</button></span>
      <span v-for="navs in board[7]" :key="navs.id"><button>{{ navs }}</button></span>
    </div>
    <div class="asdf-row">
      <span><button>{{ board[8][0] }}</button></span>
      <span v-for="char in board[9]" :key="char.id"><button>{{ char }}</button></span>
      <span><button>{{ board[10][0] }}</button></span>
    </div>
    <div class="zxcv-row">
      <span><button>{{ board[11][0] }}</button></span>
      <span v-for="char in board[12]" :key="char.id"><button>{{ char }}</button></span>
      <span><button>{{ board[13][0] }}</button></span>
      <span v-for="arrs in board[17]" :key="arrs.id"><button>{{ arrs }}</button></span>
    </div>
    <div class="ctrl-row">
      <span v-for="ctrl in board[14]" :key="ctrl.id"><button>{{ ctrl }}</button></span>
      <span><button>{{ board[15][0] }}</button></span>
      <span v-for="ctrl in board[16]" :key="ctrl.id"><button>{{ ctrl }}</button></span>
      <span v-for="arrs in board[18]" :key="arrs.id"><button>{{ arrs }}</button></span>
    </div>
  </div>
</template>

<script>
export default {
  name: "Keyboard",
  props: { board: Array }
};
</script>

<style lang="scss">
@import "@/styles/keyboard.scss";
</style>
