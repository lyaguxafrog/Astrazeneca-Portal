<template>
  <div
    class="bg-ellipse"
    :class="{ pale }"
    :style="{
      width: `${size}px`,
      height: `${size}px`,
      background: bg,
    }"
  ></div>
</template>

<script lang="ts" setup>
const props = defineProps<{
  size: string | number;
  color: string;
  pale?: boolean;
}>();

const bg = toRef(() =>
  !props.pale
    ? `radial-gradient(50% 50% at 50% 50%, ${props.color} 0%, ${props.color}00 100%)`
    : `radial-gradient(50% 50% at 50% 50%, ${props.color}60 0%, ${props.color}00 100%)`
);
</script>

<style lang="scss" scoped>
.bg-ellipse {
  position: absolute;
  z-index: -1;

  border-radius: 50%;

  filter: blur(50px);
  pointer-events: none;

  &:not(.pale) {
    opacity: 0.5;
  }

  @include only-safari {
    filter: none;
  }

  @include md-and-down {
    &:not(.pale) {
      opacity: 1;
    }
  }
}
</style>
