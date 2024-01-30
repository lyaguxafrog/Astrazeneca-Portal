<template>
  <component
    :is="to ? defineNuxtLink({}) : 'button'"
    class="app-button"
    :to="to"
    :class="{ icon: mode === 'icon', primary, petite, mini, white, selected }"
    :target="target"
  >
    <slot />
  </component>
</template>

<script lang="ts" setup>
import { defineNuxtLink } from '#app';
defineProps<{
  mode?: 'icon';
  to?: string;
  primary?: boolean;
  petite?: boolean;
  mini?: boolean;
  white?: boolean;
  selected?: boolean;
  target?: '_blank';
}>();
</script>

<style lang="scss" scoped>
.app-button {
  display: flex;
  justify-content: center;
  align-items: center;

  min-height: 82px;
  padding: 0 35px;

  font-size: 30px;
  line-height: 1;
  color: $primary-color;

  border: 1px solid $primary-color;
  border-radius: 38px;

  cursor: pointer;
  transition: color $tr-dur, background-color $tr-dur;

  &.icon {
    width: 72px;
    height: 72px;
    padding: 0;
    &.petite {
      width: 62px;
      height: 62px;
    }
  }

  &.selected {
    pointer-events: none;
  }

  &.primary {
    color: $secondary-text-color;

    background-color: $primary-color;
  }

  &.petite {
    min-height: 62px;

    font-size: 30px;
  }

  &.white {
    background-color: $white-color;
  }

  &.mini {
    min-height: 41px;
    padding: 0 20px;

    font-size: 18px;
  }

  @include hover {
    background-color: $white-color;

    &.primary {
      background-color: $white-color;
    }

    &.white {
      background-color: rgba($primary-color, 0.5);
    }
  }

  @include xl-and-down {
    font-size: 24px;
  }

  @include md-and-down {
    min-height: 50px;
    padding: 0 50px;

    font-size: 19px;

    &.petite {
      min-height: 42px;

      font-size: 17px;
    }

    &.icon {
      width: 42px;
      &.petite {
        width: 42px;
        height: 42px;
      }
    }
  }
}
</style>
