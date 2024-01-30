<template>
  <div class="confirm-button">
    <AppButton primary class="confirm-button__btn" @click="showConfirm">
      <slot />
    </AppButton>

    <OnClickOutside @trigger="hideConfirm">
      <div class="confirm-button__message-wrapper" :class="{ shown: isConfirmShown }">
        <div class="confirm-button__message">
          <p>Вы подтверждаете свой выбор?</p>
          <div class="confirm-button__message-btn-container">
            <div class="confirm-button__message-btn active" @click="apply">Да</div>
            <div class="confirm-button__message-btn" @click="hideConfirm">НЕТ</div>
          </div>
        </div>
      </div>
    </OnClickOutside>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { OnClickOutside } from '@vueuse/components';

const props = defineProps<{
  action: () => void | Promise<void>;
}>();

const isConfirmShown = ref(false);
const showConfirm = () => {
  isConfirmShown.value = true;
};
const hideConfirm = () => {
  isConfirmShown.value = false;
};

const apply = () => {
  props.action();
  hideConfirm();
};
</script>

<style scoped lang="scss">
.confirm-button {
  position: relative;

  &__btn {
    min-height: 76px;
    margin-bottom: 30px;

    font-size: 24px;
    line-height: 24px;
    letter-spacing: -0.48px;
  }

  &__message {
    display: flex;
    justify-content: flex-end;
    align-items: center;

    width: 100%;
    min-width: 600px;
    height: 100%;

    font-size: 24px;
    line-height: 26px;
    color: $main-bg-color;
    letter-spacing: -0.48px;

    background-color: $primary-color;
    border-radius: 42px;

    &-wrapper {
      position: absolute;
      top: 0;
      right: 0;

      display: flex;
      justify-content: flex-end;

      width: 0;
      height: 100%;
      overflow: hidden;

      transition: width $tr-dur-l;

      &.shown {
        width: calc(100% + 150px);
      }
    }

    p {
      width: 240px;
      margin-right: 40px;
    }

    &-btn {
      display: flex;
      justify-content: center;
      align-items: center;

      width: 132px;

      font-size: 24px;
      color: $primary-color;

      background-color: $main-bg-color;

      cursor: pointer;
      transition: background-color $tr-dur, color $tr-dur;

      &:nth-of-type(1) {
        border-radius: 42px 0 0 42px;
      }
      &:nth-of-type(2) {
        border-radius: 0 42px 42px 0;
      }

      &.active {
        color: $secondary-text-color;

        background-color: $primary-color;
      }

      &:hover {
        color: $secondary-text-color;

        background-color: $white-color;
      }

      &-container {
        position: relative;

        display: flex;

        height: 100%;

        border: 2px solid $primary-color;
        border-radius: 42px;

        &:before {
          content: '';
          position: absolute;
          top: -4px;
          left: 0;
          @include z-index(2);

          width: calc(100% + 50px);
          height: calc(100% + 8px);

          border: 2px solid $main-bg-color;
          border-radius: 42px;

          pointer-events: none;
        }
      }
    }
  }

  @include lg-and-down {
    &__btn {
      min-height: 60px;

      font-size: 18px;
      line-height: 1;
    }
  }

  @include md-and-down {
    max-width: 400px;
    margin: 0 auto;

    &__btn {
      height: auto;
      margin-bottom: 22px;
      padding: 7px 10px;

      font-size: 15px;
      line-height: 16px;
      letter-spacing: -0.15px;
    }

    &__message {
      flex-direction: column;

      min-width: auto;
      padding: 20px 0 73px 0;

      font-size: 15px;
      line-height: 16px;
      text-align: center;
      letter-spacing: -0.15px;

      border-radius: 20px 20px 0 0;

      p {
        width: 100%;
        margin-right: 0;
      }

      &-wrapper {
        position: fixed;
        top: auto;
        bottom: 0;
        @include z-index(10);

        width: 100%;
        height: auto;

        transform: translateY(110%);
        transition: transform $tr-dur;

        &.shown {
          width: 100%;

          transform: translateY(0);
        }
      }

      &-btn {
        width: 83px;
        height: 49px;
        margin: 16px 7px 0;

        font-size: 19px;
        color: $secondary-text-color;

        background-color: transparent;
        border: 1px solid $secondary-text-color;
        border-radius: 72px !important;

        &-container {
          border: none;

          &:before {
            display: none;
          }
        }

        &.active {
          color: $white-color;

          background-color: $secondary-text-color;
        }
      }
    }
  }
}
</style>
