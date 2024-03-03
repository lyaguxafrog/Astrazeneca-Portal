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
    screens: []
  });

  const savePracticum = () => {
    editablePracticum.value.id = getUiId();
  };

  const saveScreen = (screen: ScreenInfo) => {
    editablePracticum.value.screens.push(screen);
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
