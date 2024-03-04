import { ref, watch } from 'vue';
import { Practicum, PracticumScreenElement, ScreenInfo } from '@/types/practicum';
import { getUiId } from '@/utils/functions';

const defaultPatientInfo =
  '<p><strong style="color: rgb(0, 209, 255);">Имя:</strong></p><p><strong style="color: rgb(0, 209, 255);">Возраст:</strong></p><p><strong style="color: rgb(0, 209, 255);">Образ жизни:</strong></p><p><strong style="color: rgb(0, 209, 255);">Семейный анамнез:</strong></p><p><strong style="color: rgb(0, 209, 255);">Перенесенные заболевания:</strong></p><p><strong style="color: rgb(0, 209, 255);">Оценка состояния:</strong></p><p><strong style="color: rgb(0, 209, 255);">Диагноз:</strong></p>';

export const usePracticumStore = () => {
  const editablePracticum = ref<Practicum>({
    id: 0,
    title: '',
    image: null,
    description: '',
    patientInfo: defaultPatientInfo,
    speciality: [],
    screens: [
      {
        id: 1,
        literature: '',
        literatureDescription: '',
        description: '',
        leftElements: [],
        rightElements: []
      },
      {
        id: 2,
        literature: '',
        literatureDescription: '',
        description: '',
        leftElements: [],
        rightElements: []
      }
    ]
  });

  const savePracticum = () => {
    editablePracticum.value.id = getUiId();
  };

  const saveScreen = (screen: ScreenInfo) => {
    const newScreen = { ...screen };
    newScreen.id = getUiId();

    editablePracticum.value.screens.push(newScreen);
  };

  watch(
    editablePracticum,
    () => {
      console.log(editablePracticum.value);
    },
    {
      deep: true
    }
  );

  return {
    editablePracticum,
    saveScreen,
    savePracticum
  };
};
