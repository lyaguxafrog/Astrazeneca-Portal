import { ref } from 'vue';
import { Speciality } from '@/types/specisalities';
import { useRequest } from '@/utils/composables/request';

const specialities = ref<Speciality[]>([]);

export const useSpecialitiesStore = () => {
  const { get } = useRequest();

  const getSpecialities = async () => {
    specialities.value = await get<Speciality[]>('/specialty');
  };

  return {
    specialities,
    getSpecialities
  };
};
