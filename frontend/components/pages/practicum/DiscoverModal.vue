<template>
  <AppModal :name="ModalsName.PracticumDiscoverModal">
    <div class="discover">
      <div class="discover__title">{{ data.title }}</div>
      <div class="discover__text" v-html="data.text" />
      <AppButton class="discover__btn" primary mini @click="openNext">
        {{ nextItem.title }}
      </AppButton>
    </div>
  </AppModal>
</template>

<script lang="ts" setup>
import { ModalsName, useModal } from '~/utils/composables/useModal';

type DiscoverItem = {
  title: string;
  text: string;
  id: number;
};

const props = defineProps<{
  items: DiscoverItem[];
}>();

const { getModalPayload, setModalPayload } = useModal();

const data = toRef(() => getModalPayload(ModalsName.PracticumDiscoverModal) as DiscoverItem);

const activeItem = toRef(() => getModalPayload(ModalsName.PracticumDiscoverModal));

const nextItem = toRef(() => {
  const index = props.items.findIndex((i) => i.id === activeItem.value?.id);

  if (index !== props.items.length - 1) {
    return props.items[index + 1];
  } else {
    return props.items[0];
  }
});

const openNext = () => {
  setModalPayload(ModalsName.PracticumDiscoverModal, nextItem.value);
};
</script>

<style lang="scss" scoped>
.discover {
  &__title {
    margin-bottom: 26px;

    font-size: 32px;
    line-height: 36px;
    font-weight: 700;
    color: $primary-color;
  }

  &__text {
    font-size: 20px;
    line-height: 24px;
    font-weight: 300;

    :deep(ul) {
      margin-top: 18px;
      padding-left: 24px;
    }

    :deep(li) {
      margin-bottom: 20px;
    }
  }

  &__btn {
    margin: 10px 0 0 auto;
  }
}
</style>
