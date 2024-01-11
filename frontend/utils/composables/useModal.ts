import { computed, nextTick, Ref, toRef } from 'vue';
import { useState } from '#app';
import { disableScroll, enableScroll } from '~/utils/functions/scroll-lock';
import { useScreen } from '~/utils/composables/useScreen';

export enum ModalsName {
  DrugProps = 'drug-props',
  VideosAddContent = 'videos-add-content',
}

type RegisteredModal = {
  name: ModalsName;
  scrollEl: Ref<HTMLElement | undefined>;
  onClose?: () => void;
  onOpen?: () => void;
  payload?: Record<string, any>;
};

export function useModal() {
  const modalState = useState('modal', () => ({
    openedModals: [] as ModalsName[],
    registeredModals: {} as Record<string, RegisteredModal>,
  }));

  const openedModals = computed(() => modalState.value.openedModals);

  const { $screen } = useScreen();

  const registerModal = (modal: RegisteredModal) => {
    modalState.value.registeredModals[modal.name] = modal;
  };

  const getRegisteredModal = (modalName: ModalsName) =>
    computed(() => modalState.value.registeredModals[modalName]);

  const openModal = async (modalName: ModalsName, payload?: Record<string, any>) => {
    if (openedModals.value.includes(modalName)) {
      return;
    }

    const openingModal = modalState.value.registeredModals[modalName];
    if (openingModal) {
      openingModal.payload = payload;
    }

    await openingModal?.onOpen?.();

    modalState.value.openedModals.push(modalName);

    await nextTick();

    const scrollEl = toRef(modalState.value.registeredModals[modalName], 'scrollEl');
    const allowScrollEl = scrollEl.value;

    if (allowScrollEl) {
      disableScroll(allowScrollEl, $screen.value.smAndDown);
    } else {
      console.error('Modal is not registered');
    }
  };

  const closeModal = (modalName: ModalsName) => {
    const closingModal = modalState.value.registeredModals[modalName];

    modalState.value.openedModals = openedModals.value.filter((modal) => modal !== modalName);

    closingModal?.onClose?.();

    if (openedModals.value.length) {
      return;
    }

    const scrollEl = toRef(modalState.value.registeredModals[modalName], 'scrollEl');
    const allowScrollEl = scrollEl.value;

    if (allowScrollEl) {
      enableScroll(allowScrollEl, $screen.value.smAndDown);
    }
  };

  return {
    openedModals,
    getRegisteredModal,
    registerModal,
    openModal,
    closeModal,
  };
}
