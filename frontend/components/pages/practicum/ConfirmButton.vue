<template>
  <div class="confirm-button" :class="{right}">
    <template v-if="!props.active">
      <AppButton v-if="props.to" :primary="primary" class="confirm-button__btn" :to="props.to" :target="isAbsoluteUrl(props.to) ? '_blank' : undefined">
        <slot />
      </AppButton>
      <AppButton v-else-if="props.file" :primary="primary" target="_blank" class="confirm-button__btn" :to="`${baseUrl}${props.file}`">
        <slot />
      </AppButton>
      <AppButton v-else :primary="primary" class="confirm-button__btn" @click="action">
        <slot />
      </AppButton>
    </template>

    <AppButton v-else :primary="primary" class="confirm-button__btn" @click="showConfirm">
      <slot />
    </AppButton>

    <OnClickOutside @trigger="hideConfirm">
      <div class="confirm-button__message-wrapper" :class="{ shown: isConfirmShown }">
        <div class="confirm-button__message">
          <p>Вы подтверждаете свой выбор?</p>
          <div class="confirm-button__message-btn-container">
            <div class="confirm-button__message-btn active" @click="apply">ДА</div>
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
import { isAbsoluteUrl } from '~/utils/url';

const props = defineProps<{
  action: () => void | Promise<void>;
  active: boolean;
  primary?: boolean;
  to?: string;
  file?: string;
  right?: boolean;
}>();

const isConfirmShown = ref(false);
const { baseUrl } = useRuntimeConfig().public;

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

  @include md-and-up {
    &.right {
      .confirm-button__message {
        flex-direction: row-reverse;

        p {
          margin-right: 0;
          margin-left: 40px;
        }

        &-wrapper {
          right: auto;
          left: 0;

          justify-content: flex-start;
          &.shown {
            width: 60vw;
          }
        }

        &-btn-container {
          &:before {
            display: none;
          }
        }
      }
    }
  }

  &__btn {
    width: 100%;
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


    &__message {
      font-size: 20px;

      &-btn {
        width: 96px;

        font-size: 20px;
      }
    }

    p {
      width: 218px;
      margin-right: 10px;
    }
  }

  @include md-and-down {
    max-width: 400px;
    margin: 0 auto;

    &__btn {
      height: auto;
      margin-bottom: 22px;
      padding: 7px 20px;

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
      box-shadow: 0 0 16px 5px rgba($main-bg-color, 0.3);

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
        overflow: initial;

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
