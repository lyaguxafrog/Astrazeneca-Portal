import { ref } from 'vue';
import { Practicum, ScreenInfo } from '@/types/practicum';
import { getUiId } from '@/utils/functions';
import { useRequest } from '@/utils/composables/request';

const defaultPatientInfo =
  '<p><strong style="color: rgb(0, 209, 255);">Имя:</strong></p><p><strong style="color: rgb(0, 209, 255);">Возраст:</strong></p><p><strong style="color: rgb(0, 209, 255);">Образ жизни:</strong></p><p><strong style="color: rgb(0, 209, 255);">Семейный анамнез:</strong></p><p><strong style="color: rgb(0, 209, 255);">Перенесенные заболевания:</strong></p><p><strong style="color: rgb(0, 209, 255);">Оценка состояния:</strong></p><p><strong style="color: rgb(0, 209, 255);">Диагноз:</strong></p>';

export const usePracticumStore = () => {
  const { get, post } = useRequest();

  const practicums = ref<Practicum[]>([]);

  const editablePracticum = ref<Practicum>({
    id: 0,
    priority: 50,
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

  const savePracticum = async () => {
    const mappedPracticum = {
      title: editablePracticum.value.title,
      description: editablePracticum.value.description,
      pacient_description: editablePracticum.value.patientInfo,
      speciality: editablePracticum.value.speciality,
      priority: editablePracticum.value.priority,
      screens: []
    };

    const res = await post('/practicum/create', mappedPracticum);

    console.log(res);
  };

  const saveScreen = (screen: ScreenInfo) => {
    const newScreen = { ...screen };
    newScreen.id = getUiId();

    editablePracticum.value.screens.push(newScreen);
  };

  const getPracticums = async () => {
    await get('/practicum/speciality');
  };

  return {
    editablePracticum,
    saveScreen,
    savePracticum,
    practicums,
    getPracticums
  };
};
