import { ref, watch } from 'vue';
import { PracticumScreenElement } from '@/types/practicum';

const defaultPatientInfo =
  '<p><strong style="color: rgb(0, 209, 255);">Имя:</strong></p><p><strong style="color: rgb(0, 209, 255);">Возраст:</strong></p><p><strong style="color: rgb(0, 209, 255);">Образ жизни:</strong></p><p><strong style="color: rgb(0, 209, 255);">Семейный анамнез:</strong></p><p><strong style="color: rgb(0, 209, 255);">Перенесенные заболевания:</strong></p><p><strong style="color: rgb(0, 209, 255);">Оценка состояния:</strong></p><p><strong style="color: rgb(0, 209, 255);">Диагноз:</strong></p>';

export const usePracticumStore = () => {
  const editablePracticum = ref({
    title: '',
    image: null as File | null,
    description: '',
    patientInfo: defaultPatientInfo,
    speciality: [],
    screens: [
      {
        literature: '',
        literatureDescription: '',
        description: '',
        elements: [
          {
            type: PracticumScreenElement.Button,
            title: ''
          }
        ]
      }
    ]
  });

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
    editablePracticum
  };
};
