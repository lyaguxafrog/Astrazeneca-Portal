import { ref } from 'vue';
import {
  BDPracticum,
  isButtonBlock,
  Practicum,
  PracticumScreenElement,
  ScreenBlock,
  ScreenInfo
} from '@/types/practicum';
import { useRequest } from '@/utils/composables/request';
import { useNotificationStore } from '@/store/notification';
import { useRoute } from 'vue-router';
import { cloneFnJSON } from '@vueuse/core';

const defaultPatientInfo =
  '<p><strong style="color: rgb(0, 209, 255);">Имя:</strong></p><p><strong style="color: rgb(0, 209, 255);">Возраст:</strong></p><p><strong style="color: rgb(0, 209, 255);">Образ жизни:</strong></p><p><strong style="color: rgb(0, 209, 255);">Семейный анамнез:</strong></p><p><strong style="color: rgb(0, 209, 255);">Перенесенные заболевания:</strong></p><p><strong style="color: rgb(0, 209, 255);">Оценка состояния:</strong></p><p><strong style="color: rgb(0, 209, 255);">Диагноз:</strong></p>';

const practicums = ref<BDPracticum[]>([]);

const defaultPracticum = {
  id: 0,
  priority: 50,
  title: '',
  image: undefined,
  loadedImage: '',
  description: '',
  patientInfo: defaultPatientInfo,
  speciality: [],
  screens: []
};

const editablePracticum = ref<Practicum>(cloneFnJSON(defaultPracticum));

export const usePracticumStore = () => {
  const { get, post, put, del } = useRequest();
  const { showNotification } = useNotificationStore();

  const getPracticum = async (id: number) => {
    const res = await get<BDPracticum>(`/practicum/${id}/`);

    if (res) {
      editablePracticum.value.id = res.id;
      editablePracticum.value.title = res.title;
      editablePracticum.value.priority = res.priority;
      editablePracticum.value.description = res.description;
      editablePracticum.value.patientInfo = res.pacient_description;
      editablePracticum.value.loadedImage = res.image;
      editablePracticum.value.speciality = res.speciality;
      editablePracticum.value.screens = res.screens.map((s) => ({
        id: s.id,
        literature: s.literature,
        description: s.approvals_and_decodings,
        literatureDescription: s.leterature_approvals_and_decodings,
        leftElements: [],
        rightElements: []
      }));
    }
  };

  const savePracticumRequest = async (practicumData: any) => {
    try {
      let res;

      const id = practicumData.id;
      if (!id) {
        res = await post<{
          id: number;
        }>('/practicum/create/', practicumData, true);

        if (res && res.id) {
          editablePracticum.value.id = res.id;
        }
      } else {
        res = await put<{
          id: number;
        }>(`/practicum/update/${id}/`, practicumData, true);
      }

      showNotification({
        text: 'Изменения сохранены'
      });

      return res as BDPracticum;
    } catch (e) {
      console.error(e);
      showNotification({
        text: 'Не удалось сохранить практикум',
        type: 'error'
      });

      return false;
    }
  };

  const savePracticum = async () => {
    const mapScreenBlocks = (screen: ScreenInfo) => {
      const screen_button_block: any[] = [];
      const screen_popup_block: any[] = [];
      const screen_image_block: any[] = [];
      const screen_text_block: any[] = [];

      screen.leftElements.forEach((e) => {
        if (isButtonBlock(e)) {
          screen_button_block.push({
            id: e.id,
            screen_id: e.screenId,
            button_title: e.title,
            side: 'left',
            screen_number: e.screenNumber,
            url: e.link,
            fill_flag: e.withBg,
            confirmation: e.confirmation
          });
        }

        if (e.type === PracticumScreenElement.Text) {
          screen_text_block.push({
            id: e.id,
            screen_id: e.screenId,
            side: 'left',
            text: e.text
          });
        }
      });

      return {
        screen_button_block,
        screen_popup_block,
        screen_image_block,
        screen_text_block
      };
    };

    const mappedPracticumData = {
      id: editablePracticum.value.id,
      title: editablePracticum.value.title,
      description: editablePracticum.value.description,
      pacient_description: editablePracticum.value.patientInfo,
      speciality: editablePracticum.value.speciality,
      priority: editablePracticum.value.priority,
      screens: editablePracticum.value.screens.map((s) => {
        const blocks = mapScreenBlocks(s);

        return {
          literature: s.literature,
          leterature_approvals_and_decodings: s.literatureDescription,
          approvals_and_decodings: s.description,
          practicum: editablePracticum.value.id
          // screen_button_block: blocks.screen_button_block
        };
      })
    } as any;

    return savePracticumRequest(mappedPracticumData);
  };

  const saveScreen = async (screen: ScreenInfo) => {
    if (!screen.id) {
      editablePracticum.value.screens.push(screen);
    } else {
      let existScreen = editablePracticum.value.screens.find((s) => s.id === screen.id);
      if (existScreen) {
        existScreen = Object.assign(existScreen, screen);
      }
    }

    const res = await savePracticum();

    return res;
  };

  const saveScreenBlock = async (block: ScreenBlock, side: 'right' | 'left') => {
    const screen = editablePracticum.value.screens.find((s) => s.id === block.screenId);

    if (!screen) {
      return;
    }

    if (side === 'right') {
      screen.rightElements.push(block);
    } else {
      screen.leftElements.push(block);
    }

    await savePracticum();
  };

  const getPracticums = async () => {
    const res = await get<BDPracticum[]>('/practicum/all/');

    practicums.value = res.sort((p1, p2) => p1.priority - p2.priority);
  };

  const deletePracticum = async (id: number) => {
    await del(`/practicum/delete/${id}/`);
    await getPracticums();
  };

  const isLoaded = ref(false);
  const init = async () => {
    const $route = useRoute();

    const practicumId = +$route.params.id;

    isLoaded.value = false;
    await getPracticums();

    if (!practicumId) {
      editablePracticum.value = cloneFnJSON(defaultPracticum);
    } else if (practicumId !== editablePracticum.value.id) {
      await getPracticum(practicumId);
      editablePracticum.value.id = practicumId;
    }

    editablePracticum.value.priority = practicums.value.length + 1;
    isLoaded.value = true;
  };

  return {
    editablePracticum,
    saveScreen,
    savePracticum,
    practicums,
    getPracticum,
    getPracticums,
    deletePracticum,
    init,
    isLoaded,
    saveScreenBlock,
    savePracticumRequest
  };
};
