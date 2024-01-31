<template>
  <AppModal :name="ModalsName.PracticumInfoModal">
    <div class="info-modal">
      <div class="info-modal__title">Список литературы:</div>
      <div class="info-modal__text" v-html="literature">
      </div>
      <div v-if="description" class="info-modal__description" v-html="description">
      </div>
    </div>
  </AppModal>
</template>

<script lang="ts" setup>
import { ModalsName } from '~/utils/composables/useModal';

defineProps<{
  literature: string;
  description: string | null;
}>();
</script>

<style lang="scss" scoped>
.info-modal {
  &__title {
    margin-bottom: 46px;

    font-family: $secondary-font-family;
    font-size: 32px;
    line-height: 21px;
    font-weight: 900;
  }

  &__text {
    font-size: 20px;
    line-height: 24px;
    font-weight: 300;
  }

  &__description {
    margin-top: 30px;

    font-size: 14px;
    line-height: 18px;
    color: $primary-color;
  }

  @include md-and-down {
    &__title {
      margin-bottom: 34px;
      padding-right: 50px;

      font-size: 22px;
      line-height: 21px;
    }

    &__text {
      font-size: 14px;
      line-height: 17px;
      font-weight: 300;
    }

    &__description {
      margin-top: 20px;

      font-size: 12px;
      line-height: 14px;
    }
  }
}
</style>
