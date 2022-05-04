<template>
  <div class="keyboard">
    <div class="main-keys">
      <div class="func-row">
        <span class="esc"
          ><button v-on:click="getKeys" name="board[0]" value="board[0]">
            {{ board[0] }}
          </button></span
        >
        <span class="funcs" style="flex: 1;">
          <span v-for="func in board[1].slice(0, 4)" :key="func.id"
            ><button>{{ func }}</button></span
          >
        </span>
        <span class="funcs" style="flex: 1;">
          <span v-for="func in board[1].slice(4, 8)" :key="func.id"
            ><button>{{ func }}</button></span
          >
        </span>
        <span class="funcs" style="flex: 1;">
          <span v-for="func in board[1].slice(8, 14)" :key="func.id"
            ><button>{{ func }}</button></span
          >
        </span>
      </div>
      <div class="num-row">
        <span style="flex: 1;" v-for="num in board[2]" :key="num.id"
          ><button>{{ num }}</button></span
        >
        <span style="flex: 1;"
          ><button>{{ board[3] }}</button></span
        >
      </div>
      <div class="qwer-row">
        <span style="flex: 1.75;"
          ><button>{{ board[5] }}</button></span
        >
        <span style="flex: 1;" v-for="char in board[6]" :key="char.id"
          ><button>{{ char }}</button></span
        >
        <span style="flex: 1.5;"
          ><button>{{ board[7] }}</button></span
        >
      </div>
      <div class="asdf-row">
        <span style="flex: 2;"
          ><button>{{ board[9] }}</button></span
        >
        <span style="flex: 1;" v-for="char in board[10]" :key="char.id"
          ><button>{{ char }}</button></span
        >
        <span style="flex: 2.25;"
          ><button>{{ board[11] }}</button></span
        >
      </div>
      <div class="zxcv-row">
        <span style="flex: 2.25;"
          ><button>{{ board[12] }}</button></span
        >
        <span style="flex: 1;" v-for="char in board[13]" :key="char.id"
          ><button>{{ char }}</button></span
        >
        <span style="flex: 2.75;"
          ><button>{{ board[14] }}</button></span
        >
      </div>
      <div class="space-row">
        <span style="flex: 1;" v-for="ctrl in board[15]" :key="ctrl.id"
          ><button>{{ ctrl }}</button></span
        >
        <span style="flex: 5;"
          ><button>{{ board[16] }}</button></span
        >
        <span style="flex: 1;" v-for="ctrl in board[17]" :key="ctrl.id"
          ><button>{{ ctrl }}</button></span
        >
      </div>
    </div>
    <div class="side-keys">
      <div></div>
      <div>
        <span v-for="navs in board[4]" :key="navs.id"
          ><button>{{ navs }}</button></span
        >
      </div>
      <div>
        <span v-for="navs in board[8]" :key="navs.id"
          ><button>{{ navs }}</button></span
        >
      </div>
      <div></div>
      <div>
        <span
          ><button>{{ board[18] }}</button></span
        >
      </div>
      <div>
        <span v-for="arrs in board[19]" :key="arrs.id"
          ><button>{{ arrs }}</button></span
        >
      </div>
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
