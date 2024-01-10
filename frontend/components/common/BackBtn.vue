<template>
  <div class="back-btn">&lt; Назад</div>
</template>

<script lang="ts" setup>
</script>

<style lang="scss" scoped>
.back-btn {
  position: relative;

  width: fit-content;

  font-size: 26px;
  line-height: 1;
  color: $primary-color;

  cursor: pointer;
  transition: color $tr-dur;

  @include hover {
    color: $white-color;

    &:after {
      background-color: $white-color;
    }
  }

  &:after {
    content: '';
    position: absolute;
    top: 100%;
    right: 0;
    left: 20px;

    height: 1px;

    background-color: $primary-color;

    transition: background-color $tr-dur;
  }

  @include md-and-down {
    font-size: 15px;
    line-height: 1;

    &:after {
      left: 12px;
    }
  }
}
</style>
