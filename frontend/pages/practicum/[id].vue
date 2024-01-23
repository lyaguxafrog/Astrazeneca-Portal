<template>
  <div class="practicum">
    <BgEllipse
      class="practicum__first-ellipse"
      color="#B32FC9"
      :size="$screen.mdAndDown ? 330 : 984"
    />
    <div class="practicum__container">
      <img src="./" alt="" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useScreen } from '~/utils/composables/useScreen';
import BgEllipse from '~/components/common/BgEllipse.vue';

const { $screen } = useScreen();
</script>

<style lang="scss" scoped></style>
