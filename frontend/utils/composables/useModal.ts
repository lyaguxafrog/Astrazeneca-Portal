import { computed, nextTick, Ref, toRef } from 'vue';
import { useState } from '#app';
import { disableScroll, enableScroll } from '~/utils/functions/scroll-lock';
import { useScreen } from '~/utils/composables/useScreen';

export enum ModalsName {
  DrugProps = 'drug-props',
  VideosAddContent = 'videos-add-content',
  PracticumInfoModal = 'practicum-info-modal',
  PracticumDiscoverModal = 'practicum-discover-modal',
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
    modalState.value.registeredModals[modalName];

  const getModalPayload = (modalName: ModalsName) => getRegisteredModal(modalName).payload;

  const setModalPayload = (modalName: ModalsName, payload?: Record<string, any>) => {
    getRegisteredModal(modalName).payload = payload;
  };

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
    getModalPayload,
    registerModal,
    openModal,
    closeModal,
    setModalPayload,
  };
}
