<template>
  <AppButton
    mode="icon"
    :petite="$screen.mdAndDown || !big"
    white
    @click="toggleFavourite(contentType, contentId)"
  >
    <AppIcon v-if="!active" :name="IconName.HeartIcon" :size="iconSize" />
    <AppIcon v-else :name="IconName.HeartIconFill" :size="iconSize" />
  </AppButton>
</template>

<script lang="ts" setup>
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';
import { useFavourites } from '~/utils/composables/useFavourites';
import { ContentType } from '~/utils/types';

const props = defineProps<{
  active: boolean;
  big?: boolean;
  white?: boolean;
  contentType: ContentType;
  contentId: number;
}>();

const { $screen } = useScreen();
const { toggleFavourite } = useFavourites();

const iconSize = toRef(() => ($screen.value.mdAndDown ? 26 : props.big ? 42 : 38));
</script>

<style lang="scss" scoped></style>
