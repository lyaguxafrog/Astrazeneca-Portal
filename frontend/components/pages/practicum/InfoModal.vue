<template>
  <AppModal :name="ModalsName.PracticumInfoModal">
    <div class="info-modal">
      <div class="info-modal__title">Список литературы:</div>
      <div class="info-modal__text">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
        labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
        laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
        voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
        cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem
        ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
        labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
        laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non
        proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit
        anim id est laborum.
      </div>
      <div class="info-modal__description">
        Место под расшифровки Номера одобрения: ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ
      </div>
    </div>
  </AppModal>
</template>

<script lang="ts" setup>
import { ModalsName } from '~/utils/composables/useModal';
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
}
</style>
