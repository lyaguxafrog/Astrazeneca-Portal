import { ref } from 'vue';
import {
  BDPracticum,
  BtnType,
  ButtonBlock,
  DropdownBlock,
  ImageBlock,
  isButtonBlock,
  isDropdownBlock,
  isImageBlock,
  isTextBlock,
  Practicum,
  PracticumScreenElement,
  ScreenBlock,
  ScreenInfo,
  TextBlock
} from '@/types/practicum';
import { useRequest } from '@/utils/composables/request';
import { useNotificationStore } from '@/store/notification';
import { useRoute } from 'vue-router';
import { useFileService } from '@/utils/composables/file-service';
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

const isSaving = ref(false);

const editablePracticum = ref<Practicum>(cloneFnJSON(defaultPracticum));

export const usePracticumStore = () => {
  const { get, post, put, del } = useRequest();
  const { loadFile } = useFileService();
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
      editablePracticum.value.screens = res.screens.map((s) => {
        const leftElements = [] as ScreenBlock[];
        const rightElements = [] as ScreenBlock[];

        s.screen_button_block.forEach((b) => {
          const block: ButtonBlock = {
            id: b.id,
            screenId: s.id,
            type: PracticumScreenElement.Button,
            title: b.button_title,
            btnType: b.screen_number ? BtnType.Screen : b.url ? BtnType.Link : BtnType.File,
            screenNumber: b.screen_number,
            link: b.url,
            file: undefined,
            loadedFile: b.pdf_file,
            withBg: b.fill_flag,
            confirmation: b.confirmation,
            side: b.side,
            order: b.order
          };

          if (b.side === 'left') {
            leftElements.push(block);
          } else {
            rightElements.push(block);
          }
        });

        s.screen_text_block.forEach((b) => {
          const block: TextBlock = {
            id: b.id,
            type: PracticumScreenElement.Text,
            screenId: s.id,
            order: b.order,
            text: b.text,
            side: b.side
          };

          if (b.side === 'left') {
            leftElements.push(block);
          } else {
            rightElements.push(block);
          }
        });

        s.screen_image_block.forEach((b) => {
          const block: ImageBlock = {
            id: b.id,
            type: PracticumScreenElement.Image,
            screenId: s.id,
            order: b.order,
            image: undefined,
            savedImage: b.image,
            side: b.side
          };

          if (b.side === 'left') {
            leftElements.push(block);
          } else {
            rightElements.push(block);
          }
        });

        s.screen_popup_block.forEach((b) => {
          const block: DropdownBlock = {
            id: b.id,
            type: PracticumScreenElement.Dropdown,
            screenId: s.id,
            side: b.side,
            items: b.popup_points,
            order: b.order
          };

          if (b.side === 'left') {
            leftElements.push(block);
          } else {
            rightElements.push(block);
          }
        });

        leftElements.sort((e1, e2) => e1.order - e2.order);
        rightElements.sort((e1, e2) => e1.order - e2.order);

        return {
          id: s.id,
          literature: s.literature,
          description: s.approvals_and_decodings,
          literatureDescription: s.leterature_approvals_and_decodings,
          order: s.order,
          leftElements,
          rightElements
        };
      });
    }
  };

  const savePracticumRequest = async (practicumData: any) => {
    isSaving.value = true;
    try {
      let res;

      const id = practicumData.id;
      if (!id) {
        res = await post<{
          id: number;
        }>('/practicum/create/', practicumData);

        if (res && res.id) {
          editablePracticum.value.id = res.id;
        }
      } else {
        res = await put<{
          id: number;
        }>(`/practicum/update/${id}/`, practicumData);
      }

      showNotification({
        text: 'Изменения сохранены'
      });

      return res as BDPracticum;
    } catch (e) {
      showNotification({
        text: 'Не удалось сохранить практикум',
        type: 'error'
      });
      return false;
    } finally {
      isSaving.value = false;
    }
  };

  const savePracticum = async () => {
    isSaving.value = true;
    const mapScreenBlocks = async (screen: ScreenInfo) => {
      const screen_button_block: any[] = [];
      const screen_popup_block: any[] = [];
      const screen_image_block: any[] = [];
      const screen_text_block: any[] = [];

      const blocks = [...screen.leftElements, ...screen.rightElements];

      for (const e of blocks) {
        if (isButtonBlock(e)) {
          let file: File | string | undefined = e.file?.[0];

          if (e.btnType === 'PDF-файл' && file && file instanceof File) {
            file = await loadFile(file);

            if (!file) {
              throw new Error();
              return;
            }
          }

          screen_button_block.push({
            id: e.id || undefined,
            screen_id: e.screenId,
            button_title: e.title,
            side: e.side,
            screen_number: e.screenNumber ? +e.screenNumber : undefined,
            url: e.link,
            pdf_file: file,
            fill_flag: e.withBg,
            confirmation: e.confirmation,
            order: e.order
          });
        }

        if (isImageBlock(e)) {
          let file: File | string | undefined = e.image?.[0];

          if (file && file instanceof File) {
            file = await loadFile(file);

            if (!file) {
              throw new Error();
              return;
            }
          }

          screen_image_block.push({
            id: e.id || undefined,
            image: file,
            side: e.side,
            order: e.order
          });
        }

        if (isTextBlock(e)) {
          screen_text_block.push({
            id: e.id || undefined,
            screen_id: e.screenId,
            side: e.side,
            text: e.text,
            order: e.order
          });
        }

        if (isDropdownBlock(e)) {
          screen_popup_block.push({
            id: e.id || undefined,
            screen_id: e.screenId,
            side: e.side,
            popup_points: e.items,
            order: e.order
          });
        }
      }

      return {
        screen_button_block: screen_button_block.length ? screen_button_block : undefined,
        screen_popup_block: screen_popup_block.length ? screen_popup_block : undefined,
        screen_image_block: screen_image_block.length ? screen_image_block : undefined,
        screen_text_block: screen_text_block.length ? screen_text_block : undefined
      };
    };

    const screens: any[] = [];

    for (const s of editablePracticum.value.screens) {
      const blocks = await mapScreenBlocks(s);

      screens.push({
        id: s.id || undefined,
        literature: s.literature,
        leterature_approvals_and_decodings: s.literatureDescription,
        approvals_and_decodings: s.description,
        order: s.order,
        screen_button_block: blocks!.screen_button_block,
        screen_text_block: blocks!.screen_text_block,
        screen_image_block: blocks!.screen_image_block,
        screen_popup_block: blocks!.screen_popup_block
      });
    }

    const mappedPracticumData = {
      id: editablePracticum.value.id,
      title: editablePracticum.value.title,
      description: editablePracticum.value.description,
      pacient_description: editablePracticum.value.patientInfo,
      speciality: editablePracticum.value.speciality,
      priority: editablePracticum.value.priority,
      image: editablePracticum.value.image?.[0],
      screens
    } as any;

    if (mappedPracticumData.image instanceof File) {
      mappedPracticumData.image = await loadFile(mappedPracticumData.image);
    }

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

  const removeScreen = async (id: number) => {
    await del(`/practicum/${editablePracticum.value.id}/screen/${id}`);

    editablePracticum.value.screens = editablePracticum.value.screens.filter((s) => s.id !== id);
  };

  const saveScreenBlock = async (block: ScreenBlock, side: 'right' | 'left') => {
    const screen = editablePracticum.value.screens.find((s) => s.id === block.screenId);

    if (!screen) {
      return;
    }

    block.side = side;
    block.order =
      block.order || side === 'left'
        ? screen.leftElements.length + 1
        : screen.rightElements.length + 1;

    try {
      if (side === 'right') {
        screen.rightElements.push(block);
      } else {
        screen.leftElements.push(block);
      }

      await savePracticum();
    } catch (e) {
      if (side === 'right') {
        screen.rightElements.pop();
      } else {
        screen.leftElements.pop();
      }

      console.error(e);
    }
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
    removeScreen,
    savePracticum,
    practicums,
    getPracticum,
    getPracticums,
    deletePracticum,
    init,
    isLoaded,
    saveScreenBlock,
    savePracticumRequest,
    isSaving
  };
};
