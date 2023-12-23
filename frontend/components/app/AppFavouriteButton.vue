<template>
  <AppButton mode="icon" :petite="$screen.mdAndDown || !big" white>
    <AppIcon v-if="!active" name="HeartIcon" :size="iconSize" />
    <AppIcon v-else name="HeartIconFill" :size="iconSize" />
  </AppButton>
</template>

<script lang="ts" setup>
import { useScreen } from '~/utils/composables/useScreen';

const props = defineProps<{
  active: boolean;
  big?: boolean;
  white?: boolean;
}>();

const { $screen } = useScreen();

const iconSize = toRef(() => ($screen.value.mdAndDown ? 26 : props.big ? 42 : 38));
</script>

<style lang="scss" scoped></style>
