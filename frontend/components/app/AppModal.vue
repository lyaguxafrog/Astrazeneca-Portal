<template>
  <transition name="modal">
    <div v-if="isModalOpen" :key="name" class="modal__overlay">
      <div ref="scrollEl" class="modal__scroll-content">
        <div class="modal__close-overlay" @mousedown.self="closeModal(name)" />
        <div class="modal__content">
          <AppIcon
            class="modal__close"
            :name="IconName.CloseIcon"
            :size="30"
            @click="closeModal(name)"
          />
          <slot />
        </div>
      </div>
    </div>
  </transition>
</template>

<script lang="ts" setup>
import { computed, ref, watch } from 'vue';
import { isClient } from '@vueuse/core';
import { useRoute } from 'vue-router';
import { IconName } from '~/components/app/AppIcon.utils';
import { ModalsName, useModal } from '~/utils/composables/useModal';

const props = withDefaults(
  defineProps<{
    name: ModalsName;
    onClose?: () => void;
    onOpen?: () => void;
  }>(),
  {
    mode: 'center',
  }
);

const $route = useRoute();
const { openedModals, registerModal, closeModal } = useModal();

const scrollEl = ref<HTMLElement>();

registerModal({
  name: props.name,
  scrollEl,
  onClose: isClient ? props.onClose : undefined,
  onOpen: isClient ? props.onOpen : undefined,
});

const isModalOpen = computed(() => openedModals.value.includes(props.name));

watch(
  () => $route,
  () => {
    if (isModalOpen.value) {
      closeModal(props.name);
    }
  },
  { deep: true }
);
</script>

<style lang="scss" scoped>
$root: modal;

.#{$root} {
  &__overlay {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    @include z-index(7);

    display: flex;
    justify-content: center;
    align-items: center;

    width: 100vw;

    background: rgba($main-bg-color, 0.9);
  }

  &__close {
    position: absolute;
    top: 30px;
    right: 26px;
    @include z-index(2);

    cursor: pointer;
  }

  &__scroll {
    &-content {
      display: flex;
      flex-direction: column;
      align-items: center;

      width: 100%;
      height: 100%;
      max-height: 100vh;

      @include scrollbar;

      &:before {
        content: '';

        width: 100%;
        min-height: 90px;
      }
      &:after {
        content: '';

        width: 100%;
        min-height: 90px;
      }
    }
  }

  &__close-overlay {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    z-index: 1;

    width: calc(100% - $body-scrollbar-width);
  }

  &__content {
    position: relative;
    @include z-index(2);

    display: flex;
    flex-direction: column;

    width: 875px;
    max-width: 100%;
    margin: auto;
    padding: 47px 53px;

    background: $main-bg-color;
    border-radius: 40px;
    box-shadow: 0 0 250px 0 rgba(144, 77, 255, 0.7);
  }

  @include md-and-down {
    &__close-overlay {
      width: 100%;
    }
    &__scroll {
      &-content {
        height: 100%;
        min-height: 100%;
      }
    }

    &__content {
      width: 100%;
      margin: 0;
    }

    &__close {
      top: 20px;
      right: 22px;
    }
  }
}

//TRANSITION
.modal-enter-from,
.modal-leave-to {
  background: transparent;

  .modal__scroll-content {
    transform: translateY(-10px);
    opacity: 0;
  }
}

.modal-enter-active,
.modal-leave-active {
  transition: background $tr-dur;

  .modal__scroll-content {
    transition: opacity $tr-dur ease-out, transform $tr-dur ease-out;
  }
}
</style>
