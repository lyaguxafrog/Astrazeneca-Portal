<template>
  <div class="title">
    <h3 class="mb-4">
      <span><slot /></span>
    </h3>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
.title {
  position: relative;
  z-index: 1;

  span {
    position: relative;
    z-index: 1;

    padding-right: 8px;

    background-color: white;
  }

  &:after {
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    z-index: -1;

    width: calc(100vw - 60px);
    height: 1px;

    background-color: #ccc;
  }
}
</style>
