<template>
  <AppModal :name="ModalsName.TestAnswerModal">
    <div class="test-answer">
      <div class="test-answer__title">{{ content.title }}</div>
      <div class="test-answer__text" v-html="content.text" />

      <AppButton mini primary class="test-answer__btn"> Следующий тест </AppButton>
    </div>
  </AppModal>
</template>

<script setup lang="ts">
import { ModalsName } from '~/utils/composables/useModal';

defineProps<{
  content: {
    text: string;
    title: string;
  };
}>();
</script>

<style scoped lang="scss">
.test-answer {
  &__title {
    font-family: $secondary-font-family;
    font-size: 32px;
    line-height: 21px;
    font-weight: 900;
  }

  &__text {
    margin-top: 50px;
    margin-bottom: 30px;

    font-size: 20px;
    line-height: 24px;
    font-weight: 300;
  }

  &__btn {
    margin-left: auto;
  }
}
</style>
