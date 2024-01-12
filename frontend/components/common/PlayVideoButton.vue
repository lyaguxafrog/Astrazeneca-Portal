<template>
  <div class="play-button">
    <AppIcon :name="IconName.Play" :size="$screen.mdAndDown ? 36 : 100" />
  </div>
</template>

<script setup lang="ts">
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';

const { $screen } = useScreen();
</script>

<style scoped lang="scss">
.play-button {
  position: absolute;
  top: 50%;
  left: 50%;
  @include z-index(2);

  display: flex;
  justify-content: center;
  align-items: center;

  width: 170px;
  height: 170px;

  background-color: rgba($white-color, 0.5);
  border-radius: 50%;

  transform: translate(-50%, -50%);
  cursor: pointer;
  transition: background-color $tr-dur;

  & > div {
    max-width: 60%;

    transform: translateX(10%);

    :deep(svg) {
      max-width: 100%;
    }
  }

  @include hover {
    background-color: rgba($white-color, 0.3);
  }

  @include lg-and-down {
    width: 100px;
    height: 100px;
  }

  @include md-and-down {
    width: 70px;
    height: 70px;
  }
}
</style>
