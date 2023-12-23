<template>
  <div class="app-icon" :class="{ inline }">
    <component :is="icons[name]" :style="{ width: `${size}px`, height: `${size}px` }" />
  </div>
</template>

<script lang="ts" setup>
import * as icons from './AppIcon.utils';
import { IconName } from './AppIcon.utils';

withDefaults(
  defineProps<{
    name: IconName;
    size?: number | string;
    inline?: boolean;
  }>(),
  {
    size: 32,
  }
);
</script>

<style lang="scss" scoped>
.app-icon {
  &::v-deep {
    svg {
      display: block;
    }
  }

  &.inline {
    display: inline-block;
    &::v-deep {
      svg {
        display: inline-block;
      }
    }
  }
}
</style>
